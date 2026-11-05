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

- `--table` lấy index 0-based từ `audit`. `propose` không sửa DOCX; `apply` cần đề xuất `PROPOSE_APPLY` chưa bị chỉnh và đầu vào **chưa đổi**.
- `--profile ND30|HD05` ghi profile vào báo cáo/đề xuất. Với `propose` đo chiều rộng, runtime chỉ dùng giới hạn cỡ chữ trong `profile_constraints` để xác định run nào đủ điều kiện đo: ND30 13/14 pt; HD05 14 pt theo lựa chọn V16. Size ngoài phạm vi trả `REVIEW_REQUIRED`; không đổi font. Preset pháp lý đầy đủ vẫn chưa xác minh, trạng thái vẫn `REFERENCE_ONLY`, không phải chứng nhận tuân thủ.
- Phông chữ phải là file Times New Roman hợp pháp có trên máy. **Không sử dụng Tinos/Liberation Serif như Times New Roman**. Runtime kiểm tra metadata family/style: slot regular từ chối face bold/italic; slot bold yêu cầu face bold không italic. Metadata không xác nhận giấy phép hay tính xác thực của font. Nếu không có face phù hợp, lệnh trả `REVIEW_REQUIRED`; không tạo giả phép đo.
- Để tránh sửa nhầm, width measurement chỉ xử lý bảng dữ liệu phẳng, một section, khi TNR và size hiệu dụng được giải từ run trực tiếp hoặc chuỗi paragraph-style `basedOn` rõ ràng tới style mặc định. Không chọn profile: 13/14 pt; ND30: 13/14 pt; HD05: 14 pt. Size ngoài scope trả `REVIEW_REQUIRED`. Table style, character style, theme font, chuỗi thiếu/cyclic hoặc hiệu ứng chưa hỗ trợ cũng trả `REVIEW_REQUIRED`. Ngoại lệ hạn chế: `gridSpan` gộp ngang hợp lệ được phép lặp header hoặc nới chiều cao hàng (không đổi width); gộp dọc, bảng lồng hoặc bảng khóa vẫn bị chặn.
- Nếu `w:pgSz/@w:orient` mâu thuẫn với `w:w`/`w:h`, hoặc section có nhiều cột/cột đơn đặt width riêng, audit trả `GEOMETRY_UNKNOWN` và optimizer giữ `REVIEW_REQUIRED`; không dùng bề rộng vùng chữ toàn trang thay cho bề rộng cột.
- Lệnh `propose` (width) chỉ sửa width của bảng được chọn; không thay font, số liệu, orientation, header/footer hoặc height. Điểm width chưa chứng minh độ vừa trang trong Word.
- Lệnh `propose-header` chỉ bật `w:tblHeader` của **hàng đầu tiên** trên bảng nội dung đơn giản, khi được chọn và áp dụng rõ ràng; không ép `cantSplit`, không sửa nội dung, không tự lặp cho biểu mẫu khóa. Không chứng nhận Word đã lặp thực tế.
- Lệnh `propose-unclip` là phép sửa có điều kiện: chuyển `w:trHeight/@w:hRule` từ `exact` sang `atLeast` **nhưng giữ nguyên `w:val` và toàn bộ nội dung**. Không tự thay line spacing của đoạn, không tuyên bố đã giải quyết mọi lỗi che chữ. Áp dụng chỉ khi người dùng yêu cầu bằng proposal riêng và bảng thuộc scope an toàn.
- Nếu ô có nhiều đoạn văn, width proposal trả REVIEW vì phép tính line-wrap hiện chưa mô phỏng nhiều paragraph; các run XML rỗng hợp lệ được bỏ qua khi đo chữ.
- Mọi score về line count chỉ là **FONT_METRIC_ESTIMATE**. Chưa có xác nhận rằng Word/WPS in không tràn/cắt.

## Exit codes / trạng thái

`0`: thao tác CLI hoàn tất, đọc trường `decision` để phân biệt `PROPOSE_APPLY` / `NO_OP_VALID` / `REVIEW_REQUIRED`. `2`: lỗi input/policy/stale/output. `word_render` luôn `NOT_RUN` khi không có renderer verification.

**Nền tri thức:** [AGENTS.md](AGENTS.md), [V15](docs/research/Bao_cao_chuan_hoa_va_toi_uu_bang_DOCX_ND30_HD05_V15_2026.md), [V16](docs/spec/AI_TABLE_FORMATTING_NO_RENDER_V16.md), [V17.5.1](docs/research/V17_5_1/README.md).

## Bằng chứng hiện có (05/11/2026)

- GitHub Actions [run 42086960094](https://github.com/quanggiaphthh/ChuanhoaBang/actions/runs/42086960094): **74/74 tests PASS** trên Ubuntu/Python 3.10–3.13 và Windows/Python 3.12. CI tạo một wheel preview có manifest SHA-256, sau đó cài và smoke-test chính wheel đó (registry, CLI, DOCX tiếng Việt) trên cả năm môi trường. Artifact là preview, Microsoft Word acceptance vẫn `NOT_RUN`.
- Đây là kiểm thử cấu trúc trên DOCX tổng hợp với metric font giả lập; không đo TNR có bản quyền, không phải Microsoft Word acceptance.
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

The API uses the same offline core and explicit proposal checks as the CLI. A missing or unsupported font can return `REVIEW_REQUIRED`; apply only a `PROPOSE_APPLY` proposal. The selected profile is recorded as `REFERENCE_ONLY`; width proposals disclose the narrow metric-size scope in `profile_constraints`, while `profile_rules_applied: false` indicates that no complete profile formatting preset has been applied. This is not a compliance result.

## Phạm vi hỗ trợ bảng gộp ngang (technical preview)

- Với `propose-header` và `propose-unclip`, nếu bảng có `gridSpan` gộp ngang, hệ thống xác minh **tổng span mỗi hàng bằng đúng số cột lưới** trước khi đưa ra đề xuất.
- Được phép thay đổi duy nhất `tblHeader` hàng đầu hoặc `trHeight.hRule` ở các hàng đã liệt kê trong proposal. Bộ invariant kiểm lại các thuộc tính không nằm trong allowlist, gồm **độ rộng bảng không được đổi ngầm**.
- Từ chối `vMerge`, `gridBefore/gridAfter`, grid không hợp lệ, biểu mẫu bảo vệ và các nội dung OOXML ngoài scope. AutoFit/đo chữ cho bảng gộp **chưa triển khai**.
- Thành công trên fixture tổng hợp **không tương đương** việc header hoặc hàng đã được dàn đúng khi in Word.
