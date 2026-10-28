# ChuanhoaBang — Rà soát nghiên cứu và đề xuất TQA-NR V17.1

**Ngày rà soát:** 29/10/2026  
**Trạng thái:** Research / specification only — KHÔNG triển khai, KHÔNG sửa GitHub, KHÔNG xác nhận đầu ra Word, KHÔNG bắt buộc render.  
**Phạm vi bất biến:** Bảng **nội dung** trong DOCX; chỉ **Times New Roman**, cỡ chữ **13 hoặc 14 pt**. Không dùng font thay thế, co chữ, Fit Text hoặc 12 pt để ép vừa trang. Các mẫu bắt buộc không tương thích phải được bảo toàn và báo xung đột.

**Tài liệu nội bộ đối chiếu:** Báo cáo V15 của repository `quanggiaphthh/ChuanhoaBang`; V16 No-Render, 118 case NR01–NR118; `ChuanhoaBang_TQA_NR_V17_Mo_hinh_dinh_luong_bang_khong_render.md` (12 metric M01–M12, 8 hard gates, mô hình 6 chiều).

## I. Phán quyết nghiên cứu

**Giữ phương pháp đo cấu trúc + font metrics + ngữ nghĩa + thứ tự ưu tiên ràng buộc của V17.** Nhưng cần sửa mô hình trước khi dùng 118 case làm chứng cứ kiểm định:

1. **Không dùng `Q=.../100` làm kết luận “đẹp/chuẩn”.** Mô hình trọng số 35/25/15/10/10/5 của V17 chỉ là ví dụ tự đề xuất, chưa được hiệu chỉnh bằng dữ liệu đọc hiểu của con người. Dùng vector chỉ số và so sánh cặp có điều kiện; chỉ hiển thị Q tùy chọn trong nghiên cứu đã có hiệu chỉnh.
2. **Không lấy `effective_font_conformity` và `protected_token_fit_rate` trung bình để che lỗi nghiêm trọng.** Phân loại hard gates xác minh được, rủi ro ước lượng, và thiếu dữ liệu độc lập. Một mã quan trọng vượt chiều rộng không thể được bù bằng 99 ô khác.
3. **Không phạt toàn bộ ô gộp.** Cần kiểm tra vai trò, vị trí và bản đồ liên hệ tiêu đề–dữ liệu. Microsoft đã cải tiến Accessibility Assistant để giảm cảnh báo sai ở tiêu đề hàng/cột hợp lệ, ô gộp ở vùng tiêu đề, bảng nhỏ; điều đó KHÔNG có nghĩa mọi ô gộp đều truy cập tốt.
4. **Chốt phiên bản Unicode 18.0.0 (01/09/2026), UAX #14 rev.57, UAX #29 rev.49** trong tài liệu nghiên cứu; ghi cả phiên bản thực sự của thư viện nếu hệ thống sử dụng bản khác.
5. **Phân biệt số đo glyph advances, bề rộng mực/glyph extents và hành vi dàn trang Word.** HarfBuzz cho vị trí/advances nhưng không tái hiện đầy đủ hàng, trang, line-height, font fallback, tab, trường động hay ranh giới in Word.
6. **Chất lượng phụ thuộc mục tiêu đọc.** Không có preset “ít viền/không màu” hay tỷ lệ cột cố định phù hợp cho mọi bảng. Cần xác định tác vụ TRA CỨU / SO SÁNH / ĐIỀU HÀNH / KIỂM TRA / BIỂU MẪU trước khi tính lợi ích của mỗi mm.

## II. Những bằng chứng mới và mức được phép suy luận

