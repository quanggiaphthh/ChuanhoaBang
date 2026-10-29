# ChuanhoaBang V17.5.1 — User-controlled orientation addendum

Bổ sung quy tắc **chỉ người dùng mới quyết định trình bày dọc/ngang**; bảng/tài liệu mới mặc định PORTRAIT; DOCX hiện có bảo toàn orientation nếu không yêu cầu. AI có thể cảnh báo quá rộng nhưng không tự chuyển ngang.

## Tài liệu
- `V17_5_1_ADMIN_TABLES_USER_CONTROLLED_ORIENTATION_SPEC.md` — đặc tả đầy đủ, giữ 10 nhóm bảng và thông tin nghiên cứu trước đó, thay quyết định orientation.
- `WORKBOOK_PROFILE_HANDOFF.md` — trích logic cho chat đang phát triển workbook/rule offline.
- `orientation_cases_32_user_controlled.jsonl` — 32 case cũ, giữ nội dung, thay nhãn và gắn policy.
- `orientation_user_request_variants_16.jsonl` — 16 ca biến thể để kiểm tra quyền và tính bảo toàn.
- `orientation_cases_all_48.jsonl` / `.csv` — toàn bộ.
- `MIGRATION_V17_5_TO_V17_5_1.csv` — đối chiếu nhãn cũ–mới.
- `QA_REPORT.json` / `MANIFEST.json` — QA và SHA-256.

Các phiên bản gốc V17.5 **không bị chỉnh sửa**; nhãn V17.5 bị thay thế chỉ trong nhánh chính sách orientation. Dữ liệu case là giả định chưa phải phép đo Word/LLM hay thẩm định chuyên gia.