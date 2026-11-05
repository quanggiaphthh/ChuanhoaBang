# Kiểm soát phát hành và những việc chưa nghiệm thu

## Trạng thái tại nhánh kỹ thuật v0.1

- **Đã chạy:** kiểm thử đọc/sửa/ghi DOCX tổng hợp (pytest) với mock/synthetic width metrics, đối chiếu cấu trúc và giữ nguồn nguyên bản.
- **Chưa chạy:** TNR thực dưới font fingerprint đã cấp phép, WPS/Microsoft Word Print Layout, corpus F01–F08 gốc, WordVN adapter.
- **Không tuyên bố:** v1.0, tương thích đầy đủ ND30/HD05, Word layout PASS, 128/152 kịch bản đã PASS.

## Gates

| Gate | Yêu cầu để v1.0 | Trạng thái ở technical preview |
|---|---|---|
| DATA | Bảo toàn số liệu, text, topology theo supported types | PASS synthetic subset: **83/83** on Ubuntu/Python 3.10–3.13 and Windows/Python 3.12 in [run 42092032457](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42092032457); not Word acceptance |
| OPC | Non-target parts và target non-width properties giữ nguyên | PASS synthetic subset: **83/83** in [run 42092032457](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42092032457), all five environments; validation-failure cleanup, concurrent-destination no-overwrite, and read-only story inventory regressions PASS |
| AUTH | Bảng layout, locked/unknown bị loại; policy V17.5.1 | PASS synthetic subset in the 83-test suite across five environments; table-wide layout-marker scan fails closed; complete legal-profile coverage PARTIAL |
| GEO | Width candidate không vượt vùng có thể, không tự landscape | PASS synthetic subset in the 83-test suite; multi-column/custom-column and mirrored-margin-plus-gutter geometry fail closed. Word page layout not verified |
| FONT | Shaping TNR thực và style cascade đầy đủ | PARTIAL, TNR runtime test NOT_RUN |
| PAGING | Header repeat/row split/trHeight xử lý theo quyền | First-row repeat + exact→atLeast row height opt-in structural PASS; row split DIAGNOSTICS_ONLY; Word NOT_RUN |
| COMPLEX | Merged/nested controlled support | PARTIAL: gridSpan ngang hợp lệ chỉ được phép header-repeat / exact→atLeast; AutoFit merged, vMerge, nested vẫn PRESERVE |
| L2-WORD | Print Layout Word không tràn/cắt | NOT_RUN; [manual protocol](../verification/WORD_ACCEPTANCE_PROTOCOL.md) is ready. Current executor has no Microsoft Word |
| WPS/LO | Renderer đối chứng | LibreOffice secondary smoke PASS on synthetic pagination/row-height fixtures ([header](../verification/HEADER_REPEAT_LO_SMOKE_2026-11-05.md), [row height](../verification/ROW_HEIGHT_LO_SMOKE_2026-11-05.md)); WPS NOT_RUN. Neither establishes Word acceptance |
| WORDVN | Adapter, preview, Undo | Source repo `quanggiaphthh/WordVN` hiện chỉ có README (05/11/2026); editor/API/Undo NOT_IMPLEMENTED, adapter BLOCKED |
| RELEASE | Clean install, pin dependencies, reproducible binary + rollback | PARTIAL: `uv.lock` pins runtime/test dependencies; exact setuptools/wheel build pins; [run 42092032457](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42092032457) built the preview wheel twice with matching SHA-256, wrote a source/lock/tool/artifact manifest, then installed that same artifact across five environments. Independent-builder reproducibility, release/update rollback, versioned release notes, and offline wheelhouse NOT_RUN |

**Nguyên tắc:** Có thể dùng CLI thử nghiệm cho phạm vi đã chứng minh; không đóng issue #7, #8, #11–#16 khi thiếu acceptance theo body issue. Không đóng những issue chỉ có tài liệu một phần.


## Tiến độ kiểm thử bổ sung 05/11/2026

- CI Python 3.11 chạy đủ thư mục `tests/`: **33 PASS** tại commit `138f709663fa21e62b8d5b067158c62958ba951b` (và commit mới nhất phải được đối chiếu CI riêng).
- Tăng fail-closed cho `fldSimple`, comment markers, `customXml`, `smartTag`, bookmark/permission, content part: **7 case regression**.
- CLI đã hỗ trợ Markdown report và kiểm tra xung đột đường dẫn để không ghi đè DOCX/JSON.
- Các ca này là kiểm thử OOXML/source integrity trên dữ liệu tổng hợp, không phải nghiệm thu Word hay TNR bản quyền.
- WordVN kiểm tra bằng GitHub connector: `main` hiện chỉ chứa README greenfield, **không có editor API hoặc Undo để tích hợp thực tế**. Không tự tạo adapter dựa trên API giả định.


## Bổ sung CI và giới hạn 05/11/2026 — kiểm tra scope chính xác

- [CI run 42042985209](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42042985209), commit `c518e5070d115806bf42003ffe8d36fcf4f45c3d`: **43/43 PASS**.
- 6 ca kiểm tra mỗi operation chỉ được sửa whitelist thuộc tính riêng, thêm 4 ca `gridSpan` ngang/vertical/malformed.
- Không thay đổi orientation/font/dữ liệu/merge topology; các trường hợp Word layout và ảnh hưởng in vẫn NOT_RUN.
- Bằng chứng pass CI của code **không** thay thế việc nhập fixture F01–F08 gốc, font TNR thật, Microsoft Word hoặc WPS.