| Nguồn | Điều đã xác nhận | Ranh giới sử dụng trong đặc tả |
|---|---|---|
| Unicode 18.0 (01/09/2026), UAX #14 rev.57 | Xác định *vị trí có thể ngắt* và thay đổi phân lớp dấu gạch ngang/dấu gạch nối mềm | **Không** xác định tự động vị trí xuống dòng thực của Word; chỉ là đầu vào cho phép đo |
| Unicode 18.0, UAX #29 rev.49 | Xác định extended grapheme clusters và phân đoạn | Grapheme không đồng nhất với “từ tiếng Việt”; không đếm code points như mm |
| HarfBuzz manual | `hb_shape()` và glyph positions/advances, bao gồm cảnh báo `UNSAFE_TO_BREAK` | Dùng font TNR face thực và provenance; không xem HarfBuzz như Word renderer |
| Microsoft Learn — TableWidth | `tblW` là preferred width; xử lý `tblGrid`/cell width có thể xung đột | Tổng width theo XML chỉ là điều kiện hình học khai báo |
| Microsoft Open Specifications — `trHeight` | Có những khác biệt giữa quy tắc chuẩn và cách Word diễn giải `hRule`/`exact`, gồm tác động padding | Tránh tuyên bố chắc chắn clipping hoặc số mm cao hàng chỉ từ thuộc tính XML |
| Microsoft 365 Insider — cải tiến Accessibility Assistant (2025) | Nhận diện row headers hợp lệ và các ô gộp tiêu đề/small tables có điều kiện | M12 phải phân loại phức tạp *có vai trò*; không đánh đồng ô gộp với lỗi |
| Ji, Perin, Nacenta — IEEE TVCG 2025 | Kết quả đọc bảng số thay đổi theo nhiệm vụ và cách hỗ trợ thị giác; striped rows không phải luôn tệ hơn màu/thanh dữ liệu | Không phổ quát hóa hiệu ứng màu hoặc hình thức vào bảng hành chính; ưu tiên tác vụ đọc |
| Researcher's Guide for the Preparation of Tables — Journal of Surgical Research 2025 | Mục đích bảng, dữ liệu cốt lõi, tiết chế yếu tố không dữ liệu và nguyên tắc tổ chức | Cơ sở định hướng rubric, không phải con số phạt/điểm ISO |
| JMIR Copyediting guidance cập nhật 25/06/2026 | Hướng dẫn caption, tiêu đề rõ và dữ liệu dễ so sánh theo house style | **Không** áp quy định house style (cỡ chữ, orientation, chiều dài) vào NĐ30/HD05 |

## III. Sửa kiến trúc đánh giá: bốn lớp bằng chứng, năm loại kết quả

### A. Lớp bằng chứng

- **E0 — DECLARED_EXACT:** Thuộc tính/chuỗi tồn tại trong gói DOCX gốc, bao gồm `w:t`, `w:sz`, `tblGrid`, `tcW` và part/relationships. Bằng chứng *khai báo*, không phải thuộc tính đã hiển thị.
- **E1 — EFFECTIVE_RESOLVED:** Đã giải quyết style cascade: docDefaults, linked/basedOn, paragraph/character/table styles, `tblStylePr`, `tblLook`, direct formatting, `rFonts`, `sz/szCs`, margins, border overrides. Nếu không giải quyết được, trả UNKNOWN.
- **E2 — MODEL_ESTIMATE:** Glyph metrics TNR chính xác trong môi trường đo, break opportunities, dự đoán line/row/width. Có `font_identity`, `metric_source`, `unicode_version`, `model_version` và sai số/giới hạn biết được; không dùng con số `%` sai số bịa đặt.
- **E3 — HUMAN_VALIDATED:** Có dữ liệu phản hồi độc lập về đọc hiểu hoặc xếp hạng phương án; dùng **chỉ trong nghiên cứu hiệu chỉnh**, không phải bắt buộc ở bước AI đánh giá DOCX. E3 không đồng nghĩa xác nhận đầu ra Word hiện tại.

Không sinh trạng thái `RENDER_VERIFIED` nếu không render; không yêu cầu render để xuất khuyến nghị có giải thích.

### B. Đầu ra tách biệt

1. `conformity`: PASS / FAIL / UNKNOWN / OUT_OF_SCOPE — chỉ nói điều kiện cấu trúc/căn cứ.
2. `readability_risks`: lỗi token, tiêu đề, ngắt dòng, hàng cao, nhầm nhóm hàng–cột; giá trị đo hoặc ước lượng và độ tin cậy cho từng lỗi.
3. `design_utility`: vector lợi ích cho tác vụ đọc (`LOOKUP`, `COMPARE`, `ACTION`, `COMPLIANCE`, `SUMMARY`), không điểm đẹp tuyệt đối.
4. `confidence`: độ bao phủ **theo tập metric đủ điều kiện**, provenance font/geometry/style, phần UNKNOWN, và bất định nếu có dữ liệu hiệu chỉnh.
5. `decision`: KEEP_EXISTING / PROPOSE_CANDIDATE / REVIEW_REQUIRED / PRESERVE / NO_SAFE_FIT, kèm reason codes; không ghi sửa file trong repo này.

## IV. Điều chỉnh cụ thể 12 metric V17

