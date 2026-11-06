# ADR-CB-001 — Lõi DOCX offline và phạm vi v0.1

**Ngày:** 05/11/2026  
**Baseline:** `main` tại `13be13e0d34ee7f603a2bdd24e84493d7cae4c33`  
**Quyết định:** triển khai core Python `zipfile + lxml`, thư viện hình chữ Pillow/RAQM cho bảng đơn giản; chỉ vá XML `word/document.xml` đúng một bảng được chọn. Không khởi tạo service, graph DB, AI, editor hoặc renderer mới.

## Các phương án đã so sánh

| Phương án | Lợi thế | Rủi ro | Quyết định |
|---|---|---|---|
| A — Python + surgical OOXML | Không cần Word; dễ kiểm diff OPC và dùng lại nghiên cứu Python | Khả năng Word layout không được bảo đảm | **Chọn làm core offline v0.1** |
| B — WordVN TS/JS | Có thể tận dụng editor/Undo hiện có | Chưa audit được API/import-export WordVN trong scope repo này | **Giữ làm adapter, không tự giả định** |
| C — .NET OpenXML SDK | Mô hình OOXML mạnh | Thêm runtime, bridge và tăng chi phí đóng gói | Phương án thay thế nếu A không đạt về fidelity |
| `python-docx` open/save full | API dễ thao tác bảng | Nguy cơ chạm vào nội dung ngoài phạm vi, khó chứng minh chỉ sửa ít thuộc tính | Chỉ dùng làm generator/reader thử nghiệm |

## Capability thực tế

| Phạm vi | v0.1 | Trạng thái |
|---|---|---|
| Đọc và liệt kê body tables, trang đơn section | Implemented | Test synthetic PASS |
| Khoá, tracked changes, signed, nested, layout heuristics | Detect/decline; audit maps valid horizontal gridSpan cells; paging operations remain width-neutral | Test subset PASS, cần thêm fixture |
| Hình học từ `sectPr/pgSz/pgMar` | Structural only | Không suy ra Word line breaks |
| Font TNR hiệu dụng | Run trực tiếp và paragraph-style `basedOn` chain được hỗ trợ | Character/theme cascade và TNR có bản quyền chưa được xác nhận |
| Đo glyph có RAQM qua file TNR người dùng cung cấp | Conditional | Chưa được test bằng TNR thật trong runtime này |
| Optimizer width bounded local search | Implemented for simple tables | Điểm số là estimated line proxy |
| Apply/ZIP round trip | Implemented with operation-specific allowlists, snapshot revalidation, sync reporting | Synthetic structural CI PASS; power-loss `NOT_RUN` |
| Header/row pagination | Repeat-first-header và exact→atLeast theo explicit proposal; split diagnostic only | Synthetic CI PASS; Microsoft Word Print Layout chưa xác minh |
| Word Print Layout / WPS | NOT_RUN | Không gắn Word PASS |
| WordVN editor/history/Undo | BLOCKED: main tại commit `cea8f4bfd494e9e84050fed333aa0a39bed01191` chỉ có `README.md` | Import/export, selection/history, and Undo APIs chưa được triển khai; chưa có adapter |

## Các giới hạn chủ ý của bản đầu

- Chỉ bảng trong `word/document.xml`, không sửa header/footer. Body tables bên trong wrappers vẫn được thống kê, nhưng không tự sửa bảng trong content control hoặc bảng lồng.
- Chỉ AutoFit bảng chữ đơn giản, không merged/field/object/track. Audit ghi marker `vMerge` và kiểm tra tiếp diễn theo hàng dựa trên cùng logical-grid range; kết quả chỉ là source diagnostics. Hai phép phân trang không đổi width chỉ xử lý **gridSpan ngang đơn giản hợp lệ** khi không có hàng bỏ qua ô. Không sửa bảng vertical merge hoặc omitted-cell. Không xử lý nested. Một section; TNR size phải được giải từ run trực tiếp hoặc paragraph-style chain đã hỗ trợ; character/theme cascade và automatic fallback không được suy diễn.
- Vùng width từ OOXML là ràng buộc khai báo, không phải kết quả render. Direct left/right `dxa` table/cell margins được đưa vào bound từng ô; khi không có cặp ngang trực tiếp đã phân giải, estimator dùng ngân sách giả định 240 twips tổng (120 mỗi phía) theo policy registry. Báo cáo chỉ ghi giá trị giả định khi fallback thực sự được dùng; với margin trực tiếp đầy đủ, trường giả định là null. Nếu bảng có `tblStyle`, padding status được đặt `UNRESOLVED` cho đến khi cascade được phân giải. Đây là gợi ý nội bộ V15, không phải margin mặc định của Word. Table-style cascade và Word render vẫn chưa được xác minh.
- Có `audit → propose / propose-header / propose-unclip → explicit apply`; không tự chạy background; nguồn DOCX không bị ghi đè.

