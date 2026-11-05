# Kiểm soát phát hành và những việc chưa nghiệm thu

## Trạng thái tại nhánh kỹ thuật v0.1

- **Đã chạy:** kiểm thử đọc/sửa/ghi DOCX tổng hợp (pytest) với mock width proposal, đối chiếu cấu trúc và giữ nguồn nguyên bản.
- **Chưa chạy:** TNR thực dưới font fingerprint đã cấp phép, WPS/Microsoft Word Print Layout, corpus F01–F08 gốc, WordVN adapter.
- **Không tuyên bố:** v1.0, tương thích đầy đủ ND30/HD05, Word layout PASS, 128/152 kịch bản đã PASS.

## Gates

| Gate | Yêu cầu để v1.0 | Trạng thái ở technical preview |
|---|---|---|
| DATA | Bảo toàn số liệu, text, topology theo supported types | PASS synthetic subset (23 pytest, 05/11/2026) |
| OPC | Non-target parts và target non-width properties giữ nguyên | PASS synthetic subset (23 pytest, 05/11/2026) |
| AUTH | Bảng layout, locked/unknown bị loại; policy V17.5.1 | PASS synthetic subset (23 pytest, 05/11/2026) |
| GEO | Width candidate không vượt vùng có thể, không tự landscape | PASS synthetic subset (23 pytest, 05/11/2026); Word not verified |
| FONT | Shaping TNR thực và style cascade đầy đủ | PARTIAL, TNR runtime test NOT_RUN |
| PAGING | Header repeat/row split/trHeight xử lý theo quyền | First-row repeat + exact→atLeast row height opt-in structural PASS; row split DIAGNOSTICS_ONLY; Word NOT_RUN |
| COMPLEX | Merged/nested controlled support | NOT_IMPLEMENTED (PRESERVE) |
| L2-WORD | Print Layout Word không tràn/cắt | NOT_RUN |
| WPS/LO | Renderer đối chứng | NOT_RUN; tùy môi trường test |
| WORDVN | Adapter, preview, Undo | NOT_RUN / out-of-repo |
| RELEASE | Clean install, pin dependencies, reproducible binary + rollback | NOT_RUN |

**Nguyên tắc:** Có thể dùng CLI thử nghiệm cho phạm vi đã chứng minh; không đóng issue #7, #8, #11–#16 khi thiếu acceptance theo body issue. Không đóng những issue chỉ có tài liệu một phần.
