# ChuanhoaBang — TQA-NR V17.4: structural QA package

**Phạm vi:** đặc tả nghiên cứu về bảng nội dung DOCX; Times New Roman 13–14 pt; không render trong quy trình chính. Đây không phải formatter.

## Những gì đã được kiểm tra
- V17.4 đã kiểm kê 118 case NR01–NR118, 64 cặp đối chứng và 128 biến thể đầu vào.
- Đối chiếu thứ tự A/B: 64/64 cặp, QA cấu trúc PASS.
- Mã kiểm tra `v174_runner.py`, giao thức, prompt, nhật ký cấu trúc và manifest được lưu trong thư mục này.
- Không có 128 phản hồi của mô hình độc lập; `BLIND_MODEL_VALIDATION=BLOCKED`, `GOLD_LABELS=BLOCKED`, `FONT_METRICS=NOT_RUN`, `RENDER=NOT_RUN`. Không tuyên bố accuracy hoặc chất lượng bản in.

## Phạm vi tệp được commit lên GitHub
Các tệp văn bản đã được đối chiếu bằng Git blob SHA với bản gốc V17.4. **Bản GitHub này chưa chứa đầy đủ 18/18 tệp của ZIP gốc.** Các thư mục `source/`, `keys/`, bản mẫu phản hồi và `results/structural_qa_summary.json` vẫn cần lấy từ gói gốc trước khi chạy lại `build`; không coi việc chạy lại trực tiếp từ bản GitHub hiện tại là đã được kiểm chứng.

**Gói gốc đầy đủ:** `ChuanhoaBang_V17_4_Reproducible_Validation_Pack.zip`, 68.924 byte, SHA-256 `759a90bf3fc1807726636f21d468988739a189397123e702d4b8f29d924386cf`. Giải nén gói này trước khi thực hiện lệnh `python v174_runner.py build`.

Kết quả kiểm tra cục bộ của gói đầy đủ trong phiên này: exit code 0; 118 case, 64 cặp, 128 prompt, 0 model calls và blind validation BLOCKED.

## Tài liệu tích hợp
- `docs/V17_4_PROTOCOL.md`: giao thức và điều kiện độc lập.
- `docs/V17_4_QA_AND_BLOCKERS.md`: QA thực thi và blocker.
- `docs/V17_4_WORKBOOK_PROFILE_INTEGRATION.md`: cách dùng kết luận trong workbook/profile.

Không thay đổi nội dung V15 hoặc lịch sử Git cũ.


## Bổ sung sau ngày 29/10/2026

- [Pilot mô phỏng và kết quả baseline](pilot/README_PILOT.md) — 128 đầu vào, không phải 128 model calls thật.
- [Prompt Antigravity và hướng dẫn input-only](antigravity/MASTER_PROMPT_ANTIGRAVITY.md).
- [Đối chiếu hậu kiểm](scoring/V17_4_INDEPENDENT_FILE_AUDIT_REPORT.md), [CSV 128 lượt](scoring/spec_scored_128.csv), [64 cặp đảo A/B](scoring/paired_order_64.csv), [reproduce script](scoring/reproduce_v174_audit.py).
- [Danh mục QA và giới hạn lưu trữ](POSTPILOT_INDEX.md).

Nhãn so sánh là SPEC-concordance; không công bố điểm thành độ chính xác pháp lý/thẩm mỹ/Word. File ZIP của raw mô hình và khóa private chỉ lưu tách biệt, không commit vào GitHub.
