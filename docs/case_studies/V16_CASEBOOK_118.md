# ChuanhoaBang V16 — Tổng hợp 118 case study (18 ca gốc + 100 ca mới)

**Ngày hợp nhất:** 29/10/2026. **Mục tiêu:** Tra cứu duy nhất toàn bộ ca `NR01–NR118`. Nội dung phần I và II giữ nguyên như file nguồn, không thay đổi quyết định trước đó.

## Phần I. 18 case đã có NR01–NR18

# ChuanhoaBang V16 — Sổ tay 18 ca quyết định định dạng bảng không render

**Tài liệu bổ trợ:** `docs/spec/NO_RENDER_DECISION_CASES_V16.md` (đường dẫn đề xuất khi đưa vào repo).  
**Ngày:** 29/10/2026.  
**Trạng thái:** `SPECIFICATION / SYNTHETIC CASES / NOT EXECUTED` — không phải kết quả chạy Word, không phải tài liệu pháp lý, không phải bằng chứng bản in.  
**Nguồn authority đặc tả:** [Báo cáo ChuanhoaBang V15](https://github.com/quanggiaphthh/ChuanhoaBang/blob/main/docs/research/Bao_cao_chuan_hoa_va_toi_uu_bang_DOCX_ND30_HD05_V15_2026.md) và `ChuanhoaBang_V16_AI_Table_Formatting_No_Render.md`.

## I. Mục đích và phương pháp

Đây là **18 case packets có nội dung bảng giả lập cụ thể**, để người hoặc AI đọc *nội dung ô, cấu trúc OOXML mô tả, font và hình học trang* rồi chọn **phương án định dạng có giải thích**, không cần render Word, ảnh hay PDF trong luồng quyết định. **Không tạo engine, API, CLI, test runner, plugin hoặc chương trình xử lý DOCX**.

- Chỉ xét **bảng nội dung đủ điều kiện** với **Times New Roman 13–14 pt**. Mặc định **14 pt**; sử dụng **13 pt** chỉ khi profile/authority cho phép và cần thiết; với bảng thuộc phạm vi HD05, profile này giữ **14 pt**, không giảm tự động.
- Bảng dàn trang, phần đầu, chữ ký, biểu mẫu chính thức và bảng không rõ quyền sửa: **bảo toàn hoặc review**; không ép font của *bảng nội dung* vào chúng.
- Mỗi bảng dưới đây chỉ là **dữ liệu mẫu**, không có DOCX fixture được đính kèm. Các độ rộng mm là **ứng viên hình học minh họa**, **không được coi đã đo chữ Times New Roman**, không xác nhận không cắt/không tràn sau dàn trang.
- Khi có `W_allow` và vector width, kiểm tra tổng và giới hạn số học là phép kiểm tra **có thể thực hiện không render**. Nhưng phải kiểm **hard floor theo glyph, header và merge** trước khi khuyến nghị áp dụng thực tế.
- Không dùng một tỷ lệ cột chung cho mọi bảng; không tự giảm font dưới 13 pt, không đổi nội dung để bảng vừa, không tự sửa source ngoài phạm vi.

### Cách hiểu đáp án

| Thuật ngữ | Ý nghĩa |
|---|---|
| `PRESERVE`, `KEEP_EXISTING` | Không đề xuất thay đổi khi bảng không thuộc scope hoặc không có cải thiện chứng minh được |
| `DESIGN_RECOMMENDED` | Lựa chọn thiết kế có căn cứ, nhưng width/height/wrap còn có thể **ESTIMATED** |
| `REVIEW_REQUIRED` | Thiếu geometry, quyền sửa, role, nguồn mẫu hoặc dữ liệu kỹ thuật đáng tin |
| `NO_SAFE_FIT` | Đã xác nhận hệ ràng buộc min width/token/merge vô nghiệm; **không** phải cảm giác “trông chật” |
| `RULE_CONFORMANT` | Chỉ những đặc tính quy tắc được kiểm chứng bằng dữ liệu đầu vào, không suy ra print-layout PASS |

## II. Mẫu quyết định thống nhất

Mỗi ca phải đưa ra đủ: `table_id` → `owner`/`authority` → `reader_task`/`column_roles` → font/size → `W_allow` và cột vật lý → bảng ứng viên → decision/reason → risk/uncertainty → `OOXML` liên quan → `QA`.

**Ký hiệu trong bảng Markdown:** `⏎` biểu diễn ranh giới đoạn/danh sách trong ví dụ, không phải một ký tự cần ghi vào DOCX. Ô đánh dấu `[thuộc ô gộp bên trái]` chỉ mô tả vùng lưới bị `gridSpan` chiếm, **không phải ô riêng**.

**Các mặc định chỉ mang tính thẩm mỹ:** Formal Grid dùng viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; Statistical Minimal ưu tiên đường ngang và căn số phải. Không nhầm các trị số này với quy định pháp lý của NĐ30/HD05; mẫu bắt buộc thắng preset.

### Quick decision lookup (IF → THEN → WHY → OOXML)

| Nếu dữ liệu/đặc điểm... | Thì chọn... | Vì sao | OOXML/logic cần đọc |
|---|---|---|---|
| Bảng công việc, nhiệm vụ rõ | Formal Grid; thường 14 pt | Cần giữ quan hệ theo hàng và trách nhiệm | `tblPr`, `tblBorders`, `pPr/jc`, `rPr/sz` |
| Cột STT ngắn | Center; width vừa header/token | STT là định danh, không phải cột mô tả | `tblGrid`, `tcW`, `pPr/jc` |
| Cột số/tiền/phần trăm | Right; bảo toàn chuỗi | Dễ so sánh, không sửa độ chính xác | `pPr/jc`, `w:t` |
| Cột diễn giải dài | Left/top; ưu tiên wrap hợp lệ | Tránh tăng chiều cao hàng vì cột quá hẹp | `vAlign`, width, đoạn/run |
| Header nhiều tầng | Ràng buộc span thật | Không nhân bản ô gộp | `gridSpan`, `tblGrid`, `tblHeader` |
| Bảng nhiều cột, NĐ30, 14 pt khó vừa | Xem 13 pt sau width/padding | Vẫn trong chính sách được phép | `rPr/sz=26` khi hợp lệ |
| Bảng HD05 cần giảm 14→13 | Từ chối tự giảm; giữ 14 | Tuân thủ profile V16 | `rPr/sz=28`, authority |
| Biểu mẫu/chữ ký/layout | PRESERVE | Giữ thể thức và khoảng trống có chủ đích | Owner/form-lock/`trHeight` |
| `w:trHeight exact` thấp + text dài | Cảnh báo nguy cơ; cân nhắc atLeast | Không kết luận đã cắt chữ | `trPr/trHeight` |
| Bảng nổi/bảng lồng chưa rõ vùng chứa | REVIEW width | Không được lấy W của A4 làm W bảng con | `tblpPr`, `tcMar`, section/parent |
| Không có header, các cột đa nghĩa | REVIEW/KEEP | Không tự tạo ngữ nghĩa | Source text/header evidence |

---

## NR01 — Bảng phân công nhiệm vụ — cân đối 4 cột

**Loại/nhóm:** `TASK_MATRIX`. **Mục tiêu/bối cảnh:** Văn bản hành chính NĐ30; bảng mới thuộc Body; tác vụ ACTION; không có mẫu chuyên ngành; các giá trị và từ ngữ là dữ liệu giả lập.

### A. Dữ liệu mẫu (nguyên văn nội dung ô)

| STT | Nội dung công việc | Đơn vị thực hiện | Thời hạn |
| --- | --- | --- | --- |
| 1 | Rà soát hồ sơ phương án bảo đảm an toàn hàng hải tại khu vực cảng | Phòng Nghiệp vụ | 05/11/2026 |
| 2 | Tổng hợp ý kiến và hoàn thiện dự thảo báo cáo đánh giá | Phòng Tổng hợp | 10/11/2026 |
| 3 | Trình lãnh đạo phê duyệt và tổ chức thực hiện | Phòng Kế hoạch | 15/11/2026 |


**Đầu vào hình học/OOXML mô tả:** A4 dọc, 210 mm; lề trái 30 mm, phải 15 mm; W_allow giả định/được khai báo = 165 mm; 4 cột vật lý, không merge; bảng inline.

**Chính sách chữ:** Times New Roman 14 pt; header 14 pt đậm; văn bản/số dùng cùng size.

### B. Ứng viên và quyết định

| Phương án minh họa | Vector cột | Điều kiện cần trước khi lựa chọn |
|---|---|---|
| BASELINE chia đều | [41.25, 41.25, 41.25, 41.25] mm — tổng **165 mm** | Kiểm hard floor theo TNR, header, merge/lock; đây **chưa phải phép đo Word** |
| Ứng viên theo mục tiêu ACTION | [14, 76, 38, 37] mm — tổng **165 mm** | Kiểm hard floor theo TNR, header, merge/lock; đây **chưa phải phép đo Word** |
| Ưu tiên mô tả quá mức (đối chứng) | [11, 95, 31, 28] mm — tổng **165 mm** | Kiểm hard floor theo TNR, header, merge/lock; đây **chưa phải phép đo Word** |



**Kết luận kỳ vọng:** `DESIGN_RECOMMENDED (chỉ là phương án để đối chiếu font metrics)`.

**Vì sao:** Cột STT phải đủ chữ “STT”; ngày là token cần đọc nguyên vẹn; nội dung dài thường cần rộng nhất nhưng không được bóp tên đơn vị. `[14,76,38,37]` kế thừa logic F01/V15, không coi là đáp án mm phổ quát.

**Đặc tả định dạng/thuộc tính:** FORMAL_GRID; ngoài 0,75 pt, trong 0,5 pt; padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; STT/hạn căn giữa, mô tả/đơn vị căn trái; mô tả căn trên; header đậm.

**Điều kiện đánh giá riêng:** Chọn ứng viên chỉ khi đo token/header TNR14 và ràng buộc lưới đều đạt; nếu ứng viên gây ngắt ngày/đơn vị thì giữ BASELINE hoặc REVIEW.

### C. Phản ví dụ và tiêu chí QA

- **Không được làm:** Không đổi hạn, không tự rút tên phòng, không áp tỷ lệ 8–50% cố định; không xác nhận ứng viên 14 mm đủ header nếu chưa đo glyph.

- **QA trọng tâm:** `QA02_OWNER`, `QA03_EFFECTIVE_FONT`, `QA04_EFFECTIVE_SIZE`, `QA07_WIDTH_GEOMETRY`, `QA09_ALIGNMENT`, `QA14_REASON_TRACE`.

- **Mức tin cậy:** `MEDIUM / TEXT_ESTIMATED`. **Truy vết:** V15 §15, §70–73, §189–193; V16-WIDTH-01/02/04, V16-PRESET-01.


---

## NR02 — Bảng thống kê — không tối ưu giả

**Loại/nhóm:** `DATA_STAT`. **Mục tiêu/bối cảnh:** Bảng tổng hợp kết quả quý trong Body; mục tiêu COMPARE; NĐ30; các số liệu minh họa, không dùng để báo cáo thực tế.

### A. Dữ liệu mẫu (nguyên văn nội dung ô)

| Chỉ tiêu | Năm 2024 | Năm 2025 | Tăng/giảm (%) |
| --- | --- | --- | --- |
| Hồ sơ tiếp nhận | 125 | 142 | 13,6 |
| Hồ sơ hoàn thành | 120 | 138 | 15,0 |
| Tỷ lệ đúng hạn (%) | 96,0 | 97,2 | 1,25 |


**Đầu vào hình học/OOXML mô tả:** A4 dọc, W_allow=165 mm được khai báo, bảng inline 4 cột không gộp; mẫu đã có bố cục số rõ.

**Chính sách chữ:** Times New Roman 14 pt thống nhất; số không tự làm tròn.

### B. Ứng viên và quyết định

| Phương án minh họa | Vector cột | Điều kiện cần trước khi lựa chọn |
|---|---|---|
| BASELINE có sẵn | [41.25, 41.25, 41.25, 41.25] mm — tổng **165 mm** | Kiểm hard floor theo TNR, header, merge/lock; đây **chưa phải phép đo Word** |
| Nới cột chỉ tiêu | [60, 35, 35, 35] mm — tổng **165 mm** | Kiểm hard floor theo TNR, header, merge/lock; đây **chưa phải phép đo Word** |
| Nới quá mạnh | [75, 30, 30, 30] mm — tổng **165 mm** | Kiểm hard floor theo TNR, header, merge/lock; đây **chưa phải phép đo Word** |



**Kết luận kỳ vọng:** `KEEP_EXISTING nếu baseline hiện tại vượt qua các kiểm tra cấu trúc và giá trị cần giữ`.

**Vì sao:** Khả năng so sánh số và header “Tăng/giảm (%)” quan trọng hơn mong muốn nới cột nhãn. F02/V15 có đối chứng nới quá mức làm tăng chiều cao trong LibreOffice; không suy rộng số đo đó sang bảng này.

**Đặc tả định dạng/thuộc tính:** STATISTICAL_MINIMAL; số căn phải, tên chỉ tiêu căn trái; header 14 pt đậm; nền trắng; viền ngang nhấn header/tổng nếu có, không tự thêm hàng tổng.

**Điều kiện đánh giá riêng:** Không sửa độ rộng chỉ để thay đổi tỷ lệ nếu không có lợi ích đã xác định; nếu header cần rộng hơn thì đề xuất can thiệp cục bộ thay vì nới cột nhãn cực đoan.

### C. Phản ví dụ và tiêu chí QA

- **Không được làm:** Không đổi “13,6” thành “13.6” hoặc thành “14”; không khẳng định width 30 mm khiến header hỏng nếu chưa đo TNR14.

- **QA trọng tâm:** `QA04_EFFECTIVE_SIZE`, `QA05_DATA_PRESERVED`, `QA09_ALIGNMENT`, `QA12_MINIMAL_CHANGE`, `QA15_TRUTHFUL_STATUS`.

- **Mức tin cậy:** `HIGH cho KEEP khi không có lỗi xác định; chưa xác nhận hình ảnh`. **Truy vết:** V15 §28, §190, §193; V16-PRESET-02/03, V16-QUALITY-01.


---

## NR03 — Bảng 7 cột dày dữ liệu — lựa chọn 13/14 pt đúng phạm vi

**Loại/nhóm:** `TASK_MATRIX_DENSE`. **Mục tiêu/bối cảnh:** Bảng theo dõi tiến độ hành chính trong Body; NĐ30 cho phép 13–14 pt; nhiều trường thông tin trên A4 dọc.

### A. Dữ liệu mẫu (nguyên văn nội dung ô)

| STT | Nhiệm vụ | Chủ trì | Phối hợp | Thời gian | Kết quả | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | Kiểm tra điều kiện an toàn cầu cảng | Phòng Nghiệp vụ | Phòng Kỹ thuật | 05/11/2026 | Biên bản | Chờ xác nhận |
| 02 | Tổng hợp các khuyến nghị sau kiểm tra | Phòng Tổng hợp | Các đơn vị | 10/11/2026 | Báo cáo | Không thay đổi số liệu |
| 03 | Theo dõi biện pháp khắc phục tồn tại | Phòng An toàn | Phòng Kế hoạch | 15/11/2026 | Danh mục | Rà soát định kỳ |


**Đầu vào hình học/OOXML mô tả:** A4 dọc, W_allow=165 mm; 7 cột; không merge; width của từng cột cần xét cả nhãn header.

**Chính sách chữ:** Ưu tiên Times New Roman 14 pt; cân nhắc 13 pt đồng nhất nếu policy NĐ30 của bảng cho phép và không thể cân đối hợp lý với 14 pt.

### B. Ứng viên và quyết định

| Phương án minh họa | Vector cột | Điều kiện cần trước khi lựa chọn |
|---|---|---|
| Ứng viên hẹp, cần đo trước | [12, 50, 26, 23, 24, 18, 12] mm — tổng **165 mm** | Kiểm hard floor theo TNR, header, merge/lock; đây **chưa phải phép đo Word** |
| Ứng viên dành thêm chỗ cho ghi chú | [12, 44, 25, 23, 24, 19, 18] mm — tổng **165 mm** | Kiểm hard floor theo TNR, header, merge/lock; đây **chưa phải phép đo Word** |



**Kết luận kỳ vọng:** `DESIGN_RECOMMENDED hoặc REVIEW_REQUIRED tùy mức chứng cứ đo chữ và giới hạn hình học`.

**Vì sao:** Cả bảy tiêu đề đều có áp lực rộng; giá trị ngày cần bảo vệ. Hai phương án chỉ là vector đúng tổng 165 mm, chưa chứng minh khả năng chứa header/nội dung. Không thể mặc định 13 pt sẽ giải quyết mọi xung đột.

**Đặc tả định dạng/thuộc tính:** FORMAL_GRID; 13/14 pt theo phê duyệt; header đậm; số STT giữa, mô tả/ghi chú trái và trên; ngày nhất quán; padding ngang 1,5 mm ban đầu nếu phù hợp.

**Điều kiện đánh giá riêng:** Nếu tổng hard-floor do đo font lớn hơn W_allow: NO_SAFE_FIT; nếu còn nhiều token/header không xác định: REVIEW_REQUIRED, không bịa mm chính xác.

### C. Phản ví dụ và tiêu chí QA

- **Không được làm:** Không nén chữ, giảm size xuống 12, giảm riêng cột ghi chú xuống 10, viết tắt nhiệm vụ, hoặc tự chuyển section ngang.

- **QA trọng tâm:** `QA03_EFFECTIVE_FONT`, `QA04_EFFECTIVE_SIZE`, `QA07_WIDTH_GEOMETRY`, `QA14_REASON_TRACE`, `QA15_TRUTHFUL_STATUS`.

- **Mức tin cậy:** `LOW–MEDIUM khi chưa có TNR metrics`. **Truy vết:** V15 §72–73, §164; V16-FONT-03, V16-WIDTH-05.


---

## NR04 — Danh sách nhân sự — ưu tiên nhận diện tên và chức vụ

**Loại/nhóm:** `PERSONNEL_LIST`. **Mục tiêu/bối cảnh:** Danh sách thành phần dự họp, chỉ chứa dữ liệu giả lập; Body NĐ30, không thuộc bảng chữ ký hay biểu mẫu cố định.

### A. Dữ liệu mẫu (nguyên văn nội dung ô)

| Họ và tên | Chức vụ | Đơn vị công tác |
| --- | --- | --- |
| Nguyễn Văn Minh | Trưởng phòng | Phòng Tổ chức – Hành chính |
| Trần Thị Mai | Phó trưởng phòng | Phòng Kế hoạch – Tổng hợp |
| Lê Quốc Hưng | Chuyên viên | Phòng Kỹ thuật |


**Đầu vào hình học/OOXML mô tả:** Bảng inline 3 cột trong W_allow=165 mm; không bắt buộc dùng hết vùng nếu nội dung đã dễ đọc.

**Chính sách chữ:** Times New Roman 14 pt, tất cả các hàng.

### B. Ứng viên và quyết định

| Phương án minh họa | Vector cột | Điều kiện cần trước khi lựa chọn |
|---|---|---|
| Ứng viên rộng 150 mm | [45, 44, 61] mm — tổng **150 mm** | Kiểm hard floor theo TNR, header, merge/lock; đây **chưa phải phép đo Word** |
| Ứng viên phủ 165 mm | [48, 49, 68] mm — tổng **165 mm** | Kiểm hard floor theo TNR, header, merge/lock; đây **chưa phải phép đo Word** |



**Kết luận kỳ vọng:** `DESIGN_RECOMMENDED, không ép kéo bảng đến W_allow`.

**Vì sao:** Tên người là nhãn quan trọng phải nguyên vẹn; đơn vị dài được wrap theo từ hợp lệ. Hai width vectors là lựa chọn sơ bộ, chọn sau khi xem độ dài token/chính sách căn bảng.

**Đặc tả định dạng/thuộc tính:** FORMAL_GRID đơn sắc; header đậm; tên/chức vụ/đơn vị căn trái; căn trên khi ô nhiều dòng; không tô màu luân phiên mặc định.

**Điều kiện đánh giá riêng:** Gán đúng vai trò PERSONNEL_LIST, ưu tiên ổn định nhận diện tên và dữ liệu; có thể giữ bảng 150 mm hợp lệ.

### C. Phản ví dụ và tiêu chí QA

- **Không được làm:** Không tự sắp xếp tên theo bảng chữ cái; không bỏ dấu họ tên hoặc rút gọn chức vụ để vừa cột.

- **QA trọng tâm:** `QA02_OWNER`, `QA05_DATA_PRESERVED`, `QA07_WIDTH_GEOMETRY`, `QA09_ALIGNMENT`.

- **Mức tin cậy:** `MEDIUM`. **Truy vết:** V15 §47, §71–72, §164; V16-PRESET-01.


---

## NR05 — Tiêu đề nhiều tầng với ô gộp ngang — ràng buộc span

**Loại/nhóm:** `DATA_STAT_MERGED`. **Mục tiêu/bối cảnh:** Bảng thống kê có header 2 tầng; Body NĐ30; cần bảo toàn ô gộp, không được coi các ô trống dưới merge là dữ liệu.

### A. Dữ liệu mẫu (nguyên văn nội dung ô)

| STT | Chỉ tiêu | Kết quả 2026 [gridSpan=2] | [thuộc ô gộp bên trái] |
| --- | --- | --- | --- |
|  |  | Số lượng | Tỷ lệ (%) |
| 1 | Hồ sơ xử lý | 52 | 86,7 |
| 2 | Hồ sơ tồn | 8 | 13,3 |


**Đầu vào hình học/OOXML mô tả:** Grid vật lý 4 cột; header hàng 1 có ô ở cột 3 với gridSpan=2; vùng W_allow=165 mm; mapping gộp phải đọc từ OOXML.

**Chính sách chữ:** Times New Roman 14 pt; cả hai tầng header bold.

### B. Ứng viên và quyết định

| Phương án minh họa | Vector cột | Điều kiện cần trước khi lựa chọn |
|---|---|---|
| Ứng viên ràng buộc theo span | [14, 70, 41, 40] mm — tổng **165 mm** | Kiểm hard floor theo TNR, header, merge/lock; đây **chưa phải phép đo Word** |



**Kết luận kỳ vọng:** `REVIEW_REQUIRED nếu không đọc được topology; DESIGN_RECOMMENDED nếu gridSpan và floor(span) xác thực`.

**Vì sao:** Header gộp “Kết quả 2026” được cấp ngân sách từ tổng cột 3+4, không tính lại như hai nội dung lặp. Header tầng dưới cũng phải đủ rộng.

**Đặc tả định dạng/thuộc tính:** FORMAL_GRID/STATISTICAL_MINIMAL theo reader task; header hai tầng đậm, căn giữa có điều kiện; số căn phải.

**Điều kiện đánh giá riêng:** Chỉ khi tổng 41+40 mm thỏa floor nội dung gộp và các cột riêng mới có thể khuyến nghị vector; chưa biết metrics phải giữ REVIEW.

### C. Phản ví dụ và tiêu chí QA

- **Không được làm:** Không tách/nhân bản ô tiêu đề gộp; không ghi thêm hàng/ô; không thay gridSpan để đạt tỷ lệ.

- **QA trọng tâm:** `QA06_GRID_MERGE`, `QA07_WIDTH_GEOMETRY`, `QA08_STYLE_CASCADE`, `QA14_REASON_TRACE`.

- **Mức tin cậy:** `MEDIUM nếu đọc đủ OOXML; LOW nếu chưa`. **Truy vết:** V15 §45, §73, §125; V16-WIDTH-03.


---

## NR06 — Bảng phụ lục dài, header hai hàng — chỉ khai báo lặp đúng chỗ

**Loại/nhóm:** `APPENDIX_REGISTER`. **Mục tiêu/bối cảnh:** Phụ lục của văn bản hành chính có nhiều hàng; không tự đánh lại số phụ lục; bảng đang có hai hàng đầu là tiêu đề.

### A. Dữ liệu mẫu (nguyên văn nội dung ô)

| STT | Hạng mục | Nội dung | Kết quả |
| --- | --- | --- | --- |
|  |  | Theo kế hoạch | Thực tế |
| 1 | Thiết bị cứu sinh | Đã kiểm tra | Đạt |
| 2 | Thiết bị thông tin | Đã kiểm tra | Đạt |
| 3 | Trang bị bảo hộ | Đang đối chiếu | Đang thực hiện |
| … | (các hàng tiếp theo) | (tiếp tục) | (tiếp tục) |


**Đầu vào hình học/OOXML mô tả:** A4 dọc, vùng W_allow=165 mm; 4 grid columns; hàng đầu gồm header 1 và header 2 liên tiếp; gộp header (nếu có) phải từ OOXML.

**Chính sách chữ:** Times New Roman 14 pt; hàng header đậm.

### B. Ứng viên và quyết định

| Phương án minh họa | Vector cột | Điều kiện cần trước khi lựa chọn |
|---|---|---|
| Ứng viên từ dữ liệu mẫu | [14, 44, 64, 43] mm — tổng **165 mm** | Kiểm hard floor theo TNR, header, merge/lock; đây **chưa phải phép đo Word** |



**Kết luận kỳ vọng:** `DESIGN_RECOMMENDED đối với tblHeader hàng 1–2; không kết luận số trang`.

**Vì sao:** Chỉ dãy hàng đầu liên tiếp đủ tư cách lặp header. `tblHeader` là khai báo cấu trúc, không chứng minh lặp thành công khi bảng có ngắt trang thủ công.

**Đặc tả định dạng/thuộc tính:** FORMAL_GRID; header hai tầng đậm, căn theo cột; gợi ý trPr/tblHeader cho hai hàng đầu được xác nhận; không bật cantSplit hàng loạt.

**Điều kiện đánh giá riêng:** Bản mô tả chỉ ra `tblHeader` trên dãy đầu liên tục; `PAGE_EFFECT=UNVERIFIED`; giữ đúng nội dung và topology.

### C. Phản ví dụ và tiêu chí QA

- **Không được làm:** Không tự thêm header ở giữa bảng; không đánh số lại phụ lục; không khẳng định “đã lặp header trên trang 2”.

- **QA trọng tâm:** `QA02_OWNER`, `QA05_DATA_PRESERVED`, `QA06_GRID_MERGE`, `QA11_ROW_HEADER`, `QA15_TRUTHFUL_STATUS`.

- **Mức tin cậy:** `HIGH cho vị trí cờ header nếu cấu trúc đủ; không phải xác nhận trang`. **Truy vết:** V15 §V, §127; V16-PAGE-01.


---

## NR07 — Bảng đầu công văn — không phải bảng nội dung

**Loại/nhóm:** `LAYOUT_TABLE`. **Mục tiêu/bối cảnh:** Công văn hành chính; bảng hai cột trong đầu văn bản chứa thông tin cơ quan/quốc hiệu và có thể chứa trích yếu.

### A. Dữ liệu mẫu (nguyên văn nội dung ô)

| [Ô trái] | [Ô phải] |
| --- | --- |
| CÔNG TY HOA TIÊU HÀNG HẢI MIỀN BẮC | CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM |
| Số: …/CV-… | Độc lập – Tự do – Hạnh phúc |
| V/v: Phối hợp bảo đảm an toàn | Hải Phòng, ngày … tháng … năm … |


**Đầu vào hình học/OOXML mô tả:** Bảng layout đầu trang; 2 cột; topology có thể hỗ trợ bố trí thể thức, không thuộc Body content table.

**Chính sách chữ:** Không áp chính sách size của bảng nội dung vào các thành phần thể thức; nếu có xung đột chỉ ghi SCOPE_CONFLICT.

### B. Ứng viên và quyết định

**Không sinh vector chiều rộng.** Bảng bị loại trừ hoặc thiếu đầu vào/authority đáng tin để đề xuất thay đổi width.

**Kết luận kỳ vọng:** `PRESERVE_LAYOUT / NOT_APPLICABLE`.

**Vì sao:** Các ô có chức năng thể thức chứ không phải bảng dữ liệu. Chỉnh đường viền, chia cột như bảng công việc có thể làm sai quốc hiệu, số và trích yếu.

**Đặc tả định dạng/thuộc tính:** Không áp FORMAL_GRID hoặc STATISTICAL_MINIMAL; để cơ chế chuẩn hóa phần đầu theo authority riêng xử lý.

**Điều kiện đánh giá riêng:** Classifier nhận `LAYOUT_TABLE`, action=no-op, `changed_fields=[]`.

### C. Phản ví dụ và tiêu chí QA

- **Không được làm:** Không thêm viền 0,75 pt, không ép 13/14 vào toàn bộ bảng layout, không xóa trích yếu V/v.

- **QA trọng tâm:** `QA02_OWNER`, `QA05_DATA_PRESERVED`, `QA12_MINIMAL_CHANGE`.

- **Mức tin cậy:** `HIGH khi nhận diện từ vị trí + nhãn gốc`. **Truy vết:** V15 §9, §30, §47; V16-SCOPE-02.


---

## NR08 — Bảng nơi nhận và chữ ký — bảo toàn

**Loại/nhóm:** `SIGNATURE_LAYOUT`. **Mục tiêu/bối cảnh:** Bảng kỹ thuật 2 cột cuối văn bản dùng để đặt nơi nhận và vị trí ký; không phải danh sách nội dung.

### A. Dữ liệu mẫu (nguyên văn nội dung ô)

| Nơi nhận | Người ký |
| --- | --- |
| Nơi nhận: – Như trên; – Lưu: VT. | GIÁM ĐỐC |
|  | (Ký, ghi rõ họ tên) |


**Đầu vào hình học/OOXML mô tả:** Bảng cuối văn bản, thường không kẻ khung; có thể có ô trống dành cho chữ ký.

**Chính sách chữ:** Phạm vi Times New Roman 13–14 pt không được dùng để ép thay đổi phần ký đã theo mẫu.

### B. Ứng viên và quyết định

**Không sinh vector chiều rộng.** Bảng bị loại trừ hoặc thiếu đầu vào/authority đáng tin để đề xuất thay đổi width.

**Kết luận kỳ vọng:** `PRESERVE / NOT_APPLICABLE`.

**Vì sao:** Đây là thành phần thể thức phải giữ khoảng trống ký và căn chỉnh chức danh; không có nhiệm vụ đọc kiểu bảng hàng–cột.

**Đặc tả định dạng/thuộc tính:** Giữ style gốc, không tô màu, không tạo border theo preset bảng nội dung.

**Điều kiện đánh giá riêng:** Không đề xuất width hoặc font patch cho bảng ký; báo lý do loại trừ rõ ràng.

### C. Phản ví dụ và tiêu chí QA

- **Không được làm:** Không gộp/xóa ô trống, không thêm viền, không rút khoảng ký, không đánh lại dòng nơi nhận.

- **QA trọng tâm:** `QA02_OWNER`, `QA05_DATA_PRESERVED`, `QA12_MINIMAL_CHANGE`.

- **Mức tin cậy:** `HIGH nếu xác định chủ sở hữu signature`. **Truy vết:** V15 §9, §47, §159; V16-SCOPE-02.


---

## NR09 — Biểu mẫu chính thức — khóa kích thước và cấu trúc

**Loại/nhóm:** `OFFICIAL_FORM`. **Mục tiêu/bối cảnh:** Mẫu phiếu xác nhận đã được cơ quan có thẩm quyền ban hành, có ô điền, gộp, vùng xác nhận.

### A. Dữ liệu mẫu (nguyên văn nội dung ô)

| Mục | Thông tin kê khai | Xác nhận |
| --- | --- | --- |
| 1 | Họ tên: … |  |
| 2 | Đơn vị: … |  |
| 3 | Ngày: … | Người xác nhận (ký) |


**Đầu vào hình học/OOXML mô tả:** Biểu mẫu có định dạng/chiều cao/độ rộng cột theo mẫu gốc; data binding và content controls có thể tồn tại.

**Chính sách chữ:** Không ghi đè font theo chính sách bảng nội dung khi mẫu có quy định riêng; trả SCOPE_CONFLICT nếu ngoài phạm vi.

### B. Ứng viên và quyết định

**Không sinh vector chiều rộng.** Bảng bị loại trừ hoặc thiếu đầu vào/authority đáng tin để đề xuất thay đổi width.

**Kết luận kỳ vọng:** `PRESERVE_OFFICIAL_FORM`.

**Vì sao:** Chuẩn biểu mẫu được ưu tiên hơn preset thẩm mỹ; mẫu có thể cố ý dùng chiều cao chính xác để bố trí vùng điền hoặc chữ ký.

**Đặc tả định dạng/thuộc tính:** Không tự thay đổi thuộc tính; chỉ có thể mô tả chẩn đoán trong giới hạn đọc được.

**Điều kiện đánh giá riêng:** `allowed_changes=[]`; không có bảng ứng viên về width; reason=OFFICIAL_FORM_LOCK.

### C. Phản ví dụ và tiêu chí QA

- **Không được làm:** Không đổi `trHeight=exact` sang auto, không thay `tblGrid`/merge/control, không tự tăng padding.

- **QA trọng tâm:** `QA02_OWNER`, `QA06_GRID_MERGE`, `QA12_MINIMAL_CHANGE`.

- **Mức tin cậy:** `HIGH nếu mẫu được xác nhận`. **Truy vết:** V15 §29, §47, §159; V16-SCOPE-02.


---

## NR10 — Mã hồ sơ có số 0 đầu và token không được bẻ

**Loại/nhóm:** `APPENDIX_REGISTER`. **Mục tiêu/bối cảnh:** Danh mục hồ sơ nội dung phụ lục; mã là chuỗi ký tự có ý nghĩa, không phải số nguyên.

### A. Dữ liệu mẫu (nguyên văn nội dung ô)

| Mã hồ sơ | Nội dung hồ sơ | Đơn vị phụ trách |
| --- | --- | --- |
| 0012-A/2026 | Hồ sơ kiểm tra lần đầu | Phòng Nghiệp vụ |
| 0007-B/2026 | Hồ sơ bổ sung lần hai | Phòng Tổng hợp |
| 0123-X/2026 | Hồ sơ nghiệm thu | Phòng Kế hoạch |


**Đầu vào hình học/OOXML mô tả:** A4 dọc, W_allow=165 mm; 3 grid columns; token mã phải xét điều kiện no-break theo nguồn, không tự thay dấu nối.

**Chính sách chữ:** Times New Roman 14 pt.

### B. Ứng viên và quyết định

| Phương án minh họa | Vector cột | Điều kiện cần trước khi lựa chọn |
|---|---|---|
| Ứng viên ưu tiên mã | [36, 77, 52] mm — tổng **165 mm** | Kiểm hard floor theo TNR, header, merge/lock; đây **chưa phải phép đo Word** |
| Ứng viên bóp mã (để loại nếu không đủ token) | [24, 88, 53] mm — tổng **165 mm** | Kiểm hard floor theo TNR, header, merge/lock; đây **chưa phải phép đo Word** |



**Kết luận kỳ vọng:** `DESIGN_RECOMMENDED khi floor token đo được; NO_SAFE_FIT/REVIEW nếu không`.

**Vì sao:** Mã 0012-A/2026 cần hiển thị đủ, bao gồm 0 đầu, dấu gạch và ký tự phân cách; cột mã không nên co nhỏ hơn token quan trọng.

**Đặc tả định dạng/thuộc tính:** FORMAL_GRID; mã căn trái hoặc giữa nhất quán, mô tả/đơn vị căn trái; không sửa chữ.

**Điều kiện đánh giá riêng:** Trả `hard_floor_code` có nguồn đo nếu có; không kết luận 24 mm bị clipping nếu chưa có metrics; từ chối khi floor xác nhận vượt 24 mm.

### C. Phản ví dụ và tiêu chí QA

- **Không được làm:** Không ép mã thành số 12, tự đổi dấu gạch, chèn newline vào mã hay dùng ngắt mềm thay nguồn.

- **QA trọng tâm:** `QA05_DATA_PRESERVED`, `QA07_WIDTH_GEOMETRY`, `QA14_REASON_TRACE`.

- **Mức tin cậy:** `MEDIUM khi có token inventory; LOW nếu thiếu font metrics`. **Truy vết:** V15 §17, §72, §125; V16-WIDTH-02.


---

## NR11 — Bảng có ảnh và shape neo trong ô

**Loại/nhóm:** `DATA_WITH_OBJECTS`. **Mục tiêu/bối cảnh:** Bảng kiểm tra tài liệu gồm hình ảnh nhận diện thiết bị; hình là dữ liệu quan trọng không được làm mất.

### A. Dữ liệu mẫu (nguyên văn nội dung ô)

| STT | Hình minh họa | Mô tả |
| --- | --- | --- |
| 1 | [embedded image: equipment-a.png] | Phao tròn có đèn |
| 2 | [embedded shape/icon] | Thiết bị báo hiệu |


**Đầu vào hình học/OOXML mô tả:** Grid 3 cột nhưng hình/shape có extents, offsets và relationship riêng chưa đọc đủ.

**Chính sách chữ:** Các ô chữ trong phạm vi có thể dùng TNR 14; không ép đối tượng theo font metrics.

### B. Ứng viên và quyết định

**Không sinh vector chiều rộng.** Bảng bị loại trừ hoặc thiếu đầu vào/authority đáng tin để đề xuất thay đổi width.

**Kết luận kỳ vọng:** `REVIEW_REQUIRED / PRESERVE_OBJECT_LAYOUT`.

**Vì sao:** Không thể tính floor của cột hình chỉ bằng số chữ; việc thay width có thể đẩy hoặc cắt hình và làm lệch neo.

**Đặc tả định dạng/thuộc tính:** Chỉ đề xuất căn trái mô tả nếu có bằng chứng style; giữ toàn bộ media, rels và drawing properties.

**Điều kiện đánh giá riêng:** Gắn `OBJECT_EXTENT_UNKNOWN`; không có `candidate_widths_mm` khi chưa có kích thước hình có thể tin cậy.

### C. Phản ví dụ và tiêu chí QA

- **Không được làm:** Không xóa/resize ảnh, không chuyển ảnh thành chữ, không dùng text-only width solver.

- **QA trọng tâm:** `QA05_DATA_PRESERVED`, `QA06_GRID_MERGE`, `QA12_MINIMAL_CHANGE`, `QA15_TRUTHFUL_STATUS`.

- **Mức tin cậy:** `LOW`. **Truy vết:** V15 §9, §45, §143; V16-WIDTH-05.


---

## NR12 — Bảng lồng trong ô cha, chưa rõ vùng chứa

**Loại/nhóm:** `NESTED_TABLE`. **Mục tiêu/bối cảnh:** Bảng con nằm bên trong ô “Kết quả chi tiết” của bảng mẹ ở phụ lục.

### A. Dữ liệu mẫu (nguyên văn nội dung ô)

| Mã | Giá trị |
| --- | --- |
| A1 | Đạt |
| A2 | Chờ kiểm tra |


**Đầu vào hình học/OOXML mô tả:** Bảng mẹ có ba cột và một ô parent với `gridSpan=2`; chiều rộng thực tế của parent cell chưa resolve được, không được lấy 165 mm của A4.

**Chính sách chữ:** Times New Roman 14 pt cho ô chữ thuộc phạm vi, khi không xung đột bảng mẹ.

### B. Ứng viên và quyết định

**Không sinh vector chiều rộng.** Bảng bị loại trừ hoặc thiếu đầu vào/authority đáng tin để đề xuất thay đổi width.

**Kết luận kỳ vọng:** `GEOMETRY_UNKNOWN / REVIEW_REQUIRED`.

**Vì sao:** W của bảng con bằng không gian bên trong parent cell sau padding/border; chưa có W_parent thì mọi vector mm đều võ đoán.

**Đặc tả định dạng/thuộc tính:** Giữ table child, không tự co/căng khi thiếu parent geometry.

**Điều kiện đánh giá riêng:** Không có width vector; báo thiếu `parent_cell_width_twips` và `parent_padding`.

### C. Phản ví dụ và tiêu chí QA

- **Không được làm:** Không lấy full A4 để cho bảng con rộng 165 mm; không tháo bảng con ra ngoài.

- **QA trọng tâm:** `QA02_OWNER`, `QA06_GRID_MERGE`, `QA07_WIDTH_GEOMETRY`, `QA15_TRUTHFUL_STATUS`.

- **Mức tin cậy:** `LOW`. **Truy vết:** V15 §45, §143; V16-WIDTH-01/03.


---

## NR13 — Bảng đã đúng và nhất quán — KEEP là đáp án tốt

**Loại/nhóm:** `TASK_MATRIX_EXISTING`. **Mục tiêu/bối cảnh:** Bảng nội dung hành chính 4 cột đã dùng TNR 14 pt, header đậm và căn chỉnh nhất quán; không có lỗi cấu trúc xác định.

### A. Dữ liệu mẫu (nguyên văn nội dung ô)

| STT | Nhiệm vụ | Đơn vị | Kết quả |
| --- | --- | --- | --- |
| 1 | Rà soát tài liệu | Phòng Tổng hợp | Đã hoàn thành |
| 2 | Tổng hợp báo cáo | Phòng Nghiệp vụ | Đang thực hiện |


**Đầu vào hình học/OOXML mô tả:** W_allow=165 mm; các width hiện tại `[14,76,38,37]` mm chỉ là dữ liệu nguồn của ví dụ (không mặc định thiết kế).

**Chính sách chữ:** Hiệu dụng Times New Roman 14 pt ở mọi run thuộc bảng; bold header.

### B. Ứng viên và quyết định

| Phương án minh họa | Vector cột | Điều kiện cần trước khi lựa chọn |
|---|---|---|
| BASELINE (đang dùng) | [14, 76, 38, 37] mm — tổng **165 mm** | Kiểm hard floor theo TNR, header, merge/lock; đây **chưa phải phép đo Word** |
| Thay vì thích chỉnh sửa (không có chứng cứ lợi ích) | [16, 73, 39, 37] mm — tổng **165 mm** | Kiểm hard floor theo TNR, header, merge/lock; đây **chưa phải phép đo Word** |



**Kết luận kỳ vọng:** `KEEP_EXISTING / NO_OP_VALID`.

**Vì sao:** Không có căn cứ thay đổi; sửa bảng chỉ để tạo phiên bản mới tăng rủi ro và gây dao động định dạng.

**Đặc tả định dạng/thuộc tính:** Giữ preset/viền/padding/căn chỉnh hiện hữu nếu đã qua rule checks.

**Điều kiện đánh giá riêng:** Kết quả no-op, `changed_properties=[]`; áp cùng đặc tả lần 2 vẫn no-op.

### C. Phản ví dụ và tiêu chí QA

- **Không được làm:** Không normalize toàn bộ `w:tblGrid` hay đổi Table Style dùng chung khi không có lỗi.

- **QA trọng tâm:** `QA03_EFFECTIVE_FONT`, `QA04_EFFECTIVE_SIZE`, `QA07_WIDTH_GEOMETRY`, `QA12_MINIMAL_CHANGE`, `QA13_IDEMPOTENCE`.

- **Mức tin cậy:** `HIGH cho quyết định không sửa khi evidence đầy đủ`. **Truy vết:** V15 §73, §99, §166–169; V16-QUALITY-01.


---

## NR14 — Văn bản Đảng HD05 — không tự hạ 14 xuống 13 pt

**Loại/nhóm:** `PARTY_TASK_TABLE`. **Mục tiêu/bối cảnh:** Bảng tổng hợp công việc trong văn bản Đảng thuộc phạm vi HD05; profile dự án chọn chữ bảng 14 pt.

### A. Dữ liệu mẫu (nguyên văn nội dung ô)

| STT | Nội dung công việc | Đơn vị thực hiện | Thời gian |
| --- | --- | --- | --- |
| 1 | Rà soát hồ sơ chuyên đề | Chi bộ A | Tháng 11/2026 |
| 2 | Hoàn thiện báo cáo tổng kết | Bộ phận B | Tháng 12/2026 |


**Đầu vào hình học/OOXML mô tả:** Khổ A4 dọc; ví dụ lề trái 30 mm, phải 15 mm; W_allow 165 mm khi không có ràng buộc khác.

**Chính sách chữ:** Times New Roman 14 pt cố định theo profile; header cùng 14 pt đậm.

### B. Ứng viên và quyết định

| Phương án minh họa | Vector cột | Điều kiện cần trước khi lựa chọn |
|---|---|---|
| Ứng viên 14 pt (minh họa, không kết luận fit) | [14, 78, 43, 30] mm — tổng **165 mm** | Kiểm hard floor theo TNR, header, merge/lock; đây **chưa phải phép đo Word** |



**Kết luận kỳ vọng:** `KEEP_14PT; DESIGN_RECOMMENDED_WIDTH hoặc REVIEW_REQUIRED`.

**Vì sao:** Không sử dụng 13 pt chỉ để tiết kiệm không gian. Nếu không đủ diện tích để chứa token, cần xem lại phương án width/padding hoặc trình người có thẩm quyền lựa chọn bố cục.

**Đặc tả định dạng/thuộc tính:** FORMAL_GRID đơn sắc; TNR14; căn chỉnh theo kiểu dữ liệu; không thay khoản/điểm gốc.

**Điều kiện đánh giá riêng:** `font_pt=14`; nếu font14 và hard floors không khả thi => NO_SAFE_FIT/REVIEW, không fallback về font13.

### C. Phản ví dụ và tiêu chí QA

- **Không được làm:** Không giảm 14→13, không đưa font 12 pt, không chuyển lề/hướng trang tùy tiện.

- **QA trọng tâm:** `QA03_EFFECTIVE_FONT`, `QA04_EFFECTIVE_SIZE`, `QA07_WIDTH_GEOMETRY`, `QA14_REASON_TRACE`.

- **Mức tin cậy:** `HIGH cho chính sách size; width chưa đo`. **Truy vết:** V15 §II, §49; V16-FONT-02.


---

## NR15 — Bảng nổi hoặc section nhiều cột — không suy từ khổ A4

**Loại/nhóm:** `FLOATING_OR_MULTICOLUMN`. **Mục tiêu/bối cảnh:** Bảng dữ liệu nằm trong section hai cột hoặc có `tblpPr` floating; phần ảnh hưởng đến wrapped text chưa xác định.

### A. Dữ liệu mẫu (nguyên văn nội dung ô)

| Mã | Diễn giải | Giá trị |
| --- | --- | --- |
| A | Chi phí thực hiện | 150.000 |
| B | Thời gian kiểm tra | 02 giờ |


**Đầu vào hình học/OOXML mô tả:** Khổ trang A4 nhưng mỗi cột văn bản hẹp; có `tblpPr` hoặc cột báo chí chưa nhận diện W thực; không thể coi 165 mm là vùng chứa.

**Chính sách chữ:** Times New Roman 14 pt cho bảng nội dung khi profile cho phép.

### B. Ứng viên và quyết định

**Không sinh vector chiều rộng.** Bảng bị loại trừ hoặc thiếu đầu vào/authority đáng tin để đề xuất thay đổi width.

**Kết luận kỳ vọng:** `REVIEW_REQUIRED / GEOMETRY_UNKNOWN`.

**Vì sao:** Table floating/column layout làm width tính bằng page-left-right không đại diện container; cần vị trí/vùng cho phép từ OOXML.

**Đặc tả định dạng/thuộc tính:** Có thể gợi ý căn số phải và mô tả trái, nhưng không quyết định width.

**Điều kiện đánh giá riêng:** `geometry.status=UNKNOWN`, `candidate_widths_mm=none`; phần alignment có thể là đề xuất riêng nếu scope đủ.

### C. Phản ví dụ và tiêu chí QA

- **Không được làm:** Không tự xóa `tblpPr`, không chuyển inline, không gán W=165 khi thiếu chứng cứ.

- **QA trọng tâm:** `QA02_OWNER`, `QA07_WIDTH_GEOMETRY`, `QA12_MINIMAL_CHANGE`, `QA15_TRUTHFUL_STATUS`.

- **Mức tin cậy:** `LOW`. **Truy vết:** V15 §45, §143, §163; V16-WIDTH-01.


---

## NR16 — Chiều cao hàng Exactly thấp — chỉ kết luận có rủi ro

**Loại/nhóm:** `TASK_TABLE_ROW_HEIGHT`. **Mục tiêu/bối cảnh:** Bảng nhiệm vụ 3 cột, một hàng chứa mô tả dài nhưng cấu trúc khai báo chiều cao `exact=300 twips` (15 pt); chưa có ảnh Word.

### A. Dữ liệu mẫu (nguyên văn nội dung ô)

| STT | Mô tả | Ghi chú |
| --- | --- | --- |
| 1 | Kiểm tra bố trí các trang thiết bị an toàn và điều kiện tiếp cận trong khu vực làm việc | Hoàn thiện trong ngày |
| 2 | Tổng hợp biên bản | Đã hoàn thành |


**Đầu vào hình học/OOXML mô tả:** Inline, W_allow=165 mm; height rule hàng 1 `exact=300 twips`; chưa có computed line count.

**Chính sách chữ:** Times New Roman 14 pt.

### B. Ứng viên và quyết định

| Phương án minh họa | Vector cột | Điều kiện cần trước khi lựa chọn |
|---|---|---|
| Ứng viên width để đánh giá (nếu đo được) | [16, 94, 55] mm — tổng **165 mm** | Kiểm hard floor theo TNR, header, merge/lock; đây **chưa phải phép đo Word** |



**Kết luận kỳ vọng:** `CLIPPING_RISK_ESTIMATED; đề xuất `atLeast`/`auto` khi có quyền; không báo CLIPPED_OBSERVED`.

**Vì sao:** Hàng Exactly thấp và văn bản dài tạo nguy cơ cắt; từ OOXML có thể phát hiện cấu hình rủi ro nhưng chưa chứng minh nội dung nào đã bị che.

**Đặc tả định dạng/thuộc tính:** Không đổi kiểu chữ; xem `w:trHeight@w:hRule=exact` → `atLeast/auto` khi không có khóa mẫu và người dùng cho phép.

**Điều kiện đánh giá riêng:** `risk=ESTIMATED`, `proposal=SAFE_ROW_HEIGHT_IF_APPROVED`, `print_verified=false`.

### C. Phản ví dụ và tiêu chí QA

- **Không được làm:** Không tuyên bố “chữ đã bị cắt” khi chưa nhìn Word; không sửa bảng ký hoặc biểu mẫu cố định theo quy tắc này.

- **QA trọng tâm:** `QA04_EFFECTIVE_SIZE`, `QA11_ROW_HEADER`, `QA14_REASON_TRACE`, `QA15_TRUTHFUL_STATUS`.

- **Mức tin cậy:** `HIGH cho giá trị exact, LOW–MEDIUM cho rủi ro hiển thị`. **Truy vết:** V15 §26, §127, F08; V16-ROW-01.


---

## NR17 — Ô chứa nhiều đoạn, danh sách đánh số và chữ đậm — bảo toàn rich text

**Loại/nhóm:** `RICH_TEXT_CELL`. **Mục tiêu/bối cảnh:** Bảng kế hoạch trong phụ lục, ô Nội dung chứa 2 đoạn + danh sách 1–2 + một cụm bold và hyperlink.

### A. Dữ liệu mẫu (nguyên văn nội dung ô)

| STT | Nội dung | Đơn vị |
| --- | --- | --- |
| 1 | Đoạn 1: Yêu cầu phối hợp. ⏎ 1. Kiểm tra hồ sơ. ⏎ 2. Đối chiếu kết quả. ⏎ Đoạn 2: Xem tài liệu liên quan (hyperlink). | Phòng Nghiệp vụ |
| 2 | Lập báo cáo tổng hợp. | Phòng Tổng hợp |


**Đầu vào hình học/OOXML mô tả:** 3 cột trong W_allow=165 mm; ô (1,2) có nhiều `<w:p>`, numbering và hyperlink relationship.

**Chính sách chữ:** Times New Roman 14 pt toàn bộ nội dung được phép; giữ bold/italic và hyperlink.

### B. Ứng viên và quyết định

| Phương án minh họa | Vector cột | Điều kiện cần trước khi lựa chọn |
|---|---|---|
| Ưu tiên ô rich text (chỉ ước lượng) | [14, 101, 50] mm — tổng **165 mm** | Kiểm hard floor theo TNR, header, merge/lock; đây **chưa phải phép đo Word** |



**Kết luận kỳ vọng:** `PRESERVE_CONTENT_STRUCTURE; DESIGN_RECOMMENDED chỉ cho format-only độc lập`.

**Vì sao:** Chiều cao phụ thuộc số đoạn/list và khoảng cách; gộp thành một text run làm hỏng numbering, mạch văn, hyperlink và dấu ngắt.

**Đặc tả định dạng/thuộc tính:** FORMAL_GRID; ô diễn giải căn trái/trên, spacing giữ cấu trúc và phù hợp profile; width chỉ đề xuất khi giữ relationship và paragraph count.

**Điều kiện đánh giá riêng:** `paragraph_count` và `numbering_id`/hyperlink giữ nguyên; không dùng nội dung text-only thay XML nguồn.

### C. Phản ví dụ và tiêu chí QA

- **Không được làm:** Không flatten toàn bộ thành một chuỗi; không chèn newline thay list; không xóa bold/hyperlink.

- **QA trọng tâm:** `QA05_DATA_PRESERVED`, `QA08_STYLE_CASCADE`, `QA10_SPACING_PADDING`, `QA12_MINIMAL_CHANGE`.

- **Mức tin cậy:** `MEDIUM nếu parser giữ đủ rich content`. **Truy vết:** V15 §49, §125–128; V16-CELL-03/04.


---

## NR18 — Bảng không tiêu đề và dữ liệu đa nghĩa — không bịa phân loại

**Loại/nhóm:** `UNKNOWN_TABLE`. **Mục tiêu/bối cảnh:** Một bảng được copy từ nguồn khác vào Body, không có tiêu đề, không caption, 2 cột có chuỗi thay đổi ý nghĩa theo dòng.

### A. Dữ liệu mẫu (nguyên văn nội dung ô)

| (không có tiêu đề) | (không có tiêu đề) |
| --- | --- |
| A01 | 10/2026 |
| 03 | Đạt |
| Tổ 2 | 12 |
| 04/11 | Phòng A |


**Đầu vào hình học/OOXML mô tả:** Inline 2 cột, W_allow=165 mm, nhưng mục tiêu đọc và kiểu dữ liệu của cột không nhất quán.

**Chính sách chữ:** Times New Roman 14 pt nếu bảng thuộc scope và không có mẫu khác.

### B. Ứng viên và quyết định

**Không sinh vector chiều rộng.** Bảng bị loại trừ hoặc thiếu đầu vào/authority đáng tin để đề xuất thay đổi width.

**Kết luận kỳ vọng:** `REVIEW_REQUIRED hoặc KEEP_EXISTING`.

**Vì sao:** Không thể suy chắc cột 1 là STT hay mã và cột 2 là ngày/giá trị/trạng thái. Không có cơ sở tự thêm header hoặc căn phải mọi ô.

**Đặc tả định dạng/thuộc tính:** Chỉ gợi ý font/size và giữ nguyên lưới; không quyết định alignment/width theo nhãn tự tạo.

**Điều kiện đánh giá riêng:** `classification.confidence=LOW`, `role_evidence=AMBIGUOUS`, `selected_preset=NONE`, `width=NO_PROPOSAL`.

### C. Phản ví dụ và tiêu chí QA

- **Không được làm:** Không tự thêm “STT”/“Ghi chú”, không chuyển giá trị “03” thành số, không dồn cột theo một kiểu dữ liệu duy nhất.

- **QA trọng tâm:** `QA02_OWNER`, `QA05_DATA_PRESERVED`, `QA09_ALIGNMENT`, `QA14_REASON_TRACE`.

- **Mức tin cậy:** `LOW`. **Truy vết:** V15 §71, §159–160; V16-SCOPE-01, V16-QUALITY-02.


---


## III. Cách dùng casebook để đánh giá quyết định AI mà không render

**Đánh giá trên văn bản đặc tả, không phải kết quả chạy Word:**

1. Đưa cho AI **chỉ** phần A của một case và quy tắc tổng quát V16 (không đưa đáp án B/C). Yêu cầu phân loại/định dạng/giải thích theo hợp đồng.
2. So quyết định của AI với phần B/C ở mức **hành vi bắt buộc**, không so khớp máy móc vector mm khi thiếu font metrics thật. Các vector ở trên là **ứng viên** và phải được xử lý như vậy.
3. Chấm trước các **hard fail**: dùng font ngoài Times New Roman 13–14, giảm HD05 xuống 13 không có thẩm quyền, thay dữ liệu/merge, sửa layout/signature/official form, bịa width chính xác khi thiếu geometry, đánh dấu print PASS không render.
4. Với ca có width, kiểm tra tổng vector, số cột, khả năng truy nguyên W_allow, mọi ràng buộc khóa và ô gộp đã được nêu. Sau đó mới chấm sự hợp lý về cột trọng tâm và khoảng trắng.
5. So hai lần với cùng đầu vào: kết quả cùng trạng thái/giải thích hoặc chỉ khác trong vùng ước lượng đã công bố; không được chuyển qua lại KEEP → APPLY chỉ vì cách diễn đạt prompt thay đổi.
6. Khi câu trả lời khác đáp án, ghi **lý do và dữ liệu thiếu**, điều chỉnh đúng một rule/exception hoặc chính case có vấn đề; không thêm phép kiểm mới chỉ để tăng số lượng kịch bản.

### Phân loại PASS/FAIL của riêng đặc tả (không phải Word QA)

- `SPEC_CASE_PASS`: quyết định đúng scope, font, policy, dữ liệu không bị giả sửa, width arithmetic đúng và nói rõ các yếu tố ước lượng.
- `SPEC_CASE_FAIL`: có một lỗi hard gate hoặc kết luận không có chứng cứ.
- `SPEC_CASE_REVIEW`: case hoặc đáp án có ngữ nghĩa chưa rõ, thiếu nguồn/geometry; sửa đặc tả thay vì yêu cầu AI đoán.
- `NOT_RUN`: chưa có lượt đối chiếu độc lập; đây là trạng thái **hiện tại** của NR01–NR18.

### Mẫu bản ghi quyết định (chỉ là ví dụ Markdown, không phải schema triển khai)

```yaml
case: NR10
owner: appendix
classification: APPENDIX_REGISTER
font_family: Times New Roman
font_size_pt: 14
geometry:
  W_allow_mm: 165
  status: DECLARED_FOR_SYNTHETIC_CASE
columns:
  - {header: 'Mã hồ sơ', role: IDENTIFIER, protect_leading_zeros: true}
  - {header: 'Nội dung hồ sơ', role: PRIMARY_CONTENT}
  - {header: 'Đơn vị phụ trách', role: OWNER}
proposal:
  candidate_widths_mm: [36, 77, 52]
  width_status: ESTIMATED_NOT_WORD_RENDERED
  verdict: DESIGN_RECOMMENDED_IF_TOKEN_FLOOR_PASS
  prohibition: never_change_source_code_0012
review:
  required_if: font_metrics_missing_or_hard_floor_unknown
  print_verified: false
```

## IV. Traceability và giới hạn

| Case | Nhóm kiểm thử | Kết luận cốt lõi |
|---|---|---|
| NR01–NR04 | Bảng thường, thống kê, mật độ, danh sách | Width theo dữ liệu; TNR 13/14; bảo toàn token và header |
| NR05–NR06 | Merge, nhiều tầng, phụ lục dài | Grid span thật; header repeat đúng dãy; phân trang chưa xác minh |
| NR07–NR09 | Layout, chữ ký, biểu mẫu chính thức | Không áp preset bảng nội dung |
| NR10–NR12 | Token, đối tượng, bảng lồng | Bảo toàn nguồn và hình học parent; fail closed |
| NR13–NR15 | KEEP, HD05, section đặc biệt | Không sửa thừa; font đúng profile; không bịa W_allow |
| NR16–NR18 | Height, rich text, bảng đa nghĩa | Ghi rủi ro ước lượng; giữ rich content; không tự tạo header |

**Đối chiếu với V15:** các scenario T01–T152 của V15 vẫn có authority/coverage riêng; 18 case của V16 là **diễn giải mục tiêu không-render**, không phải 18 test mới đã PASS, và không thay thế tài liệu V15. Những giá trị gốc F01/F02/V10–V15 nếu được viện dẫn chỉ nhằm giải thích bằng chứng lịch sử, không nâng cấp ví dụ tổng hợp này thành số đo mới.

**Điều kiện khóa tài liệu:** Review độc lập 18 ca; xác nhận không có mâu thuẫn giữa mẫu/authority và chính sách font; đánh giá ít nhất một vòng blind decision trên từng case (không lộ đáp án); xử lý các `SPEC_CASE_FAIL` có tái hiện được; sau đó mới đổi trạng thái `DRAFT` sang `SPEC_READY`. Không triển khai app/code, không sửa GitHub tự động, không render Word/PDF/ảnh để “chữa” các case.


## Phần II. 100 case bổ sung NR19–NR118

# ChuanhoaBang V16 — 100 case study mới (NR19–NR118), không render

**Ngày đối chiếu:** 29/10/2026.
**Trạng thái:** `RESEARCH-BASED SPECIFICATION / 100 SYNTHETIC CASES / RULE-LEVEL QA ONLY`.
**Mục đích:** Bổ sung 100 ca mới vào 18 ca NR01–NR18. Đây là tài liệu đặc tả giúp AI **ra quyết định từ nội dung + OOXML**, không viết formatter, không sửa DOCX và không cần xem ảnh/PDF.

## Ràng buộc không được thay đổi

- Chỉ đề xuất định dạng **bảng nội dung** bằng **Times New Roman 13 hoặc 14 pt**; 14 pt mặc định, 13 pt chỉ khi có cơ sở/profile cho phép. Header/total trong bảng cũng chỉ 13 hoặc 14 pt.
- Không dùng `Fit Text`, character scale, font thay thế hay thu chữ dưới 13 pt để ép bảng.
- Với biểu mẫu chính thức, bảng dàn trang, vùng ký, footnotes/header hoặc đối tượng bị khóa: `PRESERVE`/`REVIEW_REQUIRED`, **không lấy chính sách bảng nội dung để sửa chúng**.
- Không sửa số, ngày, chữ, dấu câu, số 0 đầu, dấu không ngắt, hyperlinks, fields, nội dung bảng, ô gộp, bố trí section hoặc chữ ký số để cải thiện diện tích.
- Không render Word, ảnh, PDF; các mẫu chỉ có đầu vào văn bản + tín hiệu OOXML mô phỏng. `GEOMETRY_DECLARED` không chứng minh print layout, `TEXT_ESTIMATED` không phải đo dòng sau kết xuất.
- Các véc-tơ mm là **ví dụ hình học/đáp án tham khảo có điều kiện**, không phải kích thước cố định hay số đo Times New Roman. Khi chưa có font face/metrics đúng, AI phải ghi rõ độ bất định hoặc `REVIEW_REQUIRED`.

## Hướng dẫn đọc một case

Mỗi case chứa **A. Dữ liệu** (ít nhất một ví dụ ô), **B. OOXML/ngữ cảnh**, **C. Quyết định + font + preset + vector nếu có**, **D. Phản ví dụ**, **E. QA không render**, **F. Evidence + nguồn**. Từ dấu `⏎`, `[gộp]`, `[field]`, `[drawing]`, `[trống]` là **ký hiệu mô tả nguồn giả lập**, không được hiểu là ký tự thực phải chèn vào DOCX.

Lưu ý: nếu case có `NO_SAFE_FIT`, giá trị sàn phải là **giả định đầu vào đã xác minh** hoặc đo metrics được nêu rõ; không suy bất khả thi từ độ dài chuỗi. Một case có width vector **chỉ là đề xuất ứng viên**, không tương đương `RULE_CONFORMANT` về độ rộng chữ.

## 1. Ma trận phủ tình huống

| Nhóm | Số case | Điểm nhấn |
|---|---:|---|
| A — Vai trò đọc hiểu | 12 | Vai trò và tác vụ đọc |
| B — Chữ tiếng Việt và token | 12 | Các trường hợp khác nhau trong cùng nhóm |
| C — Số, ngày và giá trị thiếu | 12 | Các trường hợp khác nhau trong cùng nhóm |
| D — Hình học và chiều rộng | 12 | Các trường hợp khác nhau trong cùng nhóm |
| E — Ô gộp và phân trang | 12 | Các trường hợp khác nhau trong cùng nhóm |
| F — Style và đường viền | 10 | Các trường hợp khác nhau trong cùng nhóm |
| G — Nội dung đặc biệt trong ô | 10 | Các trường hợp khác nhau trong cùng nhóm |
| H — Quyền sửa và bảo toàn | 10 | Các trường hợp khác nhau trong cùng nhóm |
| I — So sánh phương án và nhất quán | 10 | Các trường hợp khác nhau trong cùng nhóm |
| **Tổng** | **100** | **Bổ sung vào 18 ca V16 trước đó → 118 ca** |

### Trạng thái đáp án dự kiến

| Kết luận | Số ca |
|---|---:|
| `DESIGN_RECOMMENDED` | 62 |
| `REVIEW_REQUIRED` | 21 |
| `KEEP_EXISTING` | 7 |
| `NO_SAFE_FIT` | 1 |
| `PRESERVE` | 9 |

## 2. Danh mục 100 case study

| ID | Tình huống | Nhóm | Quyết định dự kiến |
|---|---|---|---|
| [NR19](#case-nr19) | Bảng kết luận có cột nhận định và kiến nghị | A | `DESIGN_RECOMMENDED` |
| [NR20](#case-nr20) | Trách nhiệm chủ trì khác trách nhiệm phối hợp | A | `DESIGN_RECOMMENDED` |
| [NR21](#case-nr21) | Nhãn “Kết quả” trong bảng kế hoạch | A | `DESIGN_RECOMMENDED` |
| [NR22](#case-nr22) | Bảng tra cứu hồ sơ thiếu tiêu đề cột | A | `REVIEW_REQUIRED` |
| [NR23](#case-nr23) | Bảng ma trận phê duyệt nhiều tiêu chí | A | `DESIGN_RECOMMENDED` |
| [NR24](#case-nr24) | Bảng kiểm có ba trạng thái tuân thủ | A | `DESIGN_RECOMMENDED` |
| [NR25](#case-nr25) | Bảng đối chiếu điều khoản có dẫn chiếu dài | A | `DESIGN_RECOMMENDED` |
| [NR26](#case-nr26) | Bảng tiến độ theo mốc có ngày và việc | A | `DESIGN_RECOMMENDED` |
| [NR27](#case-nr27) | Bảng danh mục văn bản theo số hiệu | A | `DESIGN_RECOMMENDED` |
| [NR28](#case-nr28) | Bảng chỉ số KPI có mục tiêu và thực hiện | A | `DESIGN_RECOMMENDED` |
| [NR29](#case-nr29) | Bảng tổng hợp có ghi chú diễn giải dài | A | `DESIGN_RECOMMENDED` |
| [NR30](#case-nr30) | Bảng chỉ có tiêu đề cột, chưa nhập dữ liệu | A | `REVIEW_REQUIRED` |
| [NR31](#case-nr31) | Tên người nhiều âm tiết trong cột hẹp | B | `DESIGN_RECOMMENDED` |
| [NR32](#case-nr32) | Unicode tiếng Việt dạng ký tự tổ hợp | B | `DESIGN_RECOMMENDED` |
| [NR33](#case-nr33) | Dấu cách không ngắt giữa số và đơn vị | B | `DESIGN_RECOMMENDED` |
| [NR34](#case-nr34) | Dấu gạch nối không ngắt trong mã | B | `DESIGN_RECOMMENDED` |
| [NR35](#case-nr35) | STT có giá trị dài hơn header | B | `DESIGN_RECOMMENDED` |
| [NR36](#case-nr36) | Tiêu đề in hoa có nhiều phụ âm tiếng Việt | B | `DESIGN_RECOMMENDED` |
| [NR37](#case-nr37) | Chuỗi dấu gạch chéo trong số văn bản | B | `DESIGN_RECOMMENDED` |
| [NR38](#case-nr38) | Nhiều dấu cách và tab nguồn trong ô | B | `REVIEW_REQUIRED` |
| [NR39](#case-nr39) | Ký hiệu mũ trong đơn vị diện tích | B | `DESIGN_RECOMMENDED` |
| [NR40](#case-nr40) | Từ Latin và ký hiệu Hy Lạp trong một ô | B | `DESIGN_RECOMMENDED` |
| [NR41](#case-nr41) | Chữ nghiêng trích dẫn trong ô | B | `DESIGN_RECOMMENDED` |
| [NR42](#case-nr42) | Dấu nối và ký tự mềm trong tên địa danh | B | `DESIGN_RECOMMENDED` |
| [NR43](#case-nr43) | Mã hồ sơ có số 0 đầu trong cột định danh | C | `DESIGN_RECOMMENDED` |
| [NR44](#case-nr44) | Số âm và số thập phân âm | C | `DESIGN_RECOMMENDED` |
| [NR45](#case-nr45) | Dấu phân cách hàng nghìn theo kiểu Việt Nam | C | `DESIGN_RECOMMENDED` |
| [NR46](#case-nr46) | Tỷ lệ phần trăm với độ chính xác không đồng đều | C | `DESIGN_RECOMMENDED` |
| [NR47](#case-nr47) | Giá trị khoảng và bất đẳng thức | C | `DESIGN_RECOMMENDED` |
| [NR48](#case-nr48) | Đơn vị tính nằm ở cột riêng | C | `DESIGN_RECOMMENDED` |
| [NR49](#case-nr49) | Giá trị tiền lớn có ký hiệu đồng | C | `DESIGN_RECOMMENDED` |
| [NR50](#case-nr50) | Ngày tháng mơ hồ nếu diễn giải theo locale | C | `DESIGN_RECOMMENDED` |
| [NR51](#case-nr51) | Ký hiệu kỳ báo cáo không phải ngày cụ thể | C | `DESIGN_RECOMMENDED` |
| [NR52](#case-nr52) | Ô trống, dấu gạch và chữ N/A khác số 0 | C | `DESIGN_RECOMMENDED` |
| [NR53](#case-nr53) | Tổng cộng có số 0 hợp lệ và ô chưa có kết quả | C | `DESIGN_RECOMMENDED` |
| [NR54](#case-nr54) | Chỉ số kèm chú thích dạng ký hiệu tham chiếu | C | `DESIGN_RECOMMENDED` |
| [NR55](#case-nr55) | Bảng hai cột ngắn không cần kéo hết trang | D | `KEEP_EXISTING` |
| [NR56](#case-nr56) | Bảng tám cột trong section ngang đã cho phép | D | `DESIGN_RECOMMENDED` |
| [NR57](#case-nr57) | Bảng trong section khổ A5 | D | `DESIGN_RECOMMENDED` |
| [NR58](#case-nr58) | Bảng nằm trong mục đánh số có thụt lề | D | `DESIGN_RECOMMENDED` |
| [NR59](#case-nr59) | Lề đối xứng và gáy tài liệu | D | `REVIEW_REQUIRED` |
| [NR60](#case-nr60) | Bảng trong section bố cục hai cột văn bản | D | `DESIGN_RECOMMENDED` |
| [NR61](#case-nr61) | Độ rộng bảng khai báo theo phần trăm | D | `DESIGN_RECOMMENDED` |
| [NR62](#case-nr62) | Khai báo tcW xung đột với tblGrid | D | `REVIEW_REQUIRED` |
| [NR63](#case-nr63) | Fixed layout và AutoFit cùng bộ giá trị | D | `KEEP_EXISTING` |
| [NR64](#case-nr64) | Token không ngắt dài hơn vùng cho phép | D | `NO_SAFE_FIT` |
| [NR65](#case-nr65) | Bảng sát mép vùng chữ không có dự phòng | D | `REVIEW_REQUIRED` |
| [NR66](#case-nr66) | Bảng lồng có chiều rộng ô mẹ xác định | D | `DESIGN_RECOMMENDED` |
| [NR67](#case-nr67) | Tiêu đề gộp ngang hai cột con | E | `DESIGN_RECOMMENDED` |
| [NR68](#case-nr68) | Tên nhóm gộp dọc ba hàng | E | `DESIGN_RECOMMENDED` |
| [NR69](#case-nr69) | Hàng dữ liệu bỏ ô lưới đầu tiên | E | `REVIEW_REQUIRED` |
| [NR70](#case-nr70) | Hàng bỏ ô lưới cuối theo gridAfter | E | `REVIEW_REQUIRED` |
| [NR71](#case-nr71) | Bảng dài có hai hàng tiêu đề liên tiếp | E | `DESIGN_RECOMMENDED` |
| [NR72](#case-nr72) | Dòng tiêu đề phụ ở giữa bảng | E | `KEEP_EXISTING` |
| [NR73](#case-nr73) | Ngắt trang thủ công nằm trong bảng dài | E | `REVIEW_REQUIRED` |
| [NR74](#case-nr74) | Hàng có đoạn diễn giải vượt chiều cao một trang | E | `REVIEW_REQUIRED` |
| [NR75](#case-nr75) | Chiều cao Exactly nhỏ hơn một dòng 14 pt | E | `DESIGN_RECOMMENDED` |
| [NR76](#case-nr76) | AtLeast cao có chủ đích để người dùng ghi tay | E | `PRESERVE` |
| [NR77](#case-nr77) | Caption ngay trước bảng có keepNext | E | `DESIGN_RECOMMENDED` |
| [NR78](#case-nr78) | Hai bảng liền nhau cùng Table Style | E | `REVIEW_REQUIRED` |
| [NR79](#case-nr79) | Viền cấp ô ghi đè viền cấp bảng | F | `REVIEW_REQUIRED` |
| [NR80](#case-nr80) | Đơn vị độ dày viền bằng phần tám điểm | F | `DESIGN_RECOMMENDED` |
| [NR81](#case-nr81) | Nền ô báo trạng thái có ngữ nghĩa | F | `PRESERVE` |
| [NR82](#case-nr82) | Banding xen kẽ do Table Style | F | `KEEP_EXISTING` |
| [NR83](#case-nr83) | FirstRow table style không tương đương header lặp | F | `DESIGN_RECOMMENDED` |
| [NR84](#case-nr84) | Cell spacing gây khe giữa các đường kẻ | F | `DESIGN_RECOMMENDED` |
| [NR85](#case-nr85) | Bảng thống kê chỉ dùng đường ngang | F | `DESIGN_RECOMMENDED` |
| [NR86](#case-nr86) | Hàng tổng cần nhấn đường trên thay vì tô màu | F | `DESIGN_RECOMMENDED` |
| [NR87](#case-nr87) | Hàng nhóm có đường kẻ phân cấp | F | `DESIGN_RECOMMENDED` |
| [NR88](#case-nr88) | Gridlines trong Word không phải đường viền in | F | `DESIGN_RECOMMENDED` |
| [NR89](#case-nr89) | Danh sách gạch đầu dòng trong một ô | G | `DESIGN_RECOMMENDED` |
| [NR90](#case-nr90) | Ô hai đoạn có after-spacing khác nhau | G | `DESIGN_RECOMMENDED` |
| [NR91](#case-nr91) | Ngắt dòng thủ công có chủ đích trong ô | G | `DESIGN_RECOMMENDED` |
| [NR92](#case-nr92) | Đường dẫn hyperlink dài kèm anchor | G | `REVIEW_REQUIRED` |
| [NR93](#case-nr93) | Kết quả là field Word không phải text tĩnh | G | `REVIEW_REQUIRED` |
| [NR94](#case-nr94) | Bảng có nội dung đang Track Changes | G | `PRESERVE` |
| [NR95](#case-nr95) | Content control trong ô có khóa nội dung | G | `PRESERVE` |
| [NR96](#case-nr96) | Placeholder trong ô chưa phải dữ liệu người dùng | G | `REVIEW_REQUIRED` |
| [NR97](#case-nr97) | Ô chứa hình vẽ kèm chữ chú thích | G | `REVIEW_REQUIRED` |
| [NR98](#case-nr98) | Tab stop và dấu xuống dòng mềm trong ô | G | `REVIEW_REQUIRED` |
| [NR99](#case-nr99) | Biểu mẫu chính thức có chỉ định layout riêng | H | `PRESERVE` |
| [NR100](#case-nr100) | Style bảng nguồn là custom nhưng chưa có mô tả | H | `REVIEW_REQUIRED` |
| [NR101](#case-nr101) | Bảng nằm trong header tài liệu | H | `PRESERVE` |
| [NR102](#case-nr102) | Bảng trong footnote tài liệu | H | `PRESERVE` |
| [NR103](#case-nr103) | Comment range và bookmark chạy qua ô | H | `REVIEW_REQUIRED` |
| [NR104](#case-nr104) | Văn bản DOCX có chữ ký số | H | `PRESERVE` |
| [NR105](#case-nr105) | Table Style dùng chung nhiều bảng | H | `DESIGN_RECOMMENDED` |
| [NR106](#case-nr106) | Font Times New Roman chưa được xác minh có trên máy đo | H | `REVIEW_REQUIRED` |
| [NR107](#case-nr107) | Bảng nguồn trộn 13 pt và 14 pt | H | `REVIEW_REQUIRED` |
| [NR108](#case-nr108) | Mẫu được viện dẫn xung đột với preset thẩm mỹ | H | `PRESERVE` |
| [NR109](#case-nr109) | Ba bảng cùng chức năng nhưng một bảng lệch padding | I | `DESIGN_RECOMMENDED` |
| [NR110](#case-nr110) | Cùng dữ liệu nhưng mục tiêu đọc khác nhau | I | `DESIGN_RECOMMENDED` |
| [NR111](#case-nr111) | So sánh 14 pt và 13 pt trong bảng mật độ cao | I | `DESIGN_RECOMMENDED` |
| [NR112](#case-nr112) | Hai ứng viên tương đương về độ rộng nhưng khác patch cost | I | `KEEP_EXISTING` |
| [NR113](#case-nr113) | Không thay đổi khi tất cả điều kiện nội tại đạt | I | `KEEP_EXISTING` |
| [NR114](#case-nr114) | Cột mô tả không phải nút thắt của hàng | I | `DESIGN_RECOMMENDED` |
| [NR115](#case-nr115) | Header dài là nút thắt hơn dữ liệu số | I | `DESIGN_RECOMMENDED` |
| [NR116](#case-nr116) | Từ viết tắt có thể làm mất nghĩa nếu AI tự thu gọn | I | `DESIGN_RECOMMENDED` |
| [NR117](#case-nr117) | Chừa một phần width cho bảng số ngắn | I | `KEEP_EXISTING` |
| [NR118](#case-nr118) | Tái lập quyết định từ cùng dữ liệu OOXML | I | `DESIGN_RECOMMENDED` |

## 3. Các case chi tiết

<a id="case-nr19"></a>
### NR19 — Bảng kết luận có cột nhận định và kiến nghị
**Nhóm:** A — Vai trò đọc hiểu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `DECISION`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Nội dung | Kết quả rà soát | Kiến nghị |
| --- | --- | --- |
| Công tác trực ca | Đạt yêu cầu | Tiếp tục duy trì |
| Hồ sơ bàn giao | Còn thiếu biên bản | Bổ sung trước 05/11 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Cột “Kiến nghị” quyết định hành động, không phải ghi chú phụ.
**Thuộc tính cần phân tích:** `w:tblGrid,w:tcW,w:pPr/w:jc,w:vAlign`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Đặt ba cột cân bằng theo nhu cầu câu chữ, nhấn header; căn trái/trên cả cột nhận định và kiến nghị. Cỡ 14 pt.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[39, 57, 69]` mm; tổng **165 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không nới cột “Nội dung” chỉ vì nó đứng đầu và làm kiến nghị thành nhiều dòng vụn.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr20"></a>
### NR20 — Trách nhiệm chủ trì khác trách nhiệm phối hợp
**Nhóm:** A — Vai trò đọc hiểu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `ACTION`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Nhiệm vụ | Chủ trì | Phối hợp |
| --- | --- | --- |
| Khảo sát luồng | Phòng Nghiệp vụ | Bộ phận Điều độ |
| Tổng hợp báo cáo | Phòng Tổng hợp | Phòng Kỹ thuật |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Hai cột trách nhiệm có vai trò khác nhau dù đều là tên đơn vị.
**Thuộc tính cần phân tích:** `w:tblGrid,w:tr,w:tc,w:t`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Tách vai trò OWNER_MAIN và OWNER_SUPPORT trong lý giải; giữ header đậm, căn trái tên đơn vị, không suy một cột là phụ để co tùy ý.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[69, 48, 48]` mm; tổng **165 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không hợp nhất hai cột trách nhiệm hoặc đổi vị trí chủ trì–phối hợp.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr21"></a>
### NR21 — Nhãn “Kết quả” trong bảng kế hoạch
**Nhóm:** A — Vai trò đọc hiểu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `TRACK_DEADLINE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Công việc | Thời hạn | Kết quả |
| --- | --- | --- |
| Kiểm tra thiết bị | 03/11 | Đã hoàn thành |
| Bổ sung vật tư | 05/11 | Đang thực hiện |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Kết quả là trạng thái, không phải số liệu.
**Thuộc tính cần phân tích:** `w:pPr/w:jc,w:t,w:tcW`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Nhận diện STATUS; căn giữa các trạng thái ngắn nếu thống nhất và đủ chiều rộng; căn trái công việc, giữ ngày thành token.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[87, 35, 43]` mm; tổng **165 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không tự chuyển “Đã hoàn thành” thành 100% hoặc áp preset căn số phải.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr22"></a>
### NR22 — Bảng tra cứu hồ sơ thiếu tiêu đề cột
**Nhóm:** A — Vai trò đọc hiểu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| HS-001 | Đăng ký tàu | Đã nhận |
| --- | --- | --- |
| HS-002 | Thông báo đến | Chờ bổ sung |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Hàng đầu là dữ liệu, không có chứng cứ header.
**Thuộc tính cần phân tích:** `w:tblHeader,w:tr,w:t`.

**C. Kết quả kỳ vọng — `REVIEW_REQUIRED`:** Chỉ nhận diện mã ở cột 1 và trạng thái có điều kiện; không tự đánh dấu hàng đầu là tblHeader hoặc tự sáng tác nhãn cột.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không ghi thêm “Mã”, “Loại”, “Trạng thái” vào nội dung nguồn.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `SEMANTIC_AMBIGUOUS`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr23"></a>
### NR23 — Bảng ma trận phê duyệt nhiều tiêu chí
**Nhóm:** A — Vai trò đọc hiểu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `DECISION`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Phương án | Chi phí | Rủi ro | Đề xuất |
| --- | --- | --- | --- |
| A | Thấp | Trung bình | Ưu tiên |
| B | Trung bình | Thấp | Xem xét |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Mục tiêu DECISION, cột cuối quyết định cách đọc.
**Thuộc tính cần phân tích:** `w:tblGrid,w:pPr,w:rPr`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Header 14 đậm; các nhãn ngắn căn giữa; mô tả kết luận căn trái nếu nhiều chữ; cấp đủ rộng cho cột đề xuất.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[35, 36, 38, 56]` mm; tổng **165 mm** (4 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không thay từ “Xem xét” bằng “Chưa duyệt” hoặc biến nhãn rủi ro thành điểm số.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr24"></a>
### NR24 — Bảng kiểm có ba trạng thái tuân thủ
**Nhóm:** A — Vai trò đọc hiểu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `VERIFY_COMPLIANCE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Tiêu chí | Yêu cầu | Đánh giá |
| --- | --- | --- |
| Hồ sơ trực ca | Đầy đủ | Đạt |
| Sổ nhật ký | Ghi liên tục | Chưa xác định |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** “Chưa xác định” không đồng nghĩa “Không đạt”.
**Thuộc tính cần phân tích:** `w:t,w:shd,w:tcW`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Giữ nguyên ba trạng thái, nhấn header, cột Đánh giá vừa để đọc cả cụm; không dùng màu đơn độc truyền đạt trạng thái.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[47, 52, 66]` mm; tổng **165 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không tự quy đổi chưa xác định thành sai phạm.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S6](#nguon-s6).

---

<a id="case-nr25"></a>
### NR25 — Bảng đối chiếu điều khoản có dẫn chiếu dài
**Nhóm:** A — Vai trò đọc hiểu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `VERIFY_COMPLIANCE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Điều khoản | Nội dung hiện hành | Đề xuất |
| --- | --- | --- |
| Điều 5 khoản 2 | Quy định trách nhiệm cập nhật dữ liệu | Làm rõ thời điểm báo cáo |
| Điều 8 | Bổ sung yêu cầu lưu vết | Giữ nguyên |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Chuỗi dẫn chiếu là định danh pháp lý cần bảo vệ.
**Thuộc tính cần phân tích:** `w:tblGrid,w:tcW,w:t`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Căn trái toàn bộ nội dung, dành chỗ hợp lý cho các cột diễn giải, cho phép xuống dòng khoảng trắng của điều khoản mà không sửa ký tự.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[35, 68, 62]` mm; tổng **165 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không viết tắt dẫn chiếu thành “Đ5 K2” hoặc thay nội dung pháp lý.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr26"></a>
### NR26 — Bảng tiến độ theo mốc có ngày và việc
**Nhóm:** A — Vai trò đọc hiểu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `TRACK_DEADLINE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Mốc | Nội dung công việc | Phụ trách |
| --- | --- | --- |
| 03/11/2026 | Kiểm tra hệ thống liên lạc | Bộ phận Kỹ thuật |
| 05/11/2026 | Bàn giao tài liệu hướng dẫn | Phòng Nghiệp vụ |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Người đọc cần tìm ngày trước rồi mới đến việc.
**Thuộc tính cần phân tích:** `w:pPr/w:jc,w:tcW,w:t`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Cột ngày dùng sàn không ngắt; cột việc là vùng co giãn chính; cột phụ trách không thu đến mức vỡ tên cơ quan.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[40, 75, 50]` mm; tổng **165 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không tự đổi thứ tự ngày để đưa mốc gần nhất lên đầu.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr27"></a>
### NR27 — Bảng danh mục văn bản theo số hiệu
**Nhóm:** A — Vai trò đọc hiểu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Số ký hiệu | Trích yếu | Tình trạng |
| --- | --- | --- |
| 15/QĐ-HT | Phê duyệt kế hoạch thực hiện | Còn hiệu lực |
| 20/TB-HT | Thông báo lịch kiểm tra | Đang rà soát |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Mã số ký hiệu cần được nhận diện đúng, cột trích yếu có nhiều chữ.
**Thuộc tính cần phân tích:** `w:t,w:tblGrid,w:tcW`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Giữ mã dạng text; căn trái trích yếu; cấp width để mã có thể đọc như một cụm nếu đo font cho phép.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[46, 76, 43]` mm; tổng **165 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không thay dấu gạch nối, bỏ số 0 hoặc chuẩn hóa số ký hiệu thành dữ liệu số.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr28"></a>
### NR28 — Bảng chỉ số KPI có mục tiêu và thực hiện
**Nhóm:** A — Vai trò đọc hiểu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Chỉ tiêu | Mục tiêu | Thực hiện |
| --- | --- | --- |
| Hồ sơ đúng hạn (%) | ≥ 95 | 96,4 |
| Sự cố ghi nhận | 0 | 0 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Phải so sánh với ngưỡng; chữ ≥ là một phần giá trị.
**Thuộc tính cần phân tích:** `w:t,w:pPr/w:jc,w:tblGrid`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Căn phải hai cột định lượng, căn trái chỉ tiêu, header nhấn vừa phải; giữ cả đơn vị nằm trong nhãn.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[79, 43, 43]` mm; tổng **165 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không tự đánh giá đạt/không đạt và chèn cột kết luận mới.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr29"></a>
### NR29 — Bảng tổng hợp có ghi chú diễn giải dài
**Nhóm:** A — Vai trò đọc hiểu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `SUMMARY`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Nội dung | Kết quả | Ghi chú |
| --- | --- | --- |
| Kiểm tra giấy tờ | Đạt | Đã rà soát đầy đủ hồ sơ gốc theo danh mục |
| Kiểm tra thiết bị | Chưa hoàn tất | Cần phối hợp các bộ phận để đối chiếu biên bản |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Ghi chú dài nhưng không mặc nhiên là trọng tâm của tác vụ SUMMARY.
**Thuộc tính cần phân tích:** `w:tcW,w:vAlign,w:trHeight`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Cho ghi chú xuống dòng tự nhiên; không dành mọi chiều rộng cho ghi chú nếu làm cột Kết quả khó quét.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[48, 40, 77]` mm; tổng **165 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không cắt bỏ lý do trong ô ghi chú để làm hàng thấp.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr30"></a>
### NR30 — Bảng chỉ có tiêu đề cột, chưa nhập dữ liệu
**Nhóm:** A — Vai trò đọc hiểu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `ACTION`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| STT | Nội dung | Người thực hiện | Hạn hoàn thành |
| --- | --- | --- | --- |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Chưa có ô dữ liệu thực nên không thể suy sức ép width từ phân phối nội dung.
**Thuộc tính cần phân tích:** `w:tblGrid,w:tblHeader,w:tcW`.

**C. Kết quả kỳ vọng — `REVIEW_REQUIRED`:** Chọn preset Formal Grid TNR14 và căn header theo ngữ nghĩa; ghi các width chỉ là khởi tạo, chờ dữ liệu mới xác định.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không khẳng định bảng đã tối ưu độ rộng hoặc suy số dòng từ các hàng chưa tồn tại.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `DATA_INCOMPLETE`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr31"></a>
### NR31 — Tên người nhiều âm tiết trong cột hẹp
**Nhóm:** B — Chữ tiếng Việt và token. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Họ và tên | Bộ phận | Ghi chú |
| --- | --- | --- |
| Nguyễn Thị Minh Anh | Phòng Điều độ | Trực ca |
| Trần Hoàng Phúc Long | Phòng Nghiệp vụ | Phụ trách |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Cột tên phải bảo toàn cụm từ dễ nhận diện, không chỉ đo từ dài nhất.
**Thuộc tính cần phân tích:** `w:rFonts,w:sz,w:tcW,w:t`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Sử dụng TNR14, căn trái tên; đo bằng glyph TNR và hạn chế phương án làm một tên thành nhiều dòng lẻ.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[70, 58, 37]` mm; tổng **165 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không bỏ tên đệm hoặc viết tắt họ tên để vừa ô.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr32"></a>
### NR32 — Unicode tiếng Việt dạng ký tự tổ hợp
**Nhóm:** B — Chữ tiếng Việt và token. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Tên đơn vị | Số lượng |
| --- | --- |
| Phòng Kỹ thuật | 12 |
| Phòng Tổng hợp | 8 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Chuỗi đầu dùng dấu tổ hợp Unicode, nhìn gần giống chữ chuẩn NFC.
**Thuộc tính cần phân tích:** `w:t,w:rFonts,w:sz`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Đo theo grapheme/shaping Times New Roman; giữ nguyên chuỗi nguồn khi chỉ format; căn trái tên và căn phải số.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[112, 53]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không tự chuẩn hóa Unicode trong DOCX nguồn như một tác dụng phụ.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr33"></a>
### NR33 — Dấu cách không ngắt giữa số và đơn vị
**Nhóm:** B — Chữ tiếng Việt và token. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Thông số | Giá trị |
| --- | --- |
| Chiều dài | 15 m |
| Khối lượng | 20 tấn |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Ví dụ có NBSP U+00A0 giữa số và đơn vị, khác khoảng trắng thường.
**Thuộc tính cần phân tích:** `w:t,xml:space,w:tcW`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Xem cả cụm số–đơn vị như token bảo vệ khi tính sàn; căn phải giá trị; nếu không đủ phải review.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[95, 70]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không thay NBSP thành dấu cách thường hoặc ngắt số và đơn vị tùy tiện.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr34"></a>
### NR34 — Dấu gạch nối không ngắt trong mã
**Nhóm:** B — Chữ tiếng Việt và token. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Mã thiết bị | Tình trạng |
| --- | --- |
| HT‑2026‑01 | Sẵn sàng |
| HT‑2026‑02 | Đang kiểm tra |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Mã sử dụng nonbreaking hyphen U+2011.
**Thuộc tính cần phân tích:** `w:t,w:tcFitText,w:tcW`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Bảo vệ toàn chuỗi mã khi đo sàn chiều rộng; TNR14; nếu không chứa được thì không ép bằng fitText.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[82, 83]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không thay U+2011 bằng dấu trừ hoặc tách mã vào nhiều dòng.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr35"></a>
### NR35 — STT có giá trị dài hơn header
**Nhóm:** B — Chữ tiếng Việt và token. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| STT | Nội dung |
| --- | --- |
| 998 | Biên bản kiểm tra |
| 1000 | Hồ sơ bàn giao |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Giá trị “1000” có thể rộng hơn “STT” tùy font/đậm.
**Thuộc tính cần phân tích:** `w:tblGrid,w:tcW,w:rPr/w:b`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Chọn sàn từ max(header, các giá trị) cộng padding; căn giữa STT; không giữ mức 8% cố định.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[25, 140]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không dùng width “STT=10mm” như luật chung.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr36"></a>
### NR36 — Tiêu đề in hoa có nhiều phụ âm tiếng Việt
**Nhóm:** B — Chữ tiếng Việt và token. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `ACTION`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| ĐƠN VỊ THỰC HIỆN | THỜI HẠN |
| --- | --- |
| Phòng Nghiệp vụ | 05/11/2026 |
| Phòng Kỹ thuật | 06/11/2026 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Header chữ hoa và bold làm width pressure khác dữ liệu thường.
**Thuộc tính cần phân tích:** `w:rPr/w:b,w:rPr/w:sz,w:t,w:tcW`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Đo header TNR14 bold riêng, có thể cho tiêu đề xuống hai dòng tự nhiên khi hợp lý; không tự đổi hoa/thường.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[103, 62]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không giảm cỡ tiêu đề xuống 11 pt để bắt buộc một dòng.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr37"></a>
### NR37 — Chuỗi dấu gạch chéo trong số văn bản
**Nhóm:** B — Chữ tiếng Việt và token. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Số văn bản | Trích yếu |
| --- | --- |
| 123/2026/QĐ-HT | Phân công nhiệm vụ |
| 08/BC-TH | Báo cáo tháng |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Dấu gạch chéo là phần mã, không tự suy thành chỗ ngắt.
**Thuộc tính cần phân tích:** `w:t,w:tcW,w:tblGrid`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Bảo vệ mã theo phân loại identifier; dành sàn cho mã dài nhất sau đo TNR13/14, giữ trích yếu căn trái.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[65, 100]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không đưa dấu xuống dòng giữa “2026/” và “QĐ-HT” để ép cột.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2), [S12](#nguon-s12).

---

<a id="case-nr38"></a>
### NR38 — Nhiều dấu cách và tab nguồn trong ô
**Nhóm:** B — Chữ tiếng Việt và token. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Nội dung | Ghi chú |
| --- | --- |
| Đối chiếu  hồ sơ | Hai dấu cách nguồn |
| Mục	phụ | Tab nằm trong run |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Khoảng trắng kép và tab có thể mang nguồn gốc sao chép hoặc cấu trúc.
**Thuộc tính cần phân tích:** `w:tab,xml:space,w:t,w:pPr`.

**C. Kết quả kỳ vọng — `REVIEW_REQUIRED`:** Phân tích `xml:space`/tab riêng, chỉ thay căn lề qua paragraph property, ghi REVIEW nếu tab ảnh hưởng geometry.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không xóa dấu cách đôi hay đổi tab thành khoảng trắng trong tác vụ format-only.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_LAYOUT_AMBIGUOUS`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr39"></a>
### NR39 — Ký hiệu mũ trong đơn vị diện tích
**Nhóm:** B — Chữ tiếng Việt và token. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Khu vực | Diện tích |
| --- | --- |
| Kho lưu trữ | 120 m² |
| Khu tập kết | 85 m² |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Ký tự m² khác với m + số 2 dạng superscript formatting.
**Thuộc tính cần phân tích:** `w:t,w:vertAlign,w:rFonts,w:sz`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Giữ đúng Unicode/run; căn phải giá trị và cân nhắc độ rộng theo glyph của đơn vị; không đồng hóa kiểu chỉ vì hiển thị giống.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[87, 78]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không sửa “m²” thành “m2” hoặc dùng text mới.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr40"></a>
### NR40 — Từ Latin và ký hiệu Hy Lạp trong một ô
**Nhóm:** B — Chữ tiếng Việt và token. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Thông số | Ngưỡng |
| --- | --- |
| Độ lệch Δ | ≤ 0,5 |
| Tỷ lệ α | 0,15 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Có ký tự Δ, α và ≤; font mapping/fallback ảnh hưởng sàn.
**Thuộc tính cần phân tích:** `w:rFonts,w:sz,w:t`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Xác định glyph coverage TNR đúng face; ghi trạng thái đo không chắc nếu glyph fallback; căn phải ngưỡng.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[94, 71]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không thay các ký hiệu bằng chữ Latin hoặc biểu thức gần nghĩa.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr41"></a>
### NR41 — Chữ nghiêng trích dẫn trong ô
**Nhóm:** B — Chữ tiếng Việt và token. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Trích dẫn | Nguồn |
| --- | --- |
| “Bảo đảm an toàn là ưu tiên” | Tài liệu nội bộ |
| “Theo dõi liên tục” | Biên bản họp |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Một phần nội dung có run italic kế thừa; bề rộng có thể khác Roman.
**Thuộc tính cần phân tích:** `w:rPr/w:i,w:rFonts,w:tcW`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Đo từng run theo bold/italic hiệu dụng; giữ italic có dụng ý, căn trái trích dẫn, không ép justify.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[115, 50]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không đổi run nghiêng thành chữ đứng chỉ để giảm độ rộng.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr42"></a>
### NR42 — Dấu nối và ký tự mềm trong tên địa danh
**Nhóm:** B — Chữ tiếng Việt và token. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Địa danh | Mô tả |
| --- | --- |
| Bà Rịa – Vũng Tàu | Khu vực đối chiếu |
| Hải Phòng – Quảng Ninh | Tuyến phối hợp |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** En dash U+2013 cùng khoảng cách hai phía là thành phần nội dung gốc.
**Thuộc tính cần phân tích:** `w:t,w:tcW,w:pPr/w:jc`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Căn trái địa danh; cho wrap tại khoảng trắng nếu cần; không sửa dấu nối, không coi en dash như minus số.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[86, 79]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không bỏ khoảng trắng hoặc thay dấu “–” thành “-” để làm vừa.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr43"></a>
### NR43 — Mã hồ sơ có số 0 đầu trong cột định danh
**Nhóm:** C — Số, ngày và giá trị thiếu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Mã hồ sơ | Nội dung |
| --- | --- |
| 00012 | Đăng ký kiểm tra |
| 00103 | Bàn giao hồ sơ |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Chuỗi 00012 không phải số 12; giữ leading zero.
**Thuộc tính cần phân tích:** `w:t,w:pPr/w:jc,w:tcW`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Căn giữa hoặc trái mã nhất quán, width theo chuỗi dài nhất, cột nội dung căn trái; TNR14.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[56, 109]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không ép sang số, không bỏ các số 0 đầu.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr44"></a>
### NR44 — Số âm và số thập phân âm
**Nhóm:** C — Số, ngày và giá trị thiếu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Chỉ tiêu | Tháng trước | Tháng này |
| --- | --- | --- |
| Chênh lệch | −12,50 | −4,25 |
| Tồn kho | 15,00 | 8,75 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Dấu trừ Unicode U+2212 khác hyphen, dấu phẩy thập phân cần giữ.
**Thuộc tính cần phân tích:** `w:t,w:pPr/w:jc,w:tcW`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Căn phải hai cột số; bảo vệ dấu âm và số chữ số thập phân; TNR14 và không tính width theo độ dài ký tự.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[69, 48, 48]` mm; tổng **165 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không làm tròn, đổi dấu trừ, đổi dấu phẩy thành chấm.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr45"></a>
### NR45 — Dấu phân cách hàng nghìn theo kiểu Việt Nam
**Nhóm:** C — Số, ngày và giá trị thiếu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Khoản mục | Giá trị |
| --- | --- |
| Chi phí vận hành | 1.250.000 |
| Chi phí sửa chữa | 85.000 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Dấu chấm là phân cách nghìn theo dữ liệu nguồn, không phải dấu thập phân.
**Thuộc tính cần phân tích:** `w:t,w:tcW,w:pPr/w:jc`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Căn phải tiền, giữ chuỗi và đơn vị nguồn, dùng sàn từ giá trị dài nhất cộng padding.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[97, 68]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không thay “1.250.000” bằng “1,250,000”.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr46"></a>
### NR46 — Tỷ lệ phần trăm với độ chính xác không đồng đều
**Nhóm:** C — Số, ngày và giá trị thiếu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Kỳ | Tỷ lệ hoàn thành |
| --- | --- |
| Quý I | 95,0% |
| Quý II | 95,25% |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Hai giá trị khác số chữ số thập phân là dữ liệu nguồn.
**Thuộc tính cần phân tích:** `w:t,w:pPr,w:tblGrid`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Căn phải phần trăm, không tự đồng nhất precision; header đậm TNR14.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[78, 87]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không tự thêm số 0 vào 95,0% hoặc làm tròn 95,25%.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr47"></a>
### NR47 — Giá trị khoảng và bất đẳng thức
**Nhóm:** C — Số, ngày và giá trị thiếu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `VERIFY_COMPLIANCE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Tiêu chí | Giá trị yêu cầu |
| --- | --- |
| Chiều dài | ≥ 10 m |
| Thời gian | 5–7 phút |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Dấu ≥ và en dash tạo ngữ nghĩa ngưỡng/khoảng.
**Thuộc tính cần phân tích:** `w:t,w:tcW,w:rFonts`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Căn phải giá trị, bảo vệ cụm 5–7 và đơn vị liên quan; width tính cả ký hiệu.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[94, 71]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không chuyển “5–7” thành “6” hoặc “≥10” thành “10”.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr48"></a>
### NR48 — Đơn vị tính nằm ở cột riêng
**Nhóm:** C — Số, ngày và giá trị thiếu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Chỉ tiêu | Số lượng | Đơn vị |
| --- | --- | --- |
| Tàu ra vào | 205 | lượt |
| Quãng đường | 15,5 | hải lý |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Cột đơn vị phải gắn ngữ nghĩa với cột số nhưng không có quyền hợp nhất.
**Thuộc tính cần phân tích:** `w:tblGrid,w:tcW,w:jc`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Căn phải số, căn trái hoặc giữa đơn vị nhất quán; chiều rộng đơn vị tính theo token dài nhất, không cấp phần lớn diện tích.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[71, 48, 46]` mm; tổng **165 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không chuyển “hải lý” vào ô số hoặc tự đổi sang km.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr49"></a>
### NR49 — Giá trị tiền lớn có ký hiệu đồng
**Nhóm:** C — Số, ngày và giá trị thiếu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Nội dung | Kinh phí |
| --- | --- |
| Nâng cấp hệ thống | 2.500.000.000 đ |
| Bảo trì | 350.000.000 đ |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Ký hiệu “đ” là đơn vị và có thể xuống dòng nếu không có token protection.
**Thuộc tính cần phân tích:** `w:t,w:tcW,w:tcFitText`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Căn phải giá trị tiền, ưu tiên đủ chỗ cho cụm số và đơn vị; giữ chữ TNR14, không co ngang ký tự.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[72, 93]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không thu gọn thành “2,5 tỷ” khi nhiệm vụ chỉ là định dạng.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr50"></a>
### NR50 — Ngày tháng mơ hồ nếu diễn giải theo locale
**Nhóm:** C — Số, ngày và giá trị thiếu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `TRACK_DEADLINE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Sự kiện | Ngày |
| --- | --- |
| Nhận hồ sơ | 02/03/2026 |
| Ký biên bản | 03/04/2026 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Không có quyền suy ngày/tháng từ chuỗi gốc nếu thiếu profile.
**Thuộc tính cần phân tích:** `w:t,w:pPr/w:jc`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Căn giữa cột ngày, giữ nguyên text; nếu AI cần hiểu chronology phải yêu cầu context trước.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[102, 63]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không âm thầm chuyển ngày thành chuẩn ISO hoặc đảo tháng/ngày.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr51"></a>
### NR51 — Ký hiệu kỳ báo cáo không phải ngày cụ thể
**Nhóm:** C — Số, ngày và giá trị thiếu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Kỳ | Số hồ sơ |
| --- | --- |
| Quý IV/2025 | 128 |
| Quý I/2026 | 135 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** “Quý IV/2025” là nhãn kỳ, không phải ngày 01/04.
**Thuộc tính cần phân tích:** `w:t,w:tcW,w:pPr/w:jc`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Căn trái kỳ, phải số, không đưa bộ phân tích ngày vào để đổi chuỗi.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[89, 76]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không chuyển quý thành tháng hoặc lịch ngày.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr52"></a>
### NR52 — Ô trống, dấu gạch và chữ N/A khác số 0
**Nhóm:** C — Số, ngày và giá trị thiếu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Chỉ tiêu | Năm 2025 | Năm 2026 |
| --- | --- | --- |
| Sự cố | 0 | — |
| Thiếu hồ sơ | N/A |  |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** 0, —, N/A và ô trống là bốn trạng thái riêng.
**Thuộc tính cần phân tích:** `w:t,w:tc,w:pPr/w:jc`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Căn số bên phải, mã thiếu dữ liệu giữ nguyên vị trí/căn theo dữ liệu, không tạo giá trị để tính width.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[85, 40, 40]` mm; tổng **165 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không thay tất cả dữ liệu thiếu bằng 0 hoặc tự tạo nhãn.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr53"></a>
### NR53 — Tổng cộng có số 0 hợp lệ và ô chưa có kết quả
**Nhóm:** C — Số, ngày và giá trị thiếu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `SUMMARY`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Loại hồ sơ | Đã giải quyết | Chưa giải quyết |
| --- | --- | --- |
| Nhóm A | 0 | 12 |
| Nhóm B | 10 |  |
| Tổng cộng | 10 | 12 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Có ô trống ở hàng B nhưng hàng tổng đã được cung cấp.
**Thuộc tính cần phân tích:** `w:t,w:rPr/w:b,w:tc`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Giữ nguyên số tổng do nguồn ghi, có thể bôi đậm hàng tổng; không dùng suy luận phép tính để điền ô trống.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[85, 40, 40]` mm; tổng **165 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không coi ô B trống là 0 rồi tuyên bố tổng đã kiểm chứng.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr54"></a>
### NR54 — Chỉ số kèm chú thích dạng ký hiệu tham chiếu
**Nhóm:** C — Số, ngày và giá trị thiếu. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `SUMMARY`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Chỉ tiêu | Giá trị |
| --- | --- |
| Số lượng ca¹ | 28 |
| Số lượt tàu² | 135 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Ký hiệu ¹/² là phần nhãn hoặc footnote marker, không phải số lượng.
**Thuộc tính cần phân tích:** `w:t,w:footnoteReference,w:vertAlign`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Giữ marker nguyên vẹn, đo cả ký hiệu ở header/ô; căn phải giá trị, không tự tạo footnote nội dung.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[112, 53]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không bỏ ký hiệu ¹ vì cho là trang trí hoặc sửa giá trị.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr55"></a>
### NR55 — Bảng hai cột ngắn không cần kéo hết trang
**Nhóm:** D — Hình học và chiều rộng. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `SUMMARY`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Mục | Trạng thái |
| --- | --- |
| Hồ sơ | Đạt |
| Thiết bị | Đạt |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm; bảng inline; bảng hiện rộng 105 mm. **Dấu hiệu quyết định:** Đủ chỗ ở bảng 105 mm dù vùng chữ 165 mm.
**Thuộc tính cần phân tích:** `w:tblW,w:tblGrid,w:tblInd`.

**C. Kết quả kỳ vọng — `KEEP_EXISTING`:** Giữ bảng hẹp hơn vùng chữ nếu căn đặt theo mẫu hợp lệ, cột không bị nén; chọn widths 55+50 mm chỉ là minh họa.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[55, 50]` mm; tổng **105 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không cưỡng ép sum(width)=165 mm để lấp khoảng trắng.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `GEOMETRY_DECLARED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr56"></a>
### NR56 — Bảng tám cột trong section ngang đã cho phép
**Nhóm:** D — Hình học và chiều rộng. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Kỳ | Chỉ tiêu | A | B | C | D | E | Tổng |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T1 | Hồ sơ | 12 | 13 | 14 | 10 | 12 | 61 |
| T2 | Hồ sơ | 15 | 16 | 12 | 11 | 15 | 69 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 ngang; chiều ngang 297 mm, lề trái/phải 30/15 mm; W_allow=252 mm (giả lập). **Dấu hiệu quyết định:** Bảng đã ở A4 ngang, W cho phép phải lấy từ section hiện tại.
**Thuộc tính cần phân tích:** `w:sectPr,w:pgSz,w:pgMar,w:tblGrid`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Sử dụng TNR13 khi profile cho phép; cột chỉ tiêu rộng hơn cột số, không tự xoay section.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 13 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[34, 59, 26, 26, 26, 26, 26, 29]` mm; tổng **252 mm** (8 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không tính W theo A4 dọc 165 mm khi section đã ngang.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr57"></a>
### NR57 — Bảng trong section khổ A5
**Nhóm:** D — Hình học và chiều rộng. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `SUMMARY`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Nhóm | Số lượng | Ghi chú |
| --- | --- | --- |
| A | 10 | Đã hoàn thành |
| B | 8 | Đang thực hiện |

**B. Ngữ cảnh/OOXML đầu vào:** A5 dọc 148 mm; lề trái 30, phải 15 mm; W_allow=103 mm. **Dấu hiệu quyết định:** A5 dọc có vùng chữ nhỏ, không được dùng kích thước A4.
**Thuộc tính cần phân tích:** `w:pgSz,w:pgMar,w:tblW`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Đánh giá khả thi tại W 103 mm trước; nếu không đủ để giữ token TNR14, đề xuất review thay vì hạ font.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[32, 29, 42]` mm; tổng **103 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không sao chép vector 165 mm của bảng A4.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr58"></a>
### NR58 — Bảng nằm trong mục đánh số có thụt lề
**Nhóm:** D — Hình học và chiều rộng. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `ACTION`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Việc | Người thực hiện |
| --- | --- |
| Kiểm tra tài liệu | Tổ Nghiệp vụ |
| Bàn giao thiết bị | Tổ Kỹ thuật |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; page text width=165 mm; table indentation thực=10 mm; W_allow=155 mm. **Dấu hiệu quyết định:** Table indent cộng vùng đặt trong đoạn danh sách có thể giảm bề rộng.
**Thuộc tính cần phân tích:** `w:tblInd,w:tblW,w:sectPr`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Xác minh table indent và vùng chứa thực; trước khi cấp width phải trừ phần bị chiếm dụng.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[89, 66]` mm; tổng **155 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không dùng trang trừ lề là đủ nếu bảng còn có table indentation.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr59"></a>
### NR59 — Lề đối xứng và gáy tài liệu
**Nhóm:** D — Hình học và chiều rộng. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `ACTION`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Nội dung | Người phụ trách |
| --- | --- |
| Kiểm tra | Phòng Kỹ thuật |
| Bàn giao | Phòng Điều độ |

**B. Ngữ cảnh/OOXML đầu vào:** A4; mirrorMargins + gutter bật; chưa xác định vị trí trang/chiều dư. **Dấu hiệu quyết định:** Mirror margins/gutter làm vùng khả dụng theo mặt trang khác nhau.
**Thuộc tính cần phân tích:** `w:mirrorMargins,w:gutter,w:pgMar`.

**C. Kết quả kỳ vọng — `REVIEW_REQUIRED`:** Khai báo print-side/gutter, chỉ chọn vector nếu xác định được W trên trang chứa bảng.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không mặc định trang lẻ và trang chẵn cùng tọa độ mép dù vùng W có thể giống nhau.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `GEOMETRY_UNKNOWN`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr60"></a>
### NR60 — Bảng trong section bố cục hai cột văn bản
**Nhóm:** D — Hình học và chiều rộng. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `SUMMARY`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Tiêu chí | Kết quả |
| --- | --- |
| An toàn | Đạt |
| Tiến độ | Đạt |

**B. Ngữ cảnh/OOXML đầu vào:** Section 2 cột; width cột hiện tại đã xác minh W_allow=79 mm. **Dấu hiệu quyết định:** Vùng đặt bảng là một cột báo, không phải toàn vùng chữ trang.
**Thuộc tính cần phân tích:** `w:cols,w:sectPr,w:tblGrid`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Chỉ dùng W của text column đã xác minh, giữ TNR14, bảng ít cột phù hợp hơn.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[42, 37]` mm; tổng **79 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không kéo bảng 165 mm xuyên sang cột bên cạnh.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr61"></a>
### NR61 — Độ rộng bảng khai báo theo phần trăm
**Nhóm:** D — Hình học và chiều rộng. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Nội dung | Trạng thái |
| --- | --- |
| Hồ sơ đến | Đã nhận |
| Hồ sơ đi | Đã gửi |

**B. Ngữ cảnh/OOXML đầu vào:** A4 text extent W=165 mm; w:tblW 4000 pct = 80% -> width 132 mm giả định. **Dấu hiệu quyết định:** w:tblW kiểu pct không phải đơn vị twips.
**Thuộc tính cần phân tích:** `w:tblW/@w:type=pct,w:tblGrid,w:pgMar`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Giải mã pct tương ứng 1/50 phần trăm; tính theo text extents đúng section và cross-check grid.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[78, 54]` mm; tổng **132 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không lấy w:w=5000 làm 5000 twips.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S3](#nguon-s3), [S1](#nguon-s1).

---

<a id="case-nr62"></a>
### NR62 — Khai báo tcW xung đột với tblGrid
**Nhóm:** D — Hình học và chiều rộng. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Mã | Diễn giải |
| --- | --- |
| A01 | Kết quả kiểm tra |
| A02 | Hồ sơ kỹ thuật |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc W_allow=165 mm; grid sum=165 mm, tcW sum=180 mm (giả lập xung đột). **Dấu hiệu quyết định:** tcW tổng 180 mm nhưng tblGrid tổng 165 mm trên cùng bảng.
**Thuộc tính cần phân tích:** `w:tcW,w:tblGrid,w:tblLayout`.

**C. Kết quả kỳ vọng — `REVIEW_REQUIRED`:** Đánh dấu WIDTH_CONFLICT, không tin một nguồn width duy nhất; đưa cả hai vào bản ghi cấu trúc để review.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không âm thầm sửa grid theo tcW chỉ vì số dễ cộng.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `GEOMETRY_CONFLICT`. **Truy vết nguồn:** [S3](#nguon-s3), [S1](#nguon-s1).

---

<a id="case-nr63"></a>
### NR63 — Fixed layout và AutoFit cùng bộ giá trị
**Nhóm:** D — Hình học và chiều rộng. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Chỉ tiêu | Giá trị |
| --- | --- |
| Hồ sơ | 128 |
| Yêu cầu | 35 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Hai bảng có cùng tcW nhưng tblLayout khác nhau không nhất thiết cùng cách dàn.
**Thuộc tính cần phân tích:** `w:tblLayout,w:tcW,w:tblGrid`.

**C. Kết quả kỳ vọng — `KEEP_EXISTING`:** Khi đề xuất width, ghi nhận layout mode gốc và tôn trọng mode có chủ đích; so cấu trúc, không suy hai kết quả hiển thị giống.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Vector chiều rộng:** Không ấn định. Giữ nguyên hoặc đánh giá lại baseline theo dữ liệu thực.

**D. Phản ví dụ/điều cấm:** Không đổi autofit→fixed một cách ngầm định để “khóa tỷ lệ”.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `STRUCTURE_ONLY`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr64"></a>
### NR64 — Token không ngắt dài hơn vùng cho phép
**Nhóm:** D — Hình học và chiều rộng. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Mã đối tượng | Nội dung |
| --- | --- |
| KT2026LONGIDNOSEPARATORS0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ | Tài liệu kiểm thử |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc W_allow=165 mm, hard_floor đã xác minh bằng metrics TNR14=175 mm (giá trị giả lập điều kiện). **Dấu hiệu quyết định:** Hợp đồng đầu vào xác nhận hard floor token cùng padding =175 mm > W=165 mm.
**Thuộc tính cần phân tích:** `w:t,w:rFonts,w:tcW,w:pgMar,w:noWrap,w:growAutofit`.

**C. Kết quả kỳ vọng — `NO_SAFE_FIT`:** Kết luận hệ ràng buộc không có nghiệm inline với TNR14 tại width hiện tại; gợi ý review cấu trúc hoặc page profile được phép. Nếu growAutofit cho phép bảng vượt mép trong tài liệu, vẫn không coi đó là nghiệm hợp lệ trong W_allow đã yêu cầu.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Vector chiều rộng:** Không ấn định. Giữ nguyên hoặc đánh giá lại baseline theo dữ liệu thực.

**D. Phản ví dụ/điều cấm:** Không giảm font dưới 13 hoặc thêm ký tự xuống dòng vào mã.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `HARD_FLOOR_ASSUMED_FOR_CASE`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2), [S10](#nguon-s10), [S11](#nguon-s11).

---

<a id="case-nr65"></a>
### NR65 — Bảng sát mép vùng chữ không có dự phòng
**Nhóm:** D — Hình học và chiều rộng. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `SUMMARY`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Nhóm | Mô tả | Giá trị |
| --- | --- | --- |
| A | Rà soát biên bản | 35 |
| B | Lập kế hoạch | 24 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc W_allow=165 mm; baseline tổng cột=164,5 mm; ngưỡng dự phòng chưa được duyệt. **Dấu hiệu quyết định:** Width 164,5/165 mm để lại 0,5 mm trong mô hình inline.
**Thuộc tính cần phân tích:** `w:tblGrid,w:tblInd,w:pgMar`.

**C. Kết quả kỳ vọng — `REVIEW_REQUIRED`:** Giữ hoặc đề xuất co nhẹ nếu geometry và margin policy đòi dự phòng; phân loại “sát lề”, chưa coi là lỗi tràn.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không tuyên bố bảng chắc chắn chạm vùng in hoặc dùng ngưỡng 2mm là luật.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `BORDERLINE_GEOMETRY`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr66"></a>
### NR66 — Bảng lồng có chiều rộng ô mẹ xác định
**Nhóm:** D — Hình học và chiều rộng. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `SUMMARY`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Hạng mục | Số |
| --- | --- |
| Kiểm tra hồ sơ | 12 |
| Rà soát văn bản | 5 |

**B. Ngữ cảnh/OOXML đầu vào:** Bảng lồng; ô mẹ 115 mm; padding nội bộ 2 mm mỗi bên; W_allow=111 mm (giả lập rõ). **Dấu hiệu quyết định:** Bảng con thuộc ô mẹ rộng 115 mm, padding hai bên 2 mm.
**Thuộc tính cần phân tích:** `w:tcMar,w:tblGrid,w:tcW,w:tbl`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Dùng width nội bộ 111 mm sau khi xét padding của ô mẹ; TNR14; không lấy page width làm W.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[75, 36]` mm; tổng **111 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không kéo bảng con ra ngoài ô mẹ hoặc cộng padding hai lần.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S3](#nguon-s3).

---

<a id="case-nr67"></a>
### NR67 — Tiêu đề gộp ngang hai cột con
**Nhóm:** E — Ô gộp và phân trang. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Chỉ tiêu | Kết quả thực hiện [gộp 2 cột] | [thuộc ô gộp trước] |
| --- | --- | --- |
| [ô thuộc header] | Quý I | Quý II |
| Hồ sơ hoàn tất | 35 | 40 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Header row 1 có gridSpan=2 ở tiêu đề “Kết quả thực hiện”; không có ô thứ tư.
**Thuộc tính cần phân tích:** `w:gridSpan,w:tblGrid,w:tblHeader`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Giải ràng buộc width cho toàn interval cột 2–3, giữ header hai tầng và lặp đủ hai hàng đầu khi hợp lệ.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[69, 48, 48]` mm; tổng **165 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không nhân bản chữ tiêu đề vào hai ô con khi đo width.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S4](#nguon-s4), [S5](#nguon-s5).

---

<a id="case-nr68"></a>
### NR68 — Tên nhóm gộp dọc ba hàng
**Nhóm:** E — Ô gộp và phân trang. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `SUMMARY`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Nhóm | Chỉ tiêu | Giá trị |
| --- | --- | --- |
| A [gộp dọc] | Tổng hồ sơ | 26 |
| [tiếp ô gộp] | Hoàn thành | 24 |
| [tiếp ô gộp] | Đang xử lý | 2 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** w:vMerge restart/continue cùng grid interval cho cột Nhóm.
**Thuộc tính cần phân tích:** `w:vMerge,w:gridSpan,w:tr`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Bảo toàn merge chain, không tính tên nhóm thành ô mới ở mỗi hàng; 14 pt và căn dọc nhóm theo mẫu.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[34, 84, 47]` mm; tổng **165 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không tách ô nhóm thành ba “A” hoặc mất một hàng logic.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S5](#nguon-s5), [S1](#nguon-s1).

---

<a id="case-nr69"></a>
### NR69 — Hàng dữ liệu bỏ ô lưới đầu tiên
**Nhóm:** E — Ô gộp và phân trang. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| [gridBefore 1] | Chỉ tiêu | Kết quả |
| --- | --- | --- |
| [gridBefore 1] | Thực hiện | Đạt |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** gridBefore làm hàng chỉ có hai cell thực chiếm grid interval 2–3.
**Thuộc tính cần phân tích:** `w:gridBefore,w:trPr,w:tblGrid`.

**C. Kết quả kỳ vọng — `REVIEW_REQUIRED`:** Xây dựng bản đồ lưới theo offset, không dịch ô Chỉ tiêu sang cột 1; review nếu đây là biểu mẫu có chủ đích.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không tự thêm một ô vật lý đầu hàng để lấp khuyết.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TOPOLOGY_SPECIAL`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr70"></a>
### NR70 — Hàng bỏ ô lưới cuối theo gridAfter
**Nhóm:** E — Ô gộp và phân trang. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| STT | Mục | [gridAfter 1] |
| --- | --- | --- |
| 1 | Kiểm tra | [gridAfter 1] |
| 2 | Tổng hợp | [gridAfter 1] |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Hàng có gridAfter nhưng không có cell thật ở grid thứ ba.
**Thuộc tính cần phân tích:** `w:gridAfter,w:tblGrid,w:tc`.

**C. Kết quả kỳ vọng — `REVIEW_REQUIRED`:** Bảo vệ thứ tự cột thực; coi gridAfter là topology, không như ô trống có thể tô màu.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không kéo nội dung “Mục” thành ba cột và không thêm dữ liệu giả.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TOPOLOGY_SPECIAL`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr71"></a>
### NR71 — Bảng dài có hai hàng tiêu đề liên tiếp
**Nhóm:** E — Ô gộp và phân trang. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Báo cáo kiểm tra | [gộp theo mẫu] | [gộp theo mẫu] |
| --- | --- | --- |
| STT | Nội dung | Kết quả |
| 1 | Hồ sơ | Đạt |
| 2 | Thiết bị | Đạt |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Hai hàng đầu dùng làm header trong cùng bảng, không có manual page break.
**Thuộc tính cần phân tích:** `w:tblHeader,w:trPr,w:gridSpan`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Đề xuất tblHeader cho chuỗi hàng 1–2 nếu đây là header thật; giữ 14 pt và topology gộp.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[28, 93, 44]` mm; tổng **165 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không đánh dấu chỉ hàng thứ hai là header lặp.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S4](#nguon-s4), [S1](#nguon-s1).

---

<a id="case-nr72"></a>
### NR72 — Dòng tiêu đề phụ ở giữa bảng
**Nhóm:** E — Ô gộp và phân trang. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `SUMMARY`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| STT | Nội dung | Giá trị |
| --- | --- | --- |
| 1 | Nhóm A | 10 |
| [tiêu đề phụ] | Nhóm B |  |
| 2 | Hạng mục B | 20 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Hàng “Nhóm B” xuất hiện giữa bảng, không liên tiếp từ đầu.
**Thuộc tính cần phân tích:** `w:tblHeader,w:trPr,w:tblGrid`.

**C. Kết quả kỳ vọng — `KEEP_EXISTING`:** Giữ là hàng nhóm có nhấn mạnh nếu mẫu cho phép, nhưng không kỳ vọng tblHeader riêng hàng này tạo lặp trang.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Vector chiều rộng:** Không ấn định. Giữ nguyên hoặc đánh giá lại baseline theo dữ liệu thực.

**D. Phản ví dụ/điều cấm:** Không thiết lập tblHeader=true ở dòng giữa rồi báo header lặp PASS.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S4](#nguon-s4), [S1](#nguon-s1).

---

<a id="case-nr73"></a>
### NR73 — Ngắt trang thủ công nằm trong bảng dài
**Nhóm:** E — Ô gộp và phân trang. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| STT | Nội dung |
| --- | --- |
| 1 | Phần đầu |
| [pageBreak] | Chuyển trang thủ công |
| 2 | Phần tiếp |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** w:br type=page hoặc break trước đoạn giữa bảng.
**Thuộc tính cần phân tích:** `w:br,w:tblHeader,w:pPr/w:pageBreakBefore`.

**C. Kết quả kỳ vọng — `REVIEW_REQUIRED`:** Ghi giới hạn của lặp header khi có manual break; giữ nội dung, cảnh báo nếu kỳ vọng header lặp trang.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không khẳng định tblHeader bảo đảm lặp trên trang sau manual break.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `PAGINATION_UNKNOWN`. **Truy vết nguồn:** [S4](#nguon-s4), [S13](#nguon-s13).

---

<a id="case-nr74"></a>
### NR74 — Hàng có đoạn diễn giải vượt chiều cao một trang
**Nhóm:** E — Ô gộp và phân trang. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `SUMMARY`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Hạng mục | Diễn giải |
| --- | --- |
| Đánh giá tổng thể | Đoạn diễn giải rất dài được tạo bởi nhiều mục và nhiều phần phụ lục trong cùng ô |
| Phân tích rủi ro | Nội dung nhiều đoạn theo mẫu |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Dữ liệu nguồn mô tả row cao hơn khả năng một trang (chưa render).
**Thuộc tính cần phân tích:** `w:cantSplit,w:trHeight,w:pPr`.

**C. Kết quả kỳ vọng — `REVIEW_REQUIRED`:** Không bật cantSplit đồng loạt; ước lượng nguy cơ đẩy hàng và tư vấn chia đoạn nội dung theo thẩm quyền.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không đánh giá cứ cantSplit=true là hàng dài được giữ trọn một trang.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `ROW_HEIGHT_ESTIMATE`. **Truy vết nguồn:** [S7](#nguon-s7), [S1](#nguon-s1).

---

<a id="case-nr75"></a>
### NR75 — Chiều cao Exactly nhỏ hơn một dòng 14 pt
**Nhóm:** E — Ô gộp và phân trang. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Mục | Diễn giải |
| --- | --- |
| A | Nội dung một dòng |
| B | Nội dung hai dòng nếu cột hẹp |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** w:trHeight val=160 twips exact = 8pt, thấp hơn size 14pt (chưa kể line box).
**Thuộc tính cần phân tích:** `w:trHeight/@w:val,w:trHeight/@w:hRule,w:sz`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Gắn ROW_HEIGHT_RISK từ phép so số học, đề xuất auto/atLeast khi không bị khóa; không tuyên bố đã thấy clipping.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[42, 123]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không dùng exact 8pt để ép bảng ít trang.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S7](#nguon-s7), [S1](#nguon-s1).

---

<a id="case-nr76"></a>
### NR76 — AtLeast cao có chủ đích để người dùng ghi tay
**Nhóm:** E — Ô gộp và phân trang. **Vai trò bảng:** `OFFICIAL_FORM`. **Tác vụ đọc:** `FILL_FORM`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Mục | Nội dung xác nhận |
| --- | --- |
| 01 | [vùng trống để điền] |
| 02 | [vùng trống để điền] |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** trHeight atLeast=850 twips ở các hàng điền tay; biểu mẫu do đơn vị phê duyệt.
**Thuộc tính cần phân tích:** `w:trHeight,w:trPr,w:tc`.

**C. Kết quả kỳ vọng — `PRESERVE`:** Giữ nguyên chiều cao và khoảng trống, không tối ưu như bảng dữ liệu ngắn.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** PRESERVE: không áp preset, không can thiệp cấu trúc/kiểu chữ của vùng không thuộc bảng nội dung.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không giảm atLeast vì thấy hàng nhiều khoảng trắng.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `FORM_LOCK`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr77"></a>
### NR77 — Caption ngay trước bảng có keepNext
**Nhóm:** E — Ô gộp và phân trang. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `SUMMARY`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Chỉ tiêu | Giá trị |
| --- | --- |
| Hồ sơ | 25 |
| Biên bản | 10 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Đoạn caption bên ngoài bảng có keepNext=true.
**Thuộc tính cần phân tích:** `w:pPr/w:keepNext,w:tbl,w:tr`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Giữ liên kết caption–bảng trong kế hoạch bố cục; không tự thêm caption vào một hàng gộp để dễ tính height.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[103, 62]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không xóa keepNext hoặc tự tạo caption khi chưa được yêu cầu.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr78"></a>
### NR78 — Hai bảng liền nhau cùng Table Style
**Nhóm:** E — Ô gộp và phân trang. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Bảng A: Chỉ tiêu | Giá trị |
| --- | --- |
| A | 1 |
| Bảng B: Chỉ tiêu | Giá trị |
| B | 2 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Hai w:tbl kế nhau không có w:p phân cách và có cùng style.
**Thuộc tính cần phân tích:** `w:tbl,w:tblStyle,w:p`.

**C. Kết quả kỳ vọng — `REVIEW_REQUIRED`:** Xác minh WordprocessingML xem có cần coi như một chuỗi table liên tiếp; hạn chế thay đổi toàn style và review việc phân loại.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không giả định hai bảng luôn độc lập chỉ vì XML có hai phần tử tbl.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S8](#nguon-s8), [S1](#nguon-s1).

---

<a id="case-nr79"></a>
### NR79 — Viền cấp ô ghi đè viền cấp bảng
**Nhóm:** F — Style và đường viền. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Chỉ tiêu | Giá trị |
| --- | --- |
| Hồ sơ | 20 |
| Biên bản | 15 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** tblBorders insideH single 0,5pt nhưng tcBorders hàng 2 đặt nét khác.
**Thuộc tính cần phân tích:** `w:tblBorders,w:tcBorders,w:tblPrEx`.

**C. Kết quả kỳ vọng — `REVIEW_REQUIRED`:** Giải thứ tự ưu tiên border theo style và override; chỉ đề xuất style cục bộ khi không gây xung đột mới.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không đặt lại toàn bộ viền mỗi ô mà bỏ qua cạnh giáp nhau.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S9](#nguon-s9), [S1](#nguon-s1).

---

<a id="case-nr80"></a>
### NR80 — Đơn vị độ dày viền bằng phần tám điểm
**Nhóm:** F — Style và đường viền. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Mã | Giá trị |
| --- | --- |
| A | 10 |
| B | 20 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Trong OOXML w:sz=4 tương ứng viền 0,5pt, w:sz=6 =0,75pt.
**Thuộc tính cần phân tích:** `w:tblBorders/@w:sz,w:tcBorders`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Ghi rõ phép đổi đơn vị khi lập bảng thông số thẩm mỹ; đừng nhầm w:sz với twips.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[71, 94]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không đặt w:sz=10 rồi diễn giải là 0,5pt.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S9](#nguon-s9).

---

<a id="case-nr81"></a>
### NR81 — Nền ô báo trạng thái có ngữ nghĩa
**Nhóm:** F — Style và đường viền. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `ACTION`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Công việc | Trạng thái |
| --- | --- |
| Kiểm tra | Đạt |
| Bổ sung | Cần xử lý |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Tô nền vàng/đỏ trong source đã được dùng để phân biệt hành động.
**Thuộc tính cần phân tích:** `w:shd,w:tblLook,w:t`.

**C. Kết quả kỳ vọng — `PRESERVE`:** Bảo toàn shading mang thông tin; bổ sung diễn giải bằng chữ nếu người dùng được quyền sửa nội dung, ngoài phạm vi format-only.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** PRESERVE: không áp preset, không can thiệp cấu trúc/kiểu chữ của vùng không thuộc bảng nội dung.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không xóa hết nền để đạt phong cách đơn sắc hoặc chỉ dựa vào màu thay cho text.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S6](#nguon-s6), [S1](#nguon-s1).

---

<a id="case-nr82"></a>
### NR82 — Banding xen kẽ do Table Style
**Nhóm:** F — Style và đường viền. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| STT | Hạng mục | Tình trạng |
| --- | --- | --- |
| 1 | Hồ sơ | Đạt |
| 2 | Thiết bị | Đạt |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** tblLook cho phép band1Horz, nhưng tô nền có thể đến từ style conditional.
**Thuộc tính cần phân tích:** `w:tblLook,w:tblStylePr,w:shd`.

**C. Kết quả kỳ vọng — `KEEP_EXISTING`:** Khi nguồn đã có banding ổn định, đọc style cascade trước; không tự thêm màu xen kẽ mới.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Vector chiều rộng:** Không ấn định. Giữ nguyên hoặc đánh giá lại baseline theo dữ liệu thực.

**D. Phản ví dụ/điều cấm:** Không báo bảng chưa tô từng ô trực tiếp là “không có shading”.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S9](#nguon-s9), [S1](#nguon-s1).

---

<a id="case-nr83"></a>
### NR83 — FirstRow table style không tương đương header lặp
**Nhóm:** F — Style và đường viền. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Cột A | Cột B |
| --- | --- |
| Dữ liệu 1 | 20 |
| Dữ liệu 2 | 30 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** tblLook firstRow=1 làm style header, không có nghĩa trPr/tblHeader đã bật.
**Thuộc tính cần phân tích:** `w:tblLook,w:tblHeader,w:tblStylePr`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Tách quyết định phân cấp thị giác và lặp header qua trang; nếu cần lặp thì thêm quy tắc riêng khi hợp lệ.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[105, 60]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không báo repeated header PASS chỉ vì firstRow định dạng đậm.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S4](#nguon-s4), [S9](#nguon-s9).

---

<a id="case-nr84"></a>
### NR84 — Cell spacing gây khe giữa các đường kẻ
**Nhóm:** F — Style và đường viền. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Mục | Kết quả |
| --- | --- |
| A | Đạt |
| B | Chưa hoàn thành |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** tblCellSpacing khác 0 làm border tách rời dù preset muốn grid liền.
**Thuộc tính cần phân tích:** `w:tblCellSpacing,w:tblBorders,w:tcBorders`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Nếu không có mẫu khóa, đề xuất spacing=0mm cho Formal Grid; cần xét border conflicts trước.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[74, 91]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không vẽ thêm border đôi ở từng cell để vá khe do spacing.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr85"></a>
### NR85 — Bảng thống kê chỉ dùng đường ngang
**Nhóm:** F — Style và đường viền. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Năm | Số hồ sơ | Tỷ lệ |
| --- | --- | --- |
| 2024 | 128 | 96,0% |
| 2025 | 135 | 97,0% |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Dữ liệu số độc lập, header rõ, không có biểu mẫu phải giữ viền dọc.
**Thuộc tính cần phân tích:** `w:tblBorders,w:tcBorders,w:pPr/w:jc`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Chọn Statistical Minimal, ưu tiên đường dưới header/tổng; căn phải số; không bắt buộc viền mọi ô.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[53, 56, 56]` mm; tổng **165 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không biến preset nhẹ thành thiếu cấu trúc header hoặc mất nhóm số.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S6](#nguon-s6), [S1](#nguon-s1).

---

<a id="case-nr86"></a>
### NR86 — Hàng tổng cần nhấn đường trên thay vì tô màu
**Nhóm:** F — Style và đường viền. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `SUMMARY`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Khoản | Số hồ sơ |
| --- | --- |
| Nhóm A | 15 |
| Nhóm B | 25 |
| Tổng cộng | 40 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Hàng cuối là tổng đã được cung cấp, cần phân biệt từ dữ liệu nguồn.
**Thuộc tính cần phân tích:** `w:rPr/w:b,w:tcBorders/w:top,w:t`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Giữ nền trắng, đậm TNR14 ở hàng tổng và đường phân cách trên 0,5pt có điều kiện.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[105, 60]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không thêm tổng mới, không đổi số 40, không dùng quá nhiều màu để tạo nhấn.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr87"></a>
### NR87 — Hàng nhóm có đường kẻ phân cấp
**Nhóm:** F — Style và đường viền. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Nhóm | Mục | Số |
| --- | --- | --- |
| A | Hồ sơ | 12 |
| A | Biên bản | 5 |
| B | Hồ sơ | 10 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Nhóm A/B phân biệt bằng tên nhóm và trình tự nguồn.
**Thuộc tính cần phân tích:** `w:tcBorders,w:tr,w:tblGrid`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Nếu bảng cho phép, dùng đường trên tại điểm chuyển nhóm nhẹ hơn border ngoài; không gộp ô làm biến đổi topology.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[36, 85, 44]` mm; tổng **165 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không tự gộp các ô “A” hoặc phân nhóm lại bằng thứ tự mới.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr88"></a>
### NR88 — Gridlines trong Word không phải đường viền in
**Nhóm:** F — Style và đường viền. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `VERIFY_COMPLIANCE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Tiêu chí | Đánh giá |
| --- | --- |
| Hồ sơ | Đạt |
| Thiết bị | Chưa rõ |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** tblBorders không có nhưng người soạn nhìn thấy View Gridlines.
**Thuộc tính cần phân tích:** `w:tblBorders,w:tcBorders,w:tblStyle`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Không suy đường lưới editing là viền thật; nếu bảng nội dung cần viền, đề xuất local borders theo preset nhưng ghi chưa kiểm chứng bản in.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[91, 74]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không khẳng định bảng đã có viền vì Word hiển thị lưới khi chỉnh sửa.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S9](#nguon-s9).

---

<a id="case-nr89"></a>
### NR89 — Danh sách gạch đầu dòng trong một ô
**Nhóm:** G — Nội dung đặc biệt trong ô. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `ACTION`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Hạng mục | Nội dung yêu cầu |
| --- | --- |
| Chuẩn bị | • Kiểm tra hồ sơ ⏎ • Xác nhận người phụ trách |
| Báo cáo | • Tổng hợp kết quả ⏎ • Lưu biên bản |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Ô có nhiều paragraph/list items, không phải một chuỗi văn bản đơn.
**Thuộc tính cần phân tích:** `w:numPr,w:p,w:pPr,w:tc`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Bảo toàn numbering/bullet, căn trái/top, 14pt; tính chiều cao từ số đoạn và khoảng cách hiệu dụng, không tự thêm khoảng cách lớn.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[47, 118]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không làm phẳng các bullet thành một dòng hoặc xóa marker để giảm hàng.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr90"></a>
### NR90 — Ô hai đoạn có after-spacing khác nhau
**Nhóm:** G — Nội dung đặc biệt trong ô. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `SUMMARY`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Nội dung | Ghi chú |
| --- | --- |
| Kiểm tra | Đoạn 1: Hồ sơ đầy đủ ⏎ Đoạn 2: Chờ ký |
| Tổng hợp | Đoạn 1: Số liệu khớp ⏎ Đoạn 2: Chờ gửi |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Có hai đoạn riêng, paragraph after 8pt từ nguồn.
**Thuộc tính cần phân tích:** `w:pPr/w:spacing,w:p,w:rPr`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Xét pPr/spacing và style cascade; đề xuất after 0–3pt nếu không khóa và vẫn giữ ranh giới đoạn; tính lại rủi ro tăng/giảm chiều cao.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[49, 116]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không xóa một đoạn hoặc chuyển thành line break mà không được phép.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr91"></a>
### NR91 — Ngắt dòng thủ công có chủ đích trong ô
**Nhóm:** G — Nội dung đặc biệt trong ô. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Địa điểm | Đơn vị |
| --- | --- |
| Tầng 2 ⏎ Phòng họp số 1 | Phòng Tổng hợp |
| Tầng 3 ⏎ Phòng họp số 2 | Phòng Nghiệp vụ |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** w:br trong ô mô tả địa điểm là line break do tác giả đặt.
**Thuộc tính cần phân tích:** `w:br,w:r,w:t`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Giữ line break khi định dạng, không coi nó tương đương cơ hội wrap mềm; chiều cao chỉ dự báo.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[85, 80]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không gộp “Tầng 2” và “Phòng họp” thành một dòng vì thấy còn chỗ.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr92"></a>
### NR92 — Đường dẫn hyperlink dài kèm anchor
**Nhóm:** G — Nội dung đặc biệt trong ô. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Nguồn | Liên kết |
| --- | --- |
| Quy trình | https://example.org/ho-so/huong-dan-2026 |
| Văn bản | https://example.org/tai-lieu/tham-khao |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Hyperlink có relationship target và text hiển thị, không chỉ là chuỗi.
**Thuộc tính cần phân tích:** `w:hyperlink,@r:id,word/_rels/document.xml.rels,w:t`.

**C. Kết quả kỳ vọng — `REVIEW_REQUIRED`:** Giữ target/r:id nguyên vẹn; chỉ căn lề/width có điều kiện; nếu URL quá dài không fit thì review.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không tự rút URL, bỏ hyperlink hay thay label vì cho rằng đọc khó.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `LONG_URL_UNMEASURED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr93"></a>
### NR93 — Kết quả là field Word không phải text tĩnh
**Nhóm:** G — Nội dung đặc biệt trong ô. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `SUMMARY`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Hạng mục | Giá trị |
| --- | --- |
| Tổng hồ sơ | { =SUM(ABOVE) } |
| Số trang tham chiếu | { PAGE } |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Giá trị được hiển thị bởi field instruction và có thể cập nhật.
**Thuộc tính cần phân tích:** `w:fldChar,w:instrText,w:fldSimple,w:t`.

**C. Kết quả kỳ vọng — `REVIEW_REQUIRED`:** Bảo toàn fldChar/instrText hoặc fldSimple và kết quả cached; không thay bằng chuỗi tĩnh; ghi WIDTH_ESTIMATE khi chưa biết kết quả cuối.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không sửa công thức hoặc coi cached result là dữ liệu duy nhất.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `DYNAMIC_FIELD`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr94"></a>
### NR94 — Bảng có nội dung đang Track Changes
**Nhóm:** G — Nội dung đặc biệt trong ô. **Vai trò bảng:** `SPECIAL_CONTENT`. **Tác vụ đọc:** `ACTION`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Hạng mục | Trạng thái |
| --- | --- |
| Biên bản | [insert: đã duyệt] |
| Kế hoạch | [delete: bản cũ] [insert: bản mới] |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** w:ins/w:del và tcPrChange có thể thay cách đọc nguồn.
**Thuộc tính cần phân tích:** `w:ins,w:del,w:tcPrChange,w:rPrChange`.

**C. Kết quả kỳ vọng — `PRESERVE`:** Giữ mọi revision, chỉ mô tả ảnh hưởng và yêu cầu duyệt trước khi áp bất cứ can thiệp nào làm đổi markup.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** PRESERVE: không áp preset, không can thiệp cấu trúc/kiểu chữ của vùng không thuộc bảng nội dung.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không tự Accept/Reject Changes hoặc mất revision trong format-only.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `REVISION_PRESENT`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr95"></a>
### NR95 — Content control trong ô có khóa nội dung
**Nhóm:** G — Nội dung đặc biệt trong ô. **Vai trò bảng:** `OFFICIAL_FORM`. **Tác vụ đọc:** `FILL_FORM`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Mã biểu mẫu | Trường nhập |
| --- | --- |
| BM-01 | [SDT: Họ và tên] |
| BM-02 | [SDT: Ngày lập] |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Ô chứa w:sdt với lock và data binding có thể có.
**Thuộc tính cần phân tích:** `w:sdt,w:sdtPr,w:lock,w:dataBinding`.

**C. Kết quả kỳ vọng — `PRESERVE`:** Giữ SDT, mapping và khóa; chỉ xét định dạng ngoài phạm vi kiểm soát khi được ủy quyền.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** PRESERVE: không áp preset, không can thiệp cấu trúc/kiểu chữ của vùng không thuộc bảng nội dung.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không thay content control thành chữ đơn thuần hoặc xóa placeholder.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `CONTENT_CONTROL`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr96"></a>
### NR96 — Placeholder trong ô chưa phải dữ liệu người dùng
**Nhóm:** G — Nội dung đặc biệt trong ô. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `FILL_FORM`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Chỉ tiêu | Thông tin |
| --- | --- |
| Họ tên | [Nhập họ tên] |
| Số văn bản | [Nhập số văn bản] |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Placeholder có thể là văn bản gợi ý hoặc content control, chưa biết quyền sửa.
**Thuộc tính cần phân tích:** `w:sdt,w:showingPlcHdr,w:t`.

**C. Kết quả kỳ vọng — `REVIEW_REQUIRED`:** Phân biệt placeholder và text thật theo OOXML; cảnh báo thiếu dữ liệu, không biến ví dụ thành kết quả định dạng đã hoàn tất.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không thay các chuỗi placeholder bằng tên/cơ quan tự suy luận.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `PLACEHOLDER_UNRESOLVED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr97"></a>
### NR97 — Ô chứa hình vẽ kèm chữ chú thích
**Nhóm:** G — Nội dung đặc biệt trong ô. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Loại thiết bị | Minh họa và ghi chú |
| --- | --- |
| Bộ đàm | [drawing] Bộ đàm dự phòng |
| Phao | [drawing] Phao tròn |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Drawing inline/anchored khiến chiều rộng chịu constraint đối tượng, không chỉ text.
**Thuộc tính cần phân tích:** `w:drawing,a:extents,wp:anchor,r:embed`.

**C. Kết quả kỳ vọng — `REVIEW_REQUIRED`:** Chỉ đề xuất style chữ TNR14 nếu đúng scope; giữ image relationship/crop/anchor; review width nếu ảnh vượt chỗ.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không bỏ hình, nén biến dạng, hoặc coi placeholder [drawing] là văn bản trong DOCX.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `DRAWING_LAYOUT_UNKNOWN`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr98"></a>
### NR98 — Tab stop và dấu xuống dòng mềm trong ô
**Nhóm:** G — Nội dung đặc biệt trong ô. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Mục | Nội dung |
| --- | --- |
| 1 | Hồ sơ	đã nhận |
| 2 | Thiết bị ⏎ đã bàn giao |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Tab và break được mã hóa khác wrap tự động.
**Thuộc tính cần phân tích:** `w:tab,w:tabs,w:br,w:t`.

**C. Kết quả kỳ vọng — `REVIEW_REQUIRED`:** Báo cáo từng token điều khiển; giữ source, chỉ đề xuất căn theo paragraph/tab stops khi quyền cho phép.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không xóa tab và chèn dấu cách tương đương bằng cảm quan.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `SPECIAL_LINE_CONTROL`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr99"></a>
### NR99 — Biểu mẫu chính thức có chỉ định layout riêng
**Nhóm:** H — Quyền sửa và bảo toàn. **Vai trò bảng:** `OFFICIAL_FORM`. **Tác vụ đọc:** `FILL_FORM`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Hạng mục | Xác nhận | Chữ ký |
| --- | --- | --- |
| A | [trống] | [vùng ký] |
| B | [trống] | [vùng ký] |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Mẫu ban hành yêu cầu hình học và vùng ký cố định.
**Thuộc tính cần phân tích:** `w:tblStyle,w:trHeight,w:gridSpan`.

**C. Kết quả kỳ vọng — `PRESERVE`:** PRESERVE; chỉ tạo báo cáo so với phạm vi TNR 13–14, không áp preset nội dung.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** PRESERVE: không áp preset, không can thiệp cấu trúc/kiểu chữ của vùng không thuộc bảng nội dung.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không tự động đổi viền/height/font của biểu mẫu chỉ để đồng bộ bảng thường.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `FORM_LOCK`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr100"></a>
### NR100 — Style bảng nguồn là custom nhưng chưa có mô tả
**Nhóm:** H — Quyền sửa và bảo toàn. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Cột 1 | Cột 2 |
| --- | --- |
| Mã A | Kết quả A |
| Mã B | Kết quả B |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** tblStyle tên “CustomTable9”, không có thông tin về mục đích/ủy quyền.
**Thuộc tính cần phân tích:** `w:tblStyle,word/styles.xml,w:tblLook`.

**C. Kết quả kỳ vọng — `REVIEW_REQUIRED`:** Đọc styles.xml và conditional formatting; thiếu authority thì giữ nguyên cấu trúc, ghi các yếu tố có thể kiểm bằng OOXML.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không đổi sang TableGrid chỉ vì tên style không quen thuộc.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `STYLE_AUTHORITY_UNKNOWN`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr101"></a>
### NR101 — Bảng nằm trong header tài liệu
**Nhóm:** H — Quyền sửa và bảo toàn. **Vai trò bảng:** `LAYOUT_TABLE`. **Tác vụ đọc:** `LAYOUT`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Tên đơn vị | Số trang |
| --- | --- |
| CÔNG TY | [PAGE field] |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Bảng dùng bố trí đầu trang, không phải bảng nội dung.
**Thuộc tính cần phân tích:** `word/header*.xml,w:hdr,w:tbl`.

**C. Kết quả kỳ vọng — `PRESERVE`:** PRESERVE ngoài phạm vi V16, không áp TNR14/padding Formal Grid.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** PRESERVE: không áp preset, không can thiệp cấu trúc/kiểu chữ của vùng không thuộc bảng nội dung.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không coi là bảng dữ liệu vì có hai cột và chữ số.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `OUT_OF_SCOPE`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr102"></a>
### NR102 — Bảng trong footnote tài liệu
**Nhóm:** H — Quyền sửa và bảo toàn. **Vai trò bảng:** `SPECIAL_CONTENT`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Mã | Giải thích |
| --- | --- |
| 1 | Dữ liệu tham khảo |
| 2 | Quy ước đo |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Owner là footnotes.xml, không thuộc body content table tiêu chuẩn của V16.
**Thuộc tính cần phân tích:** `word/footnotes.xml,w:footnote,w:tbl`.

**C. Kết quả kỳ vọng — `PRESERVE`:** Giữ nguyên và báo vị trí, chỉ đề xuất nếu scope rõ ràng cho footnote.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** PRESERVE: không áp preset, không can thiệp cấu trúc/kiểu chữ của vùng không thuộc bảng nội dung.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không áp cỡ 14 lên chú thích chân trang do policy chỉ nói bảng nội dung.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `OUT_OF_SCOPE`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr103"></a>
### NR103 — Comment range và bookmark chạy qua ô
**Nhóm:** H — Quyền sửa và bảo toàn. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `ACTION`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Mã | Nội dung |
| --- | --- |
| A | [bookmarkStart]Cần rà soát[bookmarkEnd] |
| B | Đã đạt |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Bookmark và comment annotations gắn vào các đoạn/ô.
**Thuộc tính cần phân tích:** `w:bookmarkStart,w:bookmarkEnd,w:commentRangeStart,w:commentRangeEnd`.

**C. Kết quả kỳ vọng — `REVIEW_REQUIRED`:** Định dạng chỉ được thay thuộc tính whitelist, giữ nguyên các marker và IDs; nếu không chứng minh bảo toàn thì REVIEW.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không dựng lại toàn bảng làm mất vị trí bookmark/comment.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `ANNOTATION_PRESENT`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr104"></a>
### NR104 — Văn bản DOCX có chữ ký số
**Nhóm:** H — Quyền sửa và bảo toàn. **Vai trò bảng:** `SPECIAL_CONTENT`. **Tác vụ đọc:** `SUMMARY`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Hạng mục | Nội dung |
| --- | --- |
| A | Kết quả |
| B | Biên bản |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Package chứa digital signature parts; sửa XML có thể làm chữ ký mất giá trị.
**Thuộc tính cần phân tích:** `_xmlsignatures/,word/document.xml,OPC relationships`.

**C. Kết quả kỳ vọng — `PRESERVE`:** Bảo toàn nguyên trạng, ghi ràng buộc ký số; không cung cấp lệnh sửa định dạng trên nguồn đã ký.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** PRESERVE: không áp preset, không can thiệp cấu trúc/kiểu chữ của vùng không thuộc bảng nội dung.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không bảo đảm chữ ký còn hợp lệ sau bất kỳ thay đổi formatting nào.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `SIGNED_PACKAGE`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr105"></a>
### NR105 — Table Style dùng chung nhiều bảng
**Nhóm:** H — Quyền sửa và bảo toàn. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Mã | Kết quả |
| --- | --- |
| A | Đạt |
| B | Đang kiểm tra |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Cùng tblStyle được 12 bảng khác dùng; chỉnh style sẽ ảnh hưởng ngoài bảng đang xét.
**Thuộc tính cần phân tích:** `w:tblStyle,word/styles.xml,w:tblPrEx`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Nếu đề xuất căn chỉnh riêng bảng thì ghi override cục bộ đủ quyền hoặc KEEP; không sửa shared style.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[63, 102]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không đổi styles.xml dùng chung để sửa đúng một bảng.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr106"></a>
### NR106 — Font Times New Roman chưa được xác minh có trên máy đo
**Nhóm:** H — Quyền sửa và bảo toàn. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Tên | Ghi chú |
| --- | --- |
| Nguyễn Văn Bình | Đã đối chiếu |
| Trần Thu Hà | Đang kiểm tra |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** OOXML yêu cầu TNR14 nhưng host font metrics không có face đúng.
**Thuộc tính cần phân tích:** `w:rFonts,w:sz,word/fontTable.xml`.

**C. Kết quả kỳ vọng — `REVIEW_REQUIRED`:** Có thể kết luận font/size declared nếu resolve được; không gán confidence MEASURED_FONT hay chiều rộng glyph thực.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không đo bằng Liberation Serif rồi coi là Times New Roman tương đương tuyệt đối.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `FONT_METRICS_UNAVAILABLE`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr107"></a>
### NR107 — Bảng nguồn trộn 13 pt và 14 pt
**Nhóm:** H — Quyền sửa và bảo toàn. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `ACTION`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Hạng mục | Thời hạn |
| --- | --- |
| Kiểm tra hồ sơ | 05/11/2026 |
| Tổng hợp | 07/11/2026 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Header 14 pt, một số ô dữ liệu 13 pt và một số 14 pt, đều trong dải.
**Thuộc tính cần phân tích:** `w:rPr/w:sz,word/styles.xml,w:tblStylePr`.

**C. Kết quả kỳ vọng — `REVIEW_REQUIRED`:** Giải thích có chủ ý hay không trước khi thống nhất; nếu được phép, đề xuất cùng size đã chọn theo family; không mặc định MIXED là sai pháp luật.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không bắt buộc mọi run phải 14 nếu 13 được phê duyệt và sự khác biệt là chủ ý.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `MIXED_SIZE_REQUIRES_INTENT`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr108"></a>
### NR108 — Mẫu được viện dẫn xung đột với preset thẩm mỹ
**Nhóm:** H — Quyền sửa và bảo toàn. **Vai trò bảng:** `OFFICIAL_FORM`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Chỉ tiêu | Giá trị |
| --- | --- |
| A | 12 |
| B | 24 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Biểu mẫu chỉ định viền/nền riêng, trong khi V16 muốn Statistical Minimal.
**Thuộc tính cần phân tích:** `w:tblStyle,w:tcBorders,w:shd`.

**C. Kết quả kỳ vọng — `PRESERVE`:** Phân loại [BM] thắng [KN]; nếu mẫu không tương thích phạm vi Times New Roman 13–14, trả SCOPE_CONFLICT/PRESERVE.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** PRESERVE: không áp preset, không can thiệp cấu trúc/kiểu chữ của vùng không thuộc bảng nội dung.
**Vector chiều rộng:** Không ấn định. Do thiếu hoặc xung đột hình học/chức năng, không nên đưa ra kích thước mm.

**D. Phản ví dụ/điều cấm:** Không báo vi phạm NĐ30 chỉ vì không dùng viền 0,5pt/padding đề xuất của dự án.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `FORM_LOCK`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr109"></a>
### NR109 — Ba bảng cùng chức năng nhưng một bảng lệch padding
**Nhóm:** I — So sánh phương án và nhất quán. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Kỳ | Hồ sơ |
| --- | --- |
| Tháng 1 | 12 |
| Tháng 2 | 15 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Ba bảng thống kê cùng family, riêng bảng tháng 2 có padding 4mm.
**Thuộc tính cần phân tích:** `w:tblCellMar,w:tblStyle,w:tcMar`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Đối chiếu những thuộc tính cùng authority; đề xuất padding 2mm khi không đổi nội dung và có lợi ích mật độ; giữ cột theo dữ liệu mỗi bảng.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[81, 84]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không ép mọi bảng cùng tỷ lệ cột chỉ vì cùng họ bảng.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr110"></a>
### NR110 — Cùng dữ liệu nhưng mục tiêu đọc khác nhau
**Nhóm:** I — So sánh phương án và nhất quán. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP/ACTION`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Mã | Mô tả | Trạng thái |
| --- | --- | --- |
| A01 | Hồ sơ cần rà soát | Đang xử lý |
| A02 | Biên bản hoàn tất | Đạt |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Hai yêu cầu độc lập: tra cứu theo mã và theo dõi trạng thái.
**Thuộc tính cần phân tích:** `w:tblGrid,w:pPr/w:jc,w:t`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Đối với LOOKUP bảo vệ mã; đối với ACTION bảo vệ trạng thái; cả hai giữ nguồn, tính width theo lợi ích thực.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[42, 70, 53]` mm; tổng **165 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không suy một vector width tối ưu chung từ dữ liệu giống nhau mà bỏ qua reader_task.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr111"></a>
### NR111 — So sánh 14 pt và 13 pt trong bảng mật độ cao
**Nhóm:** I — So sánh phương án và nhất quán. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `ACTION`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| STT | Nhiệm vụ | Đơn vị | Ngày | Kết quả | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 1 | Kiểm tra khu vực | Phòng KT | 05/11 | Đạt | Đối chiếu |
| 2 | Bàn giao thiết bị | Phòng NV | 06/11 | Chờ | Theo dõi |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm; profile này cho phép 13–14 pt; chọn 13 là đề xuất có điều kiện. **Dấu hiệu quyết định:** Profile NĐ30 của dự án cho phép 13/14, W=165; 6 cột nhiều dữ liệu.
**Thuộc tính cần phân tích:** `w:rPr/w:sz,w:tblGrid,w:tcMar`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Thử width/padding tại 14 trước; cân nhắc 13 nếu vẫn áp lực, phải ghi thay đổi size như quyết định có điều kiện.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 13 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[15, 55, 31, 26, 19, 19]` mm; tổng **165 mm** (6 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không tự giảm từng ô xuống 12, không đổi size chỉ vì 6 cột.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `SIZE_CHOICE_CONDITIONAL`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr112"></a>
### NR112 — Hai ứng viên tương đương về độ rộng nhưng khác patch cost
**Nhóm:** I — So sánh phương án và nhất quán. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `LOOKUP`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Mã | Tên | Trạng thái |
| --- | --- | --- |
| 01 | Nhóm hồ sơ A | Đạt |
| 02 | Nhóm hồ sơ B | Chờ |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** A chỉnh 2 cột 4mm, B chỉnh cả 3 cột tổng dịch chuyển 12mm, đều đạt sàn cấu trúc.
**Thuộc tính cần phân tích:** `w:tblGrid,w:tcW,w:tblLayout`.

**C. Kết quả kỳ vọng — `KEEP_EXISTING`:** Chọn ứng viên ít thuộc tính/cột thay đổi khi không có lợi ích đọc tốt hơn được chứng minh.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Vector chiều rộng:** Không ấn định. Giữ nguyên hoặc đánh giá lại baseline theo dữ liệu thực.

**D. Phản ví dụ/điều cấm:** Không chọn phương án phức tạp chỉ vì tỷ lệ nhìn có vẻ đều hơn.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `EQUAL_BENEFIT_ASSUMED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr113"></a>
### NR113 — Không thay đổi khi tất cả điều kiện nội tại đạt
**Nhóm:** I — So sánh phương án và nhất quán. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `SUMMARY`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Nội dung | Kết quả |
| --- | --- |
| Hồ sơ | Đạt |
| Thiết bị | Đạt |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Baseline rõ vai trò, size 14 và geometry khả thi, không có xung đột style.
**Thuộc tính cần phân tích:** `w:tblGrid,w:tblBorders,w:pPr`.

**C. Kết quả kỳ vọng — `KEEP_EXISTING`:** Chọn NO_OP_VALID/KEEP_EXISTING, ghi lý do, không tạo bản format-only khác mà không có mục tiêu cải thiện.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Vector chiều rộng:** Không ấn định. Giữ nguyên hoặc đánh giá lại baseline theo dữ liệu thực.

**D. Phản ví dụ/điều cấm:** Không đặt viền mới chỉ để “có sửa đổi” khi preset không bắt buộc.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `STRUCTURAL_GATES_PASS`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr114"></a>
### NR114 — Cột mô tả không phải nút thắt của hàng
**Nhóm:** I — So sánh phương án và nhất quán. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `ACTION`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| STT | Nội dung | Đơn vị | Hạn |
| --- | --- | --- | --- |
| 1 | Kiểm tra | Phòng Tổng hợp và Hành chính | 05/11 |
| 2 | Báo cáo | Phòng Điều độ | 07/11 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Nội dung ngắn, tên đơn vị dài chi phối số dòng hàng.
**Thuộc tính cần phân tích:** `w:tcW,w:vAlign,w:tblGrid`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Ưu tiên tăng width cho đơn vị (nếu giảm được số dòng ước lượng) thay vì tiếp tục tăng cột Nội dung.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[18, 40, 72, 35]` mm; tổng **165 mm** (4 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không đánh đồng cột PRIMARY_CONTENT với cột luôn cần width lớn nhất.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr115"></a>
### NR115 — Header dài là nút thắt hơn dữ liệu số
**Nhóm:** I — So sánh phương án và nhất quán. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Chỉ tiêu | Hoàn thành đúng tiến độ (%) | Đang xử lý |
| --- | --- | --- |
| Hồ sơ | 95,5 | 4 |
| Biên bản | 98,0 | 2 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Header cột 2 dài hơn mọi giá trị, có thể ngắt thành 2–3 dòng.
**Thuộc tính cần phân tích:** `w:rPr/w:b,w:tcW,w:tblHeader`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Đo riêng header 14 bold và data, cân nhắc header wrap hợp lý thay vì dành phần lớn W cho cột giá trị.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[59, 64, 42]` mm; tổng **165 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không ép tiêu đề dài một dòng làm cột diễn giải bị thiếu chỗ.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr116"></a>
### NR116 — Từ viết tắt có thể làm mất nghĩa nếu AI tự thu gọn
**Nhóm:** I — So sánh phương án và nhất quán. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `ACTION`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Đơn vị | Nhiệm vụ |
| --- | --- |
| Phòng Nghiệp vụ và Đào tạo | Tổ chức kiểm tra |
| Phòng Kỹ thuật và Công nghệ | Kiểm thử thiết bị |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Tên đơn vị quá dài so với W, nhưng là text có thẩm quyền nguồn.
**Thuộc tính cần phân tích:** `w:t,w:tcW,w:pPr`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Căn trái tên, cho wrap; nếu ước lượng không vừa, REVIEW width chứ không tự tạo mã phòng.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[89, 76]` mm; tổng **165 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không thay “Phòng Nghiệp vụ và Đào tạo” bằng “P.NV&ĐT”.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr117"></a>
### NR117 — Chừa một phần width cho bảng số ngắn
**Nhóm:** I — So sánh phương án và nhất quán. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `COMPARE`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Thứ hạng | Giá trị |
| --- | --- |
| I | 5 |
| II | 8 |
| III | 9 |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm; baseline 90mm hợp lệ theo nguồn. **Dấu hiệu quyết định:** Tổng sàn các cột chỉ cần 90mm, W_allow=165mm.
**Thuộc tính cần phân tích:** `w:tblW,w:tblInd,w:tblGrid`.

**C. Kết quả kỳ vọng — `KEEP_EXISTING`:** Ưu tiên bảng 90mm căn vị trí phù hợp, giữ 14 pt và không kéo giá trị có một chữ số ra xa nhãn.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** STATISTICAL_MINIMAL (chỉ khi không bị khóa): nền trắng, ưu tiên đường kẻ ngang có nghĩa, nhãn căn trái và số căn phải; tiêu đề đậm.
**Ứng viên độ rộng:** `[50, 40]` mm; tổng **90 mm** (2 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không mặc định sử dụng hết 165mm mới đẹp.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `TEXT_ESTIMATED`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---

<a id="case-nr118"></a>
### NR118 — Tái lập quyết định từ cùng dữ liệu OOXML
**Nhóm:** I — So sánh phương án và nhất quán. **Vai trò bảng:** `DATA_TABLE`. **Tác vụ đọc:** `ACTION`.

**A. Dữ liệu mẫu (giả lập, không phải nội dung văn bản thật)**

| Mã | Nội dung | Trạng thái |
| --- | --- | --- |
| B01 | Rà soát tài liệu | Đạt |
| B02 | Cập nhật dữ liệu | Đang xử lý |

**B. Ngữ cảnh/OOXML đầu vào:** A4 dọc; W_allow=165 mm (đầu vào giả lập đã xác minh); bảng inline không bị khóa. **Dấu hiệu quyết định:** Hai lượt AI có input snapshot/profile giống hệt, cùng phiên bản rule.
**Thuộc tính cần phân tích:** `w:tblGrid,w:tblW,w:rPr/w:sz`.

**C. Kết quả kỳ vọng — `DESIGN_RECOMMENDED`:** Lưu reasoning trace: authority→role→font 14→hard gates→ứng viên→decision; phải trả cùng kết luận và vector nếu dùng cùng font metrics/config.
**Font được phép khi đề xuất định dạng bảng nội dung:** `Times New Roman 14 pt` (header đậm cùng size). **Preset:** FORMAL_GRID (chỉ khi có quyền định dạng): viền ngoài 0,75 pt, viền trong 0,5 pt, padding ngang 1,5–2 mm, dọc 0,8–1,2 mm; header đậm, căn theo vai trò ô.
**Ứng viên độ rộng:** `[40, 74, 51]` mm; tổng **165 mm** (3 cột vật lý). Đây là **vector mô phỏng theo ngữ nghĩa và ràng buộc cộng**, chưa đo glyph TNR hay được Word xác nhận. Phải kiểm hard floors của header/token, từng cell thực và ô gộp trước khi dùng.

**D. Phản ví dụ/điều cấm:** Không biến khác biệt diễn đạt trong giải thích thành thay đổi thông số tùy hứng.
**E. QA không render:** Đối chiếu mục tiêu đọc, vai trò cột và dẫn chứng từ header/ô, không suy đoán vượt dữ liệu. Đối chiếu W_allow, số cột lưới, locked widths, tổng vector và ràng buộc span; không suy kết xuất. Giữ nguyên văn bản ô, số, dấu, hyperlink, field, revision, thứ tự và cấu trúc không được sửa.
**F. Mức bằng chứng:** `SPEC_REPEATABILITY`. **Truy vết nguồn:** [S1](#nguon-s1), [S2](#nguon-s2).

---


## 4. Quy tắc kiểm tra đồng dạng (metamorphic QA) không cần render

1. **Thay nhãn cột nhưng giữ dữ liệu:** nếu đổi vai trò ngữ nghĩa thật thì kết luận/preset phải được xét lại; không giữ width chỉ do số cột bằng nhau.
2. **Thêm ký tự không ngắt vào token:** sàn nội dung không thể giảm do chuỗi được bảo vệ dài hơn, các tiêu chí khác giữ nguyên.
3. **Thay `w:sz` 28→26 theo quyền hợp lệ:** nếu chọn 13 pt có thể giảm width pressure; không tự suy chắc giảm số trang.
4. **Thay layout mode `autofit`↔`fixed`:** phải thay metadata và đánh giá lại; không tuyên bố không khác biệt.
5. **Thay margin/section:** làm mất hiệu lực vector đã tính cho container cũ; không tái sử dụng W một cách ngầm định.
6. **Đổi dữ liệu `0`→ô rỗng:** thay ngữ nghĩa, không thể coi là format-only và không chấp nhận trong phép tối ưu.
7. **Thêm `gridSpan=2`:** ràng buộc áp vào cả interval cột, không nhân bản nội dung.
8. **Chèn manual page break:** đánh dấu trạng thái lặp header chưa được xác nhận và không sửa dữ liệu.
9. **Đánh dấu official-form lock:** mọi ứng viên thay đổi style/width phải bị loại, cho dù có vẻ đẹp hơn.
10. **Lặp lại cùng snapshot:** với cùng rules/profile/font metrics/config, đầu ra quyết định và vector phải tương đương, không rung lắc.

## 5. QA và giới hạn chứng cứ

- Các kiểm tra file được ghi trong báo cáo riêng `ChuanhoaBang_V16_Research_QA_Report_100_Case.md`, chỉ kiểm **số lượng, schema, chiều rộng số học, font policy, đối chiếu danh mục**. Không khẳng định chạy thử Word hay AI blind test.
- Với case TNR14 và vector width, cần **metrics của đúng TNR face/run** trước khi coi `hard_floor` và `header_floor` là đã kiểm; với input giả lập không có DOCX, đó là công việc của hệ thống sử dụng đặc tả về sau.
- Khả năng tiếp cận/đọc bằng thiết bị hỗ trợ của bảng gộp nhiều tầng không thể được xác nhận bằng việc chỉ kiểm XML. Giữ nhãn `REVIEW` cho các tình huống không thể đảm bảo.
- Việc một case có nhãn DESIGN_RECOMMENDED không đồng nghĩa phương án sẽ đúng trong tất cả các phiên bản Word; đó là đáp án tham chiếu **ở mức thiết kế**.

## Nguồn nghiên cứu và phạm vi áp dụng
<a id="nguon-s1"></a>**[S1]** ChuanhoaBang V15 — báo cáo nghiên cứu và minh chứng theo phiên bản: https://github.com/quanggiaphthh/ChuanhoaBang/blob/main/docs/research/Bao_cao_chuan_hoa_va_toi_uu_bang_DOCX_ND30_HD05_V15_2026.md
<a id="nguon-s2"></a>**[S2]** ChuanhoaBang V16 — đặc tả 23 quy tắc ban đầu: AI_TABLE_FORMATTING_NO_RENDER_V16.md
<a id="nguon-s3"></a>**[S3]** Microsoft Learn — TableWidth / preferred width: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablewidth?view=openxml-3.0.1
<a id="nguon-s4"></a>**[S4]** Microsoft Learn — TableHeader, contiguous header rows: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tableheader?view=openxml-3.0.1
<a id="nguon-s5"></a>**[S5]** Microsoft Learn — VerticalMerge and table-cell constraints: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.verticalmerge?view=openxml-3.0.1
<a id="nguon-s6"></a>**[S6]** Section508.gov — Data tables in documents and accessibility: https://www.section508.gov/blog/accessibility-bytes/data-tables-in-documents/
<a id="nguon-s7"></a>**[S7]** Microsoft Learn — TableRowHeight / trHeight: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablerowheight?view=openxml-3.0.1
<a id="nguon-s8"></a>**[S8]** Microsoft Learn — Table Class / adjacent tables with same style: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.table?view=openxml-3.0.1
<a id="nguon-s9"></a>**[S9]** Microsoft Learn — TableProperties, table-level properties and overrides: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tableproperties?view=openxml-3.0.1
<a id="nguon-s10"></a>**[S10]** Microsoft Learn — NoWrap semantics: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.nowrap?view=openxml-3.0.1
<a id="nguon-s11"></a>**[S11]** Microsoft Learn — growAutofit may allow extension into margins: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.growautofit?view=openxml-3.0.1
<a id="nguon-s12"></a>**[S12]** Microsoft Learn — tcFitText changes character spacing: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablecellfittext?view=openxml-3.0.1
<a id="nguon-s13"></a>**[S13]** Microsoft Support — repeat header rows and manual breaks: https://support.microsoft.com/vi-vn/word/repeat-table-header-on-subsequent-pages

**Phân loại nguồn:** S1–S2 là nghiên cứu/đặc tả nội bộ; S3–S5, S7–S13 là tài liệu kỹ thuật Microsoft; S6 là hướng dẫn khả năng tiếp cận. Quy tắc thẩm mỹ của dự án (padding/viền/cỡ chữ lựa chọn) **không phải quy định pháp luật** và không được mượn nguồn Microsoft để tuyên bố chúng là chuẩn bắt buộc.
