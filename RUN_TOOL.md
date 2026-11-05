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
```

- `--table` lấy index 0-based từ `audit`. `propose` không sửa DOCX; `apply` cần đề xuất `PROPOSE_APPLY` chưa bị chỉnh và đầu vào **chưa đổi**.
- Phông chữ phải là file Times New Roman hợp pháp có trên máy. **Không sử dụng Tinos/Liberation Serif như Times New Roman**. Nếu không có font, lệnh trả `REVIEW_REQUIRED`; không tạo giả phép đo.
- Để tránh sửa nhầm, bản thử nghiệm chỉ tự động xử lý bảng dữ liệu phẳng, một section, với các run khai báo trực tiếp TNR 13/14. Các bảng phức tạp/khóa vẫn được audit nhưng không tự sửa.
- Chỉ sửa width của bảng được chọn. KHÔNG đổi font, số liệu, hướng giấy, header/footer, không tự điều chỉnh chiều cao hàng hoặc lặp tiêu đề ở bản này.
- Mọi score về line count chỉ là **FONT_METRIC_ESTIMATE**. Chưa có xác nhận rằng Word/WPS in không tràn/cắt.

## Exit codes / trạng thái

`0`: thao tác CLI hoàn tất, đọc trường `decision` để phân biệt `PROPOSE_APPLY` / `NO_OP_VALID` / `REVIEW_REQUIRED`. `2`: lỗi input/policy/stale/output. `word_render` luôn `NOT_RUN` khi không có renderer verification.

**Nền tri thức:** [AGENTS.md](AGENTS.md), [V15](docs/research/Bao_cao_chuan_hoa_va_toi_uu_bang_DOCX_ND30_HD05_V15_2026.md), [V16](docs/spec/AI_TABLE_FORMATTING_NO_RENDER_V16.md), [V17.5.1](docs/research/V17_5_1/README.md).
