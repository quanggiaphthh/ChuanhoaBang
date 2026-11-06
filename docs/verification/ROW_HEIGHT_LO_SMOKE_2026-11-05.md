# Hàng `Exactly` → `At least`: smoke test LibreOffice

**Ngày:** 05/11/2026 · **Trạng thái:** LO-only observational smoke; Microsoft Word NOT_RUN.

## Tình huống

- DOCX synthetic 2 hàng, 3 cột. Hàng 2 chứa mã `0012`, nội dung tiếng Việt nhiều dòng và trạng thái.
- Hàng 2 đặt `w:trHeight w:val="120" w:hRule="exact"` (**6 pt**).
- `propose_unclip_row_height` phát hiện chính xác hàng và đưa ra proposal cần người dùng áp dụng rõ ràng. `apply` chuyển **chỉ** `w:hRule="exact"` thành `"atLeast"`; giữ `w:val="120"`, nội dung và package ngoài scope.

## Phương pháp và quan sát

Render bằng LibreOffice headless thành PDF trước/sau, kiểm tra PDF bằng `pdftotext -layout`, render thành PNG 100 dpi và **quan sát bằng mắt**:

- **Trước:** phần thân hàng thứ hai bị cắt; PDF extraction chỉ còn phần đầu của nội dung.
- **Sau:** `0012`, nội dung tiếng Việt và trạng thái hiển thị đầy đủ; hàng mở rộng theo nội dung.
- Nội dung DOCX nguồn/đích qua diff cấu trúc không thay đổi.
- Đây là kiểm chứng giá trị phép sửa nhỏ cho một ca LO synthetic, **không suy rộng** rằng Microsoft Word có cùng kết quả hay tất cả row height exact đều phải chuyển.

## Bộ kiểm thử cục bộ

`PYTHONPATH=src python -m pytest -q` → **23 PASS**. Test bổ sung: phép sửa chỉ đổi rule, bảo toàn `w:val`, chặn proposal bị sửa, chặn document locked/complex và CLI end-to-end.

## Các cổng còn mở

- `L2_WORD_RENDER` = NOT_RUN; chưa có Word build/font TNR được xác minh.
- `OFFICIAL_FORM/PARTY_HD05` = chưa đủ fixture, không tự sửa.
- `PARAGRAPH_LINE_BOX` và `cantSplit` = chỉ chẩn đoán, chưa patch.
