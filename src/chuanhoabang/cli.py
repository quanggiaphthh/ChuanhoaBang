"""Small offline CLI: chuanhoabang audit|propose|apply."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from .core import (TableError, audit, propose, propose_header, propose_unclip_row_height,
                   apply, available_profiles)


def render_markdown(result: dict) -> str:
    """Human-readable audit trail; no layout or legal acceptance is inferred."""
    def safe(value):
        return str(value).replace("|", "\\|").replace(chr(10), " ")

    lines = ["# ChuanhoaBang — Báo cáo xử lý DOCX", "",
             f"**Quyết định:** `{safe(result.get('decision', result.get('status', 'AUDIT_ONLY')))}`",
             f"**Kết xuất Microsoft Word:** `{safe(result.get('word_render', 'NOT_RUN'))}`",
             "", "## Thông tin xử lý", "", "| Thuộc tính | Giá trị |", "|---|---|"]
    for key in ("file", "output", "input_sha256", "output_sha256", "policy",
                "profile", "profile_status", "profile_rules_applied", "profile_constraints",
                "table_index", "table_count", "non_body_story_table_count", "operation", "evidence",
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
    if "non_body_story_tables" in result:
        lines += ["", "## Bảng trong header/footer/footnote/endnote", "",
                  "Các chỉ số này không dùng làm `--table`; chủ sở hữu section chưa được phân giải "
                  "và các bảng ngoài body chỉ được kiểm kê để xem xét.", "",
                  "| Part | Chỉ số trong part | SHA-256 | Trạng thái owner | Trạng thái | Lý do |",
                  "|---|---:|---|---|---|---|"]
        for table in result["non_body_story_tables"]:
            lines.append(f"| {safe(table.get('part', '?'))} | "
                         f"{table.get('story_table_index', '?')} | "
                         f"`{safe(table.get('table_sha256', '?'))}` | "
                         f"{safe(table.get('owner_status', 'UNKNOWN'))} | "
                         f"{safe(table.get('status', 'UNKNOWN'))} | "
                         f"{safe(table.get('reason', 'UNKNOWN'))} |")
        if not result["non_body_story_tables"]:
            lines.append("| — | — | — | — | — | Không phát hiện bảng ngoài body |")
    if result.get("reasons"):
        lines += ["", "## Lý do / cảnh báo", ""]
        lines.extend(f"- {safe(reason)}" for reason in result["reasons"])
    if result.get("changed_properties"):
        lines += ["", "## Thuộc tính thay đổi", ""]
        lines.extend(f"- `{safe(prop)}`" for prop in result["changed_properties"])
    lines += ["", "## Giới hạn nghiệm thu", "",
              "Kiểm tra cấu trúc DOCX không tương đương nghiệm thu trình bày trong Microsoft Word. "
              "Không tự kết luận đúng khổ in hoặc đúng quy phạm pháp luật từ báo cáo này.", ""]
    return chr(10).join(lines)


def main(argv=None):
    # CLI JSON and help may contain Vietnamese text and non-ASCII symbols. Keep
    # console and redirected output predictable on Windows code pages as well.
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8")
            except (OSError, ValueError):
                pass
    parser = argparse.ArgumentParser(prog="chuanhoabang", description="Conservative offline DOCX table-width formatter")
    sub = parser.add_subparsers(dest="command", required=True)
    p_audit = sub.add_parser("audit", help="Inspect body tables and inventory non-body story tables")
    p_audit.add_argument("input")
    p_audit.add_argument("--report-md", help="Write a Markdown QA report to a new file")
    p_audit.add_argument("--profile", choices=available_profiles(),
                         help="Record ND30/HD05 context; no formatting profile preset is applied")
    p_prop = sub.add_parser("propose", help="Generate a deterministic width proposal")
    p_prop.add_argument("input")
    p_prop.add_argument("--table", type=int, required=True, help="0-based table index from audit")
    p_prop.add_argument("--font-regular", help="Installed, licensed Times New Roman regular TTF/OTF")
    p_prop.add_argument("--font-bold", help="Installed, licensed Times New Roman bold TTF/OTF")
    p_prop.add_argument("--output", help="Save JSON proposal to this new file")
    p_prop.add_argument("--report-md", help="Write a Markdown QA report to a new file")
    p_prop.add_argument("--profile", choices=available_profiles(),
                        help="Record ND30/HD05 context; width measurement uses profile size scope only")
    p_header = sub.add_parser("propose-header", help="Propose repeat-header for an eligible data table")
    p_header.add_argument("input")
    p_header.add_argument("--table", type=int, required=True, help="0-based table index from audit")
    p_header.add_argument("--output", help="Save JSON header proposal to this new file")
    p_header.add_argument("--report-md", help="Write a Markdown QA report to a new file")
    p_header.add_argument("--profile", choices=available_profiles(),
                          help="Record ND30/HD05 context; profile rules remain reference-only")
    p_unclip = sub.add_parser("propose-unclip", help="Propose safe exact→atLeast row-height relaxation")
    p_unclip.add_argument("input")
    p_unclip.add_argument("--table", type=int, required=True)
    p_unclip.add_argument("--output", help="Save JSON proposal to this new file")
    p_unclip.add_argument("--report-md", help="Write a Markdown QA report to a new file")
    p_unclip.add_argument("--profile", choices=available_profiles(),
                          help="Record ND30/HD05 context; profile rules remain reference-only")
    p_apply = sub.add_parser("apply", help="Explicitly apply an unmodified proposal to a new DOCX")
    p_apply.add_argument("input")
    p_apply.add_argument("--proposal", required=True)
    p_apply.add_argument("--output", required=True)
    p_apply.add_argument("--font-regular")
    p_apply.add_argument("--font-bold")
    p_apply.add_argument("--report-md", help="Write a Markdown QA report to a new file")
    p_apply.add_argument("--profile", choices=available_profiles(),
                         help="Verify the proposal's ND30/HD05 context before applying")
    args = parser.parse_args(argv)
    try:
        if args.report_md:
            report_path = Path(args.report_md).resolve()
            if report_path.exists():
                raise TableError("REPORT_OUTPUT_MUST_BE_NEW_PATH")
            if getattr(args, "output", None) and report_path == Path(args.output).resolve():
                raise TableError("REPORT_OUTPUT_CONFLICT")
            if report_path == Path(args.input).resolve():
                raise TableError("REPORT_OUTPUT_CONFLICT")
            if getattr(args, "proposal", None) and report_path == Path(args.proposal).resolve():
                raise TableError("REPORT_OUTPUT_CONFLICT")
        if args.command == "audit":
            result = audit(args.input, profile=args.profile)
        elif args.command == "propose":
            result = propose(args.input, args.table, args.font_regular, args.font_bold,
                             profile=args.profile)
        elif args.command == "propose-header":
            result = propose_header(args.input, args.table, profile=args.profile)
        elif args.command == "propose-unclip":
            result = propose_unclip_row_height(args.input, args.table, profile=args.profile)
        else:
            data = json.loads(Path(args.proposal).read_text(encoding="utf-8"))
            result = apply(args.input, data, args.output, args.font_regular, args.font_bold,
                           profile=args.profile)
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