## Quy tắc bảo toàn

- Không thay `sectPr`, không xoay trang, không tự đổi font/size, dữ liệu hoặc topology.
- `apply` so proposal với source snapshot có SHA-256, dựng candidate từ snapshot đó và kiểm tra source path lại trước khi publish; proposal hoặc source stale bị từ chối.
- Mỗi operation có allowlist riêng: width chỉ sửa `w:tblGrid`, `w:tblW`, `w:tblLayout`, `w:tcW`; repeat-header chỉ sửa `w:tblHeader`; exact-row-height chỉ đổi `w:hRule` tại các hàng proposal đã duyệt. ZIP member ngoài `word/document.xml` phải byte-identical.
- Output được kiểm tra trước khi publish không ghi đè; candidate file được fsync trước khi publish, POSIX parent-directory sync được báo cáo sau publish. Physical power-loss acceptance vẫn `NOT_RUN`.
- Cần Word acceptance riêng trước khi tuyên bố bản in được bảo đảm.

## Quyết định bổ sung về danh sách thuộc tính OOXML được phép (05/11/2026)

- Bộ so sánh L0 đã chuyển sang **allowlist riêng cho từng operation**. OPTIMIZE_WIDTH chỉ bỏ qua phép đo width; SET_REPEAT_HEADER_FIRST_ROW chỉ bỏ qua `tblHeader` ở hàng đầu; EXACT_ROW_HEIGHT_TO_AT_LEAST chỉ bỏ qua thuộc tính `hRule` tại đúng `row_indices` đã phê duyệt.
- Không còn bỏ qua thay đổi `tblGrid/tcW/tblW` khi sửa header/height, hoặc bỏ qua hRule của hàng **không** thuộc đề xuất.
- Audit exposes source-only cell-to-grid ranges, local `vMerge` markers, per-row `gridBefore`/`gridAfter` counts, and a narrow continuation-to-restart range check. This does not establish Word-effective merge rendering. Tables with omitted grid cells or vertical merges remain review-only. Valid horizontal spans are allowed only for the two width-neutral paging operations. The width optimizer and all vertical-merge edits remain blocked pending licensed TNR and Microsoft Word geometry gates.
- CI 43/43 PASS theo fixture tổng hợp; chưa có Word Print Layout hoặc TNR bản quyền.

## Cập nhật hướng kiến trúc cho v1.0 — 06/11/2026

- Giữ một engine Python offline duy nhất (`zipfile` + `lxml`), với CLI và Python API dùng chung core. `audit` cung cấp inspect/analyze; `propose`, `propose-header`, `propose-unclip` tạo proposal có giới hạn; `apply` revalidate proposal, kiểm tra candidate và chỉ publish khi các gate cấu trúc đạt. Không có network service, AI backend hoặc renderer mới trong đường chạy.
- Validation hiện là bước bắt buộc bên trong `apply`; chưa có command/API `validate` riêng. `word_render` luôn `NOT_RUN` nếu không có Microsoft Word verification. ND30/HD05 vẫn `REFERENCE_ONLY`; currentness và toàn bộ profile rule set chưa được xác nhận.
- Standalone offline CLI/API là đường triển khai v1.0 theo mục tiêu sản phẩm hiện hành. Không phụ thuộc WordVN editor adapter: repo `quanggiaphthh/WordVN` ở main commit [`cea8f4b`](https://github.com/quanggiaphthh/WordVN/commit/cea8f4bfd494e9e84050fed333aa0a39bed01191) chỉ chứa README, nên chưa có importer/exporter, selection/history hoặc Undo contract để tích hợp. Nếu editor API xuất hiện sau này, adapter cần một quyết định riêng; hiện không tạo engine thứ hai.
- CI [run 42175255868](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42175255868) passed six jobs: 221 tests on Ubuntu/Python 3.10–3.13; Windows/Python 3.12 passed 220 with one POSIX-only directory-sync test skipped. Canonical and independent-runner wheel SHA-256 matched. Synthetic CI does not establish Word/WPS, TNR licensing, legal currentness, original-fixture, or power-loss acceptance.
