"""Build and verify a target-specific offline runtime wheelhouse."""
from __future__ import annotations

import argparse
from email.parser import BytesParser
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import sysconfig
import tempfile
import zipfile


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _source_commit() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()


def _tracked_file_sha256(path: Path) -> str:
    content = subprocess.check_output(["git", "show", f"HEAD:{path.as_posix()}"])
    return hashlib.sha256(content).hexdigest()


def _wheel_requirement(wheel: Path) -> str:
    with zipfile.ZipFile(wheel) as package:
        metadata_files = [
            name for name in package.namelist() if name.endswith(".dist-info/METADATA")
        ]
        if len(metadata_files) != 1:
            raise RuntimeError(f"expected one wheel METADATA file: {wheel.name}")
        metadata = BytesParser().parsebytes(package.read(metadata_files[0]))
    name, version = metadata.get("Name"), metadata.get("Version")
    if not name or not version:
        raise RuntimeError(f"wheel metadata has no project name/version: {wheel.name}")
    return f"{name}=={version}"


def _run(command: list[str], *, cwd: Path, env: dict[str, str] | None = None) -> str:
    try:
        completed = subprocess.run(
            command,
            cwd=cwd,
            env=env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=True,
        )
    except subprocess.CalledProcessError as error:
        raise RuntimeError(
            f"command failed ({error.returncode}): {command!r}\n{error.stdout or ''}"
        ) from error
    return completed.stdout


def _verify_candidate(candidate_dir: Path) -> Path:
    wheels = list(candidate_dir.glob("*.whl"))
    manifest_path = candidate_dir / "release-manifest.json"
    if len(wheels) != 1 or not manifest_path.is_file():
        raise FileNotFoundError(
            "expected one canonical wheel and release-manifest.json in candidate directory"
        )

    wheel = wheels[0]
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest["source"]["commit"] != _source_commit():
        raise RuntimeError("candidate wheel was built from a different source commit")
    if manifest["source"]["uv_lock_sha256"] != _tracked_file_sha256(Path("uv.lock")):
        raise RuntimeError("candidate manifest does not match the current uv.lock")
    if manifest["artifact"]["filename"] != wheel.name:
        raise RuntimeError("candidate wheel filename does not match its manifest")
    if manifest["artifact"]["sha256"] != _sha256(wheel):
        raise RuntimeError("candidate wheel SHA-256 does not match its manifest")
    return wheel


def _make_docx(path: Path) -> None:
    rows = (
        ("STT", "Nội dung", "Ghi chú"),
        ("0012", "Nhiệm vụ ưu tiên", "Đang làm"),
    )
    row_xml = "".join(
        "<w:tr>" + "".join(
            f"<w:tc><w:tcPr><w:tcW w:w=\"2400\" w:type=\"dxa\"/></w:tcPr>"
            f"<w:p><w:r><w:t>{value}</w:t></w:r></w:p></w:tc>"
            for value in row
        ) + "</w:tr>"
        for row in rows
    )
    document_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        '<w:body><w:tbl><w:tblPr><w:tblW w:w="7200" w:type="dxa"/></w:tblPr>'
        '<w:tblGrid><w:gridCol w:w="2400"/><w:gridCol w:w="2400"/>'
        '<w:gridCol w:w="2400"/></w:tblGrid>' + row_xml + '</w:tbl>' +
        '<w:sectPr><w:pgSz w:w="12240" w:h="15840"/>'
        '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/>'
        '</w:sectPr></w:body></w:document>'
    )
    content_types = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/word/document.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        '</Types>'
    )
    relationships = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" '
        'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
        'Target="word/document.xml"/>'
        '</Relationships>'
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as package:
        package.writestr("[Content_Types].xml", content_types)
        package.writestr("_rels/.rels", relationships)
        package.writestr("word/document.xml", document_xml)


def _venv_python(venv: Path) -> Path:
    executable = "python.exe" if os.name == "nt" else "python"
    scripts = "Scripts" if os.name == "nt" else "bin"
    return venv / scripts / executable


