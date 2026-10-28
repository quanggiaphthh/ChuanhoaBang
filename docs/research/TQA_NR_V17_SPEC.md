# ChuanhoaBang — TQA-NR V17: Mô hình định lượng chất lượng bảng Word không render

**Loại:** Đặc tả nghiên cứu, chỉ dẫn ra quyết định; không phải phần mềm, không xác nhận bản in.  
**Ngày:** 29/10/2026. **Phạm vi:** Bảng nội dung DOCX, **Times New Roman duy nhất, 13 hoặc 14 pt duy nhất**.  
**Kế thừa:** ChuanhoaBang V15, V16, 118 case NR01–NR118. **Không ghi GitHub; không tạo engine hoặc yêu cầu render trong quy trình đánh giá.**

## 1. Câu trả lời trọng tâm

“Đẹp” không phải một thuộc tính vật lý nằm sẵn trong OOXML. Nó là phán đoán về khả năng đọc, cấu trúc thông tin và sự phù hợp với ngữ cảnh. Vì vậy không có **một công thức 100 điểm khách quan, phổ quát**. Có thể tạo **thước đo thay thế** (proxy) đủ chặt chẽ để: (a) từ chối phương án vi phạm điều kiện bắt buộc; (b) so sánh các phương án hợp lệ; (c) giải thích vì sao nên đổi hoặc giữ bảng; (d) biểu thị bất định. Tuyệt đối không dùng điểm thẩm mỹ để hợp thức hóa lỗi mất nội dung, cỡ chữ hoặc phá biểu mẫu.

Đặc tả đề xuất ba đầu ra độc lập:
1. `hard_gate_status`: PASS | FAIL | UNKNOWN | OUT_OF_SCOPE.
2. `quality_profile`: 6 điểm thành phần tùy đủ dữ liệu; điểm tổng là **chỉ số nội bộ có trọng số**, không phải chuẩn pháp luật hay chứng nhận Word.
3. `evidence_coverage` và `uncertainty`: tỷ lệ trọng số đã có bằng chứng và mức tin cậy theo nguồn/giới hạn đo; không báo giả một độ chính xác từ renderer.

## 2. Các nguồn quy chuẩn kỹ thuật

- Microsoft Learn, *Working with WordprocessingML tables*: `tblPr`, `tblGrid`, `tr`, `tc`: https://learn.microsoft.com/en-us/office/open-xml/word/working-with-wordprocessingml-tables
- Microsoft Learn, *TableWidth* và *TableCellWidth*: `tblW` và `tcW` là **preferred widths**, có thể bị layout override: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablewidth?view=openxml-3.0.1 và https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablecellwidth?view=openxml-3.0.1
- Microsoft Learn, *RunProperties*: hiệu lực phụ thuộc chuỗi style và direct formatting: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.runproperties?view=openxml-3.0.1
- Microsoft Learn, *TableHeader*: chỉ hàng đầu liên tiếp mới có hiệu lực lặp: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tableheader?view=openxml-3.0.1
- Microsoft Support, *Repeat table header on subsequent pages*: manual page break có thể ngăn lặp: https://support.microsoft.com/en-gb/word/repeat-table-header-on-subsequent-pages
- Microsoft, *trHeight* implementation notes: hRule, exact/atLeast/auto và sự khác biệt Word: https://learn.microsoft.com/en-us/openspecs/office_standards/ms-oe376/3b8129c1-9aac-4611-a50e-247d13a382b2
- HarfBuzz, *Getting started*: shaping font/runs thành glyph advances và vị trí, không cần rasterize: https://harfbuzz.github.io/getting-started.html
- Unicode, *UAX #14*: vị trí có thể ngắt dòng; *UAX #29*: grapheme clusters: https://www.unicode.org/reports/tr14/ và https://www.unicode.org/reports/tr29/
- Microsoft Support và Section508.gov, hướng dẫn cấu trúc bảng đơn giản, tiêu đề rõ, hạn chế merge/nest: https://support.microsoft.com/en-us/accessibility/word/make-your-word-documents-accessible-to-everyone-with-accessibility-assistant và https://www.section508.gov/blog/accessibility-bytes/data-tables-in-documents/
- W3C WCAG, công thức contrast 4.5:1 cho chữ thông thường trên web: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum — dùng như **định hướng khả năng đọc**, **không** tuyên bố tự động áp dụng tính pháp lý WCAG cho mọi DOCX/biểu mẫu.

