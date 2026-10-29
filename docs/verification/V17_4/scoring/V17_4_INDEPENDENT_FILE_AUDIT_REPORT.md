# ChuanhoaBang V17.4 — Đối chiếu hậu kiểm 128 phản hồi Antigravity

**Ngày hậu kiểm:** 29/10/2026  
**Phạm vi:** Chỉ dựa trên các tệp người dùng cung cấp và bundle V17.4 đã tạo trước đó. Không thực hiện suy luận mới, không render, không sửa GitHub. Font theo bộ dữ liệu: Times New Roman 13–14 pt.  
**Trạng thái khoa học:** `SPEC_CONCORDANCE_ONLY_NOT_VALIDATED_ACCURACY`; `EXPLORATORY_MODEL_BASED_PILOT`.

## 1. Nguồn đầu vào và loại bằng chứng

- `ChuanhoaBang_V17_4_Evaluation_Report_Results.zip`: 8 tệp, gồm 128 phản hồi, 128 bản ghi yêu cầu/phản hồi, manifest và QA tự báo cáo. Đây là **bằng chứng thực thi do Antigravity xuất**, không phải bằng chứng độc lập từ nhà cung cấp API.
- `ChuanhoaBang_V17_4_PRIVATE_Scoring_After_Lock_DO_NOT_ATTACH.zip`: khóa tham chiếu 128 lượt từ V17.3, tương ứng 64 cặp. Khóa là **nhãn do dự án xây dựng, chưa phải gold từ chuyên gia**. Chỉ được mở để chấm hậu kiểm sau khi dữ liệu phản hồi đã tồn tại và checksum được xác nhận.
- `ChuanhoaBang_V17_4_Antigravity_Attach_Only.zip`: bản public chứa 128 prompt và hướng dẫn evaluator. Tệp JSONL bên trong khớp checksum với manifest của Antigravity.

## 2. Tính toàn vẹn và độc lập của nhật ký

- 128/128 bản ghi có `item_id` duy nhất `TQ0001–TQ0128` ở đầu vào, khóa, phản hồi và nhật ký.
- 128/128 `raw_response` parse được và có trường quyết định, lý do, mã bằng chứng, mức bất định trùng với `parsed_result` và `responses_128.jsonl`.
- 128/128 `raw_request` chứa đúng một đối tượng dữ liệu khớp bản public; thời điểm bắt đầu/kết thúc phù hợp thời lượng từng lượt.
- 4/4 SHA-256 niêm phong của các tệp kết quả khớp `run_manifest.json`.
- SHA-256 nội dung `prompts_128_blind_candidate.jsonl` là `f908afb5a0e5be920b5b271c5bf01ff4d1b7c0043478c26265f5d43683088e87` — khớp manifest.
- **Sai khác có thật:** SHA-256 của ZIP public đang lưu trong cuộc trò chuyện là `fa2e6baf22bf8369c4d995e3f07518bf1bba139f1c2db4d8e02327a7ebdf892e`, khác `source_package_sha256=759a90bf3fc1807726636f21d468988739a189397123e702d4b8f29d924386cf` trong manifest thực thi. Chưa xác định nguyên nhân; có thể do ZIP khác bản/được đóng gói lại, nhưng **không được mặc định** như vậy. Kết luận: `SOURCE_ARCHIVE_BYTE_IDENTITY_UNVERIFIED`; hash nội dung prompt **đạt**.
- Mô hình `gemini-3.8-flash-low` và enum `MODEL_PLACEHOLDER_M320` chỉ được ghi trong nhật ký; yêu cầu RPC chạy qua endpoint localhost. Không có chứng thực riêng từ nhà cung cấp API hay chứng cứ độc lập về định danh thực tế của phiên bản model. Trạng thái `MODEL_ID_UNVERIFIED`.
- Nhật ký cho thấy từng payload chỉ chứa một input và evaluator system prompt, nhưng không chứng minh được tuyệt đối trạng thái server, phân tách ngữ cảnh nội bộ hoặc việc tác nhân không từng tiếp cận khóa bên ngoài các log.

## 3. Kết quả chấm theo khóa V17.3 — **không phải accuracy đã hiệu chỉnh**

| Loại nhãn đặc tả | Số lượt | Khớp cách chấm V17.4 | Tỷ lệ |
|---|---:|---:|---:|
| `MANDATORY` | 68 | 63 | 92,6% |
| `RECOMMENDED` | 14 | 14 | 100,0% |
| `CONDITIONAL` | 30 | 13 | 43,3% |
| `ABSTAIN` | 16 | 1 | 6,3% |

