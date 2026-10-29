# ChuanhoaBang V17.5 — Đặc tả nghiên cứu bảng nội dung hành chính và quyết định trang ngang

**Phiên bản:** V17.5 scope/landscape specification — draft nghiên cứu, 29/10/2026  | **Môi trường:** không render; không sửa repo; không phát triển formatter. **Font trong bảng:** Times New Roman, cỡ 13–14 pt.

## 1. Phân biệt đối tượng và tính áp dụng

- **ND30:** Nghị định 30/2020/NĐ-CP Điều 2 bao gồm cơ quan, tổ chức nhà nước **và doanh nghiệp nhà nước**. Phụ lục I quy định văn bản thường theo chiều dài A4; văn bản có bảng/biểu *không làm thành phụ lục riêng* có thể theo chiều rộng. Không tự diễn giải quy định này thành quyền tự động thay orientation mọi bảng trong phụ lục.
- **HD05:** Hướng dẫn 05-HD/VPTW (27/5/2026) về văn bản các cấp ủy, tổ chức/cơ quan Đảng; cơ quan hoạt động theo Luật Doanh nghiệp không phải đối tượng trực tiếp. Điều IV.4.3 cho phép bảng/biểu trình bày theo chiều ngang, căn cứ vùng trình bày dọc để sắp xếp phù hợp. Văn bản Đảng của cấp ủy trong doanh nghiệp và văn bản quản trị doanh nghiệp phải phân loại theo *chủ thể ban hành*.
- **SPECIAL_FORM:** Các mẫu biểu được quy định chuyên ngành, điều lệ nội bộ, phụ lục đã ban hành là ràng buộc riêng; phải ưu tiên mẫu được xác định hợp lệ.
- **Thiết kế V17.5:** 13 pt chỉ dùng khi authority/profile cho phép; 14 pt là mặc định theo cấu hình dự án, không giảm font tự động để làm vừa bảng.

## 2. Danh mục 10 họ bảng trọng tâm của benchmark 160 bảng gốc

| Mã | Họ bảng | Số bảng gốc đề xuất | Văn bản thường gặp | Header điển hình |
|---|---|---:|---|---|
| `PLAN_ASSIGN` | Kế hoạch, phân công nhiệm vụ | 28 | Kế hoạch, chương trình, phương án | Nhiệm vụ | Chủ trì | Phối hợp | Tiến độ | Sản phẩm | Ghi chú |
| `PROGRESS_KPI` | Theo dõi tiến độ và kết quả | 22 | Báo cáo, kế hoạch kiểm tra | Chỉ tiêu | Kế hoạch | Thực hiện | Tỷ lệ | Khó khăn | Kiến nghị |
| `STAT_PERIOD` | Thống kê theo kỳ/đơn vị | 22 | Báo cáo tháng, quý, năm | Đơn vị | Tháng 1 | Tháng 2 | Tháng 3 | Tổng | So sánh |
| `CALENDAR` | Lịch công tác/hội nghị/đào tạo | 14 | Chương trình, lịch, kế hoạch | Thời gian | Nội dung | Thành phần | Địa điểm | Phụ trách |
| `LEGAL_COMPARE` | Đối chiếu văn bản, trách nhiệm | 16 | Báo cáo rà soát, tờ trình, nghị quyết | Quy định | Hiện trạng | Hạn chế | Căn cứ | Đề xuất |
| `PERSONNEL` | Danh sách, phân công, nhân sự | 14 | Danh sách, biên bản, phụ lục | STT | Họ tên | Đơn vị | Chức vụ | Nhiệm vụ | Ghi chú |
| `COST_RESOURCE` | Kinh phí, vật tư, nguồn lực | 16 | Kế hoạch, báo cáo dự toán | Hạng mục | Khối lượng | Đơn vị | Đơn giá | Thành tiền | Ghi chú |
| `RISK_REMEDY` | Kiểm tra, giám sát, kiến nghị khắc phục | 12 | Báo cáo kiểm tra, kết luận, chương trình công tác | Vấn đề | Nguyên nhân | Rủi ro | Biện pháp | Trách nhiệm | Hạn |
| `APPENDIX_REGISTER` | Danh mục hồ sơ, phụ lục, văn bản | 10 | Phụ lục, báo cáo, danh mục | STT | Số/ký hiệu | Trích yếu | Ngày | Đơn vị | Tình trạng |
| `OFFICIAL_PRESERVE` | Mẫu biểu có cấu trúc bắt buộc | 6 | Biểu mẫu hành chính/Đảng đã ban hành | Nội dung theo mẫu — không tự thay cấu trúc |
| **Tổng** | | **160** | | |