## 3. Hợp đồng dữ liệu đầu vào

### 3.1. Dữ liệu từ DOCX/OOXML
- Các vị trí `part_uri`, table id, body/appendix, section và parent cell; `page_width`, lề, gutter, mirror, multicolumn, table indent, floating, text flow và `W_allow` với provenance.
- `tblPr`, `tblGrid`/`gridCol`, `tblW`, `tblLayout`, `tcW`, `gridSpan`, `vMerge`, gridBefore/gridAfter, `tblCellMar`, `tcMar`, `tblCellSpacing`, `tblBorders`/`tcBorders`, `tblLook`, các thuộc tính style/conditional, `trHeight`/`hRule`, `tblHeader`, `cantSplit`, `keepNext`.
- Mỗi cell/paragraph/run: nội dung nguyên gốc, whitespace, breaks, NBSP, nonbreaking hyphen, fields, links, numbering, font hiệu dụng, size, bold/italic, `pPr`/indent/tabs/spaceBefore/spaceAfter/line spacing/justification.
- Vai trò bảng: `TASK_MATRIX`, `DATA_STAT`, `SCHEDULE`, `PERSONNEL_LIST`, `LEGAL_COMPARISON`, `APPENDIX_REGISTER`, `OFFICIAL_FORM`, `LAYOUT_TABLE`, `UNKNOWN`; vai trò từng cột và `reader_task`, nguồn của nhãn ngữ nghĩa.
- Quyền sửa, biểu mẫu, trường khóa, thay đổi đang theo dõi, chữ ký số và các vùng cấm.

### 3.2. Dữ liệu đo chữ (không phải render)
- Dùng Times New Roman **đúng file face/phiên bản được cấp phép và có thực**: Regular, Bold, Italic, Bold Italic tương ứng các run; kích thước chỉ 13 hoặc 14 pt. Không dùng Liberation Serif/Arial/Calibri để thế chỗ mà vẫn ghi TNR.
- `font_identity`: family, face/style, version hoặc fingerprint phù hợp chính sách nội bộ; **không phân phối kèm file font có bản quyền**.
- `shaping_metrics`: chiều dài run sau glyph shaping, kerning và script/language; không tính `số_ký_tự × hệ_số`.
- `line_break_opportunities`: phân đoạn Unicode UAX #14/#29, theo chính sách tiếng Việt và các ngắt dòng cứng có sẵn; giữ nguyên token được bảo vệ.
- Nếu thiếu font thực hoặc có fallback/field/shape/tabs không được hỗ trợ, đánh dấu `TEXT_UNCERTAIN`; không ngụy tạo độ rộng đã đo.

## 4. Tầng G0: Hard gates trước mọi điểm số

| ID | Điều kiện cứng | Kiểm tra | Trạng thái khi không đủ dữ liệu |
|---|---|---|---|
| G0-01 | Font hiệu dụng Times New Roman | Giải quyết style cascade/run font | `UNKNOWN_FONT_EFFECTIVE` |
| G0-02 | Cỡ chữ hiệu dụng chỉ 13 hoặc 14 pt | `w:sz`/`w:szCs` và style inheritance; 26/28 half-point | `UNKNOWN_EFFECTIVE_SIZE` |
| G0-03 | Biểu mẫu và authority không bị vi phạm | Quyền sửa và khóa cấu trúc/nội dung | `PRESERVE` hoặc `REVIEW` |
| G0-04 | Không sửa nội dung/mã/số/field/quan hệ/ô gộp | So source snapshot với giả định candidate | `UNKNOWN_INTEGRITY` |
| G0-05 | Ngân sách bề rộng và `gridSpan` hợp lệ | `Σ width_i ≤ W_allow`, span constraints, locks **theo mô hình đã xác minh** | `UNKNOWN_GEOMETRY` |
| G0-06 | Không dùng fitText/scale/character compression để ép vừa | Style/run/cell properties | `REVIEW` |
| G0-07 | Nội dung không ngắt có **khả năng** vừa trong chiều rộng hiệu dụng | So `protected_token_upper_bound` với `inner_width` khi font metrics hợp lệ | `TEXT_UNCERTAIN` |
| G0-08 | Dữ liệu số nguyên bản, gồm số 0 đầu, giá trị 0 ≠ ô trống | Exact text/content compare | `UNKNOWN_INTEGRITY` |