| Metric | Phán quyết | Quy tắc V17.1 |
|---|---|---|
| M01 — font conformity | **Giữ, tăng mức ưu tiên** | Hard gate trên font TNR **hiệu dụng** 13/14. Đếm tỷ lệ chỉ cho báo cáo chẩn đoán, không dùng trung bình để hợp thức hóa run sai |
| M02 — critical token fit | **Sửa lớn** | Dùng `worst_critical_fit_margin = min(inner_width - estimated_token_extent)` và `critical_fail_count`, tách dữ liệu đã đo/UNKNOWN; không lấy trung bình tỷ lệ ô vừa thay cho bảo vệ token |
| M03 — semantic alignment | **Giữ có điều kiện** | Chỉ kiểm các ô có vai trò đáng tin; số phải, STT giữa, nội dung trái là default theo profile, trừ mẫu/cột đặc thù |
| M04 — header hierarchy | **Giữ** | Phân loại header thật bằng ngữ nghĩa + vị trí, kiểm cả tiêu đề hàng và nhiều tầng; không chỉ đếm bold |
| M05 — header fragmentation | **Sửa** | Tính `predicted_header_lines` và dòng cuối vụn, không cấm mọi header xuống dòng; cần định nghĩa `fragmentation` theo token/cụm nghĩa |
| M06 — short fragment rate | **Sửa** | Đo theo cụm/ý nghĩa tiếng Việt, ngoại lệ ngày/mã/giá trị ngắn; không dùng ngưỡng 1–2 từ chung |
| M07 — row bottleneck | **Giữ proxy có ràng buộc** | `estimated_H_row` cho hàng thường; riêng vMerge/nested/multi-paragraph/exact/objects đánh dấu model limitations. So **Δ so với baseline**, không phạt bảng dài hợp lệ |
| M08 — unused width | **Sửa lớn** | Thay phạt độ rộng dư bằng `marginal_readability_gain_per_mm` và chi phí làm xấu cột khác; một bảng hẹp hơn trang vẫn có thể là nghiệm tốt |
| M09 — padding | **Giữ** | Mốc 1,5–2 mm ngang, 0,8–1,2 mm dọc chỉ là preset nghiên cứu; phạt theo thực tế TNR13/14, nội dung và cấu trúc, không theo khoảng chung như luật |
| M10 — border consistency | **Sửa** | Xét `tblBorders`, `tcBorders`, conditional styles, ngữ nghĩa đường phân nhóm, độ rõ đen trắng; tránh lầm `view gridlines` là viền in |
| M11 — family consistency | **Giữ** | So sánh bảng cùng vai trò + authority + reader task; không ép mọi bảng trong tài liệu dùng chung width/style |
| M12 — header/merge accessibility | **Sửa lớn** | Lập bản đồ header–data theo grid/span, xử lý header ở hàng đầu/cột đầu, đánh dấu rủi ro vùng gộp phức tạp; không coi mọi merged cell là FAIL hoặc Word Accessibility Checker PASS |

**Bổ sung 04 tín hiệu xuyên suốt (không nhất thiết thêm bốn điểm độc lập):**

- `semantic_task_success_proxy`: khả năng tìm đối tượng, so sánh số, theo dõi hạn, đọc kết luận dựa trên cấu trúc hàng–cột.
- `style_effective_coverage`: tỷ lệ thuộc tính thực sự resolve được từ cascade, tránh sai màu/size/border.
- `font_coverage_and_substitution_risk`: glyph không có trong face TNR, chữ tổ hợp/field/Unicode đặc biệt; nếu fallback chưa rõ -> UNKNOWN, không giả TNR.
- `layout_robustness_risk`: độ sát ranh min width, thay đổi section/gutter/indent và sensitivity đối với một khoảng tăng giảm width; không tự ấn định margin 2 mm là an toàn.

## V. Công thức so sánh phù hợp hơn với mục tiêu không render

### 1. Bảo vệ token

```text
W_inner(c, w) = sum(widths of grid columns spanned by c)
              - effective horizontal cell margins
              - applicable border/spacing/paragraph-indent budget

critical_fit_margin(c) = W_inner(c, w) - shaped_advance_or_extent(critical_token, TNR, 13|14)
```

`shaped_advance` phục vụ dòng chữ logic; dấu tiếng Việt, overhang, kẻ viền và hình học mực có thể đòi `glyph extents`/padding dự phòng. Nếu không có exact TNR face, độ rộng margin là `UNKNOWN`, không được bịa hệ số chuyển ký tự→mm.

### 2. Tác động lên toàn hàng

```text
estimated_cell_height(r,c,w) = estimated line advances + paragraph spacing + vertical margins
estimated_row_bottleneck(r,w) = max(estimated_cell_height(r,c,w))   # chỉ hàng đơn giản
estimated_table_height(w) ≈ sum(estimated_row_bottleneck)            # ngoại lệ phải tách
```

