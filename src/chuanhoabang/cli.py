"""Small offline CLI: chuanhoabang audit|propose|apply."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from .core import TableError, audit, propose, propose_header, propose_unclip_row_height, apply


def render_markdown(result: dict) -> str:
    """Human-readable audit trail; no layout or legal acceptance is inferred."""
    def safe(value):
        return str(value).replace("|", "\\|").replace("\\n", " ")

    lines = ["# ChuanhoaBang — Báo cáo xử lý DOCX", "",
             f"**Quyết định:** \`{safe(result.get('decision', result.get('status', 'AUDIT_ONLY')))}\`",
             f"**Kết xuất Microsoft Word:** \`{safe(result.get('word_render', 'NOT_RUN'))}\`",
             "", "## Thông tin xử lý", "", "| Thuộc tính | Giá trị |", "|---|---|"]
    for key in ("file", "output", "input_sha256", "output_sha256", "policy",
                "table_index", "table_count", "operation", "evidence",
                "content_integrity", "non_target_package_parts"):
        if key in result:
            lines.append(f"| {safe(key)} | {safe(result[key])} |")
    if isinstance(result.get("tables"), list):
        lines += ["", "## Bảng được phát hiện", "",
                  "| STT | Trạng thái | Hàng | Cột | Lý do |", "|---:|---|---:|---:|---|"]
        for table in result["tables"]:
            lines.append(f"| {table.get('index', '?')} | {safe(table.get('status', 'UNKNOWN'))} | "
                         f"{table.get('rows', '?')} | {table.get('columns', '?')} | "
                         f"{safe(', '.join(table.get('reasons', [])))} |")
    if result.get("reasons"):
        lines += ["", "## Lý do / cảnh báo", ""]
        lines.extend(f"- {safe(reason)}" for reason in result["reasons"])
    if result.get("changed_properties"):
        lines += ["", "## Thuộc tính thay đổi", ""]
        lines.extend(f"- \`{safe(prop)}\`" for prop in result["changed_properties"])
    lines += ["", "## Giới hạn nghiệm thu", "",
              "Kiểm tra cấu trúc DOCX không tương đương nghiệm thu trình bày trong Microsoft Word. "
              "Không tự kết luận đúng khổ in hoặc đúng quy phạm pháp luật từ báo cáo này.", ""]
    return "\\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(prog="chuanhoabang", description="Conservative offline DOCX table-width formatter")
    sub = parser.add_subparsers(dest="command", required=True)
    p_audit = sub.add_parser("audit", help="Read-only inspection of all body tables")
    p_audit.add_argument("input")
    p_audit.add_argument("--report-md", help="Write a Markdown QA report to a new file")
    p_prop = sub.add_parser("propose", help="Generate a deterministic width proposal")
    p_prop.add_argument("input")
    p_prop.add_argument("--table", type=int, required=True, help="0-based table index from audit")
    p_prop.add_argument("--font-regular", help="Installed, licensed Times New Roman regular TTF/OTF")
    p_prop.add_argument("--font-bold", help="Installed, licensed Times New Roman bold TTF/OTF")
    p_prop.add_argument("--output", help="Save JSON proposal to this new file")
    p_prop.add_argument("--report-md", help="Write a Markdown QA report to a new file")
    p_header = sub.add_parser("propose-header", help="Propose repeat-header for an eligible data table")
    p_header.add_argument("input")
    p_header.add_argument("--table", type=int, required=True, help="0-based table index from audit")
    p_header.add_argument("--output", help="Save JSON header proposal to this new file")
    p_header.add_argument("--report-md", help="Write a Markdown QA report to a new file")
    p_unclip = sub.add_parser("propose-unclip", help="Propose safe exact→atLeast row-height relaxation")
    p_unclip.add_argument("input")
    p_unclip.add_argument("--table", type=int, required=True)
    p_unclip.add_argument("--output", help="Save JSON proposal to this new file")
    p_unclip.add_argument("--report-md", help="Write a Markdown QA report to a new file")
    p_apply = sub.add_parser("apply", help="Explicitly apply an unmodified proposal to a new DOCX")
    p_apply.add_argument("input")
    p_apply.add_argument("--proposal", required=True)
    p_apply.add_argument("--output", required=True)
    p_apply.add_argument("--font-regular")
    p_apply.add_argument("--font-bold")
    p_apply.add_argument("--report-md", help="Write a Markdown QA report to a new file")
    args = parser.parse_args(argv)
    try:
        if args.report_md and Path(args.report_md).exists():
            raise TableError("REPORT_OUTPUT_MUST_BE_NEW_PATH")
        if args.command == "audit":
            result = audit(args.input)
        elif args.command == "propose":
            result = propose(args.input, args.table, args.font_regular, args.font_bold)
        elif args.command == "propose-header":
            result = propose_header(args.input, args.table)
        elif args.command == "propose-unclip":
            result = propose_unclip_row_height(args.input, args.table)
        else:
            data = json.loads(Path(args.proposal).read_text(encoding="utf-8"))
            result = apply(args.input, data, args.output, args.font_regular, args.font_bold)
        serialized = json.dumps(result, indent=2, ensure_ascii=False)
        if args.command in ("propose", "propose-header", "propose-unclip") and args.output:
            dest = Path(args.output)
            if dest.exists():
                raise TableError("OUTPUT_MUST_BE_NEW_PATH")
            dest.write_text(serialized + "\n", encoding="utf-8")
        if args.report_md:
            report_path = Path(args.report_md)
            report_path.parent.mkdir(parents=True, exist_ok=True)
            report_path.write_text(render_markdown(result), encoding="utf-8")
        print(serialized)
        return 0
    except (TableError, json.JSONDecodeError, OSError, ValueError) as exc:
        print(json.dumps({"status": "FAIL", "reason": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