**G0 PASS** không có nghĩa “chữ chắc chắn không cắt trong Word”. Khi `G0` FAIL thì **không tính điểm thẩm mỹ để cứu**. Khi điều kiện thiết yếu UNKNOWN thì chỉ trả `REVIEW_REQUIRED` hoặc `PROPOSE_WITH_UNCERTAINTY`, không được `WORD_VERIFIED`.

**Lưu ý:** `tblW`/`tcW` là giá trị ưu tiên, nên `Σ grid widths ≤ W_allow` chỉ là cổng hình học của ứng viên giả định, không phải khẳng định biên thực tế của Word. `trHeight=exact` là chỉ báo nguy cơ khi chiều cao ước lượng vượt; không được gắn “đã cắt chữ” nếu không có kết quả kết xuất.

## 5. Đo chữ, độ rộng tối thiểu, số dòng và chiều cao — M1 không render

### 5.1. Đơn vị và đo chữ

`1 pt = 20 twips`; `1 mm ≈ 56.6929 twips`. `w:sz=26` tương đương 13 pt; `w:sz=28` tương đương 14 pt (sau giải quyết inheritance).

Với mỗi run có font face/size hiệu dụng:

```text
advance_pt(run) = Σ[glyph_advance_in_font_units × fontsize_pt / units_per_em]
```

Đây là biểu diễn ý tưởng của phép đo **glyph shaping**; trong thực tế nên lấy glyph advances từ thư viện chính xác, có xử lý ligature, kerning, dấu kết hợp, script và language. Cộng các runs **sau khi tách thích hợp theo font face/style và đặc tính shaping**; đừng tự coi phép cộng từng Unicode code point là đúng.

### 5.2. Chiều rộng hữu dụng

```text
span_width = Σ(width(grid column covered by physical cell))
cell_inner_width = span_width - padding_start - padding_end
                   - applicable_border_and_spacing_budget
                   - applicable_paragraph_indents
```

Các thành phần đệm/viền, indent và spacing phải lấy theo giá trị **hiệu dụng** cùng đơn vị. Nếu không resolve được, trường `cell_inner_width_status=UNKNOWN`.

### 5.3. Độ rộng tối thiểu cho token không ngắt

```text
hard_floor(cell) = max(shaped_width(t) for t in protected_unbreakable_tokens)
                   + horizontal_padding + applicable_border/spacing/indent
```

Với ô gộp ngang, chỉ bắt `Σ(w_i, i ∈ span) ≥ hard_floor(cell)`, không nhân bản token vào từng cột. Nếu token dài hơn toàn bộ vùng chứa, trả `NO_SAFE_INLINE_FIT`; không hạ font, không bẻ mã hoặc đổi dữ liệu.

### 5.4. Áp lực xuống dòng

```text
L_rc(w) = estimated_line_count(original text runs, break opportunities,
                               shaped glyph widths, cell_inner_width(w))
H_rc(w) ≈ Σ_paragraphs[L × line_advance + effective_paragraph_spacing]
          + vertical_padding
H_r(w)  ≈ max(H_rc(w) of ordinary physical cells in row)
```

`L_rc` và `H_rc` là **ước lượng**, không phải số dòng/chiều cao của Word. Với `vMerge`, nested table, hình/shape, `trHeight`, row spans, page breaks hoặc quy tắc paragraph đặc biệt, phải có mô hình ràng buộc riêng và giảm confidence; không cộng/max đơn giản như bảng thường.

