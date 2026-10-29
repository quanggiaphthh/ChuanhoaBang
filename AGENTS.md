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

## Policy ưu tiên — V17.5.1 / USER-ORIENTATION-001 (29/10/2026)

- **Mọi bảng/tài liệu mới mặc định hướng trang DỌC (PORTRAIT)** nếu người dùng không chỉ định.
- **Chỉ người dùng được yêu cầu chuyển hướng trang** (ngang hoặc dọc). Width overflow, nhiều cột, điểm thẩm mỹ, khuyến nghị AI hoặc rule offline **không được tự kích hoạt thay đổi orientation**.
- DOCX hiện có, nếu không có yêu cầu đổi hướng, **giữ nguyên orientation của mọi section** (kể cả section đã ngang).
- Nếu trang dọc quá hẹp: cảnh báo `PORTRAIT_WIDTH_RISK`/`REVIEW_REQUIRED`, tối ưu an toàn trong phạm vi quyền; nếu không thể bảo toàn thì `NO_SAFE_PORTRAIT_FIT`, không tự xoay trang.
- Ngay cả khi có yêu cầu ngang, chỉ đánh giá/thực hiện trong phạm vi được phép sau khi kiểm tra form locks, chữ ký, track changes, section breaks, header/footer, số trang, lề, caption, hiệu ứng lên phần khác.
- Times New Roman chỉ **13–14 pt** trong bảng nội dung, không tự giảm 14→13 khi không được phép; không biến nhãn SPEC hoặc case synthetic thành nghiệm thu Word.
- Nguồn ưu tiên: [V17.5.1](docs/research/V17_5_1/V17_5_1_ADMIN_TABLES_USER_CONTROLLED_ORIENTATION_SPEC.md) thay thế nhánh đề xuất orientation trước đó trong [V17.5](docs/research/V17_5/V17_5_ADMIN_TABLES_LANDSCAPE_SPEC.md).
