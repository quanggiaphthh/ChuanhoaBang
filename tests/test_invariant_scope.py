"""L0 invariant: each operation may change only its explicitly whitelisted OOXML."""
import copy
from zipfile import ZipFile

import pytest
from docx import Document
from lxml import etree

from chuanhoabang import TableError
from chuanhoabang import core


def _document_xml(tmp_path):
    doc = Document()
    table = doc.add_table(rows=3, cols=3)
    for row, values in zip(table.rows, [
        ("STT", "Nội dung", "Ghi chú"),
        ("0012", "Nhiệm vụ A", "Đang thực hiện"),
        ("0", "Nhiệm vụ B", "Hoàn thành"),
    ]):
        for cell, text in zip(row.cells, values):
            cell.text = text
    file = tmp_path / "input.docx"
    doc.save(file)
    with ZipFile(file) as package:
        return package.read("word/document.xml")


def _add_exact_height(root, row_index):
    table = core._tables(root)[0]
    row = table.findall(core.W + "tr")[row_index]
    props = row.find(core.W + "trPr")
    if props is None:
        props = etree.Element(core.W + "trPr")
        row.insert(0, props)
    height = props.find(core.W + "trHeight")
    if height is None:
        height = etree.SubElement(props, core.W + "trHeight")
    height.set(core.W + "val", "120")
    height.set(core.W + "hRule", "exact")


def test_header_change_only_header_is_allowed(tmp_path):
    original = _document_xml(tmp_path)
    modified = core._xml(original)
    core._apply_header(modified, 0)
    core._assert_safe(original, etree.tostring(modified), 0, allow_first_row_header=True)


def test_header_must_not_mask_unapproved_width_change(tmp_path):
    original = _document_xml(tmp_path)
    modified = core._xml(original)
    core._apply_header(modified, 0)
    grid = core._tables(modified)[0].find(core.W + "tblGrid")
    grid[0].set(core.W + "w", "777")
    with pytest.raises(TableError, match="TARGET_NON_WIDTH_CONTENT_CHANGED"):
        core._assert_safe(original, etree.tostring(modified), 0, allow_first_row_header=True)


def test_height_change_only_whitelisted_row_allowed(tmp_path):
    baseline = core._xml(_document_xml(tmp_path))
    _add_exact_height(baseline, 1)
    _add_exact_height(baseline, 2)
    original = etree.tostring(baseline)
    modified = core._xml(original)
    core._apply_unclip_row_heights(modified, 0, [1])
    core._assert_safe(original, etree.tostring(modified), 0,
                      allow_height_rule=True, height_rows=(1,))
    # Unauthorized change to another row must not be masked by an allowed repair.
    core._apply_unclip_row_heights(modified, 0, [2])
    with pytest.raises(TableError, match="TARGET_NON_WIDTH_CONTENT_CHANGED"):
        core._assert_safe(original, etree.tostring(modified), 0,
                          allow_height_rule=True, height_rows=(1,))


def test_height_change_must_not_mask_unapproved_width_change(tmp_path):
    baseline = core._xml(_document_xml(tmp_path))
    _add_exact_height(baseline, 1)
    original = etree.tostring(baseline)
    modified = core._xml(original)
    core._apply_unclip_row_heights(modified, 0, [1])
    core._tables(modified)[0].find(core.W + "tblGrid")[0].set(core.W + "w", "777")
    with pytest.raises(TableError, match="TARGET_NON_WIDTH_CONTENT_CHANGED"):
        core._assert_safe(original, etree.tostring(modified), 0,
                          allow_height_rule=True, height_rows=(1,))


def test_width_change_allowed_but_height_change_rejected(tmp_path):
    original = _document_xml(tmp_path)
    modified = core._xml(original)
    grid = core._tables(modified)[0].find(core.W + "tblGrid")
    widths = [int(n.get(core.W + "w")) for n in grid]
    widths[0] += 100
    widths[1] -= 100
    core._apply_widths(modified, 0, widths)
    core._assert_safe(original, etree.tostring(modified), 0)
    _add_exact_height(modified, 1)
    with pytest.raises(TableError, match="TARGET_NON_WIDTH_CONTENT_CHANGED"):
        core._assert_safe(original, etree.tostring(modified), 0)


def test_height_scope_validation_fails_closed(tmp_path):
    original = _document_xml(tmp_path)
    with pytest.raises(TableError, match="HEIGHT_ROW_SCOPE_INVALID"):
        core._assert_safe(original, original, 0, allow_height_rule=True, height_rows=())
    with pytest.raises(TableError, match="HEIGHT_ROW_SCOPE_INVALID"):
        core._assert_safe(original, original, 0, allow_height_rule=True, height_rows=(0, 0))
    with pytest.raises(TableError, match="MULTIPLE_UNSAFE_OPERATIONS"):
        core._assert_safe(original, original, 0,
                          allow_first_row_header=True, allow_height_rule=True, height_rows=(1,))
