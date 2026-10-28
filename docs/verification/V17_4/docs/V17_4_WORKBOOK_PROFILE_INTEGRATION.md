# Bản tích hợp ngắn V17.4 cho chat workbook/profile ChuanhoaBang

**Trạng thái nguồn:** V17.3 là đặc tả nghiên cứu; V17.4 mới xác minh *chất lượng bộ đầu vào thử nghiệm*, **không** có đo glyph thực, đánh giá model mù hoặc gold chuyên gia. Không gọi 128 prompt là 128 kết quả đạt.

**Quy tắc để workbook/profile có thể sử dụng ngay:**

1. Phạm vi bảng nội dung: `font_family=Times New Roman`, `font_size_pt in {13,14}`. 14 pt ưu tiên theo profile; 13 pt chỉ khi đúng loại văn bản/mẫu và có thẩm quyền. Không tự giảm font để vừa trang; ngoài 13–14 pt là ngoài phạm vi nghiên cứu này.
2. Giữ các trường `rule_id`, `authority`, `authority_effective_date`, `source_version`, `applicability`, `lock`, `edit_permission`, `ooxml_property`, `confidence`, `evidence_kind`, `metric_status`, `reason_code` và `decision` theo cùng ý nghĩa. Không biến khuyến nghị thẩm mỹ `[KN]` thành yêu cầu pháp luật `[PL]`.
3. Quy tắc hình học từ OOXML có thể `STRUCTURE_VERIFIED`, còn `width_mm` không đo font phải là `ILLUSTRATIVE`, **không** `TEXT_MEASURED`; chỉ được dùng làm ứng viên, không chứng nhận vừa trang.
4. `FONT_METRIC_ESTIMATE` chỉ hợp lệ khi có font fingerprint, size 13/14, shaping/measurement method, text/token và giá trị đo. V17.3 chưa có bộ đo đó.
5. Với ô gộp, form/locked styles, `trHeight=exact`, line spacing exact, bảng nổi, bảng lồng, thiếu geometry hoặc font hiệu dụng: ưu tiên `PRESERVE`, `CONDITIONAL` hoặc `REVIEW_REQUIRED` và ghi lý do. Không quy đổi thành điểm đẹp giả.
6. **Workbook profile không lấy nhãn `SPEC_EXPECTED` của 64 cặp làm đáp án chuẩn xác thực nghiệm.** Chỉ dùng làm ví dụ quy tắc/tiêu chí QA và lưu trạng thái `UNADJUDICATED`.
7. TQA-NR giữ 3 lớp tách bạch: (a) hard gates — toàn vẹn, font, authority/structure; (b) proxy readability/semantic association; (c) recommendation + uncertainty. Không có một điểm đẹp tổng hợp được hiệu chuẩn.

**Trạng thái giao tiếp đề nghị giữa 2 chat:** `SPEC_READY; STRUCTURAL_QA_128_PASS; BLIND_MODEL_VALIDATION_BLOCKED; INDEPENDENT_GOLD_BLOCKED; TNR_METRICS_NOT_RUN`. Tiếp tục công việc workbook/profile theo các rule đã xác định, nhưng **không tuyên bố** profile/thuật toán đã được 128 prompt xác nhận đẹp hoặc đúng dàn trang Word.
