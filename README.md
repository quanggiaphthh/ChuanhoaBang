# ChuanhoaBang

**Kho tri thức nghiên cứu và đặc tả chuẩn hóa bảng trong tài liệu Word (DOCX)** theo thể thức văn bản hành chính và văn bản của Đảng tại Việt Nam.

## Phạm vi hiện tại

Repo lưu **bản nghiên cứu hợp nhất V15 (21/10/2026)**, các quy tắc đánh giá, định hướng tích hợp và bằng chứng thực nghiệm đã được mô tả trong báo cáo. **Đã có lõi DOCX thử nghiệm kỹ thuật ở PR #17; chưa nghiệm thu Microsoft Word hay phát hành v1.0.**

- Văn bản hành chính: Nghị định 30/2020/NĐ-CP.
- Văn bản của Đảng: Quy định 399-QĐ/TW và Hướng dẫn 05-HD/VPTW năm 2026.
- Bảng nội dung, bảng thống kê, phụ lục, biểu mẫu, ô gộp, bảng lồng, bảng nhiều trang và bảng có yêu cầu bảo toàn cấu trúc.
- Tối ưu chiều rộng cột theo vai trò/ngữ nghĩa, nhu cầu hiển thị, hình học trang và kết quả kết xuất.

## Tài liệu chính

| Đường dẫn | Nội dung |
|---|---|
| [Báo cáo nghiên cứu hợp nhất V15](docs/research/Bao_cao_chuan_hoa_va_toi_uu_bang_DOCX_ND30_HD05_V15_2026.md) | Toàn bộ nghiên cứu V1–V15, 31 phần, 248 mục, 103 nguồn tham khảo, 152 kịch bản **đặc tả** |
| [Tổng hợp kiểm chứng V10–V15](docs/verification/EXPERIMENT_EVIDENCE.md) | Kết quả, điều kiện và giới hạn của các phép thử |
| [Lộ trình tích hợp tối thiểu](docs/implementation/ROADMAP.md) | Audit → reuse → thử nghiệm → sửa giới hạn → nghiệm thu |
| [Quy tắc đóng góp và bảo toàn](AGENTS.md) | Authority, ràng buộc, phạm vi, chứng cứ |
| [Lịch sử nghiên cứu](CHANGELOG.md) | Các bước V1–V15 và trạng thái |

## Mức độ tin cậy

1. **Pháp lý:** Chỉ những điều khoản có căn cứ rõ ràng mới được gọi là bắt buộc.
2. **Nghiệp vụ/thẩm mỹ:** Preset như Formal Grid, Statistical Minimal là khuyến nghị, không phải quy định pháp lý.
3. **Bảo toàn:** Không đổi số liệu, thứ tự, ô gộp, bảng lồng hoặc biểu mẫu gốc chỉ nhằm nâng điểm thẩm mỹ.
4. **Thực nghiệm:** Các phép thử từ V10–V15 sử dụng DOCX tổng hợp và LibreOffice; **chưa xác nhận bằng Microsoft Word**.
5. **Triển khai:** Có core offline thử nghiệm trên nhánh PR #17, chỉ xử lý phạm vi đã kiểm chứng; không phải ứng dụng định dạng Word hoàn chỉnh.

## Dùng báo cáo để triển khai

Đọc [ROADMAP](docs/implementation/ROADMAP.md), đối chiếu đầu vào/sự cho phép thay đổi và xác định mức bằng chứng. Không viết lại trình xử lý OOXML, không bổ sung hệ thống song song nếu thành phần hiện có đáp ứng; yêu cầu kết xuất cùng môi trường và diff bảo toàn trước khi chấp nhận thay đổi.

## Dữ liệu thực nghiệm

Các gói DOCX/PDF thử nghiệm V10–V15 đã được tạo trong quá trình nghiên cứu, nhưng **không mặc nhiên được coi là đã lưu trữ trong GitHub**. Danh mục, kết quả và điều kiện tái lập nằm trong báo cáo V15 và [hồ sơ kiểm chứng](docs/verification/EXPERIMENT_EVIDENCE.md). Trước khi công bố các gói nhị phân, cần đối chiếu SHA-256 và bảo đảm nguồn tệp được chuyển nguyên vẹn.