### 5.5. Không cố gán một số dòng đẹp cho mọi bảng
- STT, mã, ngày, số: ưu tiên nguyên token, thường một dòng khi có thể.
- Tên/đơn vị: xuống dòng theo cụm có nghĩa, thông thường một–hai dòng là **đích mềm**, không bắt buộc.
- Diễn giải: nhiều dòng là hợp lệ, chỉ phạt trường hợp có các dòng vụn do cột hẹp không cần thiết.
- Tiêu đề: đánh giá riêng phần header, không ưu tiên nội dung theo cách phá header.
- Số dòng `L` phải đo trên tất cả ô/hàng có vai trò khác nhau; không chỉ chọn ô dài nhất.

## 6. Danh mục 12 chỉ số định lượng có thể giải thích

| Mã | Chỉ số | Công thức hoặc phép tính đề xuất | Mức bằng chứng |
|---|---|---|---|
| M01 | `effective_font_conformity` | # runs hiệu dụng TNR13/14 / # runs trong scope (gắn cổng G0 cho vi phạm) | `STRUCTURAL` nếu style resolve đủ |
| M02 | `protected_token_fit_rate` | # token có `upper_estimated_width ≤ inner_width` / # token kiểm được; **một critical token fail không được bù bằng trung bình** | `TEXT_ESTIMATE` |
| M03 | `semantic_alignment_accuracy` | # ô căn theo vai trò / # ô có vai trò phân loại đáng tin (STT center; số right; mô tả left) | `STRUCTURAL+SEMANTIC` |
| M04 | `header_hierarchy_consistency` | # header cells có tính chất theo preset/authority / # header cells được xác định | `STRUCTURAL+SEMANTIC` |
| M05 | `header_fragmentation_rate` | # header có wrap bất hợp lý / # header có đánh giá tin cậy; định nghĩa bất hợp lý theo vai trò và trường hợp | `TEXT_ESTIMATE` |
| M06 | `short_fragment_rate` | # dòng mềm chỉ chứa cụm rất ngắn khó đọc / # dòng đủ điều kiện; không phạt ngày, mã, header ngắn có chủ đích | `TEXT_ESTIMATE` |
| M07 | `row_bottleneck_cost` | `Σ H_r(w)` và các hàng chi phối; ưu tiên **so với baseline**, không phạt bảng có nội dung dài hợp lệ | `TEXT_ESTIMATE` |
| M08 | `unused_width_pressure` | `Σ_i max(0, w_i - useful_cap_i) / Σ_i w_i`, loại trừ cột locked/mẫu; cap có provenance | `ESTIMATED+SEMANTIC` |
| M09 | `padding_legibility` | Phép phù hợp với preset và độ cao/nội dung: TNR 13/14, horizontal/vertical padding đã xác định; tránh 0 hoặc quá mức | `STRUCTURAL+HEURISTIC` |
| M10 | `border_semantic_consistency` | # đường viền phù hợp vai trò và preset / # cạnh được kiểm; xử lý border cascade, không đếm lines đơn thuần | `STRUCTURAL+SEMANTIC` |
| M11 | `table_family_consistency` | # thuộc tính hiệu dụng nhất quán trong các bảng **cùng vai trò và authority** / # thuộc tính so được | `STRUCTURAL` |
| M12 | `header_accessibility_structure` | Kiểm tra header đầu liên tiếp, nhận diện tiêu đề cột, tính phức tạp merge/nest và khóa mẫu; **không** suy tương đương screen-reader PASS | `STRUCTURAL` |

**Quy tắc quan trọng:** denominator = 0 thì `N/A`, không tự ghi 100%. Nếu một chỉ số thiếu bằng chứng thì để `UNKNOWN`, không nhận điểm 0 hoặc 100 để đánh lừa thang điểm. Cần xác định scope và vai trò cho mọi chỉ số.

## 7. Thang chất lượng 6 chiều (rubric nội bộ, không phải chuẩn pháp lý)

