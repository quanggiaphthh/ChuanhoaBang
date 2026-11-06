"""Regression: unsupported WordprocessingML structures must not be silently reformatted."""
from zipfile import ZipFile
from lxml import etree
from docx import Document
from docx.shared import Pt
import pytest
from chuanhoabang import audit, apply, propose, propose_header, propose_unclip_row_height
from chuanhoabang import TableError
from chuanhoabang import core

MC = "http://schemas.openxmlformats.org/markup-compatibility/2006"


def test_alternate_content_around_table_fails_closed(tmp_path):
    source = tmp_path / "alternate-content.docx"
    doc = Document()
    table = doc.add_table(rows=2, cols=3)
    for row, values in zip(table.rows, [("STT", "Nội dung", "Ghi chú"),
                                        ("0012", "Nội dung bảo toàn", "Hoàn thành")]):
        for cell, value in zip(row.cells, values):
            cell.text = ""
            run = cell.paragraphs[0].add_run(value)
            run.font.name = "Times New Roman"
            run.font.size = Pt(14)
    doc.save(source)
    with ZipFile(source) as package:
        entries = [(info, package.read(info.filename)) for info in package.infolist()]
    with ZipFile(source, "w") as package:
        for info, data in entries:
            if info.filename == "word/document.xml":
                root = core._xml(data)
                table = root.xpath("./w:body/w:tbl", namespaces=core.NS)[0]
                body = table.getparent()
                index = body.index(table)
                body.remove(table)
                alternate = etree.Element(f"{{{MC}}}AlternateContent", nsmap={"mc": MC})
                choice = etree.SubElement(alternate, f"{{{MC}}}Choice", Requires="w")
                choice.append(table)
                fallback = etree.SubElement(alternate, f"{{{MC}}}Fallback")
                fallback.append(etree.Element(core.W + "p"))
                body.insert(index, alternate)
                data = etree.tostring(root, encoding="UTF-8", xml_declaration=True)
            package.writestr(info, data)
    original = source.read_bytes()

    report = audit(source)

    assert "ALTERNATE_CONTENT_NOT_SUPPORTED" in report["global_locks"]
    assert report["tables"][0]["status"] == "REVIEW_REQUIRED"
    assert "ALTERNATE_CONTENT_NOT_SUPPORTED" in report["tables"][0]["reasons"]
    assert propose_header(source, 0)["decision"] == "REVIEW_REQUIRED"
    assert source.read_bytes() == original


def test_permission_range_outside_table_forces_review(tmp_path):
    source = tmp_path / "permission-range.docx"
    doc = Document()
    table = doc.add_table(rows=2, cols=3)
    for row, values in zip(table.rows, [("STT", "Nội dung", "Ghi chú"),
                                        ("0012", "Nội dung bảo toàn", "Hoàn thành")]):
        for cell, value in zip(row.cells, values):
            cell.text = ""
            run = cell.paragraphs[0].add_run(value)
            run.font.name = "Times New Roman"
            run.font.size = Pt(14)
    doc.save(source)
    with ZipFile(source) as package:
        entries = [(info, package.read(info.filename)) for info in package.infolist()]
    with ZipFile(source, "w") as package:
        for info, data in entries:
            if info.filename == "word/document.xml":
                root = core._xml(data)
                table = root.xpath("./w:body/w:tbl", namespaces=core.NS)[0]
                body = table.getparent()
                index = body.index(table)
                start_paragraph = etree.Element(core.W + "p")
                etree.SubElement(start_paragraph, core.W + "permStart", {core.W + "id": "7"})
                end_paragraph = etree.Element(core.W + "p")
                etree.SubElement(end_paragraph, core.W + "permEnd", {core.W + "id": "7"})
                body.insert(index, start_paragraph)
                body.insert(body.index(table) + 1, end_paragraph)
                data = etree.tostring(root, encoding="UTF-8", xml_declaration=True)
            package.writestr(info, data)
    original = source.read_bytes()

    report = audit(source)

    assert "RANGE_PERMISSIONS_UNRESOLVED" in report["global_locks"]
    assert report["tables"][0]["status"] == "REVIEW_REQUIRED"
    assert propose_header(source, 0)["decision"] == "REVIEW_REQUIRED"
    assert source.read_bytes() == original


@pytest.mark.parametrize(("part_name", "reason"), [
    ("_xmlsignatures/sig1.xml", "SIGNED_OPC_PACKAGE"),
    ("word/vbaProject.bin", "MACRO_CONTENT_NOT_SUPPORTED"),
])
def test_signed_or_macro_package_fails_closed(tmp_path, part_name, reason):
    source = tmp_path / "protected-package.docx"
    doc = Document()
    table = doc.add_table(rows=2, cols=3)
    for row, values in zip(table.rows, [("STT", "Nội dung", "Ghi chú"),
                                        ("0012", "Nội dung bảo toàn", "Hoàn thành")]):
        for cell, value in zip(row.cells, values):
            cell.text = ""
            run = cell.paragraphs[0].add_run(value)
            run.font.name = "Times New Roman"
            run.font.size = Pt(14)
    doc.save(source)
    original_proposal = propose_header(source, 0)
    assert original_proposal["decision"] == "PROPOSE_APPLY"
    with ZipFile(source) as package:
        entries = [(info, package.read(info.filename)) for info in package.infolist()]
    with ZipFile(source, "w") as package:
        for info, data in entries:
            package.writestr(info, data)
        package.writestr(part_name, b"synthetic unsupported package-part marker")
    original = source.read_bytes()

    report = audit(source)

    assert reason in report["global_locks"]
    assert report["tables"][0]["status"] == "REVIEW_REQUIRED"
    assert reason in report["tables"][0]["reasons"]
    assert propose(source, 0)["decision"] == "REVIEW_REQUIRED"
    assert propose_header(source, 0)["decision"] == "REVIEW_REQUIRED"
    assert propose_unclip_row_height(source, 0)["decision"] == "REVIEW_REQUIRED"
    output = tmp_path / "must-not-be-published.docx"
    with pytest.raises(TableError, match="STALE_OR_MODIFIED_PROPOSAL"):
        apply(source, original_proposal, output)
    assert not output.exists()
    assert source.read_bytes() == original


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
