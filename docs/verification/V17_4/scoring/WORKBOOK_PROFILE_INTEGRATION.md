# Tích hợp ngắn cho chat Workbook/Profile — ChuanhoaBang V17.4

**Tình trạng:** Đã hậu kiểm dữ liệu phản hồi Antigravity (128 input/result). Đã chấm theo nhãn đặc tả V17.3, chưa được chuyên gia độc lập hiệu chỉnh. Không render, chưa đo TNR glyph.

- TNR **13–14 pt duy nhất**. Không đổi 14 sang 13 chỉ để ép vừa trang khi chưa có profile cho phép. Không dùng chữ nhỏ hơn 13 pt.
- Bảo toàn content, token, field, ô gộp, mẫu chính thức và OOXML cấu trúc. Phân biệt `LEGAL_OR_FORM_LOCK`, `PRESERVE_EXISTING`, `PROPOSAL_ALLOWED`.
- Phân biệt bằng chứng `STRUCTURAL_VERIFIED`, `RULE_INFERRED`, `FONT_METRIC_NOT_RUN`, `WORD_LAYOUT_UNVERIFIED`, `VISUAL_NOT_VERIFIED`, `EXPERT_GOLD_NOT_OBTAINED`.
- **Không import điểm model làm rule:** 63/68 trường hợp bắt buộc, 14/14 khuyến nghị chỉ là mức khớp nhãn đặc tả; 59/64 nhất quán không chứng minh đúng; ABSTAIN chỉ khớp 1/16 lượt theo tiêu chí nghiêm ngặt.
- Khi thiếu width thật, style cascade, font metrics, hoặc chưa xác minh mẫu có khóa, workbook ghi `CONDITIONAL`/`REVIEW_REQUIRED` thay vì auto-apply phương án đẹp.
- Regression test: CP19, DP04, DP15, DP20, DP21; chú ý thay đổi kết luận khi đảo A/B.
- 26 prompt có dấu hiệu ngôn ngữ gợi ý; chưa có expert gold. Tránh dùng bộ thử này làm ground truth cho ngưỡng đẹp/thẩm mỹ hoặc training score.
- Có thể dùng bộ đặc tả để diễn giải quyết định; không tuyên bố kết quả đã được nghiệm thu Word/PDF/ảnh hoặc theo pháp lý khi chưa có bằng chứng tương ứng.

**Nhãn bàn giao:** `SPEC_REFERENCE_SCORED`, `HARD_GATES_PARTIALLY_SUPPORTED`, `ABSTENTION_WEAK`, `EXPERT_GOLD_BLOCKED`, `NO_RENDER_POLICY_PRESERVED`.