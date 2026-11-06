# Repeat-header smoke QA — LibreOffice (không phải Word acceptance)

**Ngày:** 05/11/2026. **Trạng thái:** LO secondary renderer PASS về quan sát hàng tiêu đề trang 2; WORD_NOT_RUN.

## Đầu vào & thao tác

- Tạo DOCX tổng hợp 90 hàng trong `smoke/long_table.docx` trên môi trường thử cục bộ (không lưu nhị phân vào GitHub).
- `propose_header(source, 0)` trả `PROPOSE_APPLY`, áp `apply(source, proposal, destination)` tạo DOCX mới với **chỉ `w:tblHeader w:val=1` hàng đầu**, kiểm soát OPC và non-target parts.
- Chạy `libreoffice --headless --convert-to pdf` độc lập với file gốc và file đầu ra.
- `pdfinfo`, `pdftotext -f 2 -l 2 -layout` để quan sát trang 2, không OCR.

## Kết quả kiểm tra

| Quan sát | Trước | Sau |
|---|---|---|
| Tổng trang LibreOffice PDF | 12 | 13 |
| Chuỗi header `STT  Nội dung  Ghi chú` ở đầu trang thứ 2 | Không | Có |
| `audit.pagination_diagnostics.header_repeat_first_row` | False | True |
| Kiểm tra text, ô, OPC, non-target parts | N/A | PASS trong core invariant |
| Microsoft Word Print Layout | NOT_RUN | NOT_RUN |
| Times New Roman thực trên máy thử | UNVERIFIED (không có face bản quyền) | UNVERIFIED |

**Hạn chế:** LO thay font nếu thiếu Times New Roman. Không dùng lần render này để chứng minh chuẩn hình học/đẹp của bảng Word. Hàng tiêu đề lặp có chi phí chiều cao và có thể làm tăng số trang; không tối ưu theo số trang đơn thuần.

## Kiểm thử tự động

`PYTHONPATH=src python -m pytest -q` → **19 passed** trên Python 3.13, synthetic fixtures.
Các thử nghiệm width dùng fake font trong một số test, được gắn nhãn rõ ràng và không đại diện font TNR. Kiểm thử Word/WPS/font TNR thật vẫn chưa chạy.
