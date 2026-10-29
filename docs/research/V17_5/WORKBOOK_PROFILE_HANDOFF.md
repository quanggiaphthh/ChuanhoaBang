# Tích hợp ChuanhoaBang V17.5 vào workbook/profile (29/10/2026)

- **Phạm vi:** bảng nội dung trong kế hoạch, báo cáo, chương trình, phương án, phụ lục, bảng nhân sự, số liệu, theo dõi thực hiện; không tự thiết kế lại bảng chữ ký hay biểu mẫu khóa.
- **Authority:** `ADMIN_ND30`, `SOE_ADMIN_ND30` (NĐ30 Điều 2 bao gồm DNNN), `PARTY_HD05` (chỉ văn bản tổ chức Đảng, không tự gán cho tài liệu công ty), `SPECIAL_FORM_LOCKED`.
- **Font:** TNR; cỡ 14 pt mặc định theo dự án, 13 pt chỉ khi profile/authority cho phép; không giảm chữ để ép bảng vào trang.
- **Orientation:** giữ dọc nếu đủ; khi chiều rộng yêu cầu có bằng chứng vượt dọc nhưng có thể vừa ngang và authority cho phép, xuất `LANDSCAPE_CANDIDATE` (chỉ đề xuất). Ngoài ra `LANDSCAPE_OPTIONAL`, `REVIEW_REQUIRED`, `PRESERVE_LOCKED`, `NO_SAFE_FIT`.
- **Section:** chuyển dọc→ngang→dọc yêu cầu 3 phần hợp lệ, kiểm tra `w:sectPr`, `w:pgSz`, `w:pgMar`, `w:pgNumType`, header/footer và chữ ký; không áp dụng tự động.
- **Giao diện tri thức:** trường `table_family`, `document_issuer`, `authority_profile`, `table_context`, `font_size_authorized`, `orientation_current`, `orientation_proposal`, `section_geometry`, `width_evidence`, `orientation_reason`, `confidence`, `approval_required`.
- **Bằng chứng:** chỉ số học trên width giả định = `SYNTHETIC_CONSTRAINT`; chỉ gắn `FONT_METRIC_ESTIMATE` sau đo glyph; `VISUAL_NOT_VERIFIED` dù proxy đẹp; `EXPERT_GOLD_NOT_OBTAINED` trước adjudication.
- **Trạng thái:** 32 ca định hướng là ví dụ nghiên cứu mới, không có nhãn chuyên gia, không phải kết quả thực nghiệm. 160 bảng là phân bổ benchmark đề xuất, không phải dữ liệu đã thu thập.