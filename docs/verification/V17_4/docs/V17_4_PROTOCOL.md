# ChuanhoaBang V17.4 — Giao thức đánh giá TQA-NR không render

**Ngày lập:** 2026-10-29 (Asia/Bangkok)  
**Đối tượng:** Bảng Word, Times New Roman 13–14 pt; kho tài liệu đặc tả, không phát triển formatter sản phẩm.  
**Kết quả thực tế trong gói:** kiểm tra cấu trúc của 128 bản ghi. **Không có 128 dự đoán AI độc lập; không có blind validation hợp lệ.**

## 1. Tài liệu nguồn và ranh giới

- `source/ChuanhoaBang_V17_3_118_Case_Evidence_Audit.jsonl`: 118 NR-case, toàn bộ là `HEURISTIC_ASSUMPTION` trong audit V17.3; không có DOCX nguồn hoặc phép đo Times New Roman hiệu dụng.
- `source/ChuanhoaBang_V17_3_40_Contrastive_Pairs.jsonl`: 40 cặp kiểm tra quy tắc, nhãn do tài liệu tác giả lập.
- `source/ChuanhoaBang_V17_3_24_Design_Utility_Pairs.jsonl`: 24 cặp utility, phần lớn là điều kiện/không thể kết luận.
- `source/ChuanhoaBang_V17_3_Blind_Test_80_Prompts.jsonl`, `source/ChuanhoaBang_V17_3_Blind_Test_48_Design_Prompts.jsonl`: 80+48 bản trình bày gốc, chính xác hai thứ tự cho mỗi cặp.
- `inputs/prompts_128_blind_candidate.jsonl`: bản trình bày mới với ID opaque, bỏ nhãn A:/B: đầu mỗi lựa chọn; **chưa loại hoàn toàn gợi ý trong nội dung lựa chọn**.
- `keys/spec_answer_key_UNADJUDICATED_KEEP_SEPARATE.jsonl`: khóa đối chiếu nhãn V17.3, phải cách ly khỏi mô hình/người chấm.

**Giới hạn bằng chứng:** vector mm chưa có font measurement không được dùng như phép đo; UAX #14 cung cấp cơ hội ngắt dòng, không quyết định dòng Word; width `tblW`/`tcW` là *preferred*, không mặc định là tọa độ thực; không có kết luận thị giác hoặc pháp lý.

## 2. Tính độc lập và quy trình mù

**Mù nội dung đáp án** chưa đủ: người/mô hình chấm phải *không từng xem* V16/V17.3, đáp án, tiêu đề nhóm, mô tả lỗi hoặc khóa. Bộ prompt V17.3 có một số lựa chọn nói thẳng hậu quả tiêu cực (ví dụ “...bị chia thành dòng ngắn”); điều đó tạo **nguy cơ answer-cue leakage**. Vì vậy:

1. Người giám sát độc lập không tham gia tạo case, không đọc khóa, rà soát và viết lại **trung lập** những cặp có ngôn ngữ gợi ý; giữ nguyên nội dung bảng, một yếu tố đối chứng và ràng buộc đo được. Lưu nguyên bản và bản đã rewrite bằng checksum, review độc lập để chắc chắn không đổi ý nghĩa hoặc tạo lợi thế mới.
2. Một **nhóm chuyên gia khác** lập nhãn chuẩn từ chính dữ liệu/OOXML, không nhìn nhãn V17.3. Mỗi cặp cần trạng thái `REQUIRED_A/B`, `PREFERRED_A/B`, `CONDITIONAL`, `ABSTAIN`, căn cứ cụ thể, điều kiện đủ/thiếu, phép đo cần có và mức tin cậy. Khi chuyên gia bất đồng, bắt buộc adjudication có biên bản; không cưỡng ép đa số thành “đúng” nếu thiếu dữ liệu.
3. Tách **khóa nhãn, meta nhóm, cặp lặp lại** khỏi dữ liệu đưa tới mô hình. Mỗi item chạy ở ngữ cảnh sạch, không cấp công cụ render, nguồn model, phiên bản, temperature, seed, hệ thống/hướng dẫn, context token và kết quả lỗi. Không cho cùng một session xem cả AB và BA. Chia thành hai wave độc lập, tráo thứ tự các cặp trong từng wave.
4. Ghi raw request/response cho mọi item với timestamp, model fingerprint và cấu hình. Parse output có cấu trúc, không tự sửa nhãn đoán bởi model; lỗi JSON phải tách `INVALID_OUTPUT`, không tự tính là đáp án sai.
5. Khóa gold sau adjudication mới thực hiện `score`; lưu nhãn gold riêng với nhãn nghiên cứu V17.3. Không cập nhật gold để khớp output model.

**Điều kiện dừng bắt buộc:** lộ khóa đáp án/label hoặc prompt chứa case ID, evaluator từng xem đáp án, session có contamination, không có response log, chưa adjudicate các cặp cần xét đo, thay đổi option không tương đương, hoặc thiếu phiên bản model. Cặp không hợp lệ chuyển `EXCLUDED_OR_REWRITE`, không tính accuracy. Không tiếp tục thử nghiệm chọn prompt đến khi điểm đẹp hơn.

## 3. Thang kết quả và chỉ số (không áp chuẩn phần trăm)