## Trạng thái

**RESEARCH + TECHNICAL PREVIEW (PR #17) — WORD ACCEPTANCE PENDING**.

Giữ một tài liệu hợp nhất làm nguồn tham chiếu thay vì sao chép các phiên bản cũ nhiều lần. Không nhầm 152 kịch bản được đặc tả với 152 test đã chạy PASS.

## Cập nhật nghiên cứu 29/10/2026 — V17.4 → V17.5.1

- **Bản đang áp dụng:** [V17.5.1 — Hướng trang do người dùng quyết định](docs/research/V17_5_1/README.md). Bảng/tài liệu mới mặc định **A4 DỌC**; chỉ xem xét đổi sang **A4 NGANG khi người dùng yêu cầu rõ**. Không tự đổi do bảng rộng/nhiều cột. DOCX hiện có thì giữ nguyên orientation nếu không yêu cầu sửa.
- [V17.5 — nghiên cứu bảng hành chính và landscape](docs/research/V17_5/README.md) là tiền nhiệm lịch sử, phần quyền tự đổi orientation đã bị V17.5.1 thay thế.
- [Pilot mô phỏng V17.4](docs/verification/V17_4/pilot/README_PILOT.md): 128 đầu vào, baseline tổng hợp, **không phải độ chính xác mô hình**.
- [Hậu kiểm Antigravity V17.4](docs/verification/V17_4/scoring/V17_4_INDEPENDENT_FILE_AUDIT_REPORT.md): 128 phản hồi báo cáo, đối chiếu **SPEC**, blind/expert-gold vẫn BLOCKED; model provider chưa xác thực độc lập.
- [Tình trạng dữ liệu và gói kết quả](docs/verification/V17_4/POSTPILOT_INDEX.md). Raw payload ZIP và khóa đáp án riêng không được đưa vào GitHub để hạn chế lộ private key và dữ liệu máy người dùng.

**Ranh giới nghiệm thu không đổi:** nghiên cứu là nguồn quy tắc, core chỉ là TECHNICAL PREVIEW; Times New Roman **13–14 pt**; không tự thay đổi dữ liệu, biểu mẫu khóa hoặc hướng trang; không tuyên bố đã nghiệm thu Microsoft Word.


## Core DOCX offline — bản thử nghiệm kỹ thuật (PR #17)

- [Hướng dẫn CLI](RUN_TOOL.md) · [Quyết định kiến trúc](docs/implementation/ARCHITECTURE_DECISION.md) · [Bảng trạng thái 16 issue](docs/implementation/ISSUE_EXECUTION_STATUS_2026-11-05.md).
- Có `audit`, `propose` độ rộng bảng dữ liệu đơn giản và `apply` theo đề xuất được cấp quyền; `propose-header` lặp tiêu đề đầu và `propose-unclip` giảm rủi ro chiều cao hàng `exact`.
- Audit ghi riêng `tblW`, `tcW` từng ô và tổng `tblGrid`; chỉ giá trị `dxa` được ghi nhận theo twips. Width sai cấu trúc chuyển bảng sang `REVIEW_REQUIRED`; độ rộng Word thực tế luôn `NOT_RUN`.
- **Bảng có ô gộp hoặc ô lưới bị bỏ qua:** audit ghi vị trí cột lưới logic/span của từng ô; ô có `vMerge` ghi marker `RESTART`/`CONTINUE` và kết quả kiểm tra marker tiếp diễn theo hàng; hàng khai báo `gridBefore`/`gridAfter` ghi số cột lưới bỏ qua. Các kiểm tra này chỉ dùng XML, không xác nhận hình học Word hay hành vi gộp khi render. Bảng có ô gộp hoặc ô bị bỏ qua vẫn `REVIEW_REQUIRED`; chỉ thao tác header-repeat/row-height giới hạn mới nhận `gridSpan` ngang hợp lệ và không áp dụng khi có hàng bỏ qua ô. Khai báo lưới sai, mơ hồ và bảng lồng bị chặn.
- Body-table audit/proposal JSON and Markdown, plus non-body story audit entries, expose source-only `role_classification`: `NESTED`, `OFFICIAL_FORM_CANDIDATE`, `LAYOUT_CANDIDATE`, `DATA_CANDIDATE` or `UNKNOWN`, with evidence codes and matched terms from a fixed hint list. Reports do not copy arbitrary cell text into the matched-term list. This is candidate evidence only: it establishes no legal authority, effective story ownership, or edit permission. Non-body tables remain `REVIEW_REQUIRED` and outside body table indices.
- Nested table entries and body proposals also report `parent_cell_location` with zero-based row/cell indexes when that immediate source-XML location resolves; `apply` rechecks the locator with the table proposal. Unsupported topology returns `UNRESOLVED`. This is a locator, not effective ownership or edit authority.
- Audit JSON và Markdown ghi `border_evidence` cho `tblBorders`/`tcBorders` trực tiếp ở body và story tables, gồm cạnh, thuộc tính, vị trí hàng/ô 0-based. Khai báo cạnh/thuộc tính không hỗ trợ hoặc trùng trả `UNRESOLVED`; inheritance style/theme là `NOT_RESOLVED`, `word_render` là `NOT_RUN`. Đây chỉ là kiểm kê source XML, không áp dụng hay xác nhận kiểu viền có hiệu lực.
- Audit JSON/Markdown and proposals report direct `w:tblLayout` declarations (`fixed`/`autofit`) for body and story tables without resolving effective Word layout. Missing declarations do not imply a Word default; duplicate table properties/layout elements or unsupported values/content are `UNRESOLVED` and block width proposals.
- Audit JSON/Markdown and proposals also report direct `w:bidiVisual` state. Active right-to-left visual order and unresolved or duplicate markers block width proposals; explicit off values are reported. The tool does not reorder source cells, and effective direction/Word rendering remain unresolved or `NOT_RUN`.
- Audit JSON/Markdown and proposals report direct `w:tblCellSpacing`. Only an explicit `dxa` value of zero is in the width-metric subset; nonzero spacing and unsupported/ambiguous values require review because spacing is not included in the solver. Effective spacing remains unresolved.
- **Bằng chứng CI đã xác minh gần nhất:** PR commit [`c00363e`](https://github.com/quanggiaphthh/ChuanhoaBang/commit/c00363e0fb596e424afc701a1d61742b0688bc16) — [GitHub Actions 42164914928](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42164914928): **196/196 tests PASS** trên Ubuntu/Python 3.10–3.13 và Windows/Python 3.12. Cả sáu job thành công; năm target qua hash-enforced offline install, CLI audit và wheel smoke. Canonical wheel SHA-256 `f883c18dbc1a76e9be36000e65a67ebd0eb2fa8b257311161c7617985dadaf5f`; preview artifact `chuanhoabang-preview-db51fa7c3b4c35e792785268619f5ba491467038` hết hạn 20/11/2026. Microsoft Word/WPS và fixture gốc vẫn `NOT_RUN`/chưa có.
- Với `propose --profile ND30|HD05`, `profile_constraints` hiện ghi cỡ chữ đo được, căn cứ lựa chọn của dự án và URL/locator nguồn chính thức trong registry. `REFERENCE_ONLY` và `profile_rules_applied: false` vẫn được giữ; đây chưa phải bộ preset pháp lý đầy đủ. `apply` tái xác minh toàn bộ constraint nguồn của proposal.
- Audit hỗ trợ cặp margin baseline `basedOn` table style trong phạm vi nêu ở [hướng dẫn CLI](RUN_TOOL.md); style conditional/không rõ vẫn `UNRESOLVED`, width proposal có mọi table style vẫn bị từ chối. `apply` trả `NO_OP_VALID` khi output đã có khớp byte với candidate được tái tạo và kiểm tra; tệp khác, không thường hoặc symlink không bị ghi đè. `audit` theo internal document relationship để inventory header/footer/footnotes/endnotes cả khi tên part tùy biến; first/even refs có activation và inheritance candidate từ XML nguồn. Bảng trong footnote/endnote kèm `note_reference` (ID, trạng thái và số lần khớp trong document body XML). Các trường này là bằng chứng nguồn; ownership/rendering hiệu lực trong Word vẫn chưa xác nhận. Malformed, external và ambiguous relationship không được gán owner. Tests dùng DOCX tổng hợp và metric font giả lập; Microsoft Word fit vẫn `NOT_RUN`.
- Khi không có cặp margin ngang trực tiếp hoặc từ style chain được hỗ trợ, width metric dùng `padding_twips_assumed=240` tổng trái/phải (120 twips mỗi phía, khoảng 2,12 mm), được version trong policy registry. Metric ghi `null` khi không cần fallback. Đây là giả định estimator theo gợi ý nội bộ V15, không phải margin mặc định của Word hay kết quả rendering.
- CI tạo wheelhouse runtime riêng cho Linux/Python 3.10–3.13 và Windows/Python 3.12; mỗi artifact chứa wheel ứng dụng, dependency wheels tải theo hash, install requirements và manifest target/install. Artifacts mới nhất `chuanhoabang-offline-*-9fa1dbb704229bf85fd8b520708892a876fed30d` được giữ đến **20/11/2026**. Xem [hướng dẫn cài offline](RUN_TOOL.md). Microsoft Word acceptance vẫn **NOT_RUN**.
- Bộ phân loại quét marker bố cục/chữ ký trên toàn bộ ô và chuẩn hóa các dấu gạch Unicode phổ biến; bước xuất bản DOCX dùng hard link nguyên tử để không ghi đè tệp xuất hiện sau bước kiểm tra đường dẫn.
- Registry gate đo width dùng ND30 13/14 pt và HD05 14 pt; section cột đều cần spacing tường minh, còn cột tùy biến cần `equalWidth=0`, số phần tử và `num` khớp, width dương, gap giữa các cột tường minh và tổng hình học nằm trong vùng chữ. Khi chưa xác định vị trí bảng, dùng cột hẹp nhất làm bound bảo thủ; bảng floating/indented, margin không hỗ trợ, và table-style margin ngoài subset trên vẫn giữ review-only; bound cấu trúc không phải Word acceptance.
- `audit` đánh index chỉnh sửa riêng cho bảng trong body; bảng ở header/footer/footnotes/endnotes được ghi riêng kèm part, story type, hash và liên kết section trực tiếp. Internal relationships cho phép part name tùy biến; bảng story vẫn `REVIEW_REQUIRED` và không nhận `--table` để sửa. Bảng liên kết mặc định cùng loại có thêm ứng viên kế thừa giữa section. Reference `first`/`even` có trạng thái kích hoạt từ `w:titlePg`/`w:evenAndOddHeaders` và ứng viên kế thừa khi control section đang bật. Table trong note part có ID definition và count của `footnoteReference`/`endnoteReference` khớp trong `word/document.xml` body; `NO_BODY_REFERENCE_FOUND` chỉ nói không thấy trong phạm vi đó. Đây là bằng chứng/candidate từ source XML, không xác nhận ownership hiệu lực hay rendering trong Word.
- Artifact preview `chuanhoabang-preview-4b00609c824f62149eaa9adc04b96a9243ddb3a8` được giữ đến 20/11/2026.
- Microsoft Word acceptance: **NOT_RUN**. Executor hiện phân giải tên TNR thành Liberation Serif; chưa có phép đo bằng TNR có bản quyền. Fixture F01–F08 gốc hiện chưa truy xuất được. Không dùng CI hoặc LibreOffice thay cho Word acceptance.
- **Mốc lịch sử:** GitHub Actions tại commit `c518e5070d115806bf42003ffe8d36fcf4f45c3d` chạy 43 test cấu trúc PASS; đây không phải kết quả hiện tại hoặc Word acceptance.
