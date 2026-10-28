# V17.4 — QA thực thi và các trạng thái bị chặn

**Ngày:** 2026-10-29  
**Gói:** ChuanhoaBang V17.4, kiểm tra cấu trúc trên dữ liệu V17.3, không render.

## Đã chạy thực tế

- `python v174_runner.py build` đã kiểm kê **118 bản ghi** NR01–NR118.
- Đã tải, giải mã và kiểm tra **40 CP + 24 DP = 64 cặp**, với **80 + 48 = 128 prompt**.
- Đã thực thi kiểm tra đảo A/B cho **64/64 cặp**; hai lượt giữ nguyên `source_rows`, reader task và quy tắc Times New Roman 13–14 pt.
- Đã phát sinh **128 bản ghi QA cấu trúc**, mỗi bản ghi có `model_response=NOT_RUN`; không phát sinh đáp án mô hình.
- Đã sinh 128 câu hỏi trình bày lại với mã opaque và tách khóa `spec_answer_key_UNADJUDICATED_KEEP_SEPARATE.jsonl`.
- `results/structural_qa_summary.json` là output thực của script, không phải số liệu mô phỏng.
- Các cặp chỉ bao phủ **53/118** case duy nhất: không nên coi bộ này đại diện toàn diện 118 trường hợp.

## Phát hiện về mức bằng chứng

- Trong audit 118 case, `font_metrics_provided=false` cho **118/118**; `normalized_evidence_kind=HEURISTIC_ASSUMPTION` cho **118/118**.
- Trong 100 case nguồn V16: **64** vector width chưa đo font; **66** gắn `TEXT_ESTIMATED` nhưng không có metric đo thực; **98** ghi 14 pt và **2** ghi 13 pt.
- Trên toàn bộ 118 bản audit, font khai báo **112 ca 14 pt, 2 ca 13 pt, 4 ca không đủ dữ liệu**, không phải 118 ca đều đo được font hiệu dụng.
- Phân bố nhãn V17.3 theo **128 prompt**: 68 REQUIRED, 14 RECOMMENDED, 30 CONDITIONAL, 16 ABSTAIN. Đây là số lượng *nhãn nghiên cứu*, **không phải output model**.
- Bộ kiểm tra ngôn ngữ phát hiện **32/128 prompt có cụm từ dễ gợi ý kết quả** theo danh sách từ khóa hạn chế; bộ dò này không bao phủ hết semantic leakage, do đó không thể báo chỉ 32 mục gây rò rỉ.

## Trạng thái nghiệm thu

| Phạm vi | Status | Bằng chứng |
|---|---|---|
| Có thể truy cập tệp V17.3 | **PASS** | source/ 5 JSONL và file checksum manifest |
| Đếm/định danh 118 case | **PASS** | structural_qa_summary.json |
| 64 cặp / 128 thứ tự | **PASS** | structural_execution_128.jsonl |
| Đảo A/B và bảo toàn nội dung bảng | **PASS** | runner + mỗi bản ghi `option_mapping_correct` |
| Font TNR và 13–14 pt trong 128 prompt | **PASS** | `font_in_range` |
| Tách khóa nhãn khỏi prompt công khai | **PASS (syntactic)** | input/ vs keys/ |
| Bảo đảm prompt vô tư, không gợi ý đáp án | **UNVERIFIED** | Cần rewrite/review độc lập |
| Phép đo glyph Times New Roman thực | **NOT_RUN** | Thiếu fixture/font metrics và benchmark |
| Mô hình độc lập xử lý 128 đầu vào | **BLOCKED** | Chưa có evaluator độc lập/API/runner và chứng cứ mù |
| Chấm kết quả model hoặc precision/accuracy | **NOT_RUN** | 0 raw model responses |
| Gold labels chuyên gia độc lập | **BLOCKED** | 0 adjudication labels |
| Valid blind validation | **BLOCKED** | Thiếu độc lập + nhãn gold + output mô hình |

## Cơ chế không công bố quá mức

Kết quả có thể tuyên bố: `STRUCTURAL_INPUT_AUDIT_PASS`. Kết quả **không được** tuyên bố: `MODEL_VALIDATED`, `BLIND_VALIDATED`, `TNR_METRIC_VERIFIED`, `WORD_LAYOUT_VERIFIED`, `EXPERT_ACCEPTED`.

Không sử dụng ngưỡng điểm “đẹp” hoặc trọng số làm chuẩn pháp lý hay thực nghiệm nếu chưa hiệu chỉnh độc lập.
