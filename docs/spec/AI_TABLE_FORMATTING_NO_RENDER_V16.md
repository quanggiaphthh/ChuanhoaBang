# ChuanhoaBang — V16: Đặc tả quyết định định dạng bảng nội dung DOCX không cần render

**Trạng thái:** DRAFT SPEC — tài liệu nghiên cứu/đặc tả; **không phải** phần mềm đã triển khai, engine Word hoặc chứng nhận chất lượng bản in.  
**Ngày biên soạn:** 29/10/2026.  
**Authority nghiên cứu:** [Báo cáo hợp nhất V15](https://github.com/quanggiaphthh/ChuanhoaBang/blob/main/docs/research/Bao_cao_chuan_hoa_va_toi_uu_bang_DOCX_ND30_HD05_V15_2026.md).  
**Mục tiêu độc lập:** hướng dẫn AI/công cụ đọc **nội dung + cấu trúc + thông số định dạng** của bảng trong DOCX, đưa ra phương án **cụ thể, có căn cứ, có thể tái lập** mà **không phải render/chụp ảnh/xem PDF** trong quy trình ra quyết định.  
**Ràng buộc dự án:** **chỉ Times New Roman; kích thước chữ trong bảng nội dung chỉ 13 hoặc 14 pt** (không sử dụng 12 pt, 10 pt, font khác hoặc nén/kéo giãn glyph để ép vừa).

> **Ranh giới quan trọng:** “Đặc tả không render” đồng nghĩa với khả năng **kiểm tra cấu trúc và chọn phương án có căn cứ**. Nó **không** đồng nghĩa với lời cam kết rằng Word ở mọi máy sẽ hiển thị, ngắt dòng hoặc phân trang đúng tuyệt đối. Các kết luận phụ thuộc bộ dàn trang phải ghi **ước lượng**, không giả nhận là đã quan sát.

---

## 0. Audit V15 → những thành phần tái sử dụng, không xây lại

| Nội dung cần có | Phần V15 tái sử dụng | Quyết định V16 |
|---|---|---|
| Căn cứ pháp lý; phân biệt pháp lý/mẫu/khuyến nghị | Phần I–III; ký hiệu `[PL]/[BM]/[KN]/[KT]/[BK]` | **REUSE**, không tạo bộ quy tắc pháp lý thứ hai |
| Preset cho bảng hành chính/thống kê/mẫu | Phần VII; mục 27–30; Phần XIII, mục 47–49 | **EXTEND** bằng điều kiện chọn thông số và ma trận ngoại lệ |
| Nhận diện mục tiêu người đọc và vai trò cột | Phần XIX, mục 70–73; Phần XXIV, mục 145 | **REUSE**, tách ý nghĩa cột và nhu cầu độ rộng |
| Hình học bảng, cột, ô gộp, kiểu width | Phần XII, XIV, XXIII–XXV | **REUSE**, bổ sung kết luận `STRUCTURAL` so với `ESTIMATED` |
| Phân bổ chiều rộng theo nội dung | Phần XIX/XX/XXIII, nhất là mục 72, 73, 125 | **ADAPT** để ra quyết định không có ảnh/PDF, vẫn kiểm soát bất định |
| Chống sửa nhầm, style cascade, ngoại lệ | Mục 126–128, 159, 167–169; AGENTS.md | **REUSE** hard gates và lý do KEEP/REVIEW |
| Corpus F01–F08 và V10–V15 | Phần XXVI–XXXI; EXPERIMENT_EVIDENCE | **REUSE** như ví dụ/benchmark lịch sử, không gọi là test V16 đã PASS |
| Nghiệm thu Word/renderer | Các phần V6–V15 | **KHÔNG loại bỏ khỏi V15**; V16 không đòi để **ra đề xuất**, không mượn kết quả đoán làm chứng nhận bản in |

**Khoảng trống giải quyết trong V16:** định nghĩa đầu vào tối thiểu, chính sách font 13/14, bảng quyết định thao tác, mô hình không-render, tập trường hợp cụ thể và QA trên code/OOXML. **Không** bổ sung engine, CI, server, parser, framework AI hay thư viện runtime.

## 1. Phạm vi, ưu tiên authority và trường hợp không áp dụng

### 1.1. Phạm vi được xử lý
- Bảng dữ liệu/nội dung trong **Body** hoặc **phần nội dung của Phụ lục** của văn bản hành chính và văn bản Đảng; bao gồm bảng phân công, lịch, danh sách, thống kê, đối chiếu, báo cáo, bảng nhiều cột và một số bảng nhiều hàng.
- Cho phép AI **đề xuất** định dạng cho bảng mới hoặc bảng hiện có, nhưng đối với bảng hiện có chỉ xem xét **format-only** và các thuộc tính được phép thay đổi.
- Đặc tả tương thích để nơi sử dụng ánh xạ sang API Word, ONLYOFFICE hay OOXML hiện có; **không định nghĩa cách triển khai một engine độc lập**.

### 1.2. Loại trừ/chặn sửa tự động
- Bảng dàn trang quốc hiệu, cơ quan, nơi nhận, chữ ký, đóng dấu; bảng biểu mẫu chính thức đã ban hành/đã khóa; bảng có chữ ký số, field nhạy cảm, control khóa hoặc đang ở tracked changes mà chưa có quy trình bảo toàn chứng minh được.
- Bảng lồng, bảng nổi, bảng có ô gộp phức tạp, nhiều section, cột văn bản đặc biệt, text direction, shape/ảnh trong ô hoặc cấu trúc không đọc đầy đủ: **được chẩn đoán nhưng không tự áp preset**; chỉ đề xuất khi những ràng buộc liên quan đã được xác nhận.
- Không đổi nội dung, giá trị, số liệu, thứ tự hàng/cột, mã có số 0 đầu, dấu câu, màu mang ngữ nghĩa, số mục phụ lục, biểu mẫu hoặc vùng ngoài bảng.
- Mẫu chính thức/điều kiện pháp lý được áp dụng trước khuyến nghị thẩm mỹ. Nếu yêu cầu font 13–14 của dự án không tương thích mẫu bắt buộc, **không cố sửa mẫu**, trả `SCOPE_CONFLICT`/`PRESERVE`.

### 1.3. Định nghĩa mức bắt buộc
- **`HARD`** — ràng buộc an toàn, dữ liệu, phạm vi quyền sửa, font/size của chính *đặc tả dự án*, hoặc điều khoản/mẫu đã xác minh; không dùng điểm thẩm mỹ để vượt qua.
- **`RECOMMENDED`** — thông số thẩm mỹ theo loại bảng, không phải định mức pháp luật.
- **`ESTIMATED`** — thông số hình học chữ, xuống dòng, chiều cao hoặc phân trang **chưa quan sát trong Word**.
- **`UNKNOWN`** — thiếu thông tin cần để kết luận; trả review/giữ nguyên, không tự điền số đo.

## 2. Hợp đồng dữ liệu đầu vào tối thiểu

Để AI quyết định, dữ liệu không phải ảnh mà là một **bản tóm tắt có định danh nguồn** từ cấu trúc DOCX và nội dung:

| Nhóm dữ liệu | Trường tối thiểu | Nếu thiếu |
|---|---|---|
| Nguồn và thẩm quyền | Loại văn bản, profile, nguồn/mẫu bắt buộc, phạm vi sửa, định danh bảng, nguồn gốc dữ liệu | `REVIEW_REQUIRED` hoặc `PRESERVE` |
| Vị trí | Body/Appendix/Other, section hoặc parent cell, bảng inline/floating | Không tối ưu width tự động |
| Trang/vùng chứa | Page width/orientation, lề, gutter/mirror, text column, indent, container width | `GEOMETRY_UNKNOWN` |
| Lưới | `tblGrid`, số cột vật lý, `gridSpan`, `vMerge`, omitted cells, locked columns, `tblLayout`, `tblW`, `tcW` | Không tạo width vector mới |
| Dữ liệu | Tiêu đề cột, từng hàng/ô, đoạn, run, ký tự gốc, kiểu dữ liệu, token không ngắt, ảnh/field | Không dự báo tin cậy độ rộng |
| Style hiệu dụng | Table style, `tblLook`, conditional style, run/paragraph direct format, border/padding thực tế, font/size | Không tuyên bố font/viền “đã đúng” |
| Chức năng | Mục tiêu tra cứu/điều hành/so sánh/tuân thủ; cột trọng tâm; ưu tiên do người dùng khai báo nếu có | Không tự suy mức quan trọng cao |
| Môi trường đo tùy chọn | Font Times New Roman hiện diện, face/version, khả năng đo glyph/shaping offline, chính sách wrap | `TEXT_ESTIMATE_LOW`, không kết luận số dòng chính xác |

**Quan trọng:** `tblW`, `tcW` và một số độ rộng khác trong WordprocessingML là **preferred width**, không phải kích thước hiển thị tuyệt đối. `tblGrid` thể hiện đường lưới logic và cần được xét cùng thuật toán layout, ô gộp, style và vùng chứa. Không gọi phép cộng XML là “đã đo bản in”.

## 3. Quy tắc bất biến font Times New Roman 13–14 pt

### 3.1. Chính sách chọn size

| Trường hợp | Giá trị lựa chọn | Điều kiện |
|---|---|---|
| Bảng nội dung hành chính thông thường, bảng 2–5 cột đọc dạng văn bản | **14 pt** mặc định | Không có profile/mẫu bắt buộc khác |
| Bảng thống kê hoặc bảng nhiều cột/mật độ cao | **13 pt** là lựa chọn có điều kiện | Chỉ khi profile/authority cho phép và cần giảm mật độ; phải ưu tiên tối ưu width/padding trước |
| Bảng của Đảng áp dụng Hướng dẫn 05/2026 | **14 pt** trong phạm vi V16 | Không tự hạ 13 pt chỉ để vừa bảng khi chưa có căn cứ áp dụng |
| Hàng tiêu đề, tổng cộng | **Cùng size được duyệt** 13/14; thường **bold** | Không tự dùng 15/16 pt cho tiêu đề nội bộ |
| Ô STT, số liệu, ngày, ghi chú | **Cùng size 13/14** theo bảng/profile | Không giảm riêng STT còn 10–12 pt |
| Bảng nguồn đã dùng 13/14 nhất quán và phù hợp | **Giữ nguyên** | Tránh thay đổi không mang lợi ích |
| Bảng nguồn chứa font khác hoặc size ngoài phạm vi | **Đề xuất chuẩn hóa** nếu đúng vùng và có quyền sửa | Nếu đối tượng/biểu mẫu đặc thù: `PRESERVE`/`SCOPE_CONFLICT` |

### 3.2. Hợp đồng kiểm tra bằng OOXML
- Xác định **font hiệu dụng** của mọi text run trong bảng nội dung, xét thứ tự kế thừa trực tiếp, paragraph style, table style/conditional style và document defaults. Không chỉ kiểm tra một `w:rFonts` ở cấp style rồi tuyên bố tất cả ô đã dùng Times New Roman.
- Các run văn bản thông thường phải có font **Times New Roman** sau khi resolve; với khai báo trực tiếp, xem các nhánh liên quan trong `w:rFonts` (ví dụ `ascii`, `hAnsi`, `eastAsia`, `cs`) theo phạm vi chữ thực tế, không nhầm thiếu thuộc tính với sai font.
- `w:sz`/`w:szCs` lưu đơn vị **half-point**: **13 pt → 26**, **14 pt → 28**. Size hiệu dụng có thể kế thừa từ style; không bắt buộc phải ghi đè tất cả run khi đã đúng.
- Giữ nguyên nội dung trong các run; không dùng font scale, char spacing âm, `fitText`, hidden text hoặc co kéo hình chữ để ép vừa bảng.
- Size 13/14 là **chính sách phạm vi của ChuanhoaBang**, không được trích thành “mọi ô bảng bắt buộc 13/14 theo NĐ30/HD05”.

## 4. Preset định dạng có điều kiện (không phải pháp lý)

| Thuộc tính | `FORMAL_GRID` — bảng hành chính/nội dung | `STATISTICAL_MINIMAL` — bảng số liệu | `PRESERVE_OFFICIAL_FORM` |
|---|---|---|---|
| Font | Times New Roman | Times New Roman | Theo mẫu; nếu ngoài 13–14 hoặc khác font thì cảnh báo xung đột, không sửa |
| Size | 14 pt; 13 pt nếu cho phép và mật độ cao | 13 hoặc 14 pt theo profile | Giữ theo mẫu |
| Màu chữ | Đen | Đen | Giữ |
| Header | Bold, nền trắng, căn theo dữ liệu | Bold, không tô màu mặc định | Giữ |
| Viền ngoài | Nét đơn **0,75 pt** (`w:sz=6`) | 0–0,5 pt tùy khả năng đọc | Giữ |
| Viền trong | Nét đơn **0,5 pt** (`w:sz=4`) | Ưu tiên viền ngang có nghĩa; viền dọc có thể bỏ | Giữ |
| Padding ngang | **1,5–2 mm** mỗi bên, điểm khởi tạo | **2–2,5 mm** nếu đủ vùng | Giữ |
| Padding dọc | **0,8–1,2 mm** mỗi phía | **1–1,5 mm** nếu không gây quá cao | Giữ |
| Cell spacing | 0 mm | 0 mm | Giữ |
| Chiều cao hàng | `auto` hoặc `atLeast` có lý do | `auto` | Giữ |
| STT | Center/middle | Center/middle nếu có | Giữ |
| Số và tiền | Right/middle; không tự làm tròn | Right/middle; đồng nhất đơn vị | Giữ |
| Văn bản dài | Left/top; cho phép wrap tự nhiên | Left/top | Giữ |
| Tổng cộng | Bold, đường phân cách khi có hàng tổng thật | Bold/đường kẻ nhóm | Giữ |
| Cỡ bảng | Có thể nhỏ hơn W hữu dụng | Có thể nhỏ hơn W hữu dụng | Giữ |

**Áp dụng preset:**
1. Có biểu mẫu/mẫu chính thức hoặc bảng dàn trang/chữ ký → **PRESERVE** (không dùng hai preset dữ liệu).
2. Bảng thống kê thuần, mục tiêu `COMPARE`/`SUMMARY`, các cột số rõ, không mẫu bắt buộc → cân nhắc **STATISTICAL_MINIMAL**.
3. Bảng dữ liệu thường, mục tiêu `ACTION`/`LOOKUP`/`COMPLIANCE` → **FORMAL_GRID**.
4. Vai trò chưa rõ hoặc bảng nhiều tầng đặc biệt → **REVIEW**, không gán preset bằng một nhãn tiêu đề đơn lẻ.
5. Nếu bảng nguồn đã nhất quán và không có lỗi xác định được → **KEEP_EXISTING**; không cần áp lại preset chỉ để có thay đổi.

### 4.1. Căn chỉnh theo kiểu dữ liệu, không căn đều tất cả ô

| Kiểu ô/cột | Căn ngang | Căn dọc | Ghi chú |
|---|---|---|---|
| STT, số thứ tự | Center | Center | Giữ `01`, `001` dạng chuỗi |
| Định danh/mã hồ sơ | Left hoặc Center đồng nhất | Center | Không ngắt token protected |
| Tên đơn vị/người | Left | Top nếu nhiều dòng | Tránh Justify tạo khoảng trắng lớn |
| Mô tả, ghi chú, căn cứ | Left | Top | Duy trì đoạn/list và xuống dòng tự nhiên |
| Giá trị số/tiền/tỷ lệ | Right | Center | Không thay dấu âm, thập phân, đơn vị |
| Ngày/hạn ngắn | Center hoặc Left nhất quán | Center | Không đổi thứ tự ngày-tháng-năm |
| Tiêu đề cột | Center **hoặc** theo kiểu dữ liệu | Center | Bold, không tự viết hoa/thêm xuống dòng cứng |
| Hàng tổng | Theo từng kiểu cột | Center | Bold khi đây thực sự là hàng tổng |

### 4.2. Khoảng cách đoạn và dòng trong ô
- Với **một đoạn văn ngắn trong mỗi ô**: khởi tạo before/after **0 pt** để tránh cộng chiều cao không cần thiết, nếu không có mẫu/authority yêu cầu khác.
- Với **ô chứa nhiều đoạn hoặc danh sách**: giữ cấu trúc đoạn, numbering và khoảng cách có nghĩa; đề xuất after **0–3 pt** ở phần cho phép, chỉ khi không trái rule/mẫu của vùng nội dung.
- Line spacing trong bảng dữ liệu thường: bắt đầu từ **single đến 1,15 lines** nếu profile cho phép; không áp mù quáng thông số của đoạn Body chung vào từng ô. Khi văn bản/mẫu yêu cầu line spacing khác, **authority thắng** hoặc chuyển review.
- Không dùng `Exactly` quá thấp so với font 13–14; đối với `trHeight=exact` có nguy cơ che nội dung, ưu tiên đề xuất `auto/atLeast` nhưng không khẳng định đã xác nhận lỗi nếu chưa có chứng cứ layout.

## 5. Thuật toán quyết định chiều rộng cột KHÔNG render

### 5.1. Hình học và đơn vị
- Xác định `W_allow` từ **section/column/parent cell thực**, sau khi xét lề, gutter, thụt bảng, phần chiếm dụng và bố cục đặc biệt; **không** tự dùng A4 165 mm cho tất cả tài liệu.
- Đơn vị nội bộ cho OOXML: **1 pt = 20 twips**, **1 mm ≈ 56,6929 twips**; kết thúc bằng **số nguyên twips**, điều chỉnh rounding có kiểm soát để tổng nhất quán.
- Nếu `W_allow` không chắc chắn (bảng nổi/lồng, nhiều cột, wrapped section, parent cell không đọc được), không cấp các giá trị mm giả chính xác: `GEOMETRY_UNKNOWN`.
- `sum(width_i) <= W_allow` cho bảng inline thông thường sau khi xác định đúng mô hình; **không** bắt buộc sử dụng hết bề rộng trang.

### 5.2. Mỗi cột có hồ sơ độc lập

| Thuộc tính | Ý nghĩa |
|---|---|
| `role` | `STT`, `IDENTIFIER`, `PRIMARY_CONTENT`, `OWNER`, `DATE`, `MEASURE`, `STATUS`, `NOTE`, `OTHER` |
| `reader_task_priority` | Độ quan trọng để đọc đúng dữ liệu — **không bằng độ rộng** |
| `hard_floor_twips` | Độ rộng tối thiểu xác minh được cho token không được ngắt + đệm + ràng buộc ô |
| `soft_floor_twips` | Độ rộng tối thiểu được khuyến nghị cho văn bản có thể wrap |
| `preferred_twips` | Độ rộng được mong muốn theo nhu cầu nội dung và header |
| `useful_cap_twips` | Mức rộng thêm không còn mang lại lợi ích rõ |
| `header_pressure` | Mức cần cho header, không chỉ giá trị trong cột |
| `cell_wrapping_pressure` | Áp lực xuống dòng từ từng ô, bao gồm các hàng thắt cổ chai |
| `locked` | Cấm đổi nếu mẫu hoặc người dùng khóa |
| `metric_confidence` | `MEASURED_FONT`, `APPROXIMATE`, `UNKNOWN` |

### 5.3. Đo chữ mà không render trang
1. **Ưu tiên** có font metrics/shaping phù hợp với Times New Roman **đúng font face/size** (13 hoặc 14), đo riêng text runs, bold/italic, khoảng trắng, dấu tiếng Việt, ký tự không ngắt và dấu tách dòng; đây là **đo chữ offline**, không phải tạo PDF hay kết xuất trang.
2. Xác định **break opportunities** dựa vào Unicode và ký tự thực (space, NBSP, nonbreaking hyphen, tab, soft break, line break, field...). Không thay đổi các ký tự nguồn để tối ưu.
3. `hard_floor_i = max(width(token bảo vệ), width(đối tượng không co), các khóa)` **cộng** padding trái/phải, viền hữu hiệu và các điều kiện áp dụng. **Không** lấy chiều rộng từ số ký tự × một hệ số mm chung.
4. `preferred_i` dựa vào chi phí wrap của tiêu đề và nội dung từng ô; xem số dòng **ước lượng** theo từng phương án width. Đừng lấy chuỗi dài nhất để bắt buộc mọi mô tả nằm trên một dòng.
5. Nếu **không có font metrics**, AI được nêu tương quan (STT cần hẹp hơn mô tả, cột số cần đủ token lớn nhất) và tạo ứng viên **LOW confidence**, nhưng **không** khẳng định `hard_floor` chính xác ở đơn vị mm hoặc chắc chắn không cắt chữ.
6. `w:tblW`, `w:tcW` là preferred widths; kể cả ứng viên thỏa tất cả phép tính, vẫn chỉ báo **geometry/estimation**, không công bố pixel hay page count thực tế.

**Công thức định hướng** (không phải phép mô phỏng Word):

```text
available_text_width(cell, col_width) = col_width
    - padding_left - padding_right - effective_border_budget

estimated_cell_lines(cell, col_width) = wrap_estimate(
    original_runs, original_breaks, available_text_width, TNR_font_metrics)

estimated_row_height(row, width_vector) ~= max(
    estimated_cell_lines * line_advance + vertical_padding + paragraph_spacing
    for each relevant physical cell)
```

Với `vMerge`, `gridSpan`, `trHeight`, `keepNext`, ảnh/field hoặc paragraph special: công thức trên là **proxy**, phải dùng constraint riêng hoặc giảm confidence; không tự lặp ô gộp thành nhiều ô.

### 5.4. Sinh và so sánh ứng viên hữu hạn

```text
INPUT source_table, source_section, authority, user_scope, font_policy=TNR_13_14
1. Xác định loại bảng, owner, phạm vi thay đổi và các khóa.
2. Đọc topology + style cascade + header + nội dung từng ô.
3. Nếu mẫu/đối tượng đặc thù/thiếu authority -> PRESERVE hoặc REVIEW.
4. Chọn size đã được phép: 14 mặc định, 13 chỉ khi cần và hợp lệ.
5. Xác định W_allow, font metric confidence, hard/soft floors, merged spans.
6. Nếu điều kiện toán học không khả thi -> NO_SAFE_FIT; không giảm font dưới 13.
7. Luôn có BASELINE; sinh tối đa 2–3 ứng viên có ý nghĩa:
   - A: phân bổ width theo token/header/nhu cầu wrap;
   - B: chỉnh cục bộ theo hàng gây áp lực cao;
   - C (tùy chọn): giảm padding trong khoảng được phép.
8. Loại ứng viên vi phạm source/authority/locks/shape/width hard gates.
9. Xếp hạng còn lại theo: bảo vệ token -> áp lực wrap ước lượng
   -> tính dễ quét cột -> nhất quán preset -> ít thay đổi.
10. Nếu bằng chứng đo thiếu hoặc các ứng viên gần tương đương -> KEEP/REVIEW.
OUTPUT: decision, selected_profile, font_pt, width_vector_twips,
        cell_styles, reason_codes, confidence, no_render_evidence.
```

**Lưu ý:** không biến `semantic_priority` thành `w_i = P_i / sum(P) × W`. Bảng có cột *thời hạn* rất quan trọng nhưng không cần rộng hơn cột mô tả nếu giá trị ngày đã vừa. Không làm hỏng header của cột khác khi nới mô tả. Một bảng nhỏ không cần ép phủ hết vùng chữ.

### 5.5. Các mức kết quả không-render
- `RULE_CONFORMANT`: kiểm tra được font/size hiệu dụng, kiểu ô, style được phép và bất biến **trên cấu trúc/metadata đã đọc**.
- `GEOMETRY_VALIDATED`: số học vùng chứa và grid/merge/locked widths đã được kiểm trên cấu trúc có đủ dữ liệu; **không phải Word visual PASS**.
- `DESIGN_RECOMMENDED`: có phương án định dạng, mục tiêu, tham số và giải thích; phần wrap/page/height chỉ là **dự đoán**.
- `KEEP_EXISTING`: bảng hiện có đạt các kiểm tra xác định; không có lợi ích có căn cứ từ phương án đổi.
- `PRESERVE`: bảng thuộc mẫu/khóa hoặc vùng không áp dụng.
- `REVIEW_REQUIRED`: thiếu authority/font metrics/geometry, bảng phức tạp hoặc kết quả bất định ảnh hưởng quyết định.
- `NO_SAFE_FIT`: không tìm được width vector thỏa ràng buộc trong font 13–14 và phạm vi hiện có; chỉ nêu lựa chọn cần phê duyệt như section ngang/phụ lục, không tự thực hiện.

## 6. Quy tắc quyết định độc lập có ID và điều kiện

| Rule ID | Điều kiện / mục tiêu | Kết luận hoặc thay đổi đề xuất | Mức |
|---|---|---|---|
| `V16-SCOPE-01` | Bảng nội dung Body/Appendix được phép | Cho phép đánh giá format-only | HARD |
| `V16-SCOPE-02` | Layout/signature/official form/unknown | PRESERVE/REVIEW; không áp preset dữ liệu | HARD |
| `V16-FONT-01` | Run hiệu dụng thuộc bảng nội dung | Times New Roman, 13 hoặc 14 pt | HARD (phạm vi dự án) |
| `V16-FONT-02` | Body dạng Đảng/HD05 | Chọn 14 pt theo profile V16; không tự hạ xuống 13 | HARD (profile) |
| `V16-FONT-03` | Nội dung đông, font 14 không hợp lý | Xem 13 pt **sau** width/padding, chỉ nếu authority cho phép | RECOMMENDED |
| `V16-PRESET-01` | Bảng công việc/danh sách | FORMAL_GRID, tiêu đề rõ, viền có nghĩa | RECOMMENDED |
| `V16-PRESET-02` | Bảng so sánh số liệu | STATISTICAL_MINIMAL khi phù hợp | RECOMMENDED |
| `V16-PRESET-03` | Bảng nguồn đã nhất quán | KEEP nếu không có lỗi có căn cứ | HARD (chống sửa thừa) |
| `V16-CELL-01` | Số/tiền/% | Căn phải; không sửa định dạng giá trị | HARD + RECOMMENDED |
| `V16-CELL-02` | STT | Căn giữa, width vừa đủ header/giá trị | RECOMMENDED |
| `V16-CELL-03` | Mô tả nhiều dòng | Căn trái/trên; wrap tự nhiên; không Justify ép | RECOMMENDED |
| `V16-CELL-04` | Một đoạn ngắn trong ô | before/after 0 pt nếu không có ngoại lệ | RECOMMENDED |
| `V16-CELL-05` | Hàng tổng được xác nhận | Đậm, phân cách mức nhẹ; không tạo tổng giả | RECOMMENDED |
| `V16-WIDTH-01` | Có geometry xác định | `sum(grid_width) <= W_allow` theo constraint đã xác lập | HARD |
| `V16-WIDTH-02` | Mã/ngày/token protected | Không cho ứng viên làm hỏng tính toàn vẹn token | HARD |
| `V16-WIDTH-03` | Ô gộp | Cấp theo **tổng span vật lý**, không nhân bản ô | HARD |
| `V16-WIDTH-04` | Cột quan trọng nhưng nội dung ngắn | Không cấp mm thừa chỉ theo priority | RECOMMENDED |
| `V16-WIDTH-05` | Thiếu TNR font metric | Chỉ ước lượng, không xác nhận số dòng/chiều cao | HARD (truthfulness) |
| `V16-ROW-01` | Bảng dữ liệu thường | `auto/atLeast`; không dùng `exact` không lý do | RECOMMENDED |
| `V16-PAGE-01` | Bảng có header dài | Chỉ gợi ý `tblHeader` cho nhóm hàng đầu liên tục; hiệu quả qua trang là chưa xác minh | RECOMMENDED |
| `V16-STYLE-01` | Shared table style/conditional style | Resolve cascade; tránh sửa style chung gây blast radius | HARD |
| `V16-QUALITY-01` | Bảng đã hợp lệ, không lợi ích rõ | KEEP_EXISTING/NO_OP_VALID | HARD |
| `V16-QUALITY-02` | Định dạng không render | Không đánh dấu `PRINT_READY`, `WORD_RENDER_VERIFIED` | HARD |

**Mỗi rule khi được dùng phải ghi**: `id`, `version`, `authority`, `scope`, `preconditions`, `input_evidence`, `action_or_noop`, `OOXML_properties`, `risk`, `confidence`, `reason_codes`. Cơ sở pháp lý vẫn ở V15/nguồn chính thức; không tạo một registry luật mới trong V16.

## 7. Ánh xạ sang OOXML để AI/formatter hiểu phải tác động vào đâu

| Quyết định | Thành phần liên quan | Cảnh báo bắt buộc |
|---|---|---|
| Font Times New Roman | `w:rFonts`, run/style inheritance, defaults | Kiểm tra **hiệu dụng**, không áp đè từng run khi không cần |
| Font size 13/14 | `w:sz=26/28`, `w:szCs` khi áp dụng | Đơn vị half-point; không lẫn với `w:sz` đường viền |
| Căn đoạn trong ô | `w:pPr/w:jc` | Phân biệt table alignment và cell paragraph alignment |
| Căn dọc | `w:tcPr/w:vAlign` | Bảng gộp dọc cần xét riêng |
| Line/paragraph spacing | `w:pPr/w:spacing` | Không ép `Exactly` hoặc body defaults vào mọi ô |
| Viền | `w:tblBorders`, `w:tcBorders`, style/conditional borders | Độ dày border `w:sz` theo **1/8 pt**; phải resolve cascade |
| Padding | `w:tblCellMar`, `w:tcMar`, exceptions | `tcMar` có thể override; xét cả `start/end` |
| Table width/layout | `w:tblW`, `w:tblLayout` | Preferred width, không phải pixel thực |
| Grid/column width | `w:tblGrid/w:gridCol`, `w:tcPr/w:tcW` | Không đổi lưới tách ô hoặc topology merge |
| Ô gộp | `w:gridSpan`, `w:vMerge`, `gridBefore/gridAfter` | Không tạo ô giả khi phân tích hàng |
| Chiều cao hàng | `w:trPr/w:trHeight` (`hRule`) | `auto`, `atLeast`, `exact`; không khẳng định clipping đã quan sát |
| Hàng tiêu đề lặp | `w:trPr/w:tblHeader` | Chỉ hàng đầu liên tiếp; không bảo đảm hành vi ở mọi ngắt trang |
| Chia hàng qua trang | `w:trPr/w:cantSplit` | Không bật đại trà cho hàng cao hơn trang |
| Conditional styling | `w:tblStyle`, `w:tblLook`, `w:tblStylePr`, `w:tblPrEx` | Không sửa shared style nếu ảnh hưởng bảng khác |

### Ví dụ OOXML minh họa **giá trị** (không phải template tài liệu đầy đủ)

```xml
<!-- Font 14 pt TNR cho một run được phép định dạng -->
<w:rPr>
  <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
  <w:sz w:val="28"/>
</w:rPr>

<!-- Border single: 0.75 pt => w:sz=6; 0.5 pt => w:sz=4 -->
<w:tblBorders>
  <w:top w:val="single" w:sz="6" w:color="000000"/>
  <w:insideH w:val="single" w:sz="4" w:color="000000"/>
</w:tblBorders>
```

Giá trị trên không đại diện XML đủ của một DOCX; cách chèn cụ thể phải tôn trọng vị trí phần tử hợp lệ, các style khác đang áp dụng và các ràng buộc của file gốc.

## 8. Quy trình AI ra quyết định (Decision Tree)

```text
[1] Bảng có thực là DATA TABLE thuộc Body/Appendix?
    NO / UNKNOWN -> PRESERVE / REVIEW
    YES -> [2]
[2] Mẫu/biểu mẫu/khóa/field/track-changes có cấm sửa?
    YES / UNKNOWN IMPACT -> PRESERVE / REVIEW
    NO -> [3]
[3] Profile cho phép TNR 13–14, chọn size hợp lệ?
    NO -> SCOPE_CONFLICT
    YES -> [4]
[4] Xác định row/column role, header, total, kiểu dữ liệu, style cascade?
    NO -> REVIEW / giữ nguyên
    YES -> [5]
[5] Geometry W_allow và lưới vật lý có xác định?
    NO -> Chỉ đề xuất style không đổi width + REVIEW width
    YES -> [6]
[6] Ước lượng font/token constraints, tạo candidate width?
    NO_SAFE_FIT -> review phương án bố cục, không xuống dưới 13 pt
    OTHERWISE -> [7]
[7] Check hard gates: authority / source / tokens / grid / merge / width?
    FAIL -> REJECT candidate
    PASS -> [8]
[8] So sánh readability proxy, header, whitespace, tính nhất quán,
    độ lớn thay đổi, mức tin cậy; chọn KEEP hoặc DESIGN_RECOMMENDED.
[9] Xuất kết quả kèm giá trị định dạng, lý do và phần chưa xác minh.
```

### 8.1. Thứ tự xử lý xung đột
1. Quy định/mẫu/khóa bảo toàn.
2. Giữ nguyên dữ liệu và topology.
3. Times New Roman 13–14 **trong phạm vi được phép**.
4. Hình học xác định, token thiết yếu, header.
5. Độ dễ đọc và tính nhất quán của bảng/bộ bảng cùng loại.
6. Can thiệp nhỏ nhất; với các phương án tương đương, ưu tiên BASELINE.

Không có “điểm đẹp” nào được dùng để bù lỗi mất dữ liệu, sai mẫu hoặc vượt phạm vi được phép.

## 9. Hợp đồng kết quả để AI trả lời cụ thể

Mỗi bảng nên có **một bản ghi quyết định**. Đây là **schema minh họa**, không cần tạo registry/dịch vụ:

```yaml
spec: ChuanhoaBang-V16-NoRender
source:
  table_id: "body-table-01"
  owner: body
  authority: ND30
  evidence_ref: "docx:word/document.xml; source-snapshot-id"
classification:
  type: TASK_MATRIX
  reader_task: ACTION
  confidence: HIGH
  preset: FORMAL_GRID
font_policy:
  family: Times New Roman
  size_pt: 14
  scope: all_eligible_content_runs
  effective_font_check: REQUIRED
page_geometry:
  status: VERIFIED
  usable_width_mm: 165
  width_mode: fixed_or_current_validated
column_analysis:
  - {column: 1, role: STRUCTURAL_INDEX, header: "STT", nowrap_required: true}
  - {column: 2, role: PRIMARY_CONTENT, header: "Nội dung công việc", wrap_allowed: true}
  - {column: 3, role: OWNER_ACCOUNTABLE, header: "Đơn vị thực hiện", wrap_allowed: true}
  - {column: 4, role: DEADLINE, header: "Thời hạn", nowrap_required: true}
recommendation:
  decision: DESIGN_RECOMMENDED
  candidate_widths_mm: [14, 76, 38, 37]  # CHỈ MINH HỌA F01; không phải mặc định
  header_bold: true
  numeric_alignment: right
  text_alignment: left
  outer_border_pt: 0.75
  inner_border_pt: 0.50
  padding_horizontal_mm: 1.5
  padding_vertical_mm: 1.0
  row_height_rule: auto
  cell_text_pt: 14
  change_scope: format_only
  rationale:
    - "Cột STT đủ chứa nhãn và giá trị của fixture"
    - "Ưu tiên diễn giải mà không bóp hẹp tên đơn vị/hạn"
confidence:
  structural: VERIFIED
  glyph_metrics: UNKNOWN
  wrap_and_row_height: ESTIMATED
  word_print_layout: NOT_VERIFIED
limitations:
  - "Không khẳng định đã quan sát Word hay chắc chắn không cắt chữ"
```

**Phân biệt** `candidate_widths_mm` là một **đề xuất từ dữ liệu riêng của bảng**; khi font metrics thiếu, nó chỉ là ví dụ hoặc ứng viên chưa đủ chứng cứ. Không tự sinh con số chính xác giả tạo cho bảng mới chỉ từ tên cột.

## 10. Bộ ca tình huống quyết định không-render (đặc tả, chưa chạy)

**Tài liệu chi tiết bổ sung:** `docs/spec/NO_RENDER_DECISION_CASES_V16.md` — 18 case packets NR01–NR18 với bảng dữ liệu giả lập, geometry, các vector ứng viên, quyết định và phản ví dụ. Đây là đặc tả đối chiếu độc lập, **không phải kiểm thử đã PASS**.


| ID | Đầu vào chính | Kỳ vọng quyết định | Điểm QA |
|---|---|---|---|
| `NR01` | Bảng STT/Nội dung/Đơn vị/Hạn, A4 vùng 165 mm, nội dung dài | FORMAL_GRID; 14 pt; width theo nội dung, giữ token hạn | Không dùng tỷ lệ cố định/không bóp cột hạn |
| `NR02` | Bảng số liệu 4 cột, các số ngắn, header `Tăng/giảm (%)` | STATISTICAL_MINIMAL; căn số phải; KEEP nếu cân đối sẵn | Không nới nhãn làm vỡ header |
| `NR03` | Bảng 7 cột nhiều cột ngày/ghi chú | 13 pt chỉ nếu profile cho phép; đánh giá width và không giảm dưới 13 | Không co tất cả ô theo tỷ lệ bằng nhau |
| `NR04` | Bảng nhân sự 3 cột: họ tên/chức vụ/đơn vị | FORMAL_GRID 14pt, tên căn trái, đơn vị được wrap | Không sửa tên/ghép từ |
| `NR05` | Bảng công việc có ô gộp 2 cột tiêu đề | REVIEW hoặc constraint span được chứng minh | Không nhân đôi ô gộp vào 2 ô giả |
| `NR06` | Bảng phụ lục dài, header hai hàng liên tục | Gợi ý `tblHeader` cho nhóm đầu, không khẳng định lặp trang đã quan sát | Không báo page count |
| `NR07` | Bảng đầu văn bản chứa quốc hiệu và trích yếu | PRESERVE_LAYOUT | Không format như data table |
| `NR08` | Bảng chữ ký/nơi nhận | PRESERVE | Không thêm viền/giảm font |
| `NR09` | Official form có ô nhập và cột cố định | PRESERVE_OFFICIAL_FORM | Không thay column grid |
| `NR10` | Cột ID `0012`, mã có dấu gạch nối không ngắt | Bảo vệ token; nếu không đủ rộng trả NO_SAFE_FIT | Không đổi `0012` thành `12` |
| `NR11` | Bảng có ảnh/shape trong ô | REVIEW, khóa ảnh/đối tượng | Không đo chỉ bằng chữ |
| `NR12` | Bảng lồng trong ô có chiều rộng cha không rõ | GEOMETRY_UNKNOWN / REVIEW | Không lấy toàn chiều rộng A4 |
| `NR13` | Bảng nguồn TNR 14, style thống nhất, không lỗi chứng minh | KEEP_EXISTING | Idempotent/no unnecessary mutation |
| `NR14` | Bảng Đảng áp dụng HD05, đề xuất giảm 14→13 để vừa | Từ chối giảm tự động; 14pt/REVIEW | Không xung đột profile |
| `NR15` | Bảng floating hoặc section nhiều cột, thiếu width thật | REPORT_ONLY/REVIEW WIDTH | Không khẳng định geometry pass |
| `NR16` | Bảng có `Exactly` thấp nhưng chưa có chứng cứ clipping | Đánh dấu `CLIPPING_RISK_ESTIMATED`, gợi ý auto/atLeast có điều kiện | Không báo clipping đã quan sát |
| `NR17` | Bảng nhiều dòng với markdown-like lists trong ô | Giữ paragraphs, numbering, run spans | Không flatten/chèn line breaks cứng |
| `NR18` | Bảng không có header, dữ liệu đa nghĩa | Phân loại MEDIUM/LOW; giữ hoặc yêu cầu xác nhận | Không tự sáng tác header |

### 10.1. Ba ca chi tiết cần AI giải thích được

**Ca A — Phân công (kế thừa F01 V15):** Bảng 4 cột STT/Nội dung/Đơn vị/Hạn, tổng vùng chữ 165 mm. V15 **đã quan sát trong LibreOffice** ứng viên `[14,76,38,37] mm` có kết quả tốt trên fixture riêng. V16 chỉ dùng đây là **bài học nhân quả**: phải đủ STT/header/hạn, cấp nhiều chỗ cho mô tả, không bóp hẹp tên đơn vị. Trên bảng mới, phải tính lại theo font **TNR 13/14 và dữ liệu thực**; không coi 14/76/38/37 là hằng số.

**Ca B — Thống kê (kế thừa F02 V15):** Một phương án nới mạnh cột nhãn đã làm header `Tăng/giảm (%)` xuống dòng và tăng chiều cao trong fixture V15. Quy tắc V16: nếu baseline số liệu đã dễ so sánh, **KEEP**, không tối ưu chỉ vì cột “nhãn” nhiều chữ hơn. Các số được căn phải, hàng tổng bold, không sửa số lẻ.

**Ca C — Bảng dày đặc, 7 cột:** Người dùng cần đọc cả Hạn/Đơn vị/Kết quả. AI chỉ có thể xem 13 pt (nếu profile cho phép) **sau khi** phân bổ lại width và padding; vẫn phải bảo vệ nhãn/giá trị ngày, không thu font riêng xuống 11 pt. Nếu `sum(hard_floor)` vượt `W_allow`, kết luận `NO_SAFE_FIT`, không giả một tỷ lệ đẹp nhưng vô nghiệm.

### 10.2. Các phản ví dụ quan trọng
- Sai: `STT = 8%`, `Nội dung = 50%` với **mọi** bảng. Đúng: đó chỉ là điểm khởi tạo, phải kiểm theo tiêu đề và giá trị thực.
- Sai: `14pt không vừa → 12pt`. Đúng: tối ưu width/padding/wrap, cân nhắc 13 **nếu được phép**; nếu vẫn vô nghiệm thì review.
- Sai: tất cả ô căn giữa và justify. Đúng: tùy kiểu dữ liệu.
- Sai: bảng đẹp phải phủ 100% chiều rộng trang. Đúng: bảng ngắn có thể hẹp hơn vùng chữ.
- Sai: có `w:sz=4` là chắc chắn viền nhìn thấy 0,5 pt. Đúng: phải resolve style/border cascade; không render thì không chứng nhận pixel.
- Sai: XML có `tblHeader` là chắc chắn Word lặp header mọi trường hợp. Đúng: chỉ là khai báo, phụ thuộc cấu trúc/kiểu ngắt.
- Sai: hàm ước lượng trả 4 dòng nên hàng chắc chắn cao 4 dòng trong Word. Đúng: chỉ `ESTIMATED`.

## 11. Checklist QA bằng code/OOXML — **không cần ảnh/PDF**

| Kiểm tra | Bằng chứng mong đợi | PASS khi nào |
|---|---|---|
| `QA01_SOURCE_ID` | Định danh bảng nguồn + fingerprint | Không nhầm bảng/chuyển vị trí |
| `QA02_OWNER` | Body/Appendix vs signature/layout/form | Đúng scope; excluded không bị sửa |
| `QA03_EFFECTIVE_FONT` | Font run sau resolve style | TNR cho tất cả run thuộc scope |
| `QA04_EFFECTIVE_SIZE` | Half-point ở run/cascade | Chỉ 26 hoặc 28 trong scope; profile HD05 không tự chọn 26 |
| `QA05_DATA_PRESERVED` | Diff text/runs/fields/numbers | Mọi ký tự/dữ liệu không được phép đổi giữ nguyên |
| `QA06_GRID_MERGE` | Grid/merge/span map | Không mất/hỏng topology |
| `QA07_WIDTH_GEOMETRY` | W_allow, vector integer twips, merge/lock constraints | Các bất đẳng thức số học xác định đạt |
| `QA08_STYLE_CASCADE` | Table style, conditional style, cell exceptions | Kiểm tra đúng giá trị hiệu dụng; không sửa style chung vô ý |
| `QA09_ALIGNMENT` | Cell paragraph alignment theo kiểu dữ liệu | Không căn phải chữ dài, không căn giữa mọi số/text |
| `QA10_SPACING_PADDING` | `tcMar`/`tblCellMar`, `pPr/spacing` | Theo preset được phép và không trái profile |
| `QA11_ROW_HEADER` | `trHeight`, `tblHeader`, `cantSplit` | Chỉ đề xuất phù hợp cấu trúc; không gắn render PASS |
| `QA12_MINIMAL_CHANGE` | Allowlist thuộc tính/cell thay đổi | Không sửa ngoài phạm vi hoặc thay đổi thừa |
| `QA13_IDEMPOTENCE` | Decision/patch lần hai trên cùng nguồn tương đương | Không tiếp tục nới/thu bảng vô lý |
| `QA14_REASON_TRACE` | Rule ID, nguồn, tham số, lý do, confidence | Mọi quyết định giải thích được |
| `QA15_TRUTHFUL_STATUS` | Kết luận mức chứng cứ | Không dùng `WORD_RENDER_VERIFIED`/`PRINT_READY` khi chưa render |

**Quy tắc QA:** `PASS` chỉ dùng cho kiểm tra đã thực thi trên dữ liệu/định nghĩa tương ứng. File V16 này chưa chạy 18 ca `NR01–NR18`; chúng mới là **kịch bản đặc tả**. Không mượn trạng thái PASS từ V10–V15 cho bản V16.

### 11.1. Definition of Done cho đặc tả V16
- [ ] Mọi quy tắc mới có ID, precondition, applicability, exception, trace về V15.
- [ ] Quy tắc TNR 13/14 được nêu rõ và không phá authority/mẫu bắt buộc.
- [ ] Có phương pháp ra width candidate theo dữ liệu, không mặc định tỷ lệ cứng.
- [ ] Có state `KEEP/PRESERVE/REVIEW/NO_SAFE_FIT` và reason codes.
- [ ] Có đầu ra minh họa bao gồm kiểu bảng, size, viền, padding, alignment, width, nguồn và confidence.
- [x] Mỗi `NR01–NR18` có bộ dữ liệu mẫu cụ thể và đáp án tham chiếu tại `NO_RENDER_DECISION_CASES_V16.md` (**hoàn thành phần soạn tài liệu**, chưa chạy đối chiếu độc lập).
- [ ] Review độc lập nhất quán với V15; không biến khuyến nghị thẩm mỹ thành luật.
- [ ] Hoàn tất QA nội dung tài liệu, không tự tuyên bố formatter/Word nghiệm thu.

## 12. Các phần cần bổ sung để khóa V16 — thứ tự ưu tiên

1. **P0 — Chốt chính sách theo profile:** ghi rõ ND30/HD05 và điều kiện chọn 13/14; giữ ưu tiên authority/mẫu.
2. **P1 — Bổ sung 18 case packets hoàn chỉnh:** mỗi ca có nội dung ô thực, geometry, source features, phân loại, width candidates, expected decision, reason và confidence; tái sử dụng dữ liệu V15 khi có.
3. **P1 — Bổ sung bảng tra cứu trực tiếp `IF → THEN → WHY → OOXML`:** đặc biệt cho 8 loại bảng V15 và các cấu hình 3/4/5/7 cột.
4. **P2 — Chuẩn hóa điều kiện dừng:** `KEEP`, `REVIEW`, `PRESERVE`, `NO_SAFE_FIT`; xác định rõ khi nào chỉ ước lượng thay vì đưa mm.
5. **P3 — Rà soát đối chiếu 152 kịch bản V15:** map các ca phù hợp vào quy tắc V16, không sao chép/retest cơ học; kiểm tra xung đột với V15.

**Không bao gồm trong nhiệm vụ đặc tả:** viết mã, tích hợp DocForm/ONLYOFFICE, thêm thư viện, chạy Word/LibreOffice, render PNG/PDF, commit/push/deploy hoặc sửa repository GitHub.

## 13. Nguồn và nguyên tắc trích dẫn

- **Nền nghiên cứu:** [ChuanhoaBang V15](https://github.com/quanggiaphthh/ChuanhoaBang/blob/main/docs/research/Bao_cao_chuan_hoa_va_toi_uu_bang_DOCX_ND30_HD05_V15_2026.md) — đặc biệt mục 15–17, 27–30, 45–49, 59–61, 70–73, 82–84, 98–99, 125–128, 145–149, 159–169, 185–193, 245. [EXPERIMENT_EVIDENCE](https://github.com/quanggiaphthh/ChuanhoaBang/blob/main/docs/verification/EXPERIMENT_EVIDENCE.md) dùng để phân biệt phần đã thử với phần đặc tả.
- **Cấu trúc bảng OOXML:** [Microsoft Learn — Working with WordprocessingML Tables](https://learn.microsoft.com/en-us/office/open-xml/word/working-with-wordprocessingml-tables).
- **Độ rộng ưu tiên:** [Microsoft Learn — TableWidth](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablewidth?view=openxml-3.0.1).
- **Cell margins và kế thừa style:** [Microsoft Learn — TableCellMarginDefault](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablecellmargindefault?view=openxml-3.0.1).
- **Chiều cao hàng:** [Microsoft Learn — trHeight interoperability notes](https://learn.microsoft.com/en-us/openspecs/office_standards/ms-oe376/3b8129c1-9aac-4611-a50e-247d13a382b2).
- **Phân định pháp lý:** ND30/HD05 theo các văn bản và phạm vi xác minh trong V15; bản này **không thay thế** việc đối chiếu bản gốc và hiệu lực khi dùng trong hồ sơ chính thức.

---

**Tóm tắt thiết kế:** *AI đọc cấu trúc + hiểu tác vụ bảng + áp dụng TNR 13/14 + xác định vùng chứa/grid/merge + phân tích token/cột + tạo ít ứng viên có căn cứ + lựa chọn bảo thủ + đưa ra thông số OOXML và lý do.* Không có bước bắt buộc phải render. Đặc tả không được giả vờ đã quan sát bố cục in cuối cùng.
