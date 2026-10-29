# ChuanhoaBang V17.5.1 — Đặc tả bảng nội dung: hướng trang do người dùng quyết định

**Phiên bản:** V17.5.1 — user-controlled orientation policy, 29/10/2026  | **Môi trường:** không render; không sửa repo; không phát triển formatter. **Font trong bảng:** Times New Roman, cỡ 13–14 pt.

> **QUY TẮC ƯU TIÊN USER-ORIENTATION-001 — BẮT BUỘC:** Mặc định trang **DỌC (PORTRAIT)** khi tạo bảng/tài liệu mới và người dùng không chỉ định hướng. **Chỉ người dùng mới được quyết định chuyển sang NGANG (LANDSCAPE)** bằng yêu cầu rõ ràng có phạm vi xác định. AI không được tự chuyển, đề xuất như một quyết định mặc định, hoặc tự chỉnh `sectPr/pgSz` sang ngang vì bảng nhiều cột, quá rộng, tỷ lệ hình học hay điểm thẩm mỹ. Với DOCX hiện hữu, giữ nguyên orientation đã có nếu người dùng không yêu cầu thay đổi. Các điều khoản cho phép trình bày ngang trong ND30/HD05 là **khả năng pháp lý**, không phải sự ủy quyền thay người dùng.

> **Hệ quả:** Nếu bảng không phù hợp trên trang dọc, AI chỉ chẩn đoán `PORTRAIT_WIDTH_RISK`, đề xuất tối ưu trong trang dọc theo quyền sửa và có thể báo `REVIEW_REQUIRED/NO_SAFE_PORTRAIT_FIT`. **Không tự ý xoay trang ngang.** Khi người dùng yêu cầu ngang, kiểm tra mẫu, bảo vệ, geometry và ảnh hưởng section; không mặc nhiên bỏ qua các ràng buộc này.

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

## 3. Quy tắc `USER_ORIENTATION_CONTROL` — người dùng quyết định, AI không tự chuyển ngang

### 3.1. Phân tách ý định người dùng và điều kiện kỹ thuật

- `orientation_request = UNSPECIFIED | EXPLICIT_PORTRAIT | EXPLICIT_LANDSCAPE`. Chỉ lấy `EXPLICIT_*` từ chỉ dẫn trực tiếp có thể truy vết đến người dùng hoặc quyết định được người dùng phê duyệt rõ phạm vi. Không suy ý định từ số cột, độ rộng, loại bảng, ND30/HD05 hoặc ý kiến do AI tự sinh.
- `orientation_default = PORTRAIT` chỉ dành cho **tài liệu/bảng mới khi không có chỉ dẫn**. Với DOCX đã tồn tại, `orientation_current` lấy từ section thực tế, `UNSPECIFIED` → `KEEP_EXISTING_ORIENTATION` để không phá văn bản gốc.
- `orientation_change_authorized`: `false` nếu `UNSPECIFIED`; khi `EXPLICIT_*`, được phép **xem xét** thay đổi, không đồng nghĩa đã hoàn thành kiểm tra mẫu, bảo vệ và tác động section.
- `width_evidence`: `SYNTHETIC_CONSTRAINT` không chứng minh độ vừa trang thực tế. Width chỉ được dùng cảnh báo và phân tích phương án trong **hướng trang người dùng đã chọn**.
- Ghi tách `requested_orientation`, `effective_orientation`, `change_approved_by_user`, `section_impact_reviewed`, `permission_to_edit` để không vô tình dùng đánh giá kỹ thuật làm chỉ thị xoay trang.

### 3.2. Bảng quyết định mang tính quy phạm cho dự án

