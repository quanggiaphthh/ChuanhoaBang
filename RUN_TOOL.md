# ChuanhoaBang — Technical preview v0.1

Đây là **module thử nghiệm**, không phải công cụ bảo đảm định dạng Word 1.0. Engine hoạt động offline; không dùng AI, server hoặc Internet trong lúc chạy. Cài dependencies bằng wheel nội bộ nếu thiết bị không có mạng.

## Cài đặt

```bash
# Reproducible install from the committed dependency lock
uv sync --locked
# Include the test tools when developing
uv sync --locked --extra test
# Alternative unlocked package install
python -m pip install .
# With the locked environment: uv run --locked python -m pytest -q tests/
```

`uv.lock` pins the runtime and test dependency graph used by CI. The first `uv sync` still needs an internet connection or a prefilled package cache/wheelhouse; once installed, the formatter itself runs offline.

### Cài đặt trên máy không có mạng

CI tạo wheelhouse riêng theo hệ điều hành, kiến trúc và phiên bản Python. Tải artifact `chuanhoabang-offline-<OS>-py<Python>-<commit>` khớp với máy đích; artifact gồm `wheelhouse/`, `requirements.txt` có hash và `offline-bundle-manifest.json`. Trên máy đích, từ thư mục artifact:

```bash
python -m pip install --no-index --find-links ./wheelhouse --require-hashes --only-binary=:all: -r ./offline-install-requirements.txt
chuanhoabang --help
```

Wheelhouse chỉ dùng cho đúng OS/kiến trúc/Python minor ghi trong manifest. `offline-install-requirements.txt` pin và kiểm tra SHA-256 cho dependency wheels và wheel preview của ứng dụng. Bundle không chứa bộ test hoặc Times New Roman. Lệnh cài đặt đặt `--no-index`, nên pip chỉ tìm package trong thư mục nội bộ.

## Sử dụng

```bash
chuanhoabang audit INPUT.docx --profile ND30 --report-md AUDIT_REPORT.md
chuanhoabang propose INPUT.docx --table 0 --profile HD05 --font-regular /path/to/TimesNewRoman.ttf --font-bold /path/to/TimesNewRoman-Bold.ttf --output proposal.json
chuanhoabang apply INPUT.docx --proposal proposal.json --output INPUT_DINHDANG.docx --font-regular /path/to/TimesNewRoman.ttf --font-bold /path/to/TimesNewRoman-Bold.ttf

# Độc lập với đo chữ: đề xuất lặp hàng tiêu đề đầu tiên của bảng nội dung
chuanhoabang propose-header INPUT.docx --table 0 --output repeat-header.json --report-md HEADER_PROPOSAL.md
chuanhoabang apply INPUT.docx --proposal repeat-header.json --output INPUT_HEADER.docx

# Xử lý nguy cơ chữ bị che bởi hàng cố định Exactly, chỉ khi người dùng chọn
chuanhoabang propose-unclip INPUT.docx --table 0 --output unclip.json
chuanhoabang apply INPUT.docx --proposal unclip.json --output INPUT_UNCLIPPED.docx
```

