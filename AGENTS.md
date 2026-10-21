# Quy tắc làm việc với ChuanhoaBang

## Mục đích
Kho tài liệu nghiên cứu/đặc tả về chuẩn hóa bảng Word trong văn bản hành chính và Đảng. Không suy diễn repo hiện tại đã có formatter hoạt động.

## Authority
- **Căn cứ pháp lý:** Nghị định 30/2020/NĐ-CP, Quy định 399-QĐ/TW, Hướng dẫn 05-HD/VPTW và các biểu mẫu/chuyên ngành áp dụng tại thời điểm sử dụng. Kiểm tra văn bản gốc và tình trạng hiệu lực trước khi kết luận.
- **Nguồn nghiên cứu hợp nhất:** `docs/research/Bao_cao_chuan_hoa_va_toi_uu_bang_DOCX_ND30_HD05_V15_2026.md`. Các phần V1–V14 đã được kế thừa bên trong.
- **Nghiệm thu:** `docs/verification/EXPERIMENT_EVIDENCE.md` ghi bằng chứng hiện có và giới hạn. Không đánh đồng mô phỏng LibreOffice với Microsoft Word.
- **Bằng chứng triển khai:** Code, CI, runtime, bản in Word và diff DOCX chỉ được báo PASS khi thực sự kiểm tra.

## Quy trình thay đổi
1. Xác định loại văn bản, loại bảng, đầu vào/đầu ra, vùng ảnh hưởng, mức quyền sửa và định nghĩa thành công.
2. Audit repo và công cụ/hệ điều hành đã có trước; ưu tiên REUSE LOCAL → EXTEND LOCAL → NATIVE API → OSS trưởng thành → MINIMUM NEW CODE.
3. Không nhân đôi engine DOCX, kho quy tắc, bộ parse, nguồn chân lý hoặc hệ thống kiểm chứng.
4. Định nghĩa contract sửa tối thiểu và bất biến: text, số liệu, công thức, ô gộp, bảng lồng, cấu trúc/quan hệ OPC, chữ ký, form locks, tracked changes và AlternateContent (nếu gặp).
5. Phân biệt HARD GATE (pháp lý/bảo toàn/hình học) với khuyến nghị thẩm mỹ.
6. So sánh với baseline trong cùng renderer, đo theo ô–hàng–bảng–trang, kiểm tra lại khả năng mở DOCX, không chỉ dựa vào XML hoặc điểm số.
7. Chấp nhận `NO_OP_VALID` khi không có cải thiện có chứng cứ; chặn/`REVIEW` khi confidence thấp; rollback khi validation thất bại.
8. Test theo phạm vi ảnh hưởng và tái sử dụng test/evidence đã PASS của phần bất biến; không tạo số lượng test mới chỉ để tăng chỉ tiêu.
9. Không mô tả 152 kịch bản đặc tả là 152 phép thử đã PASS.
10. Không tự commit, push, merge, deploy, migrate production, thay dữ liệu người dùng hoặc sửa phần đã khóa nếu chưa có yêu cầu/quyền tương ứng.

## Nguyên tắc tối ưu bảng
- Không cấp chiều rộng chỉ theo độ dài chữ: phải xét mục đích bảng, mức quan trọng của cột, khả năng ngắt dòng, số đo nội dung, ràng buộc lưới, trang in và ảnh hưởng đến chiều cao hàng.
- Kiểm tra riêng tổng lưới cột trong vùng hình học DOCX và đường viền/nội dung nhìn được trên bản kết xuất.
- Nếu section/lề/cỡ chữ/renderer thay đổi, không tái dùng chiều rộng cũ trước khi đánh giá lại.
- Không thu nhỏ font, xoay trang, thay bảng biểu mẫu hoặc chia/tách dữ liệu nếu chưa được phép.
- Thao tác trên Table Style, tcW/tblW/tblGrid, merge và phân trang phải được xét trong bối cảnh Word/OOXML hiện hữu.

## Nguyên tắc hoàn thành
Ghi rõ `PASS`, `FAIL`, `NOT_RUN`, `UNVERIFIED` và bộ công cụ thực hiện. Không khẳng định "đúng khi in Word" nếu chưa kiểm trên Microsoft Word/Print Layout phù hợp.