| Chiều | Trọng số thử nghiệm | Thành phần có thể xét |
|---|---:|---|
| R — Readability / khả năng đọc | 35% | M02, M03, M05, M06 |
| G — Geometry / bố cục và độ rộng | 25% | M07, M08; M02 và span constraints đã là G0 |
| H — Hierarchy / phân cấp thông tin | 15% | M04, M12 |
| S — Spacing / đệm và nhịp đọc | 10% | M09, khoảng cách đoạn/line spacing |
| C — Consistency / tính nhất quán | 10% | M01 (hard gate), M11 và nhất quán cỡ, căn lề, header |
| V — Visual economy / viền và mức tiết chế | 5% | M10, xử lý theo preset/authority |
| **Tổng** | **100%** | Mỗi chiều 0–100 **nếu có dữ liệu đủ tin cậy** |

Các tỷ trọng **35/25/15/10/10/5 chỉ là baseline nghiên cứu để thử nghiệm**, không phải tỷ trọng đúng với mọi loại bảng. `FORMAL_GRID` và `STATISTICAL_MINIMAL` có thể có trọng số khác nhau sau khi được hiệu chỉnh; biểu mẫu khóa chỉ PRESERVE.

```text
quality_score_observed = Σ(weight_k × score_k) / Σ(weight_k for observed k)
evidence_coverage = Σ(weight_k for observed k) / Σ(all applicable weights)
```

Không so sánh hai điểm số nếu `coverage`, độ tin cậy phép đo, các chiều được đánh giá hoặc profile khác nhau. Chỉ công bố `quality_score_observed` khi hard gates có đủ dữ liệu, và đi kèm `evidence_coverage`. **Không có threshold “≥85 = đẹp” được xác minh trong dự án này**. Nếu muốn đặt các ngưỡng vận hành, phải có bộ nhãn chuyên gia và đo lỗi phân loại.

Đề xuất dùng điểm số cho *xếp hạng sau hard gates*; thứ tự quyết định thực tế là **lexicographic**:

```text
1. Chặn FAIL của authority / form / content / font-size / geometry.
2. Giữ số lượng lỗi critical token và ambiguity bằng 0 (nếu đo được).
3. Không làm xấu khả năng đọc tiêu đề, mã, số, tên chủ thể quan trọng.
4. Không gây hồi quy row bottleneck / padding / chi phí wrap đã dự đoán.
5. Cải thiện thứ bậc thông tin, consistency, border/spacing theo profile.
6. Nếu khác biệt nhỏ hơn bất định/không có lợi ích cụ thể: KEEP_EXISTING.
```

## 8. Ví dụ lựa chọn ứng viên với 4 cột

**Tình huống giả lập, không phải số đo bằng Times New Roman trên một tài liệu thật**: A4, vùng hữu dụng cho bảng inline là 165 mm, header `STT | Nội dung công việc | Đơn vị thực hiện | Hạn`, Times New Roman 14 pt; hàng nội dung có mô tả dài, tên phòng và ngày. Không có biểu mẫu khóa, không có ô gộp. Giá trị mm sau đây là **vector minh họa để giảng giải quyết định**, KHÔNG là ngưỡng dùng lại cho bảng khác.

| Ứng viên | STT | Nội dung | Đơn vị | Hạn | Tổng |
|---|---:|---:|---:|---:|---:|
| A — hiện có | 26 | 50 | 58 | 31 | 165 |
| B — cân đối | 14 | 80 | 40 | 31 | 165 |
| C — ưu tiên nội dung quá mạnh | 14 | 90 | 29 | 32 | 165 |

Từ dữ liệu cấu trúc: A có STT lớn hơn nhu cầu giả định trong khi mô tả bị co; B dùng bề rộng ấy cho nội dung, **nếu** các token/tiêu đề của STT, Đơn vị, Hạn đều đạt hard floors; C có thể khiến tên đơn vị thành các dòng vụn. Ứng viên B là **giả thuyết đáng thử**, không phải phương án tối ưu được chứng minh bằng tổng mm; cần bảng giá trị run cụ thể và font metrics TNR để tính M02–M08. Giữ A làm baseline, chọn B chỉ khi lợi ích toàn hàng vượt bất định và không làm xấu trường quan trọng; nếu không, `KEEP_EXISTING`.