- `--table` lấy index 0-based của bảng trong body từ `audit`. Bảng trong header/footer/footnotes/endnotes được liệt kê riêng bằng part, story type, chỉ số trong part và SHA-256; cả bốn loại có thể dùng tên part tùy biến nếu được document relationship nội bộ tham chiếu. External/malformed targets và relationship mode không hỗ trợ không được theo dõi; duplicate IDs không gán owner. Báo cáo thêm ứng viên kế thừa cùng loại cho header/footer `default`; với `first`/`even`, báo cáo thêm candidate khi một direct source cùng loại đang hoạt động, control của section hiện tại bật, và reference tương ứng vắng mặt. Các ứng viên là source-only; chúng không xác nhận ownership hiệu lực hay layout Word. Direct `first`/`even` references show source activation as `ENABLED`, `DISABLED`, or `UNKNOWN`, with control and `SOURCE_XML_ONLY` evidence. Với bảng trong note part, JSON/Markdown nêu note ID, trạng thái đối chiếu và số lượng reference cùng loại trong document body XML. `NO_BODY_REFERENCE_FOUND` chỉ áp dụng cho document body XML; không phải khẳng định note không được tham chiếu ở mọi story hoặc Word không hiển thị. ID trùng trả `AMBIGUOUS_NOTE_ID`; thiếu container hoặc ID hợp lệ trả trạng thái rõ ràng. Căn cứ quan hệ ID: [Microsoft Open XML FootnoteEndnoteReferenceType.Id](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.footnoteendnotereferencetype.id?view=openxml-3.0.1) và [separator/reference ID guidance](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.footnoteendnoteseparatorreferencetype.id?view=openxml-3.0.1). Đây là source-only evidence, không xác nhận ownership hiệu lực hay layout Word. Non-body tables are review-only and cannot be selected by CLI. `propose` does not modify DOCX; `apply` requires an unmodified `PROPOSE_APPLY` proposal and unchanged input. If output already exists, the command rebuilds and validates the candidate; only a regular non-symlink file with byte-identical content returns `NO_OP_VALID` without rewriting. A different or non-regular output returns `OUTPUT_MUST_BE_NEW_PATH` and remains unchanged.
- JSON audit ghi `width_evidence` tách `tblW`/`tcW` khai báo khỏi lưới `tblGrid`: giá trị `dxa` được quy đổi sang twips, các kiểu khác giữ nguyên giá trị OOXML, và khai báo lỗi/nhập nhằng buộc `REVIEW_REQUIRED`. Đây là dữ liệu XML khai báo, không phải độ rộng Word đã kết xuất (`word_rendered: NOT_RUN`).
- `--profile ND30|HD05` ghi profile vào báo cáo/đề xuất. Với `propose` đo chiều rộng, runtime chỉ dùng giới hạn cỡ chữ trong `profile_constraints` để xác định run nào đủ điều kiện đo: ND30 13/14 pt; HD05 14 pt theo lựa chọn V16. Constraint cũng ghi căn cứ lựa chọn và URL/locator nguồn chính thức từ policy registry; `apply` tái so sánh cả metadata nguồn khi xác minh proposal. Size ngoài phạm vi trả `REVIEW_REQUIRED`; không đổi font. Preset pháp lý đầy đủ vẫn chưa xác minh, trạng thái vẫn `REFERENCE_ONLY`, không phải chứng nhận tuân thủ.
- Phông chữ phải là file Times New Roman hợp pháp có trên máy. **Không sử dụng Tinos/Liberation Serif như Times New Roman**. Runtime kiểm tra metadata family/style: slot regular từ chối face bold/italic; slot bold yêu cầu face bold không italic. Metadata không xác nhận giấy phép hay tính xác thực của font. Nếu không có face phù hợp, lệnh trả `REVIEW_REQUIRED`; không tạo giả phép đo.
- Để tránh sửa nhầm, width measurement chỉ xử lý bảng dữ liệu phẳng, một section, khi TNR và size hiệu dụng được giải từ run trực tiếp hoặc chuỗi paragraph-style `basedOn` rõ ràng tới style mặc định. Không chọn profile: 13/14 pt; ND30: 13/14 pt; HD05: 14 pt. Size ngoài scope trả `REVIEW_REQUIRED`. Table style, character style, theme font, chuỗi thiếu/cyclic hoặc hiệu ứng chưa hỗ trợ cũng trả `REVIEW_REQUIRED`. Với bảng có `gridSpan` ngang hợp lệ, audit ghi vị trí cột logic và số cột span theo XML nguồn; width proposal vẫn bị chặn. Chỉ thao tác lặp header/nới chiều cao hàng (không đổi width) mới nhận grid span này. Gộp dọc, lưới sai/thiếu, bảng lồng hoặc bảng khóa vẫn bị chặn.
- Nếu `w:pgSz/@w:orient` mâu thuẫn với `w:w`/`w:h`, hoặc section thiếu thông số hình học, audit trả `GEOMETRY_UNKNOWN` và optimizer giữ `REVIEW_REQUIRED`. Nhiều cột đều chỉ được tính khi `w:num`, `w:equalWidth`, `w:space` hợp lệ và tường minh. Cột tùy biến chỉ được tính khi `w:equalWidth="0"`, số phần tử `w:col` khớp `w:num`, mỗi cột có `w:w` dương và mỗi khoảng giữa hai cột có `w:space` không âm tường minh; tổng độ rộng và khoảng cách giữa cột phải nằm trong vùng chữ. JSON/Markdown ghi riêng width và spacing từng cột. Khi chưa biết bảng nằm ở cột nào, `available_twips` dùng cột hẹp nhất làm giới hạn bảo thủ cho mọi vị trí; đây là dữ liệu XML, không phải kết quả dàn trang Word. Các thuộc tính `w:col` bị bỏ qua khi `w:equalWidth` vắng mặt vì Microsoft Word mặc định cột đều.
- `mc:AlternateContent` trong `word/document.xml`, dấu `w:permStart`/`w:permEnd`, và trạng thái `w:documentProtection` bật, không hợp lệ hoặc lặp đều khóa proposal cho bảng body; package có part dưới `_xmlsignatures/` hoặc `word/vbaProject.bin` cũng bị khóa. Runtime không chọn nhánh compatibility, không tự xác định vùng permission/danh tính người sửa, không kiểm tra chữ ký số và không chạy macro. Các nguồn lần lượt là [MCE/AlternateContent](https://learn.microsoft.com/en-us/openspecs/office_standards/ms-docx/ec34035b-0da9-4849-a064-e4e57d1e7245), [permStart](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.permstart?view=openxml-3.0.1), [permEnd](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.permend?view=openxml-3.0.1), và [documentProtection enforcement](https://learn.microsoft.com/en-us/openspecs/office_standards/ms-oi29500/e12d2773-e2d0-45bf-b1c2-b8f0548e156d).
- Line estimate coi U+00A0, U+180E, U+2007 và U+202F là không ngắt; dấu nối không ngắt và word joiner vốn nằm trong cùng token. Đây là guard bảo thủ một phần, không phải triển khai đầy đủ [Unicode UAX #14](https://unicode.org/reports/tr14/) hay kết xuất Word.
- Lệnh `propose` (width) chỉ sửa width của bảng được chọn; không thay font, số liệu, orientation, header/footer hoặc height. Điểm width chưa chứng minh độ vừa trang trong Word.
- Lệnh `propose-header` chỉ bật `w:tblHeader` của **hàng đầu tiên** trên bảng nội dung đơn giản, khi được chọn và áp dụng rõ ràng; không ép `cantSplit`, không sửa nội dung, không tự lặp cho biểu mẫu khóa. Không chứng nhận Word đã lặp thực tế.
- Lệnh `propose-unclip` là phép sửa có điều kiện: chuyển `w:trHeight/@w:hRule` từ `exact` sang `atLeast` **nhưng giữ nguyên `w:val` và toàn bộ nội dung**. Không tự thay line spacing của đoạn, không tuyên bố đã giải quyết mọi lỗi che chữ. Áp dụng chỉ khi người dùng yêu cầu bằng proposal riêng và bảng thuộc scope an toàn.
- Nếu ô có nhiều đoạn văn, width proposal trả REVIEW vì phép tính line-wrap hiện chưa mô phỏng nhiều paragraph; các run XML rỗng hợp lệ được bỏ qua khi đo chữ.
- Mọi score về line count chỉ là **FONT_METRIC_ESTIMATE**. Chưa có xác nhận rằng Word/WPS in không tràn/cắt.

## Exit codes / trạng thái

`0`: thao tác CLI hoàn tất, đọc trường `decision` để phân biệt `PROPOSE_APPLY` / `NO_OP_VALID` / `REVIEW_REQUIRED`. `2`: lỗi input/policy/stale/output. `word_render` luôn `NOT_RUN` khi không có renderer verification.

**Nền tri thức:** [AGENTS.md](AGENTS.md), [V15](docs/research/Bao_cao_chuan_hoa_va_toi_uu_bang_DOCX_ND30_HD05_V15_2026.md), [V16](docs/spec/AI_TABLE_FORMATTING_NO_RENDER_V16.md), [V17.5.1](docs/research/V17_5_1/README.md).

## Bằng chứng hiện có (06/11/2026)

- Latest code evidence: commit [`b8b20c8`](https://github.com/quanggiaphthh/ChuanhoaBang/commit/b8b20c8318341cf071aa8690242916a1a0dae494), [Actions run 42144166384](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42144166384): **164/164 tests PASS** trên Ubuntu/Python 3.10–3.13 và Windows/Python 3.12. Mỗi target cài wheelhouse trong virtualenv mới với `pip --no-index --require-hashes`, rồi chạy CLI help, audit DOCX tiếng Việt và wheel smoke. Runner Ubuntu/Python 3.12 độc lập tái tạo canonical wheel SHA-256 `7f269282e3e226dc601b7792da171c66029c77b92ff1b8669f550e9a58750fc1`. Artifacts `chuanhoabang-offline-*-7cc9d20875a091b4eddb4a42eca5f67f03d97526` và `chuanhoabang-preview-7cc9d20875a091b4eddb4a42eca5f67f03d97526` hết hạn 20/11/2026. Microsoft Word acceptance vẫn `NOT_RUN`.
- Regression bổ sung khóa marker bố cục/chữ ký ở mọi hàng bảng vào REVIEW, nhận dạng dấu gạch Unicode trong khẩu hiệu hành chính; một regression khác xác nhận tệp đầu ra được tạo đồng thời không bị ghi đè sau khi DOCX đã được kiểm tra.
- Đây là kiểm thử cấu trúc trên DOCX tổng hợp với metric font giả lập; không đo TNR có bản quyền, không phải Microsoft Word acceptance.
- Effective direct left/right `dxa` margins được đo theo từng ô; khai báo không hỗ trợ chuyển bảng sang `REVIEW_REQUIRED`. Ô không có cặp margin ngang trực tiếp hoặc từ style chain được hỗ trợ dùng ngân sách estimator `padding_twips_assumed=240` tổng trái/phải, chưa được đối chiếu với effective cell margin của Word. Nếu không dùng fallback, trường giả định trả `null`; bảng hỗn hợp báo ma trận padding theo ô và ngân sách giả định.
- Với `w:tblStyle`, audit chỉ giải baseline có chuỗi `basedOn` table style rõ ràng và cặp left/right `dxa` đầy đủ trong `tblPr/tblCellMar`. Margin trực tiếp ở table/cell được ưu tiên. Conditional margins, `tcMar` trong style, partial/malformed margins, style ID thiếu và cycle trả `UNRESOLVED` với `TABLE_STYLE_CASCADE_NOT_SUPPORTED`. JSON/Markdown nêu style ID, chuỗi `basedOn`, margin source và liệu style margin có tham gia ma trận hay không. Width proposal vẫn `REVIEW_REQUIRED` với mọi table style vì font cascade chưa hỗ trợ.
- Markdown report hiển thị status, reason/basis, fallback budget, nguồn style margin và ma trận padding theo hàng/ô để người rà soát thấy cùng chứng cứ với JSON. Đây là audit nguồn OOXML; không xác nhận effective Word layout.
- Commit `59d3da3` mở rộng style-margin audit; run [42128033502](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42128033502) xác nhận suite **140/140 PASS** trên cả năm môi trường. Commit `b6a9f52` bổ sung apply idempotence có so sánh byte; run [42129232635](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42129232635) xác nhận suite **142/142 PASS** trên cả năm môi trường.
- Kiểm chứng LibreOffice 25.x tại bảng 90 dòng (không phải Word acceptance): header ở trang 2 có sau patch; số trang thay đổi 12 → 13 do chi phí chiều cao hàng tiêu đề.
- Không được hiểu kết quả LibreOffice là chính xác Microsoft Word; cần xác minh bản in Word và font Times New Roman có bản quyền trên máy mục tiêu.
- Smoke `Exactly 6 pt` → `At least 6 pt` trên LibreOffice: trước khi sửa một phần nội dung hàng bị che; sau khi sửa các dòng nhìn thấy đầy đủ. Đây là kết quả riêng trên LO, không phải Word.
- Xem `docs/verification/HEADER_REPEAT_LO_SMOKE_2026-11-05.md` và `ROW_HEIGHT_LO_SMOKE_2026-11-05.md`.


## Báo cáo Markdown và giới hạn

- `--report-md PATH.md` tạo báo cáo đọc được cho `audit`, `propose`, `propose-header`, `propose-unclip` và `apply`.
- Đường dẫn Markdown phải mới, không được trùng nguồn DOCX, JSON proposal hoặc DOCX output. Xung đột bị chặn **trước khi áp dụng**.
- Báo cáo ghi quyết định, bằng chứng, bảng, cảnh báo và thuộc tính thay đổi; **không thay thế** kiểm chứng hiển thị Microsoft Word.
- Kiểm thử GitHub Actions gồm toàn bộ `tests/`, không bỏ qua các kiểm thử an toàn bổ sung.

## Python API

```python
from pathlib import Path
from chuanhoabang import audit, apply, available_profiles, propose

source = Path("input.docx")
regular_tnr = Path("/path/to/TimesNewRoman.ttf")
bold_tnr = Path("/path/to/TimesNewRoman-Bold.ttf")
print(available_profiles())  # ('ND30', 'HD05')

report = audit(source, profile="ND30")
proposal = propose(source, table_index=0, font_regular=regular_tnr,
                   font_bold=bold_tnr, profile="ND30")
if proposal["decision"] == "PROPOSE_APPLY":
    result = apply(source, proposal, Path("output.docx"),
                   font_regular=regular_tnr, font_bold=bold_tnr, profile="ND30")
```

The API uses the same offline core and explicit proposal checks as the CLI. A missing or unsupported font can return `REVIEW_REQUIRED`; apply only a `PROPOSE_APPLY` proposal. The selected profile is recorded as `REFERENCE_ONLY`; width proposals disclose the metric-size scope, project selection basis, and official source URLs/locators in `profile_constraints`, while `profile_rules_applied: false` indicates that no complete profile formatting preset has been applied. This is not a compliance result.

## Phạm vi hỗ trợ bảng gộp ngang (technical preview)

- Audit JSON/Markdown ghi `cell_grid_spans` theo từng hàng: `start_column` là vị trí zero-based trong `tblGrid`, `span` là số cột logic được phủ. Đây chỉ là ánh xạ từ XML nguồn; bảng gộp vẫn `REVIEW_REQUIRED` cho width proposal.
- Với `propose-header` và `propose-unclip`, nếu bảng có `gridSpan` gộp ngang, hệ thống xác minh **tổng span mỗi hàng bằng đúng số cột lưới** trước khi đưa ra đề xuất.
- Được phép thay đổi duy nhất `tblHeader` hàng đầu hoặc `trHeight.hRule` ở các hàng đã liệt kê trong proposal. Bộ invariant kiểm lại các thuộc tính không nằm trong allowlist, gồm **độ rộng bảng không được đổi ngầm**.
- Từ chối `vMerge`, `gridBefore/gridAfter`, span malformed, grid không đầy đủ, biểu mẫu bảo vệ và các nội dung OOXML ngoài scope. Đo chữ/width proposal cho bảng gộp **chưa triển khai**; cần qua cổng TNR có bản quyền và hình học Microsoft Word trước khi mở rộng.
- Thành công trên fixture tổng hợp **không tương đương** việc header hoặc hàng đã được dàn đúng khi in Word.