Số lượng ở đây là **đề xuất phân tầng benchmark**, không phải 160 ca đã thu thập hay chạy. Phân tầng bổ sung: loại chủ thể (ADMIN_ND30, PARTY_HD05, SOE_ND30, SPECIAL_FORM), số cột (2–3, 4–6, 7+), cấu trúc (simple/merged/multilevel), ngữ nghĩa (nhiệm vụ, số liệu, văn bản pháp lý, tên người, lịch), tình trạng mẫu (tự soạn/khóa), phông 13/14 được cấp quyền.

## 3. LANDSCAPE_DECISION: không đồng nhất số cột với quyết định xoay trang

**Đầu vào bắt buộc:** loại văn bản và chủ thể ban hành; trạng thái đã ban hành/mẫu; bảng thuộc body hay appendix; section chứa bảng; khổ giấy/hướng/lề/gutter; các ràng buộc `tblW/tblGrid/tcW/gridSpan/vMerge`; cỡ chữ hiệu dụng và nguồn mẫu; tiêu đề/caption; header/footer, số trang, chữ ký; quyền chỉnh sửa.

**Bước 1 — Authority gate:** xác nhận trường hợp pháp lý/profile có thể đề xuất landscape, không tự xoay biểu mẫu locked, chữ ký số, văn bản đã ban hành. Với ND30, riêng bảng ở body áp dụng điều kiện của Phụ lục I; phụ lục riêng phải đối chiếu quy định mẫu/kiểu trình bày và cần review.

**Bước 2 — Feasibility gate:** xác định `W_portrait`, `W_landscape` của section giả định sau khi trừ lề/gutter/indent/column width/spacing hợp lệ; kiểm tra `sum(min_width_i)` và ràng buộc các ô gộp. `tcW`/`tblW` là preferred width, không lấy phép cộng XML làm bảo chứng Word hiển thị.

**Bước 3 — So sánh PORTRAIT và LANDSCAPE theo cùng nội dung, cùng TNR 13/14, cùng cấu trúc và mẫu:** nếu dọc feasible và dễ đọc, giữ dọc; nếu dọc không feasible theo các ngưỡng **đã được khai báo/đo** còn ngang feasible và hợp pháp, `LANDSCAPE_CANDIDATE`; nếu cả hai feasible, `OPTIONAL`/`KEEP` theo lợi ích và độ bất định; nếu không đủ dữ liệu `REVIEW_REQUIRED`; nếu khóa `PRESERVE_LOCKED`. Không áp đặt điểm số thẩm mỹ chung.

**Bước 4 — Vertical trade-off:** ngang tăng bề ngang nhưng giảm chiều cao trang khả dụng; bảng có nhiều hàng dài có thể tăng số trang. Không kết luận tổng số trang hay ngắt hàng chính xác từ OOXML khi chưa dàn trang Word.

**Bước 5 — Section-impact gate:** nếu định đặt trang ngang xen trang dọc, phải có đề xuất 3 đoạn section: dọc trước, ngang chứa bảng và caption, dọc sau. Kiểm tra sectPr ở kết thúc đúng section, page size/orientation, pgMar, `headerReference/footerReference`, `pgNumType`, `titlePg`, odd/even, page fields, section breaks, caption và vùng ký. Mặc định **chỉ đề xuất**, mọi thay đổi section cần người dùng duyệt.

**Nhãn output:** `KEEP_PORTRAIT`, `LANDSCAPE_CANDIDATE`, `LANDSCAPE_OPTIONAL`, `REVIEW_REQUIRED`, `PRESERVE_LOCKED`, `NO_SAFE_FIT`. `LANDSCAPE_CANDIDATE` không bằng `LANDSCAPE_VERIFIED`.


### 3.1. Phân biệt hai nghĩa của "layout ngang"

- **LANDSCAPE_PAGE:** giữ nguyên thứ tự hàng/cột và dữ liệu, đổi orientation của **section chứa bảng** từ portrait sang landscape. Đây là phương án nghiên cứu mặc định cho yêu cầu hiện tại.
- **TABLE_RESTRUCTURE:** chuyển đổi một bảng nhiều cột thành cấu trúc trải ngang theo nhóm hoặc chuyển vị hàng/cột. Đây là **biến đổi cấu trúc/ngữ nghĩa**, không phải thao tác đổi orientation; chỉ đề xuất khi được phép sửa bảng và có quyết định của người dùng. Không tự gộp/tách/xóa/thêm hàng cột.
- **MOVE_TO_APPENDIX:** khi bảng ở thân văn bản không thể bố trí hợp lý và quy định cho phép, có thể đề xuất tách thành phụ lục; đối với ND30 phải đối chiếu điều kiện ghi rõ trong Phụ lục I và mẫu áp dụng, không tự di dời.

Mọi phương án so sánh cùng dữ liệu phải bảo toàn text, kiểu dữ liệu, công thức, mã định danh, hàng tổng, numbering và thứ tự trừ khi phương án cấu trúc được phê duyệt riêng.

## 4. Ví dụ hình học A4 (số học chính xác đối với giả định lề; không phải đo Word)

| Điều kiện | Trang dọc | Trang ngang |
|---|---:|---:|
| A4 (rộng × cao) | 210 × 297 mm | 297 × 210 mm |
| Lề ví dụ: trái 30, phải 15, trên/dưới 20 mm | Giống nhau | Giống nhau |
| Bề ngang vùng chữ tính thô `W = pageW-left-right` | **165 mm** | **252 mm** |
| Chiều cao vùng chữ tính thô `H = pageH-top-bottom` | **257 mm** | **170 mm** |
| Tác động | Hẹp hơn nhưng nhiều chỗ theo chiều cao | **+87 mm ngang; −87 mm cao** |

Không tái sử dụng mặc định 165/252 mm như điều kiện pháp lý của mọi hồ sơ: lề theo profile, gutter, 2 mặt, cột báo, bảng lồng, floating table có thể thay đổi vùng hợp lệ. Với ND30 lề quy định theo khoảng; với HD05 vùng trình bày khác theo loại in một/hai mặt.

## 5. Kiểm tra OOXML tối thiểu để đề xuất chuyển dọc ↔ ngang

| Kiểm tra | Căn cứ thuộc tính | Kiểm tra được bằng cấu trúc | Phần chưa xác nhận nếu không render |
|---|---|---|---|
| Xác định section | `w:sectPr` (paragraph/body), `w:type` | Vị trí và loại break | Chỗ ngắt trang hiển thị cuối cùng |
| Hướng và khổ | `w:pgSz` `w:w/w:h/w:orient` | Giá trị trang của section | Khả năng Word dàn theo intent trong môi trường đích |
| Vùng chữ | `w:pgMar`, `w:cols`, gutter | Phép tính từ giá trị | Ranh giới in thực tế nếu đặc tính thiết bị khác |
| Chiều rộng bảng | `w:tblW`, `w:tblGrid`, `w:tcW`, `gridSpan`, `vMerge` | Ràng buộc lưới, width giả định | Độ rộng thực tế khi Word auto layout |
| Header/footer | `headerReference`, `footerReference`, `titlePg`, `pgNumType` | Định danh, link, kiểu và cấu trúc | Vị trí hiển thị của số trang sau xoay |
| Bảo toàn | source text + styles + OPC relationships + section inventory | Diff thuộc tính và quan hệ | Thay đổi hiển thị ngoài vùng |

**Cảnh báo:** Không tạo section break trong ô/hàng như một phép thay thuộc tính bảng. Không đổi hướng bằng `w:pgSz` của toàn bộ tài liệu khi chỉ một bảng cần ngang. `continuous` không phải lựa chọn mặc định an toàn cho đổi page-level orientation; ưu tiên mô tả logic `nextPage` và review.

## 6. Bộ 32 tình huống nghiên cứu orientation (chi tiết ở CSV/JSONL)