Không dùng công thức `max` cho các trường hợp vertical merge, shape, table nested, tracked layout/section hoặc height exact nếu chưa có mô hình tương ứng. `trHeight=exact` là cảnh báo rủi ro, không chứng minh chữ đã bị cắt; Microsoft có implementation notes riêng.

### 3. So sánh ứng viên theo điều kiện không thua kém

```text
A = baseline candidate
B = proposed candidate

IF B violates a verified hard constraint: reject B.
IF B introduces estimated critical-token risk not present in A: reject or REVIEW B.
IF B improves one task-critical metric and worsens no higher-priority metric
   under the same font/geometry/source assumptions:
   B is a provisional candidate.
IF improvement is inside uncertainty OR same evidence not available:
   KEEP_EXISTING or REVIEW_REQUIRED.
```

**Kết quả được dùng trong ChuanhoaBang:** `PROPOSE_CANDIDATE` kèm vector width/spacing, diff thuộc tính cho phép, khoảng bất định và reasons. Không suy `PRINT_READY` từ các proxy.

### 4. Không dùng Q làm cổng nghiệm thu

Giữ sáu chiều của V17 như *ngôn ngữ báo cáo*, nhưng bỏ tính mặc định phổ quát của trọng số `35/25/15/10/10/5`. Nếu phải công bố một chỉ số nghiên cứu, dùng:

```text
Q_task(B | corpus, rubric_version) = calibrated_task_specific_score
pairwise_outcome(B,A) = BETTER | EQUIVALENT | WORSE | INCOMPARABLE
```

`Q_task` mặc định `NOT_CALIBRATED` nếu chưa có dữ liệu người đánh giá. `INCOMPARABLE` là kết luận hợp lệ khi các phương án đánh đổi chất lượng theo những chiều không có thẩm quyền đánh đổi.

## VI. Các phát hiện thay đổi cách thiết kế case study

- **Không cần thêm 100 case kiểu mẫu nữa trước khi QA.** 118 case cũ đều là synthetic, 21/21 kiểm tra trước chỉ là QA tài liệu, chưa có đo TNR glyph, chưa blind-test AI hoặc đánh giá cảm nhận độc lập.
- Nên **gắn thêm 12 metric IDs + 4 signals** vào từng case, xác định `measurable/estimated/unknown`, `source_of_expectation`, `decision`, `reason_codes`.
- Tạo **30–40 cặp đối chứng đặc tả** từ case hiện có, không cần tạo 80–100 case mới: một cặp chỉ thay 1–2 thông số (padding, cột số, cột tên, header, font 13/14 có quyền, vMerge, borders, task reader) để biết vì sao A tốt hơn B.
- Thêm **mẫu đối nghịch (adversarial):** cột STT rộng giả tạo; chữ ngày có NBSP; `01` bị ép thành `1`; header nhóm `gridSpan`; ô gộp ở header hợp lệ; ô gộp gây mất bản đồ tiêu đề; OOXML style 14pt nhưng trực tiếp 12pt; TNR font thiếu glyph; `hRule` omitted/exact; row height with bottom padding; width `pct` vs `dxa`; table floating/mirror margins; caption đã có; mã siêu dài không thể ngắt; blank cell là dữ liệu thiếu khác số 0.
- Chia kiểm định thành **blind rules test** (AI chỉ đọc đầu vào và rubric, không thấy answer key), **consistency/invariance** (cùng nguồn/khác thứ tự XML tương đương phải cùng quyết định) và **counterfactual** (một thuộc tính đổi phải gây ảnh hưởng đúng dự báo). Dùng tập holdout không cho AI nghiên cứu đáp án trước.
- Muốn nói “tương ứng với cảm nhận đẹp” thì phải có **nhãn độc lập của người đọc/chuyên gia** để hiệu chỉnh và đánh giá khả năng dự đoán, ngoài dữ liệu synthetic. Đây là nghiên cứu tùy chọn riêng, **không** đặt bước render trong quy trình AI áp dụng đặc tả.

## VII. Danh sách cập nhật ưu tiên cho repo tài liệu (không triển khai)

