# Tích hợp workbook/profile — V17.4 pilot (giả định)

- Font trong bảng: **Times New Roman, chỉ 13–14 pt**; 13 pt cần authority phù hợp.
- Không tuyên bố đã đo glyph, dàn trang Word, render, hay nghiệm thu thẩm mỹ.
- Pilot thực hiện 128 input × 4 baseline quy tắc = 512 synthetic outputs, **0 truy vấn LLM độc lập**.
- Phép chấm so với nhãn **V17.3 authored SPEC**, không phải gold chuyên gia. Chỉ dùng để rà giao thức, không làm ngưỡng chất lượng hay chuẩn tỷ lệ đạt.
- Tiêu chí hard gate (bảo toàn dữ liệu, topology, signed form, size) là điều kiện trước điểm mềm.
- Quy tắc width/padding/row-height cần context và font metrics; thiếu => CONDITIONAL/ABSTAIN/UNVERIFIED, tránh tự tạo số đo.
- Workbook nên lưu `evidence_type`, `uncertainty`, `authority`, `reason_codes`, `metric_status`, `allowed_actions`.
- Không cần/cấm mặc định render trong quy trình chính; tài liệu này không sửa rule workbook đang làm song song.