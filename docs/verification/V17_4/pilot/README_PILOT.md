# ChuanhoaBang V17.4 — Pilot test bằng dữ liệu giả định

**Thời điểm:** 2026-10-29 (Asia/Bangkok)  
**Phạm vi:** Times New Roman 13–14 pt; không render; không sửa repo GitHub.  
**Tính chất:** chạy thực nghiệm bộ kiểm tra dữ liệu và 4 baseline xác định bằng Python, KHÔNG chạy mô hình AI.

## 1. Dữ liệu và cách chạy
- Bundle: `ChuanhoaBang_V17_4_Reproducible_Validation_Pack.zip`, SHA-256 `759a90bf3fc1807726636f21d468988739a189397123e702d4b8f29d924386cf`.
- Dùng chính 128 bản ghi V17.4 giả định (64 cặp, mỗi cặp 2 thứ tự), không phát sinh thêm nội dung nghiệp vụ.
- V17.3 author spec answer key chỉ dùng trong bước chấm đối chiếu sau khi response đã được tạo và ghi tệp.
- Bốn bộ đáp ứng thử nghiệm từ một chương trình xác định: luôn chọn option 1; luôn từ chối; heuristic lexical v1 (lỗi); heuristic lexical v2 (đã sửa lỗi đảo A/B).
- `pilot_lexical_heuristic` cố ý nhạy với những từ như “tự đổi”, “mất hiệu lực”, “12 pt” để đo nguy cơ lộ đáp án. Không phải mô hình AI hiểu OOXML.

## 2. Kết quả chấm SPEC concordance (không phải accuracy)

| Baseline giả định | Số responses | Nhất quán đảo A/B | Khớp nhãn bắt buộc trong SPEC | Từ chối đúng theo SPEC |
|---|---:|---:|---:|---:|
| `control_always_option1` | 128 | 0/64 | 34/68 | 0/16 |
| `control_always_abstain` | 128 | 64/64 | 0/68 | 16/16 |
| `pilot_lexical_heuristic` | 128 | 63/64 | 42/68 | 4/16 |
| `pilot_lexical_heuristic_v2_fixed` | 128 | 64/64 | 42/68 | 4/16 |

**Cách đọc:** số liệu trên là kết quả chạy Python thật của các baseline mô phỏng, KHÔNG là tỷ lệ chính xác của GPT-6, ChatGPT hay một LLM. Vì không có gold độc lập, nhãn SPEC chỉ dùng để debug giao thức.

## 3. Diễn giải
- Baseline luôn chọn `OPTION_1`: theo cấu trúc hoán vị, lựa chọn này không thể nhất quán về phương án nội dung qua cặp A/B. Bài thử xác định scorer có phát hiện được position bias.
- Baseline luôn `ABSTAIN`: có thể hoàn toàn nhất quán A/B nhưng không phát hiện hard violation. Do đó **order consistency không suy ra correct judgment**.
- Baseline lexical: chọn dựa trên từ gợi ý trong option; nếu đạt điểm cao với SPEC thì nhiều khả năng test có lexical leakage, KHÔNG chứng minh AI nhận biết một bảng đẹp bằng OOXML.
- **Regression thực tế DP06:** lexical v1 dùng regex với hai option nối chung, làm 63/64 cặp nhất quán. v2 phân tích độc lập từng option, loại bỏ lỗi do thứ tự A/B; lưu cả hai log để tái lập lỗi và kiểm tra bản vá.
- Không có phép đo font Times New Roman thật. Các so sánh mm và dòng vẫn chỉ là ước lượng/spec.

## 4. QA và giới hạn
- 128/128 prompt, 64/64 cặp đảo A/B: structural QA PASS theo `v174_runner.py build` chạy lại.
- 4 × 128 phản hồi **được tạo bằng thuật toán xác định**, không phải 512 truy vấn LLM.
- Những cặp `CONDITIONAL` và `ABSTAIN` không được ép một lựa chọn A/B.
- Pilot chưa mù: cùng nguồn phát triển đã thiết kế đáp án; không có chuyên gia đọc độc lập, không có model sạch, chưa neutralize 128 prompts.
- **Không có tỷ lệ đạt chuẩn thẩm mỹ, không có chứng nhận Word, không có kiểm định blind validation.**

## 5. Tái lập
1. Cần Python 3.9+; không cần thư viện bên ngoài, Internet hay Word.
2. Giải nén ZIP pilot vào một thư mục; bundle nguồn đã nằm cùng `run_v174_pilot.py` (không cần sửa đường dẫn).
3. Chạy `python run_v174_pilot.py`. Chương trình giải nén một bản riêng, xuất 4 × 128 responses và dùng `v174_runner.py score` để chấm.
4. Đối chiếu `pilot_summary.json`, `qa_checks.json`, thư mục `scores/` và SHA-256 manifest.
5. Chỉ cung cấp `inputs/prompts_128_blind_candidate.jsonl` cho evaluator; không gửi `keys/` cùng dữ liệu prompt.

## 6. Bổ sung thực sự cần có để kiểm định AI độc lập
1. Evaluator độc lập (model/version hoặc chuyên gia) chưa tiếp xúc với nhãn V17.3.
2. Nhãn gold 64 cặp do chuyên gia độc lập adjudicate và xác định cặp nào phải `ABSTAIN`.
3. Prompt trung lập về câu chữ, sửa lexical cue nhưng không đổi A/B semantics, và checksum trước/sau.
4. 128 raw model responses, timestamps, ID model, cấu hình suy luận, cách cô lập wave AB/BA.
5. Các trường hợp độ rộng cần cấu trúc DOCX, bảng cell/style và fingerprint font TNR 13/14 (hoặc kết luận không đủ dữ kiện).

## 7. Hướng dẫn tích hợp ngắn cho workbook/profile
> Bộ V17.4 pilot dùng dữ liệu giả định. Chỉ được dùng các hard gate cấu trúc (bảo toàn nội dung, không tự giảm font dưới 13, không đổi authority và quan hệ ô), các chỉ số proxy kèm bất định, và status `RULE_INFERRED` / `ESTIMATED` / `UNVERIFIED`. Không dùng tỷ lệ SPEC concordance của baseline mô phỏng để khẳng định workbook hoặc rule offline đạt chất lượng AI. Giữ nguyên yêu cầu TNR 13–14 pt; không tự áp phương án 13 pt nếu chưa có authority. Các cặp thiếu glyph metrics phải `CONDITIONAL`/`ABSTAIN`.

## 8. Danh mục
- `responses_control_always_option1.jsonl`, `responses_control_always_abstain.jsonl`, `responses_pilot_lexical_heuristic.jsonl`, `responses_pilot_lexical_heuristic_v2_fixed.jsonl` – phản hồi baseline giả lập; có provenance.
- `scores/*/results/{score_report.json,scored_responses_detailed.jsonl}` – báo cáo chấm của runner chính thức.
- `pilot_summary.json` – bảng chỉ số kiểm tra; `qa_checks.json` – checklist đã/chưa chạy.
- `bundle/` – bản sao tệp nguồn và runner V17.4; không được dùng gold trong input evaluator.