| Ưu tiên | Việc cần bổ sung vào đặc tả | Tiêu chí chấp nhận |
|---|---|---|
| P0 | V17.1 errata/corrections, versioned provenance | 12 metric có mô tả phần sửa, tất cả trạng thái/nguồn rõ ràng |
| P0 | `TNR_METRIC_CONTRACT.md`: nguồn face/font, size 13/14, shaping, ink/advance, break, fallback, Unicode | Không có phép `char_count × mm` giả; thiếu font → UNKNOWN |
| P1 | `TASK_CONDITIONED_QUALITY_RUBRIC.md`: chấm theo nhiệm vụ đọc, từ chối điểm tổng chưa hiệu chỉnh | Một lỗi cứng không được bù, không có “85/100 = đẹp” không chứng minh |
| P1 | `MERGED_HEADER_AND_ACCESSIBILITY_POLICY.md`: header map, gộp có điều kiện | Không phạt mọi ô gộp; không tuyên bố screen reader PASS |
| P1 | `V17_118_CASE_METRIC_MAPPING.md`: mapping 118 case và gap analysis | Mỗi case chỉ rõ metrics đo được/không được, nguồn giả định |
| P2 | 30–40 paired-counterfactual cases + blind test protocol | Mỗi cặp lý giải được thắng/thua/giữ nguyên qua hard gates & task utility |
| P2 | `VALIDATION_RUBRIC.md`: nhãn độc lập, tập giữ lại, báo cáo sai số/chênh lệch | Nếu chưa có nhãn thì công bố `NOT_VALIDATED`, không suy độ chính xác |

**Quy tắc giữ gọn:** Repo nghiên cứu có thể lưu các tài liệu trên hoặc tích hợp dưới phụ lục V17; không bắt buộc tạo đủ tên file. Tuyệt đối không xây engine, API, plugin, backend, pipeline render hoặc can thiệp project khác.

## VIII. Nguồn tham khảo chính (truy cập, đối chiếu đến 29/10/2026)

1. Unicode Consortium, *UAX #14 Unicode Line Breaking Algorithm*, Unicode 18.0.0, rev.57, 01/09/2026: https://www.unicode.org/reports/tr14/
2. Unicode Consortium, *UAX #29 Unicode Text Segmentation*, Unicode 18.0.0, rev.49, 01/09/2026: https://www.unicode.org/reports/tr29/
3. HarfBuzz, *Getting Started* (glyph shaping, unsafe-to-break): https://harfbuzz.github.io/getting-started.html
4. HarfBuzz, *Shaping and Shape Plans* (x_advance, x_offset): https://harfbuzz.github.io/shaping-and-shape-plans.html
5. Microsoft Learn, *TableWidth (Preferred Table Width)*: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablewidth?view=openxml-3.0.1
6. Microsoft Learn, *trHeight Word implementation notes*: https://learn.microsoft.com/en-us/openspecs/office_standards/ms-oe376/3b8129c1-9aac-4611-a50e-247d13a382b2
7. Microsoft Learn, *Table style conditional precedence*: https://learn.microsoft.com/en-us/openspecs/office_standards/ms-oe376/f7f85a73-5f60-4f7e-a725-4f1f06198388
8. Microsoft 365 Insider, *Accessibility Assistant updates: Smarter handling of tables and shapes* (2025): https://techcommunity.microsoft.com/blog/microsoft365insiderblog/accessibility-assistant-updates-smarter-handling-of-tables-and-shapes/4462325
9. Microsoft Support, *Make your Word documents accessible to people with disabilities*: https://support.microsoft.com/en-us/accessibility/word/make-your-word-documents-accessible-to-people-with-disabilities
10. Section508.gov, *Accessibility Bytes: Data Tables in Documents*: https://www.section508.gov/blog/accessibility-bytes/data-tables-in-documents/
11. Yongfeng Ji, Charles Perin, Miguel A. Nacenta, *The Effect of Visual Aids on Reading Numeric Data Tables*, IEEE TVCG 31(1), 2025, DOI 10.1109/TVCG.2024.3456403: https://pubmed.ncbi.nlm.nih.gov/39250406/
12. *Researcher's Guide for the Preparation of Tables*, Journal of Surgical Research 310 (06/2025): https://www.sciencedirect.com/science/article/pii/S0022480425001556
13. JMIR Copyediting Team, *How should tables and textboxes be formatted?*, cập nhật 25/06/2026: https://support.jmir.org/hc/en-us/articles/115004167607-How-should-tables-and-textboxes-be-formatted

## IX. Kết luận

**Đề xuất điều chỉnh V17 thành V17.1 ở cấp tài liệu nghiên cứu**, không thay đổi ý đồ dự án. Chỉ số đẹp cần trở thành *mức lợi ích trong tác vụ đọc của bảng*, kết hợp giới hạn cấu trúc/OOXML và mô hình TNR 13–14 có provenance. Giữ 118 case; ưu tiên chứng minh tính phân biệt tốt/xấu bằng paired-counterfactual và blind decision trước khi sinh thêm nhiều case tổng hợp. Mọi chấm điểm nhận thức phải báo là dự đoán nếu chưa được xác nhận bằng nhãn độc lập.