- **Độ ổn định khi đảo A/B:** **59/64 cặp = 92,2%**; 5 cặp không nhất quán: `CP19`, `DP04`, `DP15`, `DP20`, `DP21`. Dữ liệu chi tiết trong `paired_order_64.csv`.
- 5 lượt `MANDATORY` không trùng đáp án đều trả `CONDITIONAL`, **không phải chọn phương án trái ngược**. Đây là sự khác biệt đáng kể khi diễn giải rủi ro.
- Trong 16 lượt `ABSTAIN`: 1 `ABSTAIN`, 8 `CONDITIONAL`, 7 chọn phương án cụ thể. Theo cách chấm nghiêm ngặt chỉ có **1/16** đúng nhãn; theo tiêu chí **thận trọng tối thiểu**, **9/16** không ép chọn một phương án.
- Trong 30 lượt `CONDITIONAL`: 13 trả `CONDITIONAL`, 17 chọn phương án cụ thể. Tổng 46 lượt phải từ chối hoặc có điều kiện theo đặc tả: **24 lượt đưa ra lựa chọn cứng**, **22 lượt không ép chọn**.
- 95/128 phản hồi tự liệt kê phép đo còn thiếu; 76 trong số này đồng thời tự đánh dấu `LOW` uncertainty. Đây là dấu hiệu **cần hiệu chỉnh cách báo mức tin cậy**, không phải bằng chứng một kết luận cụ thể sai.
- 26/128 prompt bị Antigravity đánh dấu có từ ngữ có nguy cơ gợi ý đáp án; chưa có biên bản rà soát độc lập để xác nhận hoặc loại trừ tác động. Không được suy từ 14/14 `RECOMMENDED` rằng mô hình đã nhận biết thẩm mỹ bảng Word với độ chính xác 100%.

## 4. Các giới hạn của phép thử

**Đã thực sự chạy trong lượt hậu kiểm này:** kiểm tra ZIP, tính checksum, đối chiếu bản ghi raw/parsed/final, tái chấm bằng `v174_runner.py` và tái tính điểm bằng trình kiểm tra thứ hai; kết quả hai cách chấm phù hợp.

**Chưa chạy trong lượt này:** 128 suy luận LLM mới, đo glyph Times New Roman, render Word, đánh giá người dùng/chuyên gia.

**Không được tuyên bố:** tỷ lệ accuracy đã kiểm chứng bằng gold người thật; benchmark không thiên lệch; tuân thủ quy phạm pháp lý; khả năng dàn trang/không clipping trong Microsoft Word; xác thực nhà cung cấp model qua file log đơn thuần.

Mức xử lý: `MODEL_EXECUTION_LOGS_PRESENT`, `INPUT_AND_OUTPUT_INTEGRITY_PASS`, `SPEC_CONCORDANCE_COMPUTED`, `ORDER_CONSISTENCY_59_OF_64`, `PROMPT_NEUTRALITY_UNVERIFIED`, `SOURCE_ZIP_HASH_MISMATCH`, `EXPERT_GOLD_BLOCKED`, `FORMAL_BLIND_VALIDATION_BLOCKED`.

## 5. Khuyến nghị điều chỉnh ngay cho bộ rule/workbook

1. Giữ các **hard gates xác định rõ**: TNR 13–14 pt theo profile/authority, bảo toàn văn bản và OOXML, không thu chữ để giải quyết bố cục, không phá biểu mẫu khóa.
2. **Không dùng mức khớp 63/68 hoặc 14/14 làm hệ số tin cậy** trong workbook. Chúng là điểm khớp với nhãn V17.3 do dự án soạn, chưa đo tính đúng đẹp của bản Word.
3. Nếu profile/geometry/font metric chưa đủ, ưu tiên `CONDITIONAL` hoặc `REVIEW_REQUIRED`; đừng mặc định chọn A/B. Phân biệt thiếu chứng cứ ở cấp quyết định với lựa chọn ràng buộc đã chắc chắn.
4. Không chuyển mặc định mọi bảng sang 13 pt; chỉ sử dụng khi profile cho phép rõ ràng; TNR 14 pt vẫn là điểm xuất phát phù hợp cho bảng thông thường.
5. Dùng `CP19`, `DP04`, `DP15`, `DP20`, `DP21` làm ca kiểm hồi quy về thiên lệch thứ tự.
6. Thiết kế thang `uncertainty` dựa trên **loại phép đo bị thiếu và tác động tới quyết định**; `LOW` kèm yêu cầu đo glyph/width cần giải thích, không tự động coi là calibrated confidence.
7. Giữ hai bộ khác nhau: `(a) kiểm tra quy tắc xác định/OOXML` và `(b) khuyến nghị thẩm mỹ bằng proxy chưa được kiểm chứng thị giác`.

## 6. Tái lập

Trong cùng thư mục có `reproduce_v174_audit.py`. Đặt cạnh ba ZIP và chạy:

```sh
python reproduce_v174_audit.py \
  --results ChuanhoaBang_V17_4_Evaluation_Report_Results.zip \
  --private ChuanhoaBang_V17_4_PRIVATE_Scoring_After_Lock_DO_NOT_ATTACH.zip \
  --public ChuanhoaBang_V17_4_Antigravity_Attach_Only.zip \
  --output result.json
```

`spec_scored_128.csv` và `paired_order_64.csv` được xuất bằng kiểm tra độc lập từ chính những ZIP này. `reference_runner_score_report.json` là báo cáo từ `v174_runner.py` gốc. `qa_recheck.json` ghi kết quả từng hạng mục, bao gồm cả mục không đạt về SHA-256 toàn gói ZIP public.

**Bảo mật tính mù:** Các CSV chấm và gói hậu kiểm **đã chứa đáp án tham chiếu** — tuyệt đối không cấp cho evaluator trong lượt thử tiếp theo.