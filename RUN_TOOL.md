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
chuanhoabang audit INPUT.docx
chuanhoabang propose INPUT.docx --table 0 --font-regular /path/to/TimesNewRoman.ttf --font-bold /path/to/TimesNewRoman-Bold.ttf --output proposal.json
chuanhoabang apply INPUT.docx --proposal proposal.json --output INPUT_DINHDANG.docx --font-regular /path/to/TimesNewRoman.ttf --font-bold /path/to/TimesNewRoman-Bold.ttf

# Độc lập với đo chữ: đề xuất lặp hàng tiêu đề đầu tiên của bảng nội dung
chuanhoabang propose-header INPUT.docx --table 0 --output repeat-header.json
chuanhoabang apply INPUT.docx --proposal repeat-header.json --output INPUT_HEADER.docx
```

- `--table` lấy index 0-based từ `audit`. `propose` không sửa DOCX; `apply` cần đề xuất `PROPOSE_APPLY` chưa bị chỉnh và đầu vào **chưa đổi**.
- Phông chữ phải là file Times New Roman hợp pháp có trên máy. **Không sử dụng Tinos/Liberation Serif như Times New Roman**. Nếu không có font, lệnh trả `REVIEW_REQUIRED`; không tạo giả phép đo.
- Để tránh sửa nhầm, bản thử nghiệm chỉ tự động xử lý bảng dữ liệu phẳng, một section, với các run khai báo trực tiếp TNR 13/14. Các bảng phức tạp/khóa vẫn được audit nhưng không tự sửa.
- Lệnh `propose` (width) chỉ sửa width của bảng được chọn; không thay font, số liệu, orientation, header/footer hoặc height. Điểm width chưa chứng minh độ vừa trang trong Word.
- Lệnh `propose-header` chỉ bật `w:tblHeader` của **hàng đầu tiên** trên bảng nội dung đơn giản, khi được chọn và áp dụng rõ ràng; không ép `cantSplit`, không sửa nội dung, không tự lặp cho biểu mẫu khóa. Không chứng nhận Word đã lặp thực tế.
- Nếu ô có nhiều đoạn văn, width proposal trả REVIEW vì phép tính line-wrap hiện chưa mô phỏng nhiều paragraph; các run XML rỗng hợp lệ được bỏ qua khi đo chữ.
- Mọi score về line count chỉ là **FONT_METRIC_ESTIMATE**. Chưa có xác nhận rằng Word/WPS in không tràn/cắt.

## Exit codes / trạng thái

`0`: thao tác CLI hoàn tất, đọc trường `decision` để phân biệt `PROPOSE_APPLY` / `NO_OP_VALID` / `REVIEW_REQUIRED`. `2`: lỗi input/policy/stale/output. `word_render` luôn `NOT_RUN` khi không có renderer verification.

**Nền tri thức:** [AGENTS.md](AGENTS.md), [V15](docs/research/Bao_cao_chuan_hoa_va_toi_uu_bang_DOCX_ND30_HD05_V15_2026.md), [V16](docs/spec/AI_TABLE_FORMATTING_NO_RENDER_V16.md), [V17.5.1](docs/research/V17_5_1/README.md).

## Bằng chứng hiện có (05/11/2026)

- Pytest cục bộ: **19 PASS** (bảng tự tạo; khẳng định structural/integrity only).
- Kiểm chứng LibreOffice 25.x tại bảng 90 dòng (không phải Word acceptance): header ở trang 2 có sau patch; số trang thay đổi 12 → 13 do chi phí chiều cao hàng tiêu đề.
- Không được hiểu kết quả LibreOffice là chính xác Microsoft Word; cần xác minh bản in Word và font Times New Roman có bản quyền trên máy mục tiêu.
- Xem `docs/verification/HEADER_REPEAT_LO_SMOKE_2026-11-05.md`.