| Ý định người dùng | Trạng thái nguồn | Hành động được phép | Nhãn kết quả |
|---|---|---|---|
| Không nêu hướng, bảng/tài liệu **mới** | Không khóa | Tạo trong trang **dọc**; chỉnh width/padding trong giới hạn | `KEEP_PORTRAIT_DEFAULT` |
| Không nêu hướng, DOCX **đã có** | Trang dọc hoặc ngang | Giữ nguyên orientation hiện hữu; không tự chuẩn hóa về dọc | `KEEP_EXISTING_ORIENTATION` |
| Không nêu hướng, trang dọc bị quá rộng | Width rủi ro/không đo được | Cảnh báo, tối ưu trong trang dọc hoặc yêu cầu hướng dẫn; **không xoay ngang** | `KEEP_PORTRAIT_WARN_WIDTH` / `KEEP_PORTRAIT_REVIEW_GEOMETRY` |
| Yêu cầu rõ "chuyển bảng này sang trang ngang" | Quyền sửa và mẫu cho phép, section có thể can thiệp | Lập phương án thay đổi section trong phạm vi chỉ định; cần rà soát trước khi thực hiện | `LANDSCAPE_REQUESTED_REVIEW_SECTION` |
| Yêu cầu rõ "chuyển bảng này sang trang dọc" | Section hiện đang ngang | Đánh giá phương án chuyển về dọc, không thay đổi ngoài vùng được yêu cầu | `PORTRAIT_REQUESTED_REVIEW_SECTION` |
| Có bất kỳ yêu cầu đổi hướng | Mẫu, chữ ký, section hoặc tài liệu khóa | Giữ nguyên, báo ràng buộc cần phê duyệt/xử lý | `PRESERVE_LOCKED_REVIEW_AUTHORITY` |

**Không tồn tại nhãn tự động `LANDSCAPE_CANDIDATE` hoặc `LANDSCAPE_OPTIONAL` khi không có yêu cầu người dùng.** Các nhãn này trong V17.5 là **lịch sử đã thay thế** bởi chính sách V17.5.1; mọi workbook/profile phải đọc trường `expected_spec_decision` của bản mới.

### 3.3. Khi có yêu cầu ngang rõ ràng

Quy trình: xác thực nguồn/phạm vi yêu cầu → xác định hồ sơ ND30/HD05/mẫu → đọc orientation hiện tại → so sánh hình học của phương án **được yêu cầu** → đánh giá section, caption, header/footer, page numbering, chữ ký, bảo toàn XML → kết luận có thể áp dụng / cần review / bị khóa. Không dùng `tcW/tblW` như số đo hiển thị Word. Vẫn chỉ dùng TNR 13–14 pt theo profile.

Nếu yêu cầu làm một bảng trong tài liệu từ dọc→ngang→dọc, chỉ thao tác theo phạm vi đã yêu cầu, xem xét ba đoạn section trước/giữa/sau, không đặt section break tùy tiện trong bảng và không tự thay đổi đầu/chân trang.

### 3.4. Phân biệt chuyển trang và chuyển cấu trúc bảng

- `LANDSCAPE_PAGE`: chỉ được thực hiện **theo yêu cầu người dùng**, thay orientation của section chứa bảng, giữ nguyên hàng/cột/nội dung. Quyền và an toàn là điều kiện riêng.
- `TABLE_RESTRUCTURE`: xoay trục, chuyển vị hoặc nhóm lại hàng/cột là sửa cấu trúc, cần yêu cầu và quyền riêng; không suy từ yêu cầu "trang ngang".
- `MOVE_TO_APPENDIX`: là quyết định sửa cấu trúc tài liệu khác; chỉ theo yêu cầu/phê duyệt riêng, không là mặc định khi bảng quá rộng.

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

## 6. Bộ 32 case gốc đã cập nhật và 16 biến thể kiểm thử quyền người dùng

**32 case ORI001–ORI032 giữ nguyên nội dung/tình huống cũ, bổ sung `orientation_request=UNSPECIFIED` và cập nhật nhãn theo mặc định dọc, không tự xoay trang.** Có bảng chuyển đổi nhãn cũ/mới ở `MIGRATION_V17_5_TO_V17_5_1.csv`. `assumed_required_width_mm` vẫn là **giả định, không đo font**.