Bộ được chủ động chia 8 `PORTRAIT_KEEP`, 8 `LANDSCAPE_CANDIDATE`, 8 `REVIEW_REQUIRED`, 8 `PRESERVE_LOCKED`. **Tất cả đều là case giả định thiết kế đặc tả**; `assumed_required_width_mm` là giá trị giả định chưa đo font; không có expert-gold, không có Word-render, không có quyết định pháp lý cá biệt. `LANDSCAPE_CANDIDATE` là đề xuất có điều kiện, không là chứng nhận.

| ID | Loại | Văn bản | Font | Số cột | Width giả định | Kỳ vọng |
|---|---|---|---|---:|---:|---|
| ORI001 | `PLAN_ASSIGN` | Kế hoạch năm | 14 pt | 4 | 153 mm | `PORTRAIT_KEEP` |
| ORI002 | `STAT_PERIOD` | Báo cáo quý | 14 pt | 4 | 140 mm | `PORTRAIT_KEEP` |
| ORI003 | `CALENDAR` | Chương trình họp | 14 pt | 5 | 159 mm | `PORTRAIT_KEEP` |
| ORI004 | `PERSONNEL` | Danh sách họp chi bộ | 14 pt | 4 | 145 mm | `PORTRAIT_KEEP` |
| ORI005 | `COST_RESOURCE` | Báo cáo vật tư | 13 pt | 5 | 160 mm | `PORTRAIT_KEEP` |
| ORI006 | `APPENDIX_REGISTER` | Phụ lục văn bản | 14 pt | 4 | 152 mm | `PORTRAIT_KEEP` |
| ORI007 | `RISK_REMEDY` | Báo cáo khắc phục | 14 pt | 3 | 161 mm | `PORTRAIT_KEEP` |
| ORI008 | `LEGAL_COMPARE` | Đối chiếu quy định | 14 pt | 3 | 164 mm | `PORTRAIT_KEEP` |
| ORI009 | `PLAN_ASSIGN` | Kế hoạch triển khai | 14 pt | 8 | 218 mm | `LANDSCAPE_CANDIDATE` |
| ORI010 | `PROGRESS_KPI` | Báo cáo tiến độ quý | 14 pt | 9 | 230 mm | `LANDSCAPE_CANDIDATE` |
| ORI011 | `STAT_PERIOD` | Bảng so sánh 6 tháng | 13 pt | 10 | 240 mm | `LANDSCAPE_CANDIDATE` |
| ORI012 | `LEGAL_COMPARE` | Báo cáo kiểm tra | 14 pt | 7 | 220 mm | `LANDSCAPE_CANDIDATE` |
| ORI013 | `CALENDAR` | Lịch trực vận hành | 14 pt | 8 | 210 mm | `LANDSCAPE_CANDIDATE` |
| ORI014 | `PERSONNEL` | Danh sách phân công | 14 pt | 8 | 235 mm | `LANDSCAPE_CANDIDATE` |
| ORI015 | `COST_RESOURCE` | Bảng dự toán theo hạng mục | 14 pt | 9 | 246 mm | `LANDSCAPE_CANDIDATE` |
| ORI016 | `APPENDIX_REGISTER` | Danh mục tài liệu đính kèm | 14 pt | 8 | 229 mm | `LANDSCAPE_CANDIDATE` |
| ORI017 | `PLAN_ASSIGN` | Kế hoạch nhiệm vụ | 14 pt | 7 | ? mm | `REVIEW_REQUIRED` |
| ORI018 | `PROGRESS_KPI` | Báo cáo chuyên môn | 14 pt | 8 | 208 mm | `REVIEW_REQUIRED` |
| ORI019 | `STAT_PERIOD` | Thống kê cơ sở | 13 pt | 10 | 239 mm | `REVIEW_REQUIRED` |
| ORI020 | `LEGAL_COMPARE` | Phụ lục đối chiếu | 14 pt | 6 | 216 mm | `REVIEW_REQUIRED` |
| ORI021 | `CALENDAR` | Lịch kiểm tra | 14 pt | 7 | 220 mm | `REVIEW_REQUIRED` |
| ORI022 | `PERSONNEL` | Danh sách ký nhận | 14 pt | 7 | 209 mm | `REVIEW_REQUIRED` |
| ORI023 | `RISK_REMEDY` | Bảng kiểm tra | 14 pt | 6 | 200 mm | `REVIEW_REQUIRED` |
| ORI024 | `COST_RESOURCE` | Báo cáo tài chính | 14 pt | 10 | 265 mm | `REVIEW_REQUIRED` |
| ORI025 | `OFFICIAL_PRESERVE` | Mẫu báo cáo đã ban hành | 14 pt | 9 | 238 mm | `PRESERVE_LOCKED` |
| ORI026 | `OFFICIAL_PRESERVE` | Mẫu Đảng có khung cố định | 14 pt | 7 | 210 mm | `PRESERVE_LOCKED` |
| ORI027 | `PERSONNEL` | Bảng có chữ ký số | 14 pt | 8 | 232 mm | `PRESERVE_LOCKED` |
| ORI028 | `APPENDIX_REGISTER` | Phụ lục đã phê duyệt | 14 pt | 8 | 226 mm | `PRESERVE_LOCKED` |
| ORI029 | `LEGAL_COMPARE` | Bảng trong tài liệu theo mẫu ngành | 14 pt | 9 | 236 mm | `PRESERVE_LOCKED` |
| ORI030 | `PLAN_ASSIGN` | Kế hoạch đã ký ban hành | 14 pt | 8 | 231 mm | `PRESERVE_LOCKED` |
| ORI031 | `CALENDAR` | Lịch làm việc phát hành | 14 pt | 7 | 218 mm | `PRESERVE_LOCKED` |
| ORI032 | `COST_RESOURCE` | Phụ lục dự toán theo mẫu | 13 pt | 9 | 245 mm | `PRESERVE_LOCKED` |

