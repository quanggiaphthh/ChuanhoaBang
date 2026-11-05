"""Build and smoke-test the wheel outside the source checkout on any OS."""
from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

from docx import Document


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="chuanhoabang-wheel-") as temp_dir:
        temp = Path(temp_dir)
        wheel_dir = temp / "wheel"
        install_dir = temp / "install"
        wheel_dir.mkdir()
        install_dir.mkdir()

        subprocess.run([
            "uv", "build", "--wheel", "--out-dir", str(wheel_dir), ".",
        ], check=True)
        wheel = next(wheel_dir.glob("*.whl"))
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
        subprocess.run([sys.executable, "-m", "chuanhoabang", "audit", str(source),
                        "--profile", "ND30"], cwd=temp, env=env, check=True)


if __name__ == "__main__":
    main()
