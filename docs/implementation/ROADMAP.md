# Lộ trình từ nghiên cứu đến triển khai tối thiểu

**Baseline tri thức:** Báo cáo V15 (21/10/2026). **Baseline mã nguồn:** Chưa có ứng dụng để audit trong repo ChuanhoaBang tại thời điểm khởi tạo tài liệu.

## Mục tiêu

Chuẩn hóa và tối ưu bảng trong DOCX phù hợp loại văn bản, giữ nguyên ngữ nghĩa/đối tượng và tạo bố cục cân đối, dễ đọc, in an toàn. Không tự động làm hỏng mẫu biểu hoặc thay số liệu.

## P0 — Xác lập căn cứ và audit, chưa viết engine
**Đầu vào:** các tài liệu mẫu được phép sử dụng, báo cáo V15, bộ thử có checksum.

- Kiểm tra HEAD và mọi code/dependency/API hiện có trước khi triển khai.
- Phân biệt bảng dữ liệu / layout / official form / nested / unknown, owner body/appendix/header.
- Khóa nguồn quy tắc cho NĐ30 và HD05; đối chiếu mẫu chuyên ngành và hiệu lực pháp lý.
- Lập danh sách ràng buộc bất biến và phạm vi quyền sửa.
- Đọc lại DOCX và chụp baseline Word/Print Layout trên máy mục tiêu.

**Gate P0:** có bảng phân tích capability và các trường hợp không được tự sửa; xác định những việc có thể reuse.

## P1 — Chứng minh phép sửa nhỏ với thư viện hiện có
- Reuse Microsoft Word/OOXML hoặc thư viện trưởng thành; không tự xây package/renderer mới.
- Ưu tiên 1–2 ca có bằng chứng: F08 `exact → atLeast`, F07 refit khi giảm vùng chứa.
- Giữ snapshot đầu vào, chỉ patch thuộc tính cần thiết.
- Diff text, grid, merge, object, relationship và các part không được sửa; mở lại sau khi ghi.
- So sánh Word Print Layout cùng môi trường; ghi mọi khác biệt.

**Gate P1:** có ít nhất một ứng viên hợp lệ, baseline và ảnh Word trước/sau, lý do quyết định `APPLY` hoặc `NO_OP_VALID`, phép thử phạm vi liên quan PASS. Nếu không, dừng và ghi `UNVERIFIED`.

## P2 — Nhận diện cột trọng tâm và tối ưu có giới hạn
- Phân loại cột theo nhiệm vụ người đọc và bằng chứng, không dùng LLM cho sắp xếp/validation xác định.
- Xác định min/preferred/max theo font, đệm ô, số liệu, token không thể ngắt, ô gộp và độ rộng vùng chứa.
- Tạo số lượng ứng viên hữu hạn, so sánh cột/hàng/bảng/trang; không bắt buộc dùng hết chiều rộng.
- Chấp nhận chỉ khi giữ các hard gates, không cắt, không xấu đi và có cải thiện đo được; nếu không `KEEP` hoặc `REVIEW`.
- Khi thay đổi section/lề/font, làm mất hiệu lực cache ứng viên và đo lại.

**Gate P2:** đánh giá lặp lại được, giải thích được phép lựa chọn và rollback an toàn.

## P3 — Tích hợp nhỏ và nghiệm thu
- Chỉ sửa file cần thiết, đặt tính năng sau capability/HITL hiện có nếu tích hợp sang dự án khác.
- Không tạo engine thứ hai, không tự động thay mẫu biểu hoặc biến quyết định pháp lý thành "điểm đẹp".
- Tận dụng test sẵn có, chạy regression theo blast radius; không test lại toàn hệ thống nếu không liên quan.
- Báo cáo kết quả theo `PASS/FAIL/NOT_RUN/UNVERIFIED`, giữ nhật ký thay đổi và rollback.

**Gate P3:** kiểm tra DOCX mở lại, bất biến đúng, render Word đạt, người dùng duyệt, không phá phần đã ổn định.

## Cấu trúc quy tắc đề xuất

Mỗi quy tắc cần các trường tối thiểu: `id`, `authority`, `scope`, `preconditions`, `severity`, `measurement`, `safe_action`, `requires_approval`, `postconditions`, `evidence_level`. Khác biệt pháp lý đặt trong profile cấu hình, không nhân đôi engine.

## Điều không thuộc phạm vi hiện tại

- Không tự tạo một công cụ hoàn chỉnh, UI, add-in, service, hay backend khi chưa audit nhu cầu.
- Không bổ sung hạ tầng AI, vector DB hoặc quy trình chạy nền.
- Không tự merge, deploy, thay tài liệu người dùng hoặc đánh dấu các thử nghiệm chưa chạy là PASS.