Một ví dụ **giả lập điểm thành phần**, không phải kết quả test/nhãn chuyên gia:

| Chỉ số | A | B | C |
|---|---:|---:|---:|
| R (35%) | 52 | 84 | 79 |
| G (25%) | 69 | 88 | 66 |
| H (15%) | 88 | 90 | 88 |
| S (10%) | 73 | 87 | 85 |
| C (10%) | 90 | 90 | 90 |
| V (5%) | 84 | 84 | 84 |
| `Q` giả lập | **69.15** | **86.80** | **79.05** |

Điểm 86.80 **không chứng minh** B đẹp; chỉ cho thấy cách tổng hợp **sau** khi đã có điểm thành phần đáng tin. B không đủ điều kiện nếu bất kỳ critical token nào không vừa, dù `Q` cao hơn.

## 9. Dải bất định để tránh “độ chính xác giả”

```text
shape_width(token) ∈ [lower_bound, upper_bound]  # nếu được hiệu chỉnh
inner_width(candidate) = exact/estimated/unknown
fit_status(token):
  if lower_bound > inner_width:  HIGH_RISK_NOT_FIT
  elif upper_bound <= inner_width: ESTIMATED_FIT
  else:                           BORDERLINE_REVIEW
```

Khoảng bất định phải đến từ bộ dữ liệu hiệu chỉnh font, Word version/environment hoặc độ chính xác phép đo; **không tự mặc định ±3%, ±5%** khi chưa có số liệu. Nếu không có TNR face hợp lệ, `lower_bound`/`upper_bound` không đáng tin và kết luận là `UNKNOWN`, không đoán mm bằng số ký tự.

`G` về width và `M02` có thể ước lượng; `page_count`, ranh giới ngắt trang, hoàn toàn không bị clipping và vẻ đẹp bản in vẫn là `NOT_VERIFIED_BY_RENDER`. **Không chạy render là lựa chọn thiết kế hợp lệ; chỉ cần báo cáo đúng phạm vi kết luận**.

## 10. Biểu mẫu đầu ra máy đọc — mô tả JSON tham khảo, không phải API hay schema đã xây

```json
{
  "spec": "TQA-NR-V17-DRAFT",
  "table_id": "document.xml#tbl-04",
  "scope": "CONTENT_TABLE",
  "font_policy": {"family": "Times New Roman", "allowed_pt": [13, 14], "resolved_pt": 14},
  "table_type": "TASK_MATRIX",
  "authority": "ND30_PROFILE_WITHOUT_LOCKED_FORM",
  "metric_source": "OOXML_STRUCTURAL_PLUS_TNR_SHAPING",
  "geometry": {"W_allow_twips": 9354, "geometry_status": "VERIFIED_FOR_INLINE_MODEL"},
  "hard_gates": {"status": "UNKNOWN", "failures": [], "unknowns": ["CRITICAL_TOKEN_FIT_NOT_MEASURED"]},
  "quality_dimensions": {"R": null, "G": null, "H": null, "S": null, "C": null, "V": null},
  "quality_score": null,
  "evidence_coverage": 0,
  "source_confidence": "PARTIAL",
  "candidate_widths_twips": null,
  "decision": "MEASURE_REQUIRED",
  "reasons": ["NO_TRUSTED_TNR_GLYPH_METRICS"],
  "claims_forbidden": ["WORD_RENDER_VERIFIED", "PRINT_READY"]
}
```

JSON trên là **ví dụ cấu trúc**, không phải một case đã chấm: `null` cố ý chỉ dữ liệu chưa đo; `W_allow_twips` minh họa phép làm tròn 165 mm (≈9354 twips), không xác nhận geometry của tài liệu thực tế.

## 11. Hiệu chỉnh chất lượng từ đánh giá chuyên gia, không đưa render vào quy trình AI

118 case V16 là **tình huống đặc tả**, không phải 118 nhãn “đẹp” độc lập. Chúng có thể kiểm tra hard gates và logic nhưng không đủ để kết luận điểm thẩm mỹ tương quan với đánh giá con người.

