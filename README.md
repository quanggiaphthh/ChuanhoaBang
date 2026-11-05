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
- **Bảng có gộp ngang `gridSpan`:** chỉ cho phép hai thao tác phân trang không thay đổi độ rộng khi mọi hàng phủ kín lưới vật lý; gộp dọc `vMerge`, lưới sai, nested và AutoFit bảng gộp **vẫn được chặn**.
- **Bằng chứng code mới nhất:** PR commit [`754d05f`](https://github.com/quanggiaphthh/ChuanhoaBang/commit/754d05fe2e322502bc6b2df537c25a38960ddf41) — [GitHub Actions 42119947056](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42119947056): **129/129 tests PASS** trên Ubuntu/Python 3.10–3.13 và Windows/Python 3.12. Audit có bound cho cột đều và cột tùy biến; MCE, permission/protection states, signed OPC package parts và macro parts fail closed; `apply` chặn proposal cũ sau khi package có marker khóa; audit báo ứng viên kế thừa header/footer mặc định cùng loại nhưng giữ trạng thái review, đồng thời không suy diễn kế thừa default từ header `first` trực tiếp; bảng floating/indent bị chặn; direct left/right `dxa` margins tại table/cell level được đưa vào bound từng ô, còn margin không hỗ trợ chuyển sang review; line estimate giữ NBSP/figure-space glue unbroken. Word fit vẫn `NOT_RUN`. Runner Ubuntu/Python 3.12 độc lập tái tạo wheel SHA-256 `b1890d8ed918b26d5d36ffbf306f24eff1f5c6a7396bda3fd24a01181bff59f9`. Bài test dùng DOCX tổng hợp và metric font giả lập.
- Width metric vẫn trả `padding_twips_assumed=150` cho ô không có margin ngang trực tiếp để kế thừa; đây là giả định estimator, không phải margin cascade hoặc Word rendering đã xác minh.
- CI tạo wheelhouse runtime riêng cho Linux/Python 3.10–3.13 và Windows/Python 3.12; mỗi artifact chứa wheel ứng dụng, dependency wheels tải theo hash, install requirements và manifest target/install. Artifacts `chuanhoabang-offline-*-06132a7adfde1b26dd05dc604a70c7f9162a49cd` được giữ đến **19/11/2026**. Xem [hướng dẫn cài offline](RUN_TOOL.md). Microsoft Word acceptance vẫn **NOT_RUN**.
- Bộ phân loại quét marker bố cục/chữ ký trên toàn bộ ô và chuẩn hóa các dấu gạch Unicode phổ biến; bước xuất bản DOCX dùng hard link nguyên tử để không ghi đè tệp xuất hiện sau bước kiểm tra đường dẫn.
- Registry gate đo width dùng ND30 13/14 pt và HD05 14 pt; section cột đều cần spacing tường minh, còn cột tùy biến cần `equalWidth=0`, số phần tử và `num` khớp, width dương, gap giữa các cột tường minh và tổng hình học nằm trong vùng chữ. Khi chưa xác định vị trí bảng, dùng cột hẹp nhất làm bound bảo thủ; bảng floating/indented và margin không hỗ trợ vẫn review-only; bound cấu trúc không phải Word acceptance.
- `audit` đánh index chỉnh sửa riêng cho bảng trong body; bảng ở header/footer/footnotes/endnotes được ghi riêng kèm part, hash và liên kết section trực tiếp. Bảng liên kết mặc định cùng loại có thêm ứng viên kế thừa giữa section; đây không phải xác nhận ownership, các bảng story vẫn `REVIEW_REQUIRED` và không nhận `--table` để sửa. Test bảo đảm header `first` trực tiếp không bị dùng làm ứng viên kế thừa default; ownership trang first/even và footnote/endnote chưa được phân giải.
- Artifact preview `chuanhoabang-preview-06132a7adfde1b26dd05dc604a70c7f9162a49cd` được giữ đến 19/11/2026.
- Microsoft Word acceptance: **NOT_RUN**. Executor hiện phân giải tên TNR thành Liberation Serif; chưa có phép đo bằng TNR có bản quyền. Fixture F01–F08 gốc hiện chưa truy xuất được. Không dùng CI hoặc LibreOffice thay cho Word acceptance.
- **Mốc lịch sử:** GitHub Actions tại commit `c518e5070d115806bf42003ffe8d36fcf4f45c3d` chạy 43 test cấu trúc PASS; đây không phải kết quả hiện tại hoặc Word acceptance.
