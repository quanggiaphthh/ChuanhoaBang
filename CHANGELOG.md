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

#### 06/11/2026 — Source-only mapping for horizontal merged cells

- Commit [`b8b20c8`](https://github.com/quanggiaphthh/ChuanhoaBang/commit/b8b20c8318341cf071aa8690242916a1a0dae494) reports valid horizontal `gridSpan` cells as zero-based logical-grid start/span evidence in audit and proposal JSON/Markdown. Width proposals for merged tables remain `REVIEW_REQUIRED`; width-neutral paging operations retain their limited valid-horizontal-span support.
- GitHub Actions [run 42144166384](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42144166384) passed **164/164 tests** on five targets. The independent Ubuntu/Python 3.12 wheel rebuild matched SHA-256 `7f269282e3e226dc601b7792da171c66029c77b92ff1b8669f550e9a58750fc1`; artifacts expire 20/11/2026.
- This source mapping does not verify Word layout or permit width optimization. Microsoft Word/WPS, licensed Times New Roman, and original fixtures remain unverified.

#### 06/11/2026 — Primary-source excerpt trace for profile size metrics

- The packaged ND30 and HD05 profile records now identify that their cited primary-source excerpts were checked on 06/11/2026. ND30’s official Gazette citation points to the 13–14 pt main-text rule; HD05’s official source points to its 14–15 pt main-text row. Excerpt review status is included in proposal evidence and rechecked on apply.
- Legal currentness remains `NOT_ASSESSED`; the Ministry of Justice legal-status pages returned HTTP 502 in this check, and the Gazette metadata confirms promulgation/effective dates only. Full profile coverage remains `verified_legal_presets: false` and `REFERENCE_ONLY`. The project still selects 14 pt for HD05 table-width measurement as a metric-specific policy.
- Commit [`215719c`](https://github.com/quanggiaphthh/ChuanhoaBang/commit/215719ca8068eef3759d375a291875e4ba6ed760) adds source-review provenance and tamper-rejection coverage. Targeted local tests: **22 passed**. GitHub Actions [run 42146173732](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42146173732) passed **164/164** across five targets; the independent Ubuntu/Python 3.12 wheel rebuild matched SHA-256 `4638fe3658e2fc2fc1ac28eaee564ba008d3f2c66b85cb8e699e9675b2a571aa`. Artifacts expire 20/11/2026.

#### 06/11/2026 — Source-only vertical-merge markers

- Commit [`1bbc6da`](https://github.com/quanggiaphthh/ChuanhoaBang/commit/1bbc6da42557ddb444c4c45c607706deca07c089) extends `cell_grid_spans` with local `vMerge` state (`RESTART`/`CONTINUE`) and zero-based grid positions. Invalid marker values keep the mapping unresolved. No continuation-chain validation or vertical-merge operation is enabled.
- Microsoft Open XML documents that omitted `w:val` means `continue`; the `vMerge` element controls local merge state and continuation groups must span matching grid columns ([VerticalMerge.Val](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.verticalmerge.val?view=openxml-3.0.1), [VerticalMerge](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.verticalmerge?view=openxml-3.0.1)). This implementation reports source markers only.
- Local suite: **165/165 PASS**. GitHub Actions [run 42147976513](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42147976513) passed all five targets; independent Ubuntu/Python 3.12 wheel SHA-256 `21d4b0ac6deb48f6a2baddd8516dcfb33782489557f080d09d8efb30745ab670`. Artifacts expire 20/11/2026.

#### 06/11/2026 — Source-only mapping for omitted grid columns

- Audit maps valid per-row `gridBefore`/`gridAfter` declarations to zero-based logical cell columns and exposes nonzero omission counts in audit/proposal JSON and Markdown. Missing declarations mean zero; malformed, duplicate, nested, or grid-inconsistent markers leave the mapping unresolved.
- These tables remain `REVIEW_REQUIRED` for every edit. Existing width-neutral paging operations stay blocked when a row omits grid cells. Microsoft Word rendering and original-fixture validation remain `NOT_RUN`.
- Commit [`e5de772`](https://github.com/quanggiaphthh/ChuanhoaBang/commit/e5de772d3eacf14f8fc165806a6b781a29f9a8b3) adds this source-only mapping and fail-closed coverage. The focused file passed **10/10** and the local full suite passed **170/170**.
- GitHub Actions [run 42150370005](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42150370005) passed all six jobs and **170/170 tests** across Ubuntu/Python 3.10–3.13 and Windows/Python 3.12. An independent Ubuntu/Python 3.12 rebuild matched canonical wheel SHA-256 `452731c38b1e6c248dfc866bb41188607baa7bd4bdff0228d06210c334fe0636`; artifacts `chuanhoabang-*-4748dff1aa396b3c7f9b0e9df4471f76392c6dba` expire **20/11/2026**.
- The mapping does not enable omitted-cell edits or establish Word layout. Microsoft Word/WPS, licensed TNR, and original-fixture acceptance remain **NOT_RUN** or unavailable.

#### 06/11/2026 — Source-only vertical-merge chain checks

- Audit and all proposal reports expose `vertical_merge_chain_validation` for tables with `vMerge` markers. It reports `VALID`, `INVALID` with orphan/misaligned continuation details, or `UNRESOLVED` when the logical cell-grid mapping cannot be trusted.
- This checks direct source markers against immediately adjacent rows and exact grid start/span ranges. It does not verify Word-effective merge rendering or enable vertical-merge edits; all vertical-merge proposals remain `REVIEW_REQUIRED`.
- Commit [`724bbcb`](https://github.com/quanggiaphthh/ChuanhoaBang/commit/724bbcb047f95e68a14501ebce7b31dbe6abe28a) adds the source-only check and regression coverage. The focused file passed **12/12** and the local full suite passed **172/172**.
- GitHub Actions [run 42152170192](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42152170192) passed all six jobs and **172/172 tests** across Ubuntu/Python 3.10–3.13 and Windows/Python 3.12. An independent Ubuntu/Python 3.12 rebuild matched canonical wheel SHA-256 `fb0771049574c11fefa27df1ab6b4a39b2aef5840799355280eacb648ac16f49`; artifacts `chuanhoabang-*-da3b4d5c59c1a00b6d1b9259b341c42a4a566627` expire **20/11/2026**.
- The check is source-only and does not establish Word rendering or enable vertical-merge edits. Microsoft Word/WPS, licensed TNR, and original-fixture acceptance remain **NOT_RUN** or unavailable.

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
- The first/even inheritance-candidate CI [run 42136989071](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42136989071) passed **158/158 tests** on Ubuntu/Python 3.10–3.13 and Windows/Python 3.12. Independent canonical wheel SHA-256: `b3f6d300f817c9aa76156a299203cdf4c050bdb638ecdb7b02e8e1957509445e`.
- Commit `ee6f13d` adds source-only note linkage evidence for tables in footnote/endnote parts: match the nearest note definition ID against same-type references in `word/document.xml` body, count matches, and report duplicate/invalid/missing cases explicitly. The `NO_BODY_REFERENCE_FOUND` status is scoped to document body XML only; note tables remain read-only. ID semantics cite Microsoft's [reference ID](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.footnoteendnotereferencetype.id?view=openxml-3.0.1) and [separator ID](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.footnoteendnoteseparatorreferencetype.id?view=openxml-3.0.1) guidance. This is not Word rendering or effective ownership evidence.
- Commit `1465722` adds the profile metric selection rationale and official source URLs/locators to width proposal evidence. `apply` rechecks that metadata with the selected profile constraint. The profiles remain `REFERENCE_ONLY`, and no full legal preset is claimed.
- Latest code CI [run 42140650308](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42140650308) passed **164/164 tests** on Ubuntu/Python 3.10–3.13 and Windows/Python 3.12; all five targets passed hash-enforced offline install and CLI/wheel smoke. An independent Ubuntu/Python 3.12 runner reproduced the canonical wheel SHA-256 `143082ee36d5c0fb6f38e39464a05a05be6a5bb91b92e9384ce566bae308f692`. Artifacts `chuanhoabang-*-4b00609c824f62149eaa9adc04b96a9243ddb3a8` expire 20/11/2026.
- Chưa là bản phát hành/tag. Microsoft Word/WPS, TNR có bản quyền, fixture gốc, full profile conformance và rollback/update release vẫn `NOT_RUN` hoặc chưa khả dụng; xem [release gates](docs/implementation/RELEASE_GATES.md).
