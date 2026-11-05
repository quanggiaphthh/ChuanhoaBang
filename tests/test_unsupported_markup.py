"""Regression: unsupported WordprocessingML structures must not be silently reformatted."""
from zipfile import ZipFile
from lxml import etree
from docx import Document
from docx.shared import Pt
import pytest
from chuanhoabang import audit, propose, propose_header, propose_unclip_row_height
from chuanhoabang import core


@pytest.mark.parametrize("element,container", [
    ("fldSimple", "tc"),
    ("commentReference", "r"),
    ("commentRangeStart", "tc"),
    ("customXml", "tc"),
    ("smartTag", "p"),
    ("bookmarkStart", "p"),
    ("permStart", "p"),
])
def test_unsupported_word_markup_fail_closed(tmp_path, element, container):
    source = tmp_path / "original.docx"
    doc = Document()
    t = doc.add_table(rows=2, cols=3)
    for row, values in zip(t.rows, [("STT", "Nội dung", "Ghi chú"),
                                    ("0012", "Nội dung bảo toàn", "Hoàn thành")]):
        for cell, value in zip(row.cells, values):
            cell.text = ""
            run = cell.paragraphs[0].add_run(value)
            run.font.name = "Times New Roman"
            run.font.size = Pt(14)
    doc.save(source)
    with ZipFile(source) as zi:
        entries = [(info, zi.read(info.filename)) for info in zi.infolist()]
    with ZipFile(source, "w") as zo:
        for info, data in entries:
            if info.filename == "word/document.xml":
                root = core._xml(data)
                cell = root.xpath(".//w:body/w:tbl/w:tr[2]/w:tc[2]", namespaces=core.NS)[0]
                if container == "tc":
                    parent = cell
                elif container == "p":
                    parent = cell.find(core.W + "p")
                else:
                    parent = cell.find(core.W + "p").find(core.W + "r")
                extra = etree.SubElement(parent, core.W + element)
                if element == "fldSimple":
                    extra.set(core.W + "instr", "PAGE")
                elif element in ("bookmarkStart", "commentRangeStart", "permStart"):
                    extra.set(core.W + "id", "1")
                data = etree.tostring(root, encoding="UTF-8", xml_declaration=True)
            zo.writestr(info, data)
    original_hash = core.digest(source.read_bytes())
    result = audit(source)
    assert result["tables"][0]["status"] == "REVIEW_REQUIRED"
    assert "COMPLEX_CONTENT_OR_TRACKED_CHANGES" in result["tables"][0]["reasons"]
    assert propose(source, 0)["decision"] == "REVIEW_REQUIRED"
    assert propose_header(source, 0)["decision"] == "REVIEW_REQUIRED"
    assert propose_unclip_row_height(source, 0)["decision"] == "REVIEW_REQUIRED"
    assert core.digest(source.read_bytes()) == original_hash
