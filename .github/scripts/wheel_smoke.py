"""Build or verify ChuanhoaBang's canonical preview wheel on any OS."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10
    import tomli as tomllib

from docx import Document


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _source_commit() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()


def _installed_wheel_smoke(wheel: Path, temp: Path) -> None:
    install_dir = temp / "install"
    install_dir.mkdir()
    subprocess.run([
        "uv", "pip", "install", "--python", sys.executable,
        "--no-deps", "--no-index", "--target", str(install_dir), str(wheel),
    ], check=True)

    env = os.environ.copy()
    env["PYTHONPATH"] = str(install_dir)
    smoke = """from importlib.resources import files
import json
import chuanhoabang
registry = files('chuanhoabang').joinpath('POLICY_REGISTRY.json')
assert registry.is_file()
policy = json.loads(registry.read_text(encoding='utf-8'))
assert policy['profiles']['ND30']['table_width_measurement']['font_sizes_pt'] == [13, 14]
assert policy['profiles']['HD05']['table_width_measurement']['font_sizes_pt'] == [14]
assert chuanhoabang.available_profiles() == ('ND30', 'HD05')
"""
    subprocess.run([sys.executable, "-c", smoke], cwd=temp, env=env, check=True)
    subprocess.run([sys.executable, "-m", "chuanhoabang", "--help"],
                   cwd=temp, env=env, check=True)

    document = Document()
    table = document.add_table(rows=2, cols=3)
    for row, values in zip(table.rows, (("STT", "Nội dung", "Ghi chú"),
                                        ("0012", "Nhiệm vụ ưu tiên", "Đang làm"))):
        for cell, value in zip(row.cells, values):
            cell.text = value
    source = temp / "utf8-smoke.docx"
    document.save(source)
    subprocess.run([
        sys.executable, "-m", "chuanhoabang", "audit", str(source),
        "--profile", "ND30",
    ], cwd=temp, env=env, check=True)


def _build_candidate(output_dir: Path) -> None:
    if output_dir.exists() and any(output_dir.iterdir()):
        raise FileExistsError(f"candidate output directory must be empty: {output_dir}")
    output_dir.mkdir(parents=True, exist_ok=True)

    source_commit = _source_commit()
    source_date_epoch = int(subprocess.check_output(
        ["git", "show", "-s", "--format=%ct", "HEAD"], text=True,
    ).strip())
    build_env = os.environ.copy()
    build_env["SOURCE_DATE_EPOCH"] = str(source_date_epoch)
    build_requirements = tomllib.loads(
        Path("pyproject.toml").read_text(encoding="utf-8")
    )["build-system"]["requires"]

    with tempfile.TemporaryDirectory(prefix="chuanhoabang-wheel-") as temp_dir:
        temp = Path(temp_dir)
        wheel_dir = temp / "wheel"
        repeat_dir = temp / "repeat"
        wheel_dir.mkdir()
        repeat_dir.mkdir()

        for build_dir in (wheel_dir, repeat_dir):
            subprocess.run([
                "uv", "build", "--wheel", "--out-dir", str(build_dir), ".",
            ], check=True, env=build_env)

        wheel = next(wheel_dir.glob("*.whl"))
        repeated_wheel = next(repeat_dir.glob("*.whl"))
        wheel_sha256 = _sha256(wheel)
        repeated_sha256 = _sha256(repeated_wheel)
        if wheel.name != repeated_wheel.name or wheel_sha256 != repeated_sha256:
            raise RuntimeError("Repeated wheel builds differ for the same source commit")

        _installed_wheel_smoke(wheel, temp)
        artifact = output_dir / wheel.name
        shutil.copyfile(wheel, artifact)
        manifest = {
            "schema_version": 1,
            "release_status": "PREVIEW_WORD_ACCEPTANCE_NOT_RUN",
            "source": {
                "commit": source_commit,
                "source_date_epoch": source_date_epoch,
                "uv_lock_sha256": _sha256(Path("uv.lock")),
            },
            "artifact": {
                "filename": wheel.name,
                "sha256": wheel_sha256,
            },
            "build": {
                "uv": subprocess.check_output(["uv", "--version"], text=True).strip(),
                "python": platform.python_version(),
                "build_requirements": build_requirements,
                "same_runner_rebuild": "PASS",
                "repeat_sha256": repeated_sha256,
            },
            "checks": {
                "isolated_install": "PASS",
                "packaged_policy_registry": "PASS",
                "cli_help": "PASS",
                "vietnamese_docx_audit": "PASS",
                "microsoft_word_acceptance": "NOT_RUN",
            },
            "ci_run": {
                "id": os.environ.get("GITHUB_RUN_ID"),
                "url": (
                    "https://github.com/"
                    f"{os.environ['GITHUB_REPOSITORY']}/actions/runs/{os.environ['GITHUB_RUN_ID']}"
                    if os.environ.get("GITHUB_REPOSITORY") and os.environ.get("GITHUB_RUN_ID")
                    else None
                ),
            },
        }
        (output_dir / "release-manifest.json").write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print(json.dumps(manifest, indent=2, ensure_ascii=False))


def _verify_candidate(candidate_dir: Path) -> None:
    wheels = list(candidate_dir.glob("*.whl"))
    manifest_path = candidate_dir / "release-manifest.json"
    if len(wheels) != 1 or not manifest_path.is_file():
        raise FileNotFoundError("expected one wheel and release-manifest.json in candidate directory")

    wheel = wheels[0]
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest["source"]["commit"] != _source_commit():
        raise RuntimeError("candidate wheel was built from a different source commit")
    if manifest["artifact"]["filename"] != wheel.name:
        raise RuntimeError("candidate wheel filename does not match its manifest")
    if manifest["artifact"]["sha256"] != _sha256(wheel):
        raise RuntimeError("candidate wheel SHA-256 does not match its manifest")
    if manifest["release_status"] != "PREVIEW_WORD_ACCEPTANCE_NOT_RUN":
        raise RuntimeError("candidate manifest does not identify the Word acceptance limitation")

    with tempfile.TemporaryDirectory(prefix="chuanhoabang-install-") as temp_dir:
        _installed_wheel_smoke(wheel, Path(temp_dir))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--output-dir", type=Path,
                       help="build twice, smoke-test, and write candidate wheel and manifest")
    group.add_argument("--candidate-dir", type=Path,
                       help="verify and smoke-test an existing candidate wheel and manifest")
    args = parser.parse_args()
    if args.output_dir is not None:
        _build_candidate(args.output_dir)
    else:
        _verify_candidate(args.candidate_dir)


if __name__ == "__main__":
    main()
