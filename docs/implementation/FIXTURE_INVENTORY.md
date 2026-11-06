# Fixture & acceptance inventory — 05/11/2026

| Nguồn | Khả năng truy xuất trong GitHub | Mức bằng chứng / hành động |
|---|---|---|
| V10 F01–F08 ZIP lịch sử | **UNAVAILABLE** trong repository hiện tại; manifest/checksum mô tả tại `docs/verification/EXPERIMENT_EVIDENCE.md` | Chưa thể chạy lại nguyên bản. Không dựng lại fixture mới rồi gọi là bản gốc. |
| V11 F01/F02, V12 F03/F07/F08, V15 4 ca boundary | **UNAVAILABLE** dưới dạng DOCX gốc | Chờ nhập artifact có checksum đúng |
| V17.4 128 prompt / 64 cặp | JSONL/CSV có trong repo | Chỉ có thể tái lập protocol/spec-scoring, **không phải** DOCX formatter tests |
| `tests/test_core.py` | Synthetic unit fixtures tạo tại thời điểm test | Có thể chạy lại ngay, nhưng không xác nhận Word render |

## Gate

- **L0 (structure):** ZIP hợp lệ, source không đổi, non-target OPC parts byte-identical, target text/topology không đổi, output reopen, signer/lock fail-closed.
- **L1 (rules & geometry):** orientation không đổi; auto-width chỉ trong `available_twips` và không nhỏ hơn protected token floor theo font được cung cấp; unsupported → REVIEW.
- **L2 (renderer):** Word Print Layout với version/build, font fingerprint, ảnh before/after và file hash. `NOT_RUN` đến khi có bằng chứng.

## Bài thử ưu tiên khi nhập lại dữ liệu thật

1. F01 (width benefit), F02 (wrong candidate KEEP), F03 (multi-page), F07 (margin), F08 (`trHeight=exact`), V15 DOCX-grid/PDF-border mismatch.
2. Văn bản ND30/HD05 có layout header/signature tables; biểu mẫu khóa, nested/merged; số 0 đầu, 0, dấu tiếng Việt, token NBSP.
3. ZIP lỗi hoặc trùng tên part, nguồn đổi sau propose, orientation dọc/ngang và multi-section.

Mọi fixture được nhận thêm phải có `sha256`, license/nguồn, ẩn danh dữ liệu thật, renderer version, expected action và trạng thái Word acceptance độc lập.