## 7. Thiết kế pilot V17.5 cập nhật: tập trung tài liệu hành chính/Đảng/doanh nghiệp

- Giữ quy mô nghiên cứu **160 bảng gốc × 2 cặp cùng nội dung × 2 thứ tự = 640 input** cho một model; chỉ là kế hoạch, không phải lượt đã chạy.
- Để kiểm tra orientation có trọng tâm, quy hoạch **48/160 bảng** có ít nhất một cặp `PORTRAIT vs LANDSCAPE`, phân đủ: ND30 body, HD05, SOE (ND30), phụ lục, biểu mẫu khóa, thiếu dữ liệu. Tương ứng 48 cặp × 2 thứ tự = 96 lượt liên quan orientation trong 640 đầu vào.
- Cặp đối chứng orientation **chỉ thay orientation và hình học section được khai báo**. Nếu phải tái phân bổ cột, dùng một cặp khác, không trộn hai yếu tố lỗi trong cùng một cặp mà không đánh dấu điều kiện phụ thuộc.
- Trong mỗi cặp, header và nội dung giữ nguyên; font Times New Roman 13/14 theo profile; ghi rõ các thuộc tính được phép thay và thứ tự kiểm tra hard gates → readability proxy → section side-effects → choose/abstain.
- Nhãn theo nguồn `RULE_DETERMINED`, `SYNTHETIC_CONSTRAINT`, `FONT_METRIC_ESTIMATE` (chỉ dùng khi có kết quả đo thực), `HUMAN_ADJUDICATED` (chỉ khi có người đánh giá độc lập), `VISUAL_NOT_VERIFIED` mặc định.
- Không tự gọi 32 ca mới là blind-gold. Phải tách dữ liệu chạy mô hình và rubric/đáp án, trung lập hoá cách diễn đạt, có điều kiện dừng khi rò rỉ answer key.

## 8. Bản tích hợp ngắn cho workbook/profile

Thêm profile `ADMIN_ND30`, `PARTY_HD05`, `SOE_ADMIN_ND30`, `SPECIAL_FORM_LOCKED`; trường `table_family`, `context(body|appendix)`, `allow_landscape_source`, `orientation_state`, `section_geometry`, `width_evidence`, `section_impact`, `confidence`. Không suy HD05 từ việc doanh nghiệp có tổ chức Đảng; phải xác định chủ thể phát hành tài liệu. Không tự giảm font xuống dưới 13, hoặc tự đổi từ 14 sang 13 khi hồ sơ không cho phép. Mặc định `KEEP_PORTRAIT`; khuyến nghị ngang chỉ khi có chứng cứ và quyền. `LANDSCAPE_CANDIDATE` không là yêu cầu áp dụng tự động. Sửa section phải được chấp thuận; kiểm tra cả vùng trước/sau, header/footer và page numbering. Không tuyên bố render/print-pass từ proxy.

