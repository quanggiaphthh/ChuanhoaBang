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

    def width_label(width):
        status = width.get("status", "UNKNOWN")
        if status != "DECLARED":
            return status
        value = width.get("raw_value")
        label = f"{width.get('type', 'UNKNOWN')}:{value if value is not None else '—'}"
        if width.get("type") == "dxa" and width.get("twips") is not None:
            label += " twips"
        return label

    lines = ["# ChuanhoaBang — Báo cáo xử lý DOCX", "",
             f"**Quyết định:** `{safe(result.get('decision', result.get('status', 'AUDIT_ONLY')))}`",
             f"**Kết xuất Microsoft Word:** `{safe(result.get('word_render', 'NOT_RUN'))}`",
             "", "## Thông tin xử lý", "", "| Thuộc tính | Giá trị |", "|---|---|"]
    for key in ("file", "output", "input_sha256", "output_sha256", "policy",
                "profile", "profile_status", "profile_rules_applied", "profile_constraints",
                "table_index", "table_count", "non_body_story_table_count", "operation", "evidence",
                "cell_grid_spans", "row_grid_omissions",
                "content_integrity", "non_target_package_parts"):
        if key in result:
            value = (json.dumps(result[key], ensure_ascii=False)
                     if key in ("cell_grid_spans", "row_grid_omissions") else result[key])
            lines.append(f"| {safe(key)} | {safe(value)} |")
    geometry = result.get("geometry")
    if isinstance(geometry, dict):
        lines += ["", "## Geometry evidence", "", "| Field | Value |", "|---|---|"]
        for key in ("status", "reason", "orientation", "sections", "page_width_twips",
                    "page_text_width_twips", "column_count", "column_gap_twips",
                    "custom_column_widths_twips", "custom_column_spacing_after_twips",
                    "available_width_scope", "available_twips"):
            if key not in geometry:
                continue
            value = geometry[key]
            if key.endswith("_twips") and value is not None:
                value = (", ".join(f"{item} twips" if item is not None else "UNSPECIFIED"
                                    for item in value)
                         if isinstance(value, list) else f"{value} twips")
            lines.append(f"| {safe(key)} | {safe(value)} |")
        lines.append(f"| word_rendered_width | {safe(result.get('word_render', 'NOT_RUN'))} |")
    if isinstance(result.get("tables"), list):
        lines += ["", "## Bảng được phát hiện", "",
                  "| Table ID | Parent table ID | STT | Trạng thái | Hàng | Cột | Lý do |",
                  "|---|---|---:|---|---:|---:|---|"]
        for table in result["tables"]:
            parent_id = table.get("parent_table_id") or "—"
            lines.append(f"| `{safe(table.get('table_id', '?'))}` | "
                         f"`{safe(parent_id)}` | {table.get('index', '?')} | "
                         f"{safe(table.get('status', 'UNKNOWN'))} | "
                         f"{table.get('rows', '?')} | {table.get('columns', '?')} | "
                         f"{safe(', '.join(table.get('reasons', [])))} |")
        if any("width_evidence" in table for table in result["tables"]):
            lines += ["", "## Width evidence (OOXML declarations; not Word measurements)", "",
                      "| Table ID | Grid and sum | Cell grid spans / vertical merge markers (source XML) | tblW preferred | tcW preferred by row/cell | Cell padding evidence | Word rendered width |",
                      "|---|---|---|---|---|---|---|"]
            for table in result["tables"]:
                evidence = table.get("width_evidence", {})
                grid = table.get("grid_twips")
                grid_sum = evidence.get("grid_sum_twips")
                grid_label = (f"grid={grid if grid is not None else 'UNKNOWN'} twips; "
                              f"sum={grid_sum if grid_sum is not None else 'UNKNOWN'} twips")
                span_evidence = table.get("cell_grid_spans")
                if table.get("row_grid_omissions") is not None:
                    span_evidence = {
                        "cell_grid_spans": span_evidence,
                        "row_grid_omissions": table["row_grid_omissions"],
                    }
                span_label = json.dumps(span_evidence, ensure_ascii=False,
                                        separators=(",", ":"))
                cell_labels = []
                for row_index, row in enumerate(evidence.get("cell_preferred", [])):
                    for cell_index, width in enumerate(row):
                        cell_labels.append(f"r{row_index}c{cell_index}={width_label(width)}")
                cells_label = "; ".join(cell_labels) or "no tcW declarations"
                padding = evidence.get("cell_padding")
                if not isinstance(padding, dict):
                    padding_label = "NOT_REPORTED"
                else:
                    padding_parts = [f"status={padding.get('status', 'UNKNOWN')}"]
                    for key in ("reason", "basis"):
                        if padding.get(key) is not None:
                            padding_parts.append(f"{key}={padding[key]}")
                    assumed = padding.get("assumed_default_twips")
                    padding_parts.append(
                        f"fallback={assumed} twips" if assumed is not None else "fallback=not used"
                    )
                    table_style = padding.get("table_style")
                    if isinstance(table_style, dict):
                        padding_parts.append(
                            f"table style={table_style.get('style_id', 'UNKNOWN')}"
                        )
                        chain = table_style.get("based_on_chain")
                        if chain:
                            padding_parts.append(f"chain={' -> '.join(map(str, chain))}")
                        source = table_style.get("margin_source_style_id")
                        margins = table_style.get("horizontal_margin_twips")
                        if source and isinstance(margins, dict):
                            padding_parts.append(
                                f"margin source={source} "
                                f"(left={margins.get('left', 'UNKNOWN')}, "
                                f"right={margins.get('right', 'UNKNOWN')} twips)"
                            )
                        padding_parts.append(
                            "style margin used=" +
                            ("yes" if table_style.get("margin_used") else "no")
                        )
                    matrix = padding.get("twips_by_row")
                    if matrix is not None:
                        row_labels = "; ".join(
                            f"r{row_index}={values}" for row_index, values in enumerate(matrix)
                        )
                        padding_parts.append(f"per-cell twips: {row_labels}")
                    padding_label = "; ".join(padding_parts)
                lines.append(f"| `{safe(table.get('table_id', '?'))}` | "
                             f"{safe(grid_label)} | "
                             f"{safe(span_label)} | "
                             f"{safe(width_label(evidence.get('table_preferred', {})))} | "
                             f"{safe(cells_label)} | "
                             f"{safe(padding_label)} | "
                             f"{safe(evidence.get('word_rendered', 'NOT_RUN'))} |")
    if "non_body_story_tables" in result:
        lines += ["", "## Bảng trong header/footer/footnote/endnote", "",
                  "Các chỉ số này không dùng làm `--table`. Báo cáo liệt kê liên kết trực tiếp "
                  "và ứng viên kế thừa cùng loại cho default cùng first/even khi control nguồn "
                  "đang bật; story type lấy từ tên part chuẩn hoặc document relationship. "
                  "Footnote/endnote ID chỉ được đối chiếu với reference trong document body XML; "
                  "đây là bằng chứng cấu trúc nguồn, không xác nhận Word hiển thị hoặc quyền sở hữu "
                  "hiệu lực. Ứng viên kế thừa cũng không xác nhận quyền sở hữu hiệu lực trong Word.", "",
                  "| Part | Story type | Table ID | Parent table ID | Chỉ số trong part | SHA-256 | Owner evidence | Reference evidence | Trạng thái | Lý do |",
                  "|---|---|---|---|---:|---|---|---|---|---|"]
        for table in result["non_body_story_tables"]:
            references = "; ".join(
                f"section {ref.get('section_index', '?')} "
                f"{ref.get('story_type', '?')}/{ref.get('reference_type', '?')}" +
                (" (source activation "
                 f"{ref['activation'].get('status', 'UNKNOWN')}; "
                 f"{ref['activation'].get('control', 'UNKNOWN')}; "
                 f"{ref['activation'].get('evidence', 'UNKNOWN')})"
                 if ref.get("activation") else "")
                for ref in table.get("section_references", [])
            )
            candidate_labels = []
            for candidate in [
                *table.get("default_inheritance_candidates", []),
                *table.get("first_even_inheritance_candidates", []),
            ]:
                label = (
                    f"possible inherited section {candidate.get('section_index', '?')} "
                    f"{candidate.get('story_type', '?')}/"
                    f"{candidate.get('reference_type', '?')} "
                    f"from section {candidate.get('inherited_from_section_index', '?')}"
                )
                activation = candidate.get("activation")
                if activation:
                    label += (
                        " (section activation "
                        f"{activation.get('status', 'UNKNOWN')}; "
                        f"{activation.get('control', 'UNKNOWN')}; "
                        f"{activation.get('evidence', 'UNKNOWN')})"
                    )
                candidate_labels.append(label)
            candidates = "; ".join(candidate_labels)
            note_reference = table.get("note_reference")
            note_label = ""
            if isinstance(note_reference, dict):
                note_id = note_reference.get("note_id") or "UNKNOWN"
                reference_count = note_reference.get("body_reference_count")
                note_label = (
                    f"{note_reference.get('note_type') or 'note'} id {note_id} "
                    f"{note_reference.get('status', 'UNKNOWN')} "
                    f"(body_reference_count={reference_count if reference_count is not None else 'UNKNOWN'}; "
                    f"{note_reference.get('reference_scope', 'UNKNOWN')}; "
                    f"{note_reference.get('evidence', 'UNKNOWN')})"
                )
            reference_evidence = "; ".join(
                value for value in (references, candidates, note_label) if value
            ) or "unresolved"
            lines.append(f"| {safe(table.get('part', '?'))} | "
                         f"{safe(', '.join(table.get('story_types', [])) or 'UNKNOWN')} | "
                         f"`{safe(table.get('table_id', '?'))}` | "
                         f"`{safe(table.get('parent_table_id') or '—')}` | "
                         f"{table.get('story_table_index', '?')} | "
                         f"`{safe(table.get('table_sha256', '?'))}` | "
                         f"{safe(table.get('owner_status', 'UNKNOWN'))} | "
                         f"{safe(reference_evidence)} | "
                         f"{safe(table.get('status', 'UNKNOWN'))} | "
                         f"{safe(table.get('reason', 'UNKNOWN'))} |")
        if not result["non_body_story_tables"]:
            lines.append("| — | — | — | — | — | — | — | — | — | Không phát hiện bảng ngoài body |")
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