Để có độ tin cậy khoa học, giai đoạn nghiên cứu **có thể** thực hiện một lần ngoại tuyến với những người am hiểu trình bày văn bản: (1) chọn 30–50 bảng đại diện từ nguồn có quyền sử dụng, tách tập để hiệu chỉnh và tập giữ lại; (2) ít nhất hai hoặc ba người đánh giá độc lập theo rubric “đọc dễ”, “cân đối”, “đúng ngữ cảnh” và cặp phương án; (3) đo mức bất đồng và đồng thuận giữa người đánh giá; (4) so độ chính xác xếp hạng cặp và sai số trên tập giữ lại; (5) sửa rubric dựa trên lỗi thực, không chỉnh nhãn để ép mô hình PASS. **Nếu người đánh giá không nhìn bản trình bày, thước đo chỉ kiểm chứng độ nhất quán của quy tắc, không kiểm chứng cảm nhận thẩm mỹ.**

Công đoạn nghiên cứu/hiệu chỉnh này **không phải bước runtime**: về sau AI chỉ cần cấu trúc OOXML, nội dung và font metrics, hoàn toàn không yêu cầu render Word/PDF/ảnh để lựa chọn ứng viên.

## 12. Mapping đến case NR01–NR118

- Nhóm ngữ nghĩa, phân loại bảng: M03, M04, M11; ưu tiên `reader_task` và scope.
- Unicode/chuỗi không ngắt: M02, M05, M06 và interval confidence.
- Số liệu, ngày, mã có số 0 đầu: G0-08, M02, M03.
- Geometry, bảng lồng: G0-05, M07/M08 nếu geometry có đủ bằng chứng; không thì REVIEW.
- Tiêu đề đa tầng, ô gộp: M04/M05/M12 và `gridSpan/vMerge` constraints.
- Border, Table Style: M09–M11 và style cascade, locks.
- Field/hyperlink/ảnh: G0-04, `TEXT_UNCERTAIN`, không gán số đo glyph cho field chưa xác định.
- Biểu mẫu/chữ ký số: G0-03 → PRESERVE/BLOCK, không chấm preset.
- KEEP/NO_OP: baseline là nghiệm chính thức, chỉ đổi khi cải thiện có ý nghĩa vượt bất định.

**Chính sách chống lặp lại:** bổ sung cột `metric_ids`, `expected_behavior`, `evidence_type`, `confidence`, `not_supported` vào case hiện có khi biên soạn trong tương lai; không tự phát sinh 118 điểm giả để tuyên bố đã kiểm định.

## 13. Definition of Done ở mức tài liệu nghiên cứu

- [ ] 12 chỉ số có định nghĩa đo, đơn vị, phạm vi áp dụng và ranh giới `UNKNOWN/N/A`.
- [ ] G0 hard gates được thực hiện trước Q; một lỗi critical không thể được bù bằng điểm đẹp.
- [ ] Ví dụ của tất cả loại bảng trong V16 có mapping metric IDs và expected decisions, không có xung đột.
- [ ] Có tập TNR 13/14 font metrics provenance hoặc trường `TEXT_UNCERTAIN` đúng; không giả bộ đã đo.
- [ ] Rà soát 100 case mới/18 case cũ bằng blind decision với dữ liệu đầu vào và rubric thống nhất, không lộ answer key.
- [ ] Khi có số liệu đánh giá chuyên gia, công bố độ đồng thuận và kết quả trên tập holdout; trước đó không gọi là “độ đẹp được chứng minh 90%”.
- [ ] Không có mã xử lý Word, plugin, API, CI, engine, backend, ảnh hoặc PDF được sinh như yêu cầu dự án này.

**Trạng thái hiện tại:** `RESEARCH_SPEC_DRAFT`. Tài liệu giới thiệu mô hình định lượng và công thức/điều kiện đánh giá, **chưa có bộ dữ liệu font glyph TNR thực, nhãn chuyên gia độc lập hoặc blind-test được thực thi**.