## 9. Các nguồn đối chiếu chính thức (truy cập 29/10/2026)

- **[L01]** [Nghị định 30/2020/NĐ-CP, Điều 2, Phụ lục I](https://thuvienphapluat.vn/van-ban/bo-may-hanh-chinh/Nghi-dinh-30-2020-ND-CP-cong-tac-van-thu-436532.aspx) — nguồn truy xuất toàn văn; đối chiếu cơ sở dữ liệu VBPL và bản Chính phủ.
- **[L02]** [Phụ lục I NĐ30 tại Cổng Công an Đắk Lắk](https://congan.daklak.gov.vn/laws/detail/Nghi-dinh-so-30-2020-ND-CP-quy-dinh-ve-cong-tac-van-thu-40/?download=1&id=0) — nguồn cơ quan nhà nước; trang có thể lỗi truy xuất HTTP.
- **[L03]** [05-HD/VPTW 27/5/2026 — Tư liệu Văn kiện Đảng](https://tulieuvankien.dangcongsan.vn/van-ban-cua-dang/huong-dan-so-05-hd-vptw-ngay-27-5-2026-cua-van-phong-trung-uong-dang-ve-the-thuc-va-ky-thuat-trinh-bay-van-ban-cua-dang.html) — trang văn bản gốc/siêu dữ liệu.
- **[L04]** [05-HD/VPTW — bài toàn văn/diễn giải trên Báo điện tử Chính phủ](https://xaydungchinhsach.chinhphu.vn/huong-dan-so-05-hd-vptw-ve-the-thuc-va-ky-thuat-trinh-bay-van-ban-cua-dang-119260601101535274.htm) — phạm vi và đối tượng Đảng; công bố tháng 10/2026.
- **[L05]** [05-HD/VPTW — bản HTML có mục IV.4.3](https://thuvienphapluat.vn/van-ban/bo-may-hanh-chinh/huong-dan-05-hd-vptw-2026-the-thuc-va-ky-thuat-trinh-bay-van-ban-cua-dang-707499.aspx) — bản tra cứu thứ cấp, đối chiếu nguồn chính.
- **[T01]** [Microsoft: Print with landscape orientation in Word](https://support.microsoft.com/en-us/word/print-with-landscape-orientation-in-word) — orientation một phần tài liệu.
- **[T02]** [Microsoft: Use section breaks](https://support.microsoft.com/en-us/word/use-section-breaks-to-change-the-layout-or-formatting-in-one-section-of-your-word-document) — section break và page layout.
- **[T03]** [Microsoft Learn: PageSize / pgSz](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.pagesize?view=openxml-3.0.1) — hình học và orient theo section.
- **[T04]** [Microsoft Learn: SectionProperties / sectPr](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.sectionproperties?view=openxml-3.0.1) — thuộc tính section và header/footer.
- **[T05]** [Microsoft Learn: SectionType / break](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.sectiontype?view=openxml-3.0.1) — nextPage, continuous, odd/even.
- **[T06]** [Microsoft Support: Link to Previous](https://support.microsoft.com/en-us/word/link-to-previous) — đầu/chân trang liên kết qua section.
- **[T07]** [Microsoft Support: Repeat table header rows](https://support.microsoft.com/en-gb/word/repeat-table-header-on-subsequent-pages) — tiêu đề lặp nếu bảng dài.

## 10. Giới hạn và QA

- `NOT_RUN`: Chưa tiến hành bất kỳ phép suy luận AI mới, đo glyph, Word render, đánh giá chuyên gia hay thay đổi DOCX thực tế.
- `UNVERIFIED`: Ràng buộc width tối thiểu trong case nghiên cứu là dữ liệu giả định, không phải min-width TNR đã đo.
- `REVIEW_REQUIRED`: Tính áp dụng pháp lý với biểu mẫu chuyên ngành/phụ lục theo hồ sơ cụ thể; tính phù hợp trang ngang đối với chữ ký/page numbering khi thiếu section data.
- **QA đã chạy:** kiểm đếm 10 họ bảng/tổng 160 bảng đề xuất, 32 ca không trùng mã, 8 ca trong mỗi nhãn, font hợp lệ, số cột dương, range mm giả định; định dạng xuất CSV/JSONL nhất quán.