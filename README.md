# ChuanhoaBang

**Kho tri thức nghiên cứu và đặc tả chuẩn hóa bảng trong tài liệu Word (DOCX)** theo thể thức văn bản hành chính và văn bản của Đảng tại Việt Nam.

## Phạm vi hiện tại

Repo lưu **bản nghiên cứu hợp nhất V15 (21/10/2026)**, các quy tắc đánh giá, định hướng tích hợp và bằng chứng thực nghiệm đã được mô tả trong báo cáo. **Chưa phải công cụ định dạng DOCX đã triển khai hoặc nghiệm thu.**

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
5. **Triển khai:** Chưa có bộ định dạng tự động được triển khai trong repo này.

## Dùng báo cáo để triển khai

Đọc [ROADMAP](docs/implementation/ROADMAP.md), đối chiếu đầu vào/sự cho phép thay đổi và xác định mức bằng chứng. Không viết lại trình xử lý OOXML, không bổ sung hệ thống song song nếu thành phần hiện có đáp ứng; yêu cầu kết xuất cùng môi trường và diff bảo toàn trước khi chấp nhận thay đổi.

## Dữ liệu thực nghiệm

Các gói DOCX/PDF thử nghiệm V10–V15 đã được tạo trong quá trình nghiên cứu, nhưng **không mặc nhiên được coi là đã lưu trữ trong GitHub**. Danh mục, kết quả và điều kiện tái lập nằm trong báo cáo V15 và [hồ sơ kiểm chứng](docs/verification/EXPERIMENT_EVIDENCE.md). Trước khi công bố các gói nhị phân, cần đối chiếu SHA-256 và bảo đảm nguồn tệp được chuyển nguyên vẹn.

## Trạng thái

**RESEARCH / SPECIFICATION — NOT IMPLEMENTED — WORD ACCEPTANCE PENDING**.

Giữ một tài liệu hợp nhất làm nguồn tham chiếu thay vì sao chép các phiên bản cũ nhiều lần. Không nhầm 152 kịch bản được đặc tả với 152 test đã chạy PASS.

## Cập nhật nghiên cứu 29/10/2026 — V17.4 → V17.5.1

- **Bản đang áp dụng:** [V17.5.1 — Hướng trang do người dùng quyết định](docs/research/V17_5_1/README.md). Bảng/tài liệu mới mặc định **A4 DỌC**; chỉ xem xét đổi sang **A4 NGANG khi người dùng yêu cầu rõ**. Không tự đổi do bảng rộng/nhiều cột. DOCX hiện có thì giữ nguyên orientation nếu không yêu cầu sửa.
- [V17.5 — nghiên cứu bảng hành chính và landscape](docs/research/V17_5/README.md) là tiền nhiệm lịch sử, phần quyền tự đổi orientation đã bị V17.5.1 thay thế.
- [Pilot mô phỏng V17.4](docs/verification/V17_4/pilot/README_PILOT.md): 128 đầu vào, baseline tổng hợp, **không phải độ chính xác mô hình**.
- [Hậu kiểm Antigravity V17.4](docs/verification/V17_4/scoring/V17_4_INDEPENDENT_FILE_AUDIT_REPORT.md): 128 phản hồi báo cáo, đối chiếu **SPEC**, blind/expert-gold vẫn BLOCKED; model provider chưa xác thực độc lập.
- [Tình trạng dữ liệu và gói kết quả](docs/verification/V17_4/POSTPILOT_INDEX.md). Raw payload ZIP và khóa đáp án riêng không được đưa vào GitHub để hạn chế lộ private key và dữ liệu máy người dùng.

**Phạm vi không đổi:** RESEARCH / SPEC ONLY; Times New Roman **13–14 pt**; không tự thay đổi dữ liệu, biểu mẫu khóa hoặc hướng trang; không tuyên bố đã nghiệm thu Microsoft Word.