def _build_bundle(candidate_dir: Path, output_dir: Path) -> None:
    candidate_dir = candidate_dir.resolve()
    output_dir = output_dir.resolve()
    wheel = _verify_candidate(candidate_dir)
    if output_dir.exists() and any(output_dir.iterdir()):
        raise FileExistsError(f"offline bundle output directory must be empty: {output_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)
    wheelhouse = output_dir / "wheelhouse"
    wheelhouse.mkdir()
    requirements = output_dir / "requirements.txt"
    offline_install_requirements = output_dir / "offline-install-requirements.txt"

    _run([
        "uv", "export", "--locked", "--format", "requirements.txt", "--no-dev",
        "--no-emit-project", "--output-file", str(requirements),
    ], cwd=Path.cwd())
    _run([
        sys.executable, "-m", "pip", "download", "--require-hashes",
        "--only-binary=:all:", "-r", str(requirements), "--dest", str(wheelhouse),
    ], cwd=Path.cwd())

    bundled_app_wheel = wheelhouse / wheel.name
    shutil.copyfile(wheel, bundled_app_wheel)
    offline_install_requirements.write_text(
        requirements.read_text(encoding="utf-8").rstrip()
        + "\n\n"
        + _wheel_requirement(bundled_app_wheel)
        + " \\\n    --hash=sha256:"
        + _sha256(bundled_app_wheel)
        + "\n",
        encoding="utf-8",
    )

    with tempfile.TemporaryDirectory(prefix="chuanhoabang-offline-") as temp_dir:
        temp = Path(temp_dir)
        venv = temp / "venv"
        source_docx = temp / "vietnamese-smoke.docx"
        report_md = temp / "audit.md"
        _make_docx(source_docx)

        _run([sys.executable, "-m", "venv", str(venv)], cwd=temp)
        offline_env = os.environ.copy()
        offline_env.pop("PYTHONPATH", None)
        offline_env.pop("PYTHONHOME", None)
        offline_env["PIP_NO_INDEX"] = "1"
        offline_env["PIP_DISABLE_PIP_VERSION_CHECK"] = "1"

        _run([
            str(_venv_python(venv)), "-m", "pip", "install", "--no-index",
            "--find-links", str(wheelhouse), "--require-hashes", "--only-binary=:all:",
            "-r", str(offline_install_requirements),
        ], cwd=temp, env=offline_env)

        entrypoint = (
            venv / "Scripts" / "chuanhoabang.exe"
            if os.name == "nt"
            else venv / "bin" / "chuanhoabang"
        )
        _run([str(entrypoint), "--help"], cwd=temp, env=offline_env)
        _run([
            str(entrypoint), "audit", str(source_docx), "--profile", "ND30",
            "--report-md", str(report_md),
        ], cwd=temp, env=offline_env)
        if not report_md.is_file() or report_md.stat().st_size == 0:
            raise RuntimeError("offline CLI audit did not write its Markdown report")

    wheel_entries = [
        {"filename": item.name, "sha256": _sha256(item)}
        for item in sorted(wheelhouse.glob("*.whl"), key=lambda item: item.name.lower())
    ]
    if len(wheel_entries) < 2 or bundled_app_wheel.name not in {
        item["filename"] for item in wheel_entries
    }:
        raise RuntimeError("wheelhouse is missing the project wheel or runtime dependency wheels")

    run_id = os.environ.get("GITHUB_RUN_ID")
    manifest = {
        "schema_version": 1,
        "bundle_status": "OFFLINE_INSTALL_SMOKE_PASS_WORD_ACCEPTANCE_NOT_RUN",
        "source": {
            "commit": _source_commit(),
            "uv_lock_sha256": _tracked_file_sha256(Path("uv.lock")),
            "preview_wheel": {
                "filename": wheel.name,
                "sha256": _sha256(wheel),
            },
        },
        "target": {
            "os": platform.system(),
            "machine": platform.machine(),
            "platform_tag": sysconfig.get_platform(),
            "python_implementation": platform.python_implementation(),
            "python_version": platform.python_version(),
            "python_cache_tag": sys.implementation.cache_tag,
        },
        "runtime_requirements": {
            "filename": requirements.name,
            "sha256": _sha256(requirements),
            "export": "uv export --locked --no-dev --no-emit-project",
            "hash_checked_binary_wheels_only": True,
            "offline_install_filename": offline_install_requirements.name,
            "offline_install_sha256": _sha256(offline_install_requirements),
        },
        "wheelhouse": wheel_entries,
        "checks": {
            "fresh_virtual_environment": "PASS",
            "install_with_pip_no_index_and_require_hashes": "PASS",
            "console_entrypoint_help": "PASS",
            "vietnamese_docx_audit_and_markdown_report": "PASS",
            "microsoft_word_acceptance": "NOT_RUN",
        },
        "ci_run": {
            "id": run_id,
            "url": (
                "https://github.com/"
                f"{os.environ['GITHUB_REPOSITORY']}/actions/runs/{run_id}"
                if run_id and os.environ.get("GITHUB_REPOSITORY")
                else None
            ),
        },
    }
    manifest_path = output_dir / "offline-bundle-manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    _build_bundle(args.candidate_dir, args.output_dir)


if __name__ == "__main__":
    main()
