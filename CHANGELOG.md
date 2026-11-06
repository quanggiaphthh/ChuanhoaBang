# Lịch sử nghiên cứu và ghi chú phiên bản

## Lịch sử nghiên cứu

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

## Nhật ký phiên bản kỹ thuật

### `0.1.0.dev0` — technical preview trên PR #17, chưa phát hành

- Cung cấp CLI/API offline để audit, lập proposal và apply có xác nhận cho tập bảng DOCX giới hạn; ND30/HD05 được ghi nhận là `REFERENCE_ONLY`, chưa áp dụng preset pháp lý đầy đủ.
- Audit JSON/Markdown tách độ rộng `tblW`/`tcW` khai báo khỏi tổng lưới `tblGrid`; khai báo width lỗi chuyển sang `REVIEW_REQUIRED`. Section nhiều cột đều có spacing tường minh dùng bound dưới cho từng cột. Cột tùy biến chỉ được dùng khi `equalWidth=0`, `col` count/width/spacing được khai báo đủ và hình học nằm trong vùng chữ; optimizer dùng width cột hẹp nhất khi vị trí bảng chưa xác định. `AlternateContent`, permission ranges, protection, signed OPC package parts and macro parts fail closed; line estimate does not break NBSP/figure-space glue. Microsoft Word rendering remains `NOT_RUN`.
- Audit gán ID xác định theo phạm vi/chỉ số/hash và liên kết bảng lồng với ID của bảng cha trong body lẫn header/footer story; liên kết section mặc định cùng loại được báo thêm dưới dạng ứng viên kế thừa read-only. Các chỉ số body dùng cho `--table` vẫn giữ nguyên.
- CI tạo wheelhouse theo Linux/Python 3.10–3.13 và Windows/Python 3.12. `offline-install-requirements.txt` pin SHA-256 của ứng dụng và runtime dependencies; cài sạch với `pip --no-index --require-hashes`, audit DOCX tiếng Việt, và **129/129 tests PASS** trên cả năm target trong [run 42119947056](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42119947056). Regression xác nhận direct `dxa` table/cell margins ảnh hưởng bound per-cell; margin không hỗ trợ bị từ chối.
- Runner Ubuntu/Python 3.12 độc lập tái tạo canonical wheel cùng SHA-256 `b1890d8ed918b26d5d36ffbf306f24eff1f5c6a7396bda3fd24a01181bff59f9`. Artifacts `chuanhoabang-preview-06132a7adfde1b26dd05dc604a70c7f9162a49cd` và `chuanhoabang-offline-*` được giữ đến 19/11/2026.
- Audit reports a bounded table-style margin baseline when the explicit `basedOn` chain is unambiguous and contains only complete left/right `dxa` pairs without conditional margins. JSON/Markdown show the style chain and margin source; unsupported style cases remain unresolved, and width proposals continue to refuse all table styles.
- Reapplying a proposal returns `NO_OP_VALID` only when the requested output is a regular non-symlink file byte-identical to the candidate that was regenerated and revalidated. Other existing outputs are never overwritten.
- Code CI [run 42133659528](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42133659528), before source activation coverage, passed **148/148 tests** on Ubuntu/Python 3.10–3.13 and Windows/Python 3.12; independent canonical wheel SHA-256 `469f91db5df4a251da576b4aa353f62ff82c8d6e9476850a3861880046402833`.
- Commit `5b179f1` adds read-only inventory of custom-named header/footer parts linked by internal document relationships. External or malformed targets are ignored, unsupported relationship modes stay unresolved, duplicate IDs do not assign owners, and custom story tables remain `REVIEW_REQUIRED` outside the editable body index.
- Commit `9d55856` extends relationship-linked discovery to custom-named footnote/endnote parts and exposes story type in JSON/Markdown inventory. These non-body tables remain read-only and excluded from the body table index.
- Commit `fdd7880` adds source-only tri-state activation evidence to direct `first`/`even` story references using section `w:titlePg` and settings `w:evenAndOddHeaders`. Missing controls are reported disabled; malformed values and duplicate controls are unknown. This does not resolve Word-effective ownership or inheritance.
- Code CI [run 42135220681](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42135220681), before inheritance-candidate coverage, passed **154/154 tests** on Ubuntu/Python 3.10–3.13 and Windows/Python 3.12; each target passed hash-enforced offline install and CLI/wheel smoke. Independent canonical wheel SHA-256: `7692a8a73c73b2b8df61ae9034d2003b032549847136ee118ab2447a451bd466`. Artifacts `chuanhoabang-*-becbd75c79e277f55e69b265517d44cc3c88bb29` expire 20/11/2026.
- Commit `71f147f` adds possible same-type `first`/`even` inheritance candidates when a valid active prior-section reference exists and the current section's corresponding control is enabled but its reference is omitted. The source-only candidate follows [Microsoft Open XML headerReference guidance](https://learn.microsoft.com/en-us/office/open-xml/word/how-to-replace-the-header-in-a-word-processing-document); it is not rendered ownership evidence.
- Latest code CI [run 42136989071](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42136989071) passed **158/158 tests** on Ubuntu/Python 3.10–3.13 and Windows/Python 3.12; all targets passed hash-enforced offline install and CLI/wheel smoke. Independent canonical wheel SHA-256: `b3f6d300f817c9aa76156a299203cdf4c050bdb638ecdb7b02e8e1957509445e`. Artifacts `chuanhoabang-*-5749080603f4217d4805c8abbaba85876e0379b2` expire 20/11/2026.
- Chưa là bản phát hành/tag. Microsoft Word/WPS, TNR có bản quyền, fixture gốc, full profile conformance và rollback/update release vẫn `NOT_RUN` hoặc chưa khả dụng; xem [release gates](docs/implementation/RELEASE_GATES.md).
