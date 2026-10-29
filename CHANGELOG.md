# Lịch sử nghiên cứu

Bản chuẩn hiện hành là **[V15 hợp nhất](docs/research/Bao_cao_chuan_hoa_va_toi_uu_bang_DOCX_ND30_HD05_V15_2026.md)**. Không sao chép toàn bộ nội dung các phiên bản trước thành 15 bản nguồn sự thật song song.

| Phiên bản | Trọng tâm được tích hợp |
|---|---|
| V1 | Quy định thể thức ND30/HD05, so sánh, ngoại lệ, best practice thẩm mỹ |
| V2 | Kiến trúc quy tắc, phân loại, phân trang, 30 tình huống thử nghiệm đề xuất |
| V3 | Semantic priority và nhu cầu chiều rộng theo nội dung trọng tâm |
| V4 | Tối ưu cấp ô/hàng/bảng/trang, so sánh baseline/ứng viên |
| V5 | Quy trình quyết định, giữ nguyên khi thiếu chứng cứ, OPC preservation |
| V6 | Benchmark, hiệu chỉnh ngưỡng, các tầng bằng chứng và gate nghiệm thu |
| V7 | Hợp đồng dữ liệu vận hành, grid/merge, style và bảng phức tạp |
| V8 | Fixed/AutoFit, floating table, môi trường kết xuất, mô hình G0–G4 |
| V9 | Unicode line breaking, gridlines/borders, tránh tối ưu giả |
| V10 | 8 DOCX fixture tổng hợp, lỗi cắt chữ `Exactly` và sửa minh họa |
| V11 | Thử có đối chứng F01/F02; phân bổ chiều rộng theo nội dung |
| V12 | Thử F03–F07; bảng nhiều trang, bảng gộp, biểu mẫu, row split |
| V13 | Thử cỡ chữ, đổi lề và khả năng duy trì hiệu quả |
| V14 | Thu hẹp vùng trang, so sánh các chính sách refit |
| V15 | 24 biến thể ranh giới lề, phân biệt gate hình học và PDF |

**Hiện trạng V15:** 31 phần, 248 mục nghiên cứu, 103 nguồn tham khảo; **152 kịch bản được đặc tả**, không phải 152 kịch bản đã chạy. Thử nghiệm LibreOffice trên DOCX giả lập có một số kết quả PASS trong phạm vi nêu ở báo cáo; Microsoft Word và sản phẩm thực tế vẫn **chưa nghiệm thu**.

**2026-10-21 — Khởi tạo repo nghiên cứu:** thêm báo cáo hợp nhất, chỉ dẫn, lịch sử, kế hoạch reuse-first và hồ sơ kiểm chứng. Không triển khai engine DOCX.


**2026-10-29 — Research update V17.4–V17.5.1:** Bổ sung synthetic pilot V17.4, hậu kiểm đối chiếu 128 phản hồi Antigravity (nhãn SPEC, không phải expert gold); nghiên cứu 10 họ bảng hành chính/DNNN/Đảng, 32 case orientation và 16 biến thể. **V17.5.1 supersedes V17.5 về orientation:** default portrait cho bảng mới, giữ nguyên section hiện hữu, chỉ người dùng mới yêu cầu chuyển ngang. Không render, chưa có nghiệm thu Microsoft Word hay blind validation độc lập.
