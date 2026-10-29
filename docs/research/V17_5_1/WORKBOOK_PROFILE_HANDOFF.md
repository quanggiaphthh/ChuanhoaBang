# ChuanhoaBang V17.5.1 — Bàn giao policy orientation cho workbook/profile

**Quy tắc bắt buộc (USER-ORIENTATION-001): Quyền quyết định DỌC/NGANG thuộc người dùng.**

- **Mặc định PORTRAIT** đối với bảng/tài liệu **mới** nếu người dùng không quy định. Không có tự động chuyển ngang do nhiều cột, width, ngắt dòng hay điểm thẩm mỹ.
- Đối với DOCX **hiện hữu**, nếu người dùng không yêu cầu đổi thì **giữ nguyên hướng section đang có** (kể cả nó đã ngang); không tự chuyển về dọc.
- Width vượt vùng dọc -> báo `PORTRAIT_WIDTH_RISK` và `REVIEW_REQUIRED` hoặc `NO_SAFE_PORTRAIT_FIT`; chỉ xem xét thay width, padding trong phạm vi có quyền, không giảm TNR dưới 13 hoặc giảm 14→13 nếu chưa được phép. **Không phát sinh lệnh đổi ngang**.
- Chỉ khi yêu cầu trực tiếp `EXPLICIT_LANDSCAPE` có phạm vi hợp lệ mới có thể xét đổi ngang. Trước khi thực hiện phải kiểm tra loại văn bản, trạng thái mẫu, chữ ký, quyền sửa, section, lề, header/footer, đánh số trang, caption và tác động vùng lân cận. Yêu cầu trực tiếp không tự vượt document/form lock.
- `EXPLICIT_PORTRAIT` với tài liệu hiện ngang: đánh giá đổi về dọc theo phạm vi chỉ định, không tự đổi vùng khác.
- ND30/HD05 cho phép các tình huống trình bày ngang theo quy định liên quan, **không trao quyền tự quyết cho AI**. Phân biệt văn bản của Đảng và văn bản DNNN; chỉ TNR 13–14 pt.

## Trường đề xuất trong profile/workbook

| Trường | Loại/giá trị | Ý nghĩa |
|---|---|---|
| `orientation_request` | `UNSPECIFIED/EXPLICIT_PORTRAIT/EXPLICIT_LANDSCAPE` | Chỉ lấy từ người dùng |
| `orientation_request_source` | `NONE/USER_MESSAGE/USER_APPROVAL` | Truy vết quyền yêu cầu |
| `orientation_current` | `PORTRAIT/LANDSCAPE/UNKNOWN` | Đọc section hiện hữu |
| `orientation_default` | `PORTRAIT` | Chỉ cho bảng/tài liệu mới |
| `orientation_change_scope` | table/section selector | Phạm vi yêu cầu |
| `orientation_change_authorized` | boolean | Không suy từ width |
| `width_overflow_flag` | boolean/unknown | Chỉ cảnh báo |
| `section_impact_reviewed` | boolean | Kiểm tra section và phụ thuộc |
| `form_lock_status` | `UNLOCKED/LOCKED/UNKNOWN` | Veto bảo toàn |
| `orientation_decision` | xem spec V17.5.1 | Nhãn quyết định sau policy gate |

## Pseudocode policy

```text
IF form_locked OR signed_or_protected: PRESERVE_LOCKED_REVIEW_AUTHORITY
ELSE IF orientation_request == UNSPECIFIED:
    IF new_document: KEEP_PORTRAIT_DEFAULT
    ELSE: KEEP_EXISTING_ORIENTATION
    IF portrait_width_issue: report PORTRAIT_WIDTH_RISK only
ELSE IF orientation_request == EXPLICIT_LANDSCAPE:
    REVIEW section/authority/geometry/scope; do not assume automatically applied
ELSE IF orientation_request == EXPLICIT_PORTRAIT:
    REVIEW section/authority/geometry/scope; do not change unrelated sections
```

**Version alignment:** V17.5 `LANDSCAPE_CANDIDATE` và `LANDSCAPE_OPTIONAL` bị thu hồi khỏi nhánh quyết định tự động. Dùng nhãn và dữ liệu `orientation_cases_all_48.jsonl` V17.5.1. 32 ca cũ có `superseded_v175_label` chỉ phục vụ truy vết. Các trị số width là giả định chưa được đo glyph/render.

**Trạng thái:** SPEC_UPDATED, DATA_QA_PASS; no model test, no Word render, no changes committed to GitHub.