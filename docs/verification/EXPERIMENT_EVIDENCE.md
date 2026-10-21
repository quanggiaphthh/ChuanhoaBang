# Hồ sơ bằng chứng nghiên cứu V10–V15

**Cập nhật:** 21/10/2026. Các kết quả dưới đây là kiểm tra thực nghiệm trên **DOCX tổng hợp** (thường dùng LibreOffice 25.2 để kết xuất), không phải nghiệm thu Microsoft Word. Mọi số liệu cần được đọc cùng điều kiện thử và giới hạn trong báo cáo V15.

## Ma trận phát hiện

| Phiên bản | Bộ thử / đặc điểm | Quan sát nổi bật | Không chứng minh được |
|---|---|---|---|
| V10 | 8 fixture F01–F08; lỗi hàng `Exactly` F08 | Sửa tối thiểu `exact → atLeast` giúp hiện phần chữ trước đó bị che trong thử nghiệm | An toàn áp dụng đại trà; Word tương đương LibreOffice |
| V11 | F01 bảng công việc và F02 bảng thống kê | F01 chiều cao từ **72,46 → 46,11 mm** (cấu hình 14–76–38–37 mm); F02 có ứng viên làm tăng chiều cao từ **30,27 → 35,56 mm** nên phải giữ baseline | Tự nhận diện mọi cột ngữ nghĩa / mọi độ rộng tối ưu |
| V12 | F03–F07: bảng dài, tiêu đề gộp, bảng lồng, biểu mẫu, trang ngang | F03 giảm **6 → 4 trang**; giữ hàng ngắn không tách qua trang trong bộ thử; F07 chiều cao **98,14 → 45,40 mm**; F04/F05 không có lợi ích rõ; F06 giữ nguyên | Rằng ít trang luôn đẹp hơn; cấm ngắt hàng dài là an toàn |
| V13 | Thử độ bền khi tăng cỡ chữ; kiểm tra thay đổi lề | F03 tối ưu vẫn 4 trang tại +1 pt; kiểm tra F07 cho thấy phương án rộng ~252 mm không còn vừa vùng ~242 mm | Độ bền với mọi cỡ chữ/phông/lề và Word |
| V14 | F07 tái phân bổ trong vùng ~242 mm | Các ứng viên đạt chiều rộng danh nghĩa 240–242 mm, không tăng chiều cao trên môi trường thử; không thể xếp hạng tuyệt đối khi đồng điểm | Một phép đo PDF là đủ để chọn phương án tối ưu |
| V15 | 24 biến thể thay đổi lề phải 0–5 mm với bốn chiến lược | **6/24** đạt hình học danh nghĩa, **10/24** có viền PDF chưa vượt lề; **4/24** viền PDF còn trong lề nhưng lưới DOCX đã vượt | Hình ảnh PDF vừa lề đồng nghĩa hình học DOCX an toàn |

### Các cổng nghiệm thu bắt buộc

| Gate | Điều kiện | Trạng thái nghiên cứu |
|---|---|---|
| G0 | Căn cứ pháp lý, profile mẫu, thẩm quyền sửa | Cần đối chiếu theo tài liệu thực tế |
| G1 | Không mất/thay dữ liệu, grid/merge, công thức, đối tượng và quan hệ OPC | Đã kiểm trong phạm vi fixture; chưa kiểm mọi cấu trúc |
| G2 | Hình học DOCX hợp lệ tại section/lề/hướng trang cụ thể | Đã phát hiện và đo các tình huống biên |
| G3 | Render Word/Print Layout không cắt/tràn và đáp ứng nhiệm vụ đọc | **NOT_RUN / chưa có Word acceptance** |
| G4 | Bản cải thiện hơn baseline hoặc `NO_OP_VALID`; thay đổi tối thiểu | Một số ứng viên tốt hơn trong LibreOffice; chưa có ngưỡng Word hiệu chỉnh |

### Trạng thái test

- **152 trường hợp T01–T152:** đặc tả kiểm thử trong báo cáo V15, **không phải** toàn bộ đã chạy.
- **V10–V15:** có thực nghiệm trên fixture giả lập và đối chứng, nhưng không suy rộng sang tài liệu thực tế.
- Chưa chứng minh tích hợp vào engine hiện hành hoặc tương thích Microsoft Word.
- Có thể không thấy chuỗi liên tục trong PDF vì bị chia trang; phải phân xử bằng cấu trúc DOCX, dữ liệu và bản in, không kết luận mất dữ liệu từ text extraction đơn lẻ.

## Gói kiểm chứng được tạo trong quá trình nghiên cứu

Các gói sau có trong lịch sử công việc, **chưa phải nội dung nhị phân được đẩy lên repo này**. SHA-256 để đối chiếu khi nhập vào GitHub hoặc kho artifact có kiểm soát:

| Gói | Kích thước (bytes) | SHA-256 |
|---|---:|---|
| `Table_DOCX_V10_Benchmark_8_Fixtures.zip` | 603594 | `4968b11006389451f6dc96cd3ec2b5ba60b19879c5f319eb231619b8a01980c8` |
| `Table_DOCX_V11_Width_Experiment.zip` | 1307597 | `974c192ce99adb133fe46a939305bebcce2370556b429b0ed7b75139a7ef52c6` |
| `Table_DOCX_V12_Cross_Type_Experiment.zip` | 3549006 | `df74705cf5675705c455dd020c6a47b3ebb56d1464aae520e6dc71493c0a6747` |
| `Table_DOCX_V13_Robustness_Experiment.zip` | 2454388 | `25641b3f81848397aaa8c67142c072dc8fefbaf22dcf980a1bea2cf04c89cfe2` |
| `Table_DOCX_V14_Margin_Refit_Experiment.zip` | 1264406 | `c628523fbaa3add3374be7306dd3f43121d8cfae924c318188165ec560c644da` |
| `Table_DOCX_V15_Boundary_Sensitivity.zip` | 2739669 | `5ba909f5760dcdaac55c500e533c3f9ef2edab107d07c3d96565de4dd9b70b07` |

> Không thay thế nhị phân bằng liên kết sandbox trong tài liệu GitHub: đường dẫn sandbox chỉ thuộc phiên làm việc, không phải URL công khai bền vững.

## Cần làm trước khi nghiệm thu Word

- Chốt hệ điều hành, Microsoft Word phiên bản/build, font thực tế, máy in/thiết lập PDF, trang A4 dọc/ngang và chế độ in một/hai mặt.
- Chạy lại đúng các fixture biên F03, F07, F08 và bốn trường hợp xung đột DOCX-vs-PDF từ V15.
- Kiểm tra row split, repeated header, cảnh báo overflow; diff nội dung và OPC.
- Ghi `render_engine`, `engine_version`, `input_sha256`, `candidate_sha256`, `section_geometry`, `baseline_metrics`, `candidate_metrics`, `decision`, `proof_files`.
- Không mở rộng module khác nếu blast radius đã được kiểm soát.