- **Mandatory gate concordance**: trên các item có gold `REQUIRED`, số chọn đúng lựa chọn / số item gold-required hợp lệ (phải báo tử số và mẫu số). Chỉ được gọi “độ chính xác” khi gold độc lập được xác nhận. Với nhãn V17.3 chỉ được gọi `spec concordance`.
- **Pair-order consistency**: trong các cặp có đủ hai response, đưa lựa chọn `OPTION_1/OPTION_2` về A/B gốc rồi đếm số cặp nhất quán / số cặp đủ dữ liệu. `ABSTAIN` cả hai lượt là nhất quán, nhưng không có nghĩa phát hiện đúng lỗi.
- **Required abstention**: với gold `ABSTAIN`, đếm phản hồi `ABSTAIN` / số lần đánh giá hợp lệ; đề xuất metric riêng cho tỷ lệ model chọn bừa khi thiếu thông số.
- **Conditional handling**: với gold `CONDITIONAL`, báo số trả `CONDITIONAL`, `ABSTAIN`, buộc chọn và lỗi; không tuyên bố tất cả `ABSTAIN` là giải đúng hoàn toàn.
- **Soft preference concordance**: tách khỏi mandatory gate; phải có gold chuyên gia trước khi diễn giải tính đẹp/dễ đọc.
- **Coverage**: 64 cặp tham chiếu 53 case NR duy nhất, không thể khái quát kết quả sang cả 118 case hoặc tài liệu Word ngoài mẫu.
- **Uncertainty/abstention explanation**: báo tỷ lệ phản hồi nêu đúng thiếu font metrics, width thực, style cascade, hình học section, merged cells và quyền sửa; cần bảng rubric có chuyên gia xác nhận reason codes.
- **Confidence intervals**: nếu cần ước lượng, báo theo mức cặp độc lập (không giả 128 item là 128 quan sát độc lập); không đặt ngưỡng đẹp 80/100 hoặc trọng số cố định không có hiệu chỉnh.

## 4. Cấu trúc dữ liệu đầu ra

Lưu mỗi raw result trong `responses.jsonl`:

```json
{"item_id":"TQ0001","decision":"OPTION_1","reason":"...","evidence_codes":["E_RULE"],"model_id":"vendor/model@version","independent_run_id":"wave1-...","response_status":"COMPLETED"}
```

`decision` chỉ nhận `OPTION_1`, `OPTION_2`, `CONDITIONAL`, `ABSTAIN`. Không lấy `MODEL_RESPONSES_NOT_RUN_TEMPLATE.jsonl` làm phản hồi thực tế, vì file này chứa toàn `NOT_RUN`/null.

## 5. Tái lập (chỉ stdlib Python)

```bash
cd ChuanhoaBang_V17_4
python v174_runner.py build
# Tách input và khóa: CHỈ cấp inputs/prompts_128_blind_candidate.jsonl cho evaluator.
# Sau khi nhận 128 output thật, điền vào responses.jsonl, có assessor independence log.
python v174_runner.py score --responses responses.jsonl
```

Lệnh `build` kiểm tra trực tiếp 128 prompt, đảo A/B, đối chiếu nguồn, font và ID; xuất `results/structural_execution_128.jsonl` và `results/structural_qa_summary.json`. Lệnh `score` **không chạy AI**; chỉ đối chiếu các output đã nhận với nhãn nghiên cứu tạm thời và ghi rõ `SPEC_CONCORDANCE_ONLY_NOT_VALIDATED_ACCURACY`. Để chấm gold độc lập thực sự phải mở rộng giao thức dùng khóa gold đã adjudicate, không sử dụng nhãn V17.3 thay thế.

## 6. Chính xác các blocker còn tồn tại

1. **Bản prompt được chuyên gia độc lập neutralize:** 128 item cần rà soát, nhất là nội dung lựa chọn diễn tả thẳng sai/hại; file hiện chỉ bỏ A/B prefix.
2. **Gold labels độc lập:** 64 case-pair được ít nhất một chuyên gia am hiểu thiết kế Word và một người phản biện/adjudicator đánh giá mà không đọc nhãn V17.3.
3. **Nguồn đo chưa tồn tại:** Với các cặp dựa vào độ rộng, cần geometry đầy đủ, hai trạng thái OOXML thực hoặc các thông số formatting đủ để tạo lại trạng thái, cùng Times New Roman font metric fixture bản 13/14 (fingerprint được xác minh). Khi chưa có, kết quả đúng là `CONDITIONAL`/`ABSTAIN` theo từng tình huống, không được ép chọn A/B.
4. **Evaluator/runner độc lập:** một model chưa tiếp xúc nguồn/khóa hoặc người chấm độc lập, kèm khả năng gọi mô hình và ghi toàn bộ 128 responses. Môi trường hiện tại không có kênh cô lập và bảo đảm evaluator đó; không tạo giả outputs.
5. **Nhãn thực nghiệm:** phải có nhật ký chạy `model/version`, per-call raw outputs, timestamps, cài đặt tham số, adjudication IDs và proof không tiết lộ khóa. Thiếu tất cả các mục này, kết quả `BLOCKED`.

## 7. Nguồn kỹ thuật chính thức được đối chiếu

- Unicode Consortium, *Unicode Standard Annex #14: Unicode Line Breaking Algorithm*, rev 57, Unicode 18.0.0, 2026-09-01: https://www.unicode.org/reports/tr14/tr14-57.html — truy cập 2026-10-29; chỉ xác định break opportunities.
- Microsoft Learn, *TableWidth Class* (`w:tblW`, preferred width), Open XML 3.0.1 reference: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablewidth?view=openxml-3.0.1 — truy cập 2026-10-29.
- HarfBuzz, *Shaping and buffer output API*: https://harfbuzz.github.io/shaping-and-shape-plans.html — tham chiếu kỹ thuật; sử dụng glyph advances không đồng nghĩa Word layout.

**Không thực hiện kết xuất PDF, ảnh, mở Word hay đo font trong bản V17.4 này.**
