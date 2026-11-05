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
| Khoá, tracked changes, signed, merged/nested, layout heuristics | Detect/decline | Test subset PASS, cần thêm fixture |
| Hình học từ `sectPr/pgSz/pgMar` | Structural only | Không suy ra Word line breaks |
| Font TNR hiệu dụng | Explicit `w:rFonts/w:sz` only | Style cascade đầy đủ chưa có |
| Đo glyph có RAQM qua file TNR người dùng cung cấp | Conditional | Chưa được test bằng TNR thật trong runtime này |
| Optimizer width bounded local search | Implemented for simple tables | Điểm số là estimated line proxy |
| Apply/ZIP round trip | Implemented, whitelist props | Test structural PASS |
| Header/row pagination | Read-only diagnostics | Patch chưa triển khai |
| Word Print Layout / WPS | NOT_RUN | Không gắn Word PASS |
| WordVN editor/history/Undo | NOT_AUDITED | Chưa có integration |

## Các giới hạn chủ ý của bản đầu

- Chỉ bảng trong `word/document.xml`, không sửa header/footer. Body tables bên trong wrappers vẫn được thống kê, nhưng không tự sửa bảng trong content control hoặc bảng lồng.
- Chỉ bảng chữ đơn giản, không merged/field/object/track. Một section; font khai báo trực tiếp TNR 13/14, không automatic fallback.
- Vùng width từ OOXML là ràng buộc khai báo, không phải kết quả render. Padding sử dụng ngân sách bảo thủ **ước lượng**: 150 twips; chưa resolve toàn bộ style cascade.
- Chỉ có `audit → propose → explicit apply`; không tự chạy background; nguồn DOCX không bị ghi đè.

## Quy tắc bảo toàn

- Không thay `sectPr`, không xoay trang, không tự đổi font/size, dữ liệu hoặc topology.
- `apply` yêu cầu kiểm lại SHA của file/tbl, candidate, profile; từ chối proposal stale/đã chỉnh.
- Chỉ patch `w:tblGrid`, `w:tblW`, `w:tblLayout` và `w:tcW` của bảng được chọn; ZIP member không phải `word/document.xml` phải byte-identical. Ghi output tạm và rollback khi kiểm tra lỗi.
- Cần Word acceptance riêng trước khi tuyên bố bản in được bảo đảm.