| ID | Nhóm | Font | Số cột | Hướng do người dùng yêu cầu | Kết luận mới |
|---|---|---:|---:|---|---|
| ORI001 | `PLAN_ASSIGN` | 14 pt | 4 | `UNSPECIFIED` | `KEEP_PORTRAIT_DEFAULT` |
| ORI002 | `STAT_PERIOD` | 14 pt | 4 | `UNSPECIFIED` | `KEEP_PORTRAIT_DEFAULT` |
| ORI003 | `CALENDAR` | 14 pt | 5 | `UNSPECIFIED` | `KEEP_PORTRAIT_DEFAULT` |
| ORI004 | `PERSONNEL` | 14 pt | 4 | `UNSPECIFIED` | `KEEP_PORTRAIT_DEFAULT` |
| ORI005 | `COST_RESOURCE` | 13 pt | 5 | `UNSPECIFIED` | `KEEP_PORTRAIT_DEFAULT` |
| ORI006 | `APPENDIX_REGISTER` | 14 pt | 4 | `UNSPECIFIED` | `KEEP_PORTRAIT_DEFAULT` |
| ORI007 | `RISK_REMEDY` | 14 pt | 3 | `UNSPECIFIED` | `KEEP_PORTRAIT_DEFAULT` |
| ORI008 | `LEGAL_COMPARE` | 14 pt | 3 | `UNSPECIFIED` | `KEEP_PORTRAIT_DEFAULT` |
| ORI009 | `PLAN_ASSIGN` | 14 pt | 8 | `UNSPECIFIED` | `KEEP_PORTRAIT_WARN_WIDTH` |
| ORI010 | `PROGRESS_KPI` | 14 pt | 9 | `UNSPECIFIED` | `KEEP_PORTRAIT_WARN_WIDTH` |
| ORI011 | `STAT_PERIOD` | 13 pt | 10 | `UNSPECIFIED` | `KEEP_PORTRAIT_WARN_WIDTH` |
| ORI012 | `LEGAL_COMPARE` | 14 pt | 7 | `UNSPECIFIED` | `KEEP_PORTRAIT_WARN_WIDTH` |
| ORI013 | `CALENDAR` | 14 pt | 8 | `UNSPECIFIED` | `KEEP_PORTRAIT_WARN_WIDTH` |
| ORI014 | `PERSONNEL` | 14 pt | 8 | `UNSPECIFIED` | `KEEP_PORTRAIT_WARN_WIDTH` |
| ORI015 | `COST_RESOURCE` | 14 pt | 9 | `UNSPECIFIED` | `KEEP_PORTRAIT_WARN_WIDTH` |
| ORI016 | `APPENDIX_REGISTER` | 14 pt | 8 | `UNSPECIFIED` | `KEEP_PORTRAIT_WARN_WIDTH` |
| ORI017 | `PLAN_ASSIGN` | 14 pt | 7 | `UNSPECIFIED` | `KEEP_PORTRAIT_REVIEW_GEOMETRY` |
| ORI018 | `PROGRESS_KPI` | 14 pt | 8 | `UNSPECIFIED` | `KEEP_PORTRAIT_REVIEW_GEOMETRY` |
| ORI019 | `STAT_PERIOD` | 13 pt | 10 | `UNSPECIFIED` | `KEEP_PORTRAIT_REVIEW_GEOMETRY` |
| ORI020 | `LEGAL_COMPARE` | 14 pt | 6 | `UNSPECIFIED` | `KEEP_PORTRAIT_REVIEW_GEOMETRY` |
| ORI021 | `CALENDAR` | 14 pt | 7 | `UNSPECIFIED` | `KEEP_PORTRAIT_REVIEW_GEOMETRY` |
| ORI022 | `PERSONNEL` | 14 pt | 7 | `UNSPECIFIED` | `KEEP_PORTRAIT_REVIEW_GEOMETRY` |
| ORI023 | `RISK_REMEDY` | 14 pt | 6 | `UNSPECIFIED` | `KEEP_PORTRAIT_REVIEW_GEOMETRY` |
| ORI024 | `COST_RESOURCE` | 14 pt | 10 | `UNSPECIFIED` | `KEEP_PORTRAIT_REVIEW_GEOMETRY` |
| ORI025 | `OFFICIAL_PRESERVE` | 14 pt | 9 | `UNSPECIFIED` | `PRESERVE_LOCKED_REVIEW_AUTHORITY` |
| ORI026 | `OFFICIAL_PRESERVE` | 14 pt | 7 | `UNSPECIFIED` | `PRESERVE_LOCKED_REVIEW_AUTHORITY` |
| ORI027 | `PERSONNEL` | 14 pt | 8 | `UNSPECIFIED` | `PRESERVE_LOCKED_REVIEW_AUTHORITY` |
| ORI028 | `APPENDIX_REGISTER` | 14 pt | 8 | `UNSPECIFIED` | `PRESERVE_LOCKED_REVIEW_AUTHORITY` |
| ORI029 | `LEGAL_COMPARE` | 14 pt | 9 | `UNSPECIFIED` | `PRESERVE_LOCKED_REVIEW_AUTHORITY` |
| ORI030 | `PLAN_ASSIGN` | 14 pt | 8 | `UNSPECIFIED` | `PRESERVE_LOCKED_REVIEW_AUTHORITY` |
| ORI031 | `CALENDAR` | 14 pt | 7 | `UNSPECIFIED` | `PRESERVE_LOCKED_REVIEW_AUTHORITY` |
| ORI032 | `COST_RESOURCE` | 13 pt | 9 | `UNSPECIFIED` | `PRESERVE_LOCKED_REVIEW_AUTHORITY` |

**16 biến thể tăng cường** tại `orientation_user_request_variants_16.jsonl`:
- 8 biến thể ORI009–ORI016-L: người dùng yêu cầu ngang rõ ràng, vẫn kiểm tra section và quyền sửa.
- 4 biến thể ORI025–ORI028-L: yêu cầu ngang nhưng biểu mẫu/tài liệu vẫn bị khóa.
- 2 biến thể ORI001–ORI002-EXIST-L: tài liệu đã ngang nhưng **không** yêu cầu đổi → giữ ngang hiện hữu.
- 2 biến thể ORI003–ORI004-REQ-P: đang ngang, người dùng yêu cầu dọc → chỉ xem xét đổi về dọc.

**Tổng 48 ca dữ liệu cấu trúc**, không phải 48 lượt AI đã chạy hoặc 48 kết luận được chuyên gia xác nhận.

## 7. Thiết kế pilot V17.5.1 theo quyền quyết định orientation

- Mô hình benchmark 160 bảng gốc × 2 cặp × 2 thứ tự = 640 đầu vào **giữ nguyên là dự kiến**.
- Khi so sánh trang dọc và trang ngang, cần tạo **hai nhóm thử riêng**: (A) không có chỉ thị hướng, đáp án luôn **không tự xoay ngang**; (B) có yêu cầu ngang rõ ràng, mới được đánh giá khả năng xử lý thích hợp và rủi ro section.
- Cặp đối chứng **chỉ khác một biến**: `orientation_request` hoặc `orientation_current` theo từng loại kiểm tra. Không trộn thay đổi yêu cầu, width và font vào cùng một phép thử.
- Chấm riêng `unauthorized_landscape_rate` (mọi đề xuất hành động xoay ngang không có yêu cầu = lỗi), `user_intent_adherence`, `locked_form_preservation`, `section_scope_safety`, `portrait_overflow_detection`, `abstention_on_missing_geometry`.
- Không sử dụng giá trị đẹp/width giả định làm ủy quyền trang ngang. `EXPERT_GOLD_NOT_OBTAINED`, `FONT_METRIC_NOT_RUN`, `VISUAL_NOT_VERIFIED` vẫn giữ nguyên.

## 8. Bản tích hợp workbook/profile (chính sách khóa)

Các trường cần có: `orientation_request`, `orientation_request_source`, `orientation_current`, `orientation_default`, `orientation_change_authorized`, `orientation_change_scope`, `width_overflow_flag`, `section_impact_reviewed`, `form_lock_status`, `orientation_decision_reason`.

**Logic bắt buộc:** `UNSPECIFIED` → `PORTRAIT` cho bảng/tài liệu mới; `UNSPECIFIED` → **PRESERVE_CURRENT** cho DOCX hiện hữu; `EXPLICIT_LANDSCAPE` → chỉ xét landscape nếu user đã yêu cầu, quyền cho phép và section được kiểm soát; width overflow chỉ sinh cảnh báo, **không sinh yêu cầu landscape**. Không tự đổi từ 14 pt xuống 13 pt nếu profile không cho phép; TNR 13–14 pt. Handoff riêng: `WORKBOOK_PROFILE_HANDOFF.md`.

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

## 10. Giới hạn và QA (cập nhật V17.5.1)

- `NOT_RUN`: Chưa tiến hành bất kỳ phép suy luận AI mới, đo glyph, Word render, đánh giá chuyên gia hay thay đổi DOCX thực tế.
- `UNVERIFIED`: Ràng buộc width tối thiểu trong case nghiên cứu là dữ liệu giả định, không phải min-width TNR đã đo.
- `REVIEW_REQUIRED`: Tính áp dụng pháp lý với biểu mẫu chuyên ngành/phụ lục theo hồ sơ cụ thể; tính phù hợp trang ngang đối với chữ ký/page numbering khi thiếu section data.
- **QA đã chạy:** kiểm đếm 10 họ bảng/tổng 160 bảng **dự kiến**, 32 ca gốc + 16 biến thể, 48 ID không trùng, Times New Roman 13/14 pt, kiểm tra mọi case không có chỉ dẫn `EXPLICIT_LANDSCAPE` đều không nhận nhãn chuyển ngang; checksum, CSV/JSONL nhất quán. Không có kiểm định render, glyph hoặc AI mới.