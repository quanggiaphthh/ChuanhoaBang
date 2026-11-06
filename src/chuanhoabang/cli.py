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

    def table_layout_label(evidence):
        if not isinstance(evidence, dict):
            return "NOT_REPORTED"
        status = evidence.get("status", "UNKNOWN")
        types = evidence.get("declared_types", [])
        label = status
        if types:
            label += ": " + ", ".join(value if value is not None else "MISSING_TYPE"
                                      for value in types)
        elif status == "NO_DIRECT_DECLARATION":
            label += ": no direct declaration"
        label += f"; effective={evidence.get('effective_type', 'NOT_RESOLVED')}"
        issues = evidence.get("issues", [])
        if issues:
            label += "; issues=" + ", ".join(issues)
        return label

    def table_direction_label(evidence):
        if not isinstance(evidence, dict):
            return "NOT_REPORTED"
        status = evidence.get("status", "UNKNOWN")
        direction = evidence.get("right_to_left_visual_order")
        if status == "NO_DIRECT_DECLARATION":
            label = "NO_DIRECT_DECLARATION: no direct declaration"
        elif direction is True:
            label = f"{status}: RIGHT_TO_LEFT"
        elif direction is False:
            label = f"{status}: RIGHT_TO_LEFT_DISABLED"
        else:
            label = status
        values = evidence.get("declared_values", [])
        if values:
            values_label = ", ".join(
                "OMITTED" if value is None else str(value) for value in values
            )
            label += f"; w:val={values_label}"
        label += f"; effective={evidence.get('effective_direction', 'NOT_RESOLVED')}"
        issues = evidence.get("issues", [])
        if issues:
            label += "; issues=" + ", ".join(issues)
        return label

    def table_spacing_label(evidence):
        if not isinstance(evidence, dict):
            return "NOT_REPORTED"
        status = evidence.get("status", "UNKNOWN")
        spacing = evidence.get("spacing_twips")
        if status == "NO_DIRECT_DECLARATION":
            label = "NO_DIRECT_DECLARATION: no direct declaration"
        elif spacing is not None:
            label = f"{status}: {spacing} twips dxa"
        else:
            label = status
        label += f"; effective={evidence.get('effective_spacing', 'NOT_RESOLVED')}"
        issues = evidence.get("issues", [])
        if issues:
            label += "; issues=" + ", ".join(issues)
        return label

    def border_geometry_label(evidence):
        if not isinstance(evidence, dict):
            return "NOT_REPORTED"
        status = evidence.get("status", "UNKNOWN")
        values = evidence.get("declared_values", [])
        size_values = evidence.get("size_declarations", [])
        missing_size_values = evidence.get("missing_size_declarations", [])
        if not values and not size_values and not missing_size_values:
            label = ("NO_DIRECT_BORDER_GEOMETRY" if status == "NO_DIRECT_BORDER_GEOMETRY"
                     else status)
        else:
            entries = [
                (f"row{value.get('row_index', '?')}:cell{value.get('cell_index', '?')}"
                 if value.get("scope") == "cell" else value.get("scope", "unknown"))
                + f":{value.get('edge', 'unknown')} "
                f"{value.get('space_points', 'INVALID')} pt"
                for value in values
            ]
            entries.extend(
                (f"row{value.get('row_index', '?')}:cell{value.get('cell_index', '?')}"
                 if value.get("scope") == "cell" else value.get("scope", "unknown"))
                + f":{value.get('edge', 'unknown')} "
                f"{value.get('size_points', 'INVALID')} pt border "
                f"(w:sz={value.get('raw_size', '?')})"
                for value in size_values
            )
            entries.extend(
                (f"row{value.get('row_index', '?')}:cell{value.get('cell_index', '?')}"
                 if value.get("scope") == "cell" else value.get("scope", "unknown"))
                + f":{value.get('edge', 'unknown')} {value.get('border_style', 'UNKNOWN')} "
                "border missing w:sz"
                for value in missing_size_values
            )
            label = status + ": " + ", ".join(entries)
        label += f"; effective={evidence.get('effective_border_geometry', 'NOT_RESOLVED')}"
        issues = evidence.get("issues", [])
        if issues:
            label += "; issues=" + ", ".join(issues)
        return label

    def parent_cell_label(owner):
        if not isinstance(owner, dict):
            return "—"
        if owner.get("status") != "LOCATED_IN_SOURCE_XML":
            return owner.get("reason", owner.get("status", "UNRESOLVED"))
        return (f"row {owner.get('row_index', '?')}, cell {owner.get('cell_index', '?')} "
                f"({owner.get('evidence', 'UNKNOWN')})")

    lines = ["# ChuanhoaBang — Báo cáo xử lý DOCX", "",
             f"**Quyết định:** `{safe(result.get('decision', result.get('status', 'AUDIT_ONLY')))}`",
             f"**Kết xuất Microsoft Word:** `{safe(result.get('word_render', 'NOT_RUN'))}`",
             "", "## Thông tin xử lý", "", "| Thuộc tính | Giá trị |", "|---|---|"]
    for key in ("file", "output", "input_sha256", "output_sha256", "policy",
                "profile", "profile_status", "profile_rules_applied", "profile_constraints",
                "table_index", "table_count", "non_body_story_table_count", "operation", "evidence",
                "parent_table_id", "parent_cell_location", "role_classification",
                "table_layout_evidence",
                "table_direction_evidence",
                "table_cell_spacing_evidence",
                "border_geometry_evidence",
                "cell_grid_spans", "row_grid_omissions",
                "vertical_merge_chain_validation",
                "content_integrity", "non_target_package_parts",
                "filesystem_durability"):
        if key in result:
            value = (json.dumps(result[key], ensure_ascii=False)
                     if key in ("parent_cell_location", "role_classification",
                                "table_layout_evidence",
                                "table_direction_evidence",
                                "table_cell_spacing_evidence",
                                "border_geometry_evidence",
                                "cell_grid_spans", "row_grid_omissions",
                                "vertical_merge_chain_validation",
                                "filesystem_durability") else result[key])
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
                  "| Table ID | Parent table ID | Parent cell | Role candidate / evidence | tblLayout evidence | Direction evidence | Cell spacing evidence | Border geometry evidence | STT | Trạng thái | Hàng | Cột | Lý do |",
                  "|---|---|---|---|---|---|---|---|---:|---|---:|---:|---|"]
        for table in result["tables"]:
            parent_id = table.get("parent_table_id") or "—"
            role = table.get("role_classification") or {}
            role_label = (
                f"{role.get('classification', 'UNKNOWN')}; "
                f"{', '.join(role.get('evidence', [])) or 'NO_EVIDENCE'}; "
                f"markers={', '.join(role.get('matched_markers', [])) or 'NONE'}; "
                f"authority={role.get('authority', 'NOT_ESTABLISHED')}"
            )
            lines.append(f"| `{safe(table.get('table_id', '?'))}` | "
                         f"`{safe(parent_id)}` | "
                         f"{safe(parent_cell_label(table.get('parent_cell_location')))} | "
                         f"{safe(role_label)} | "
                         f"{safe(table_layout_label(table.get('table_layout_evidence')))} | "
                         f"{safe(table_direction_label(table.get('table_direction_evidence')))} | "
                         f"{safe(table_spacing_label(table.get('table_cell_spacing_evidence')))} | "
                         f"{safe(border_geometry_label(table.get('border_geometry_evidence')))} | "
                         f"{table.get('index', '?')} | "
                         f"{safe(table.get('status', 'UNKNOWN'))} | "
                         f"{table.get('rows', '?')} | {table.get('columns', '?')} | "
                         f"{safe(', '.join(table.get('reasons', [])))} |")
        if any("width_evidence" in table for table in result["tables"]):
            lines += ["", "## Width evidence (OOXML declarations; not Word measurements)", "",
                      "| Table ID | Grid and sum | Cell spans, merge continuation, omitted columns (source XML) | tblW preferred | tcW preferred by row/cell | Cell padding evidence | Word rendered width |",
                      "|---|---|---|---|---|---|---|"]
            for table in result["tables"]:
                evidence = table.get("width_evidence", {})
                grid = table.get("grid_twips")
                grid_sum = evidence.get("grid_sum_twips")
                grid_label = (f"grid={grid if grid is not None else 'UNKNOWN'} twips; "
                              f"sum={grid_sum if grid_sum is not None else 'UNKNOWN'} twips")
                span_evidence = table.get("cell_grid_spans")
                if (table.get("row_grid_omissions") is not None or
                        table.get("vertical_merge_chain_validation") is not None):
                    span_evidence = {"cell_grid_spans": span_evidence}
                    if table.get("row_grid_omissions") is not None:
                        span_evidence["row_grid_omissions"] = table[
                            "row_grid_omissions"
                        ]
                    if table.get("vertical_merge_chain_validation") is not None:
                        span_evidence["vertical_merge_chain_validation"] = table[
                            "vertical_merge_chain_validation"
                        ]
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
                  "| Part | Story type | Role candidate / evidence | tblLayout evidence | Direction evidence | Cell spacing evidence | Border geometry evidence | Table ID | Parent table ID | Parent cell | Chỉ số trong part | SHA-256 | Owner evidence | Reference evidence | Trạng thái | Lý do |",
                  "|---|---|---|---|---|---|---|---|---|---|---:|---|---|---|---|---|"]
        for table in result["non_body_story_tables"]:
            role = table.get("role_classification") or {}
            role_label = (
                f"{role.get('classification', 'UNKNOWN')}; "
                f"{', '.join(role.get('evidence', [])) or 'NO_EVIDENCE'}; "
                f"markers={', '.join(role.get('matched_markers', [])) or 'NONE'}; "
                f"authority={role.get('authority', 'NOT_ESTABLISHED')}"
            )
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
                         f"{safe(role_label)} | "
                         f"{safe(table_layout_label(table.get('table_layout_evidence')))} | "
                         f"{safe(table_direction_label(table.get('table_direction_evidence')))} | "
                         f"{safe(table_spacing_label(table.get('table_cell_spacing_evidence')))} | "
                         f"{safe(border_geometry_label(table.get('border_geometry_evidence')))} | "
                         f"`{safe(table.get('table_id', '?'))}` | "
                         f"`{safe(table.get('parent_table_id') or '—')}` | "
                         f"{safe(parent_cell_label(table.get('parent_cell_location')))} | "
                         f"{table.get('story_table_index', '?')} | "
                         f"`{safe(table.get('table_sha256', '?'))}` | "
                         f"{safe(table.get('owner_status', 'UNKNOWN'))} | "
                         f"{safe(reference_evidence)} | "
                         f"{safe(table.get('status', 'UNKNOWN'))} | "
                         f"{safe(table.get('reason', 'UNKNOWN'))} |")
        if not result["non_body_story_tables"]:
            lines.append("| — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Không phát hiện bảng ngoài body |")
    border_tables = [
        (scope, table)
        for scope, entries in (("body", result.get("tables", [])),
                               ("story", result.get("non_body_story_tables", [])))
        for table in entries
        if isinstance(table.get("border_evidence"), dict)
    ]
    if border_tables:
        lines += ["", "## Direct border declarations (OOXML source; style inheritance unresolved)", "",
                  "This inventory reports direct `tblBorders` and `tcBorders` declarations. "
                  "Style/theme inheritance is not resolved; Word rendering is `NOT_RUN`.", "",
                  "| Scope | Table ID | Status | Table edges | Cell edges | Style inheritance | Word render | Issues |",
                  "|---|---|---|---|---|---|---|---|"]
        for scope, table in border_tables:
            evidence = table["border_evidence"]
            table_edges = json.dumps(evidence.get("table_borders", []), ensure_ascii=False,
                                     separators=(",", ":"))
            cell_edges = json.dumps(evidence.get("cell_borders", []), ensure_ascii=False,
                                    separators=(",", ":"))
            issues = ", ".join(evidence.get("issues", [])) or "—"
            lines.append(
                f"| {scope} | `{safe(table.get('table_id', '?'))}` | "
                f"`{safe(evidence.get('status', 'UNKNOWN'))}` | {safe(table_edges)} | "
                f"{safe(cell_edges)} | `{safe(evidence.get('style_inheritance', 'UNKNOWN'))}` | "
                f"`{safe(evidence.get('word_render', 'NOT_RUN'))}` | {safe(issues)} |"
            )
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
