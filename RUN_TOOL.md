# ChuanhoaBang — Technical preview v0.1

Đây là **module thử nghiệm**, không phải công cụ bảo đảm định dạng Word 1.0. Engine hoạt động offline; không dùng AI, server hoặc Internet trong lúc chạy. Cài dependencies bằng wheel nội bộ nếu thiết bị không có mạng.

## Cài đặt

```bash
python -m pip install .
# Để chạy kiểm thử: python -m pip install '.[test]'
python -m pytest -q
```

## Sử dụng

```bash
chuanhoabang audit INPUT.docx --report-md AUDIT_REPORT.md
chuanhoabang propose INPUT.docx --table 0 --font-regular /path/to/TimesNewRoman.ttf --font-bold /path/to/TimesNewRoman-Bold.ttf --output proposal.json
chuanhoabang apply INPUT.docx --proposal proposal.json --output INPUT_DINHDANG.docx --font-regular /path/to/TimesNewRoman.ttf --font-bold /path/to/TimesNewRoman-Bold.ttf

# Độc lập với đo chữ: đề xuất lặp hàng tiêu đề đầu tiên của bảng nội dung
chuanhoabang propose-header INPUT.docx --table 0 --output repeat-header.json --report-md HEADER_PROPOSAL.md
chuanhoabang apply INPUT.docx --proposal repeat-header.json --output INPUT_HEADER.docx

# Xử lý nguy cơ chữ bị che bởi hàng cố định Exactly, chỉ khi người dùng chọn
chuanhoabang propose-unclip INPUT.docx --table 0 --output unclip.json
chuanhoabang apply INPUT.docx --proposal unclip.json --output INPUT_UNCLIPPED.docx
```

- `--table` lấy index 0-based từ `audit`. `propose` không sửa DOCX; `apply` cần đề xuất `PROPOSE_APPLY` chưa bị chỉnh và đầu vào **chưa đổi**.
- Phông chữ phải là file Times New Roman hợp pháp có trên máy. **Không sử dụng Tinos/Liberation Serif như Times New Roman**. Nếu không có font, lệnh trả `REVIEW_REQUIRED`; không tạo giả phép đo.
- Để tránh sửa nhầm, AutoFit bản thử nghiệm chỉ xử lý bảng dữ liệu phẳng, một section, với các run khai báo trực tiếp TNR 13/14. Ngoại lệ hạn chế: `gridSpan` gộp ngang hợp lệ được phép lặp header hoặc nới chiều cao hàng (không đổi width); gộp dọc, bảng lồng hoặc bảng khóa vẫn bị chặn.
- Lệnh `propose` (width) chỉ sửa width của bảng được chọn; không thay font, số liệu, orientation, header/footer hoặc height. Điểm width chưa chứng minh độ vừa trang trong Word.
- Lệnh `propose-header` chỉ bật `w:tblHeader` của **hàng đầu tiên** trên bảng nội dung đơn giản, khi được chọn và áp dụng rõ ràng; không ép `cantSplit`, không sửa nội dung, không tự lặp cho biểu mẫu khóa. Không chứng nhận Word đã lặp thực tế.
- Lệnh `propose-unclip` là phép sửa có điều kiện: chuyển `w:trHeight/@w:hRule` từ `exact` sang `atLeast` **nhưng giữ nguyên `w:val` và toàn bộ nội dung**. Không tự thay line spacing của đoạn, không tuyên bố đã giải quyết mọi lỗi che chữ. Áp dụng chỉ khi người dùng yêu cầu bằng proposal riêng và bảng thuộc scope an toàn.
- Nếu ô có nhiều đoạn văn, width proposal trả REVIEW vì phép tính line-wrap hiện chưa mô phỏng nhiều paragraph; các run XML rỗng hợp lệ được bỏ qua khi đo chữ.
- Mọi score về line count chỉ là **FONT_METRIC_ESTIMATE**. Chưa có xác nhận rằng Word/WPS in không tràn/cắt.

## Exit codes / trạng thái

`0`: thao tác CLI hoàn tất, đọc trường `decision` để phân biệt `PROPOSE_APPLY` / `NO_OP_VALID` / `REVIEW_REQUIRED`. `2`: lỗi input/policy/stale/output. `word_render` luôn `NOT_RUN` khi không có renderer verification.

**Nền tri thức:** [AGENTS.md](AGENTS.md), [V15](docs/research/Bao_cao_chuan_hoa_va_toi_uu_bang_DOCX_ND30_HD05_V15_2026.md), [V16](docs/spec/AI_TABLE_FORMATTING_NO_RENDER_V16.md), [V17.5.1](docs/research/V17_5_1/README.md).

## Bằng chứng hiện có (05/11/2026)

- GitHub Actions Python 3.11: **43 PASS** (bảng tự tạo; khẳng định structural/integrity only).
- Kiểm chứng LibreOffice 25.x tại bảng 90 dòng (không phải Word acceptance): header ở trang 2 có sau patch; số trang thay đổi 12 → 13 do chi phí chiều cao hàng tiêu đề.
- Không được hiểu kết quả LibreOffice là chính xác Microsoft Word; cần xác minh bản in Word và font Times New Roman có bản quyền trên máy mục tiêu.
- Smoke `Exactly 6 pt` → `At least 6 pt` trên LibreOffice: trước khi sửa một phần nội dung hàng bị che; sau khi sửa các dòng nhìn thấy đầy đủ. Đây là kết quả riêng trên LO, không phải Word.
- Xem `docs/verification/HEADER_REPEAT_LO_SMOKE_2026-11-05.md` và `ROW_HEIGHT_LO_SMOKE_2026-11-05.md`.


## Báo cáo Markdown và giới hạn

- `--report-md PATH.md` tạo báo cáo đọc được cho `audit`, `propose`, `propose-header`, `propose-unclip` và `apply`.
- Đường dẫn Markdown phải mới, không được trùng nguồn DOCX, JSON proposal hoặc DOCX output. Xung đột bị chặn **trước khi áp dụng**.
- Báo cáo ghi quyết định, bằng chứng, bảng, cảnh báo và thuộc tính thay đổi; **không thay thế** kiểm chứng hiển thị Microsoft Word.
- Kiểm thử GitHub Actions gồm toàn bộ `tests/`, không bỏ qua các kiểm thử an toàn bổ sung.

## Phạm vi hỗ trợ bảng gộp ngang (technical preview)

- Với `propose-header` và `propose-unclip`, nếu bảng có `gridSpan` gộp ngang, hệ thống xác minh **tổng span mỗi hàng bằng đúng số cột lưới** trước khi đưa ra đề xuất.
- Được phép thay đổi duy nhất `tblHeader` hàng đầu hoặc `trHeight.hRule` ở các hàng đã liệt kê trong proposal. Bộ invariant kiểm lại các thuộc tính không nằm trong allowlist, gồm **độ rộng bảng không được đổi ngầm**.
- Từ chối `vMerge`, `gridBefore/gridAfter`, grid không hợp lệ, biểu mẫu bảo vệ và các nội dung OOXML ngoài scope. AutoFit/đo chữ cho bảng gộp **chưa triển khai**.
- Thành công trên fixture tổng hợp **không tương đương** việc header hoặc hàng đã được dàn đúng khi in Word.
