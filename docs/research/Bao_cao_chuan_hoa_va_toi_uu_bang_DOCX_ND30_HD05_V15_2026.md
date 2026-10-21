# BÁO CÁO NGHIÊN CỨU TỔNG HỢP
## Quy định thể thức, kỹ thuật trình bày và chuẩn chất lượng thẩm mỹ của BẢNG trong văn bản hành chính và văn bản của Đảng

**Phiên bản:** 15.0 (hợp nhất V1–V14; V15 kiểm chứng 24 biến thể margin sensitivity trên bốn phương án F07, phân biệt gate hình học với viền PDF; 152 kịch bản T01–T152 vẫn chỉ là đặc tả)  
**Thời điểm cập nhật và đối chiếu:** 21/10/2026  
**Đối tượng:** Bảng dữ liệu, bảng thống kê, bảng biểu, bảng trong nội dung và phụ lục của văn bản Microsoft Word (`.docx`).  
**Phạm vi chính:** Văn bản hành chính theo Nghị định 30/2020/NĐ-CP; văn bản của Đảng theo Quy định 399-QĐ/TW và Hướng dẫn 05-HD/VPTW năm 2026.  
**Mục đích:** Làm căn cứ nghiên cứu, lập checklist kiểm tra tài liệu, đề xuất quy tắc trình bày và đặc tả cho công cụ chuẩn hóa bảng DOCX. **Không phải văn bản quy phạm hoặc tiêu chuẩn bắt buộc do cơ quan nhà nước ban hành.**

---

## MỤC LỤC NỘI DUNG

- **Tóm tắt điều hành:** Những kết luận chính và cách phân biệt quy định với khuyến nghị.
- **Phần I:** Cơ sở pháp lý, văn bản còn hiệu lực và giới hạn áp dụng.
- **Phần II:** So sánh các thông số giữa Nghị định 30 và Hướng dẫn 05; bảng trong thân văn bản/phụ lục.
- **Phần III:** Phân loại bảng theo chức năng và vị trí sở hữu nội dung.
- **Phần IV:** Best practice về đường viền, màu, khoảng trắng, cột, căn chỉnh, số liệu và tiêu đề.
- **Phần V:** Bảng nhiều trang, phân trang, accessibility, in và chuyển đổi PDF.
- **Phần VI:** Danh mục 20 lỗi thường gặp và tình huống cần giữ nguyên hoặc xác nhận.
- **Phần VII:** Ba preset trình bày bảng và tiêu chí lựa chọn.
- **Phần VIII:** Bộ quy tắc, cơ chế phát hiện–sửa an toàn và thành phần WordprocessingML.
- **Phần IX:** Thang đánh giá chất lượng, checklist nghiệm thu và kiểm thử theo phạm vi ảnh hưởng.
- **Phần X:** Thứ tự ưu tiên và kiến nghị triển khai (nội dung nghiên cứu kế thừa từ V1).
- **Phần XI:** Định nghĩa tối ưu, rule authority, chính sách fail-closed.
- **Phần XII:** Hình học trang, đơn vị OOXML, tối ưu độ rộng cột và bảng quá rộng.
- **Phần XIII:** Tám loại bảng, design token, typography và chuẩn nghiệm thu trực quan.
- **Phần XIV:** Bảng phức tạp/lồng, merged/omitted cells, biểu mẫu bảo vệ, style cascade.
- **Phần XV:** Phân trang, Word Print Layout, khác biệt khi xuất PDF.
- **Phần XVI:** Luồng quyết định, quyền sửa, ví dụ schema quy tắc.
- **Phần XVII:** Bộ 30 tình huống kiểm thử, chứng cứ, tiêu chí PASS/FAIL.
- **Phần XVIII:** Checklist Word, đánh giá reuse và lộ trình áp dụng theo phạm vi.
- **Phần XIX (V3):** Xác định nội dung trọng tâm; chấm ưu tiên theo tác vụ; đo chiều rộng nội dung; phân phối mm theo ràng buộc và lợi ích biên; ví dụ, nguồn OSS, 22 trường hợp thử nghiệm.
- **Phần XX (V4):** Tách cấp bằng chứng và rủi ro; tối ưu dựa trên nút thắt chiều cao hàng, tác động phân trang; so sánh baseline/ứng viên; tìm kiếm hữu hạn, Pareto, nguyên twips, các trường hợp vô nghiệm, bổ sung 28 ca T53–T80.
- **Phần XXI (V5):** Hợp đồng nhận diện trọng tâm; kiểm tra vùng in hai mặt/section/bảng lồng; bốn mức phép đo; quyết định 11 bước; OPC preservation; kiểm Word/PDF; 16 ca T81–T96; điều kiện triển khai tối thiểu.
- **Phần XXII (V6):** Benchmark có manifest, hard gates, ngưỡng hiệu chỉnh, thử nghiệm A/B, bốn oracle, kiểm soát chữ ký số, tiêu chí D0–D5 và 12 ca bổ sung T97–T108.
- **Phần XXIII (V7):** Bằng chứng nhận diện trọng tâm; physical-grid & merged constraints; width ưu tiên so với width thật; style cascade/border; state machine; metric catalog; pseudocode tìm ứng viên; 16 ca T109–T124.
- **Phần XXIV (V8):** Định danh ổn định, phép đo tiếng Việt/font, giới hạn geometry Word, nhiệm vụ người đọc, danh mục hành động A0–A6, hard gates G0–G4, mô hình renderer/traceability, 20 ca T125–T144.
- **Phần XXV (V9):** Audit giới hạn V8, kiểm soát đo chữ/ngắt dòng Unicode, phân biệt gridlines/borders in, cùng họ bảng trong tài liệu, đánh giá bằng baseline có cặp, ma trận hành động và 8 ca T145–T152.
- **Phần XXVI (V10):** Corpus 8 fixture DOCX tự tạo, kiểm chứng kết xuất LibreOffice, F08 nguồn–ứng viên về hàng `Exactly` cắt chữ, manifest/checksum, protocol nghiệm thu Word và điều kiện chuyển giai đoạn; không tăng số lượng test spec thiếu bằng chứng.
- **Phần XXVII (V11):** Thử nghiệm phân bổ độ rộng cột có đối chứng F01/F02 trên 9 kết xuất LibreOffice; đo chiều cao từ PDF, ràng buộc header và nội dung, giữ baseline khi không có lợi ích; công khai dữ liệu, mã tái lập và giới hạn.
- **Phần XXVIII (V12):** Thực nghiệm trên F03–F07; bảng dài, hàng bị chia, ô gộp/bảng lồng, mẫu preserve, A4 ngang; 18 kết xuất LO, điều kiện giữ nguyên/từ chối và kiểm chứng OCR-free.
- **Phần XXIX (V13):** Kiểm định khả năng duy trì lợi ích theo biến thiên cỡ chữ, cổng kiểm hình học khi thay đổi lề, ngăn phát hiện mất dữ liệu giả do ngắt trang; 14 kết xuất LO, không thay ngưỡng hay mở rộng 152 ca T01–T152.
- **Phần XXX (V14):** Thử tái phân bổ lại chiều rộng sau khi lề F07 thay đổi: 1 đối chứng + 4 phương án × (gốc, tăng font 1 pt), 10 kết xuất LO; phân xử tie-break, phân biệt vượt lề của viền và mất chữ, bảo toàn XML/OPC; chưa nghiệm thu Word.
- **Phần XXXI (V15):** Kiểm tra lại bốn phương án V14 khi lề phải tiếp tục thay đổi: 24 DOCX/PDF, hai cổng hình học/kết xuất, phát hiện 4 trường hợp PDF chưa vượt nhưng lưới OOXML đã vượt; xác định cơ chế vô hiệu hóa ứng viên cũ và giới hạn ngưỡng dự phòng.
- **Lưu ý V14:** Chưa chứng minh N1–N4 khác nhau về thẩm mỹ trên mẫu này; không tự quảng bá N2 là tối ưu duy nhất.
- **Lưu ý V13:** F03/F07 là dữ liệu tổng hợp; tăng font +2 pt F03 là stress ngoài profile cỡ chữ nội dung chung của Đảng; chỉ công nhận phép thử LO, chưa nghiệm thu Word.
- **Lưu ý V11:** Hai bảng nguồn tổng hợp; 9 bản render, 7 bản patch chỉ thay `word/document.xml`; không suy rộng từ kết quả LibreOffice sang Microsoft Word hoặc toàn bộ bảng thực tế; **152 ca T01–T152 vẫn chỉ là đặc tả, chưa chạy toàn bộ**.
- **Lưu ý V10:** Đã thực nghiệm **riêng corpus giả lập** bằng LibreOffice (môi trường và phạm vi công khai); **chưa kiểm bằng Microsoft Word**, chưa triển khai engine dự án, chưa chạy 152 kịch bản T01–T152 trên ứng dụng.
- **Phụ lục A–C:** Thuộc tính chưa có định mức chung, ví dụ minh họa và nguồn tham khảo (tổng hợp đến [S97]).

---

# HƯỚNG DẪN SỬ DỤNG NHANH V11 — MA TRẬN QUYẾT ĐỊNH MỘT TRANG

**Đầu vào cần biết:** loại văn bản/mẫu; bảng cần xử lý; vùng chứa/section; nhiệm vụ người đọc; trường trọng tâm; thuộc tính được phép sửa; renderer đích nếu yêu cầu bảo đảm kết quả in.

| Câu hỏi kiểm tra theo thứ tự | Nếu CÓ | Nếu KHÔNG hoặc chưa rõ |
|---|---|---|
| 1. Bảng thuộc đúng loại văn bản và mẫu? | Chọn bộ authority, khóa vùng thể thức | `REVIEW_REQUIRED`, không kết luận vi phạm |
| 2. Định danh bảng, owner và source snapshot chắc chắn? | Chụp provenance & bất biến | `STALE_SOURCE` hoặc `BLOCKED` |
| 3. Bảng có lỗi đọc/tràn/cắt/viền/phan trang thực? | Đặt mục tiêu và thước đo trước khi tạo ứng viên | `A0_KEEP`, không chỉnh máy móc |
| 4. Hình học, khóa mẫu, token quan trọng, font được xác minh? | Tính khả thi và các candidate hữu hạn | Chỉ chẩn đoán hoặc review; không APPLY tự động |
| 5. Có ứng viên giữ nguyên dữ liệu/cấu trúc và không tạo hồi quy? | Đối chiếu baseline, chọn thay đổi nhỏ nhất | Giữ nguyên và ghi reason code |
| 6. Đã có O1/O2 PASS và Word render O3 khi yêu cầu khớp bản in? | Mới đủ điều kiện trình phương án tương ứng | Ghi đúng `STRUCTURE_VERIFIED`/`UNVERIFIED` |
| 7. Đã được phê duyệt trong phạm vi cần thiết? | APPLY cục bộ, reopen, diff, có rollback | Chỉ hiển thị đề xuất; không tự ghi file |

**Ba điều tuyệt đối không được nhầm:** `semantic_priority ≠ width_need`; `break_opportunity ≠ actual_word_line_break`; `Word gridlines ≠ printed borders`.

**Nguyên tắc giữ nguyên:** Khi không chứng minh được lợi ích thực chất, hoặc không có môi trường kiểm chứng theo đầu ra mà người dùng cần, `KEEP_EXISTING/REVIEW_REQUIRED` là kết quả đúng, không phải thất bại của thuật toán.

---

# TÓM TẮT ĐIỀU HÀNH

**Bổ sung trọng tâm V11:** Thử nghiệm tái lập việc phân bổ độ rộng cột với F01/F02: bảng F01 từ 72,46 mm còn 46,11 mm (giảm 36,37%) ở phương án cân đối, hai ứng viên thu hẹp quá mức khiến tiêu đề STT bị ngắt; bảng F02 khi nới nhãn quá mạnh tăng chiều cao 17,48%, do đó nên giữ nguyên baseline khi không có cải thiện. Đã bổ sung đối chứng fixed-equal với kết quả bằng baseline, kiểm bảo toàn các part và ảnh kết xuất. Kết quả chỉ trên LibreOffice 25.2 và corpus tổng hợp, chưa có Word validation. Xem Phần XXVII, mục 185–198.

**Bổ sung trọng tâm V10:** Giữ nguyên 152 ca đặc tả; bổ sung 8 fixture DOCX tự tạo có checksum, quan sát lặp tiêu đề trên 6 trang trong LibreOffice và một cặp F08 `exact → atLeast` giảm che chữ trong PDF LibreOffice mà bảo toàn chuỗi text. Đây là **kiểm chứng giới hạn trên dữ liệu giả lập**, không phải nghiệm thu Microsoft Word hay module production. Xem Phần XXVI, mục 173–184.

**Bổ sung trọng tâm V9:** Tách ba tầng nhận diện chữ/grapheme – cơ hội ngắt dòng – Word rendered line; không coi View Gridlines là viền in; không ép bảng luôn phủ toàn vùng có thể; kiểm tra thêm tính nhất quán của cùng họ bảng trong một văn bản nhưng không động đến biểu mẫu được bảo vệ. Thiết lập oracle chuẩn, mô hình phân bổ theo lợi ích toàn hàng và 8 ca T145–T152 (tổng 152 tình huống đặc tả). Xem Phần XXV, mục 158–172.

**Bổ sung trọng tâm V8:** Gắn quyết định độ rộng với **đúng story–section–vùng chứa–font–renderer**; phân biệt các hard gates G0 với tiêu chí khả năng đọc, bố cục và thẩm mỹ G1–G4; giới hạn các thao tác A0–A6, có state khi nguồn/renderer không đủ và ma trận T125–T144. Dẫn đến 144 tình huống đặc tả (không phải đã chạy). Xem Phần XXIV, mục 139–157.

**Bổ sung trọng tâm V7:** Chuyển hợp đồng V6 sang các điều kiện thao tác cụ thể: chứng cứ nào đủ xác nhận cột trọng tâm, giải constraint trên grid vật lý và ô gộp, phân biệt `preferred width` với width được render, xác định kiểu viền/nhìn hiệu dụng theo style cascade, xếp ứng viên và tie-break theo hard gates, áp dụng patch với rollback và chứng cứ rõ ràng. Bổ sung T109–T124 (16 ca đề xuất), tổng 124 ca. Xem Phần XXIII, mục 122–138.

**Bổ sung trọng tâm V6:** Bộ tiêu chí nghiệm thu không chỉ hỏi ứng viên có vẻ đẹp hơn, mà yêu cầu chứng minh cổng bảo toàn, nhận diện đúng cột trọng tâm, benchmark có thể tái lập, ngưỡng lợi ích đã hiệu chỉnh và renderer đích đã kiểm. Mẫu chữ ký số phải được nhận diện và chặn; schema PASS không đồng nghĩa Word layout PASS. Hoàn thiện 12 kịch bản T97–T108 (tổng 108 kịch bản đặc tả). Xem Phần XXII, mục 108–121.

**Bổ sung trọng tâm V5:** Chuẩn hóa quyết định thành `task brief → locks/geometry → đề xuất hữu hạn → kiểm chứng → KEEP/REVIEW/APPLY`. Tách rõ `M0_SOURCE`, `M1_ESTIMATE`, `M2_RENDER`, `M3_TARGET`; kết quả `NO_OP_VALID` là hợp lệ khi bảng đã đạt hoặc không chứng minh được lợi ích. Kiểm soát nguy cơ biến mất `AlternateContent`/Track Changes khi lưu và những đặc điểm của tài liệu in hai mặt. Xem Phần XXI, mục 94–107.

**Bổ sung trọng tâm V4:** Phải đánh giá vector độ rộng trên cả bảng, vì chiều cao hàng bị chi phối bởi ô cao nhất; thay đổi nhỏ có thể làm chuyển trang, ảnh hưởng caption hoặc phần chữ ký sau bảng. Tạo và so sánh ứng viên với bản gốc trong cùng môi trường kết xuất, đồng thời chọn phương án ít xáo trộn nhất nếu lợi ích tương đương. Xem Phần XX (mục 80–93).

**Bổ sung trọng tâm V3 (giữ nguyên):** Phân biệt **ưu tiên ngữ nghĩa** của cột với **nhu cầu chiều rộng đo bằng mm**; tối ưu theo tác vụ người đọc, ràng buộc bố cục và lợi ích biên khi mở rộng cột. Cột hạn chót có thể rất quan trọng nhưng không cần rộng hơn cột diễn giải. Xem Phần XIX, mục 70–79.

**Bổ sung quan trọng của V2:** Tối ưu là **bài toán nhiều ràng buộc**: tuân thủ văn bản/mẫu → giữ nguyên nội dung/cấu trúc → không tràn/cắt khi in → thẩm mỹ và khả năng đọc; phải xác minh định dạng hiệu dụng và hình ảnh đầu ra. Không tự sửa bảng chữ ký, biểu mẫu, ảnh bảng hoặc dữ liệu chưa được cho phép.

**Kết luận cốt lõi:** Hai hệ quy định đang áp dụng kiểm soát thể thức và kỹ thuật trình bày văn bản nói chung, trong đó có những điều kiện tác động trực tiếp đến bảng (khổ giấy, phông chữ, vùng trình bày, hướng trang và phụ lục). Nhưng **không tồn tại một bảng thông số chung bắt buộc** quy định mọi bảng Word phải có viền 0,5 pt, cột rộng bao nhiêu, hàng cao bao nhiêu, nền màu gì hoặc tất cả dữ liệu phải căn giữa.

Chất lượng bảng cần được đánh giá theo **năm trụ cột**: (1) đúng căn cứ pháp lý, (2) chính xác nội dung và cấu trúc, (3) đẹp và nhất quán về thị giác, (4) ổn định khi in/phân trang, (5) dễ đọc và dễ tiếp cận. Cần phân biệt ba nguồn quy tắc: **bắt buộc theo quy định**, **bắt buộc theo mẫu/biểu mẫu chuyên ngành được chỉ định**, và **khuyến nghị kỹ thuật–thẩm mỹ**.

Các kết luận có giá trị thực tiễn nhất:

1. **Văn bản hành chính:** Nghị định 30/2020/NĐ-CP, Phụ lục I, quy định A4; lề trên/dưới 20–25 mm, trái 30–35 mm, phải 15–20 mm; Times New Roman/Unicode/đen; nội dung chung cỡ 13–14 pt. Trường hợp có bảng, biểu **không được làm thành phụ lục riêng** thì có thể trình bày theo chiều rộng. [S01]–[S03].
2. **Văn bản Đảng:** Quy định 399-QĐ/TW ngày 09/01/2026; Hướng dẫn 05-HD/VPTW ngày 27/05/2026 quy định A4, lề mặt trước 20/20/30/15 mm (trên/dưới/trái/phải); Times New Roman/Unicode/đen; nội dung chung 14–15 pt, đoạn văn tối thiểu 6 pt, giãn dòng Exactly 18–22 pt. Có bảng, biểu thì có thể trình bày ngang theo điều kiện tại mục IV.4.3. [S04]–[S06].
3. **Phụ lục có khác biệt hệ thống:** văn bản hành chính nếu có từ hai phụ lục thì đánh bằng **chữ số La Mã**; văn bản Đảng nếu có từ hai phụ lục thì đánh bằng **chữ số Ả-rập**. Số trang đánh riêng từng phụ lục. [S02], [S06].
4. **Không áp dụng máy móc thông số đoạn văn vào tất cả ô:** các thông số cỡ chữ, giãn dòng, thụt đầu dòng được quy định cho *nội dung văn bản*; phải xét vai trò bảng, mẫu biểu và vùng chứa. Đặc biệt, **không căn đều hai lề/không thụt đầu dòng 1 cm cho mọi ô bảng** chỉ vì quy định về đoạn văn thông thường.
5. **Mẫu đề xuất:** `Formal Grid – Monochrome` cho bảng hành chính thông dụng; `Statistical Minimal` cho bảng thống kê nếu phù hợp; `Preserve Official Form` cho biểu mẫu/mẫu chính thức. Chỉ sửa khi được cho phép, bảo toàn văn bản gốc.
6. **Điều kiện không thể đánh đổi:** không mất/sai số liệu, thay đổi thứ tự hàng/cột, phá ô gộp, ảnh, trường dữ liệu, vị trí phụ lục, biểu mẫu hoặc cấu trúc bảng để đổi lấy điểm thẩm mỹ.

**Ký hiệu sử dụng trong báo cáo:**

- **[PL] – Pháp lý/quy định:** nội dung có căn cứ điều khoản từ văn bản gốc.
- **[BM] – Biểu mẫu:** phải tuân thủ nếu tài liệu sử dụng biểu mẫu chuyên ngành/cơ quan đã ban hành.
- **[KN] – Khuyến nghị:** best practice hoặc preset đề xuất, **không phải yêu cầu pháp lý bắt buộc**.
- **[KT] – Kỹ thuật:** đặc tính Microsoft Word/Office Open XML hoặc đề xuất cho công cụ DOCX.
- **[BK] – Bảo toàn:** bất biến nội dung/cấu trúc cần giữ khi thao tác trên tài liệu có sẵn.

---

# PHẦN I. CƠ SỞ PHÁP LÝ VÀ PHẠM VI ÁP DỤNG

## 1. Văn bản hành chính

**[PL] Nghị định số 30/2020/NĐ-CP ngày 05/03/2020 của Chính phủ về công tác văn thư** là căn cứ chính. Cơ sở dữ liệu quốc gia về văn bản pháp luật ghi tình trạng **còn hiệu lực** tại thời điểm đối chiếu. Cần tập trung:

- **Phụ lục I:** thể thức, kỹ thuật trình bày văn bản hành chính, bao gồm khổ giấy, hướng trang, lề, phông, cỡ chữ theo thành phần, phần nội dung và phụ lục.
- **Phụ lục III:** các mẫu trình bày văn bản và phụ lục; phải xem mẫu cụ thể khi tài liệu thuộc loại đó.
- Các mẫu biểu chuyên ngành, quyết định ban hành mẫu hoặc hướng dẫn riêng của đơn vị: kiểm tra theo phạm vi áp dụng, không tự suy ra từ bảng thông thường. [S01], [S02], [S03].

**Văn bản không còn sử dụng làm căn cứ hiện hành:** Thông tư 01/2011/TT-BNV đã bị bãi bỏ toàn bộ theo Thông tư 01/2020/TT-BNV, có hiệu lực ngày 15/06/2020. Các hướng dẫn cũ chỉ có thể tham khảo lịch sử, không làm nguồn quy tắc hiện hành. [S15].

## 2. Văn bản của Đảng

**[PL] Quy định số 399-QĐ/TW ngày 09/01/2026 của Ban Bí thư** quy định về thể loại, thẩm quyền ban hành và thể thức văn bản của Đảng; hiệu lực từ ngày ký. [S04].

**[PL] Hướng dẫn số 05-HD/VPTW ngày 27/05/2026 của Văn phòng Trung ương Đảng** hướng dẫn cụ thể thể thức và kỹ thuật trình bày văn bản giấy, điện tử; có hiệu lực từ ngày ký, thay thế Hướng dẫn 36-HD/VPTW ngày 04/03/2018. [S05], [S06].

Các mục cần đối chiếu khi bảng xuất hiện trong tài liệu:

- Phần II, Mục I, **6.2. Kỹ thuật trình bày nội dung**.
- Phần II, Mục II, **1. Phụ lục**.
- Phần II, Mục IV, **phông chữ, khổ giấy, định lề, hướng trang và số trang**, đặc biệt mục **4.3** về bảng biểu.
- **Phụ lục 2** của Hướng dẫn 05: bảng cỡ chữ/kiểu chữ theo *thành phần thể thức*. [S06].

**Giới hạn đối tượng:** Hướng dẫn 05 có phạm vi áp dụng cụ thể; văn bản chuyên ngành, văn bản in thành sách và các ấn phẩm khác được nêu là không thuộc phạm vi điều chỉnh của Hướng dẫn này. Không lấy Hướng dẫn 05 làm chuẩn cho mọi tài liệu chỉ vì có logo hoặc tiêu đề cơ quan Đảng. [S06].

## 3. Văn bản quy phạm pháp luật là hệ riêng

**[PL]** Bảng và phụ lục của **văn bản quy phạm pháp luật** cần kiểm tra theo chế độ chuyên biệt (Nghị định 78/2025/NĐ-CP và các sửa đổi liên quan, trong đó Nghị định 187/2025/NĐ-CP thay thế các phụ lục của Nghị định 78). Theo hướng dẫn về Nghị định 78, phụ lục có bảng biểu có thể trình bày ngang. Không coi đây là cách thay thế điều kiện riêng của Nghị định 30 dành cho văn bản hành chính thông thường. [S16], [S17].

**Quy tắc chọn căn cứ:** trước khi kiểm tra bảng phải xác định **loại văn bản, cơ quan ban hành, thời điểm áp dụng, mẫu bắt buộc**. Nếu chưa xác định được nguồn quy tắc thì không tự kết luận là “sai quy định”.

## 4. Thang độ tin cậy và nguyên tắc sử dụng nguồn

| Loại nguồn | Độ ưu tiên | Cách sử dụng |
|---|---|---|
| Văn bản chính thức, CSDL quốc gia VBPL, hệ thống tư liệu Đảng | Cao nhất | Xác lập yêu cầu pháp lý/quy định |
| Bản toàn văn công khai tại cổng cơ quan, báo chính phủ | Cao | Đối chiếu điều khoản và phụ lục |
| Microsoft Support / Microsoft Learn / Office Open XML | Cao về tính năng kỹ thuật | Xác định khả năng thực hiện và giới hạn Word |
| Government Analysis Function, W3C, Section508.gov | Cao về nghiệp vụ/khả năng tiếp cận | Tham khảo best practice, **không** chuyển thành luật Việt Nam |
| Blog hướng dẫn và mẹo Word | Bổ trợ | Chỉ dùng sau khi đối chiếu nguồn chính thức |

**Lưu ý phương pháp:** khi nói “chưa có một thông số bắt buộc chung”, đó là kết quả rà soát trong các văn bản nền tảng nêu tại báo cáo, **không loại trừ** biểu mẫu cụ thể hoặc quy chế được phép ban hành của cơ quan.

---

# PHẦN II. SO SÁNH THÔNG SỐ VÀ QUY ĐỊNH LIÊN QUAN ĐẾN BẢNG

## 5. Bảng so sánh tổng hợp

| Tiêu chí | Hành chính – NĐ30/2020 | Đảng – QĐ399 + HD05/2026 | Phân loại/ghi chú |
|---|---|---|---|
| Khổ giấy văn bản thông thường | A4, 210 × 297 mm | A4, 210 × 297 mm | [PL]; HD05 có ngoại lệ cho một số giấy tờ hành chính/mẫu in sẵn |
| Hướng trang mặc định | Dọc | Dọc | [PL] |
| Hướng ngang khi có bảng | Có thể dùng nếu bảng, biểu **không được làm thành phụ lục riêng** | Có thể dùng nếu có bảng, biểu; căn cứ vùng trình bày dọc để bố trí phù hợp | [PL]; điều kiện khác nhau |
| Lề trên | 20–25 mm | 20 mm | [PL] |
| Lề dưới | 20–25 mm | 20 mm | [PL] |
| Lề trái mặt trước | 30–35 mm | 30 mm | [PL] |
| Lề phải mặt trước | 15–20 mm | 15 mm | [PL] |
| In hai mặt, mặt sau | Kiểm tra phạm vi/mẫu cụ thể | Lề trên/dưới 20 mm; trái 15 mm, phải 30 mm | [PL] HD05 mục IV.4.2 |
| Phông tiếng Việt | Times New Roman | Times New Roman | [PL] |
| Bộ mã và màu chữ chung | Unicode – TCVN 6909:2001, đen | Unicode – TCVN 6909:2001, đen | [PL] |
| Cỡ chữ **nội dung chung** | 13–14 pt | 14–15 pt | [PL], **không** phải định mức độc lập cho từng ô bảng |
| Khoảng cách đoạn nội dung | Tối thiểu 6 pt | Tối thiểu 6 pt | [PL] cho nội dung chung |
| Giãn dòng nội dung | Tối thiểu đơn, tối đa 1,5 dòng | Exactly 18–22 pt | [PL] cho đoạn văn nội dung chung |
| Nhiều phụ lục | Số La Mã: I, II, III... | Số Ả-rập: 1, 2, 3... | [PL]; sự khác biệt cần bảo vệ |
| Số trang phụ lục | Riêng theo từng phụ lục | Riêng theo từng phụ lục | [PL] |
| Độ rộng cột, cao hàng, nền, nét viền | Không có bộ giá trị chung cố định cho mọi bảng | Không có bộ giá trị chung cố định cho mọi bảng | [KN]/[BM] tùy trường hợp |

**Nguồn:** Nghị định 30 và Phụ lục I [S01]–[S03]; Hướng dẫn 05, phần II và Phụ lục 2 [S05], [S06].

## 6. Áp dụng các thông số nội dung cho ô bảng: tránh suy diễn

**[PL]** Các đoạn quy định về phần nội dung văn bản có phạm vi riêng. Đặc biệt:

- Nội dung văn bản hành chính: chữ thường, đứng, cỡ 13–14; căn đều hai lề; đầu dòng lùi 1 cm hoặc 1,27 cm; đoạn cách tối thiểu 6 pt; khoảng cách dòng đơn đến 1,5. [S02].
- Nội dung văn bản Đảng: nội dung cỡ 14–15; dàn đều hai lề, đầu dòng lùi khoảng 10 mm; đoạn cách tối thiểu 6 pt; dòng 18–22 pt theo Exactly. [S06].

**[KN]/[KT] Kết luận áp dụng cho bảng:** phông/cỡ chữ văn bản là cơ sở thẩm định, song bảng có chức năng hiển thị khác đoạn văn thông thường. Không đặt chế độ thụt đầu dòng 10 mm cho tất cả ô, không bắt buộc căn đều các cột số, không thu nhỏ toàn bộ chữ xuống 9–10 pt để ép vừa trang. Khi gặp mẫu chuyên ngành cần tuân thủ chính mẫu đó.

## 7. Bảng trong phần nội dung chính

**[PL]** Bảng ở giữa các đoạn của văn bản có thể dùng để thể hiện phân công, danh sách, thống kê, lịch công tác, tiến độ, kết quả kiểm tra... Bảng không tự động trở thành phụ lục chỉ vì dài hoặc có tiêu đề riêng.

**[KN]** Một bảng trong nội dung nên có:

- Vị trí hợp lý sau đoạn giới thiệu hoặc dẫn chiếu; không tách rời đoạn liên quan.
- Độ rộng không vượt vùng có thể in; không xâm lấn lề, số trang hoặc thành phần thể thức khác.
- Kiểu chữ, tiêu đề, đường viền nhất quán với các bảng cùng chức năng.
- Tên bảng/đơn vị tính/nguồn số liệu khi có nhu cầu; không tự bổ sung dữ liệu chưa được cung cấp.
- Chiều cao hàng đủ chứa nội dung, tránh ô cắt chữ.

## 8. Bảng trong phụ lục

**[PL]** Phụ lục là đơn vị văn bản cần được nhận diện riêng, bao gồm thành phần thể thức phụ lục và phần nội dung của phụ lục; không để bộ chuẩn hóa coi toàn bộ phụ lục là bảng thuộc thân văn bản.

**Đối với hành chính:**

- Văn bản chính phải có chỉ dẫn đến phụ lục.
- Từ hai phụ lục trở lên đánh số bằng **chữ số La Mã**.
- Dòng “Phụ lục” và số thứ tự được trình bày riêng, giữa trang, cỡ 14, đứng, đậm; tên phụ lục nếu có in hoa, đậm, cỡ 13–14, giữa trang.
- Thông tin kèm theo xác định văn bản ban hành; với văn bản điện tử có sự khác biệt về việc điền thông tin tại vị trí này theo quy định cụ thể.
- Số trang đánh riêng từng phụ lục; tham chiếu mẫu phụ lục tại Phụ lục III NĐ30. [S02].

**Đối với văn bản Đảng:**

- Có chỉ dẫn phụ lục trong văn bản chính; phụ lục được trình bày riêng, có tiêu đề.
- Từ hai phụ lục trở lên đánh số bằng **chữ số Ả-rập**.
- Dòng “Phụ lục và số thứ tự” trình bày riêng, căn giữa vùng chữ; tiêu đề bên dưới, tiếp đến thông tin chỉ dẫn gắn với văn bản.
- Số trang đánh riêng từng phụ lục. [S06].

**[BK]** Khi điều chỉnh một bảng trong phụ lục, không thay đổi số phụ lục, căn cứ dẫn chiếu, chữ ký/xác nhận hoặc ngắt phần phụ lục nếu không có phê duyệt riêng.

---

# PHẦN III. ĐỊNH NGHĨA VÀ PHÂN LOẠI BẢNG TRƯỚC KHI CHỈNH SỬA

## 9. Phân loại theo nhiệm vụ của bảng

| Loại bảng | Đặc điểm nhận diện | Chiến lược mặc định |
|---|---|---|
| Bảng dữ liệu thông thường | Lưới dữ liệu, hàng đầu thường là tiêu đề | Áp dụng `Formal Grid` nếu không có mẫu |
| Bảng số liệu/thống kê | Số, tỷ lệ, đơn vị, tổng cộng | Cân nhắc `Statistical Minimal` nếu không có mẫu |
| Bảng phân công/lịch công việc | STT, nhiệm vụ, người phụ trách, thời hạn | `Formal Grid`, cột nội dung rộng hơn |
| Bảng biểu mẫu chính thức | Có ô điền, vùng ký, cấu trúc cố định | `Preserve Official Form` |
| Bảng dàn trang/thể thức | Dùng ô để đặt tên cơ quan, ngày, chữ ký, nơi nhận... | **Không** xử lý như bảng dữ liệu |
| Bảng lồng nhau | Có bảng con trong một hoặc nhiều ô | Bảo toàn, kiểm tra bố cục theo cấp |
| Bảng dài nhiều trang | Bị chia bởi ngắt trang tự động | Kiểm tra hàng tiêu đề, chiều cao hàng, mối liên hệ tiêu đề–bảng |
| Bảng có ảnh/đồ họa/ký xác nhận | Ảnh, shape, field, hyperlink | Không biến đổi cấu trúc; kiểm tra quan hệ |

**[KT]** Việc phân loại phải dựa trên cấu trúc DOCX và ngữ cảnh, không dựa vào “bảng có đường viền hay không”. Bảng dùng để dàn trang có thể không kẻ viền; bảng dữ liệu cũng có thể không có viền dọc.

## 10. Phân loại theo vị trí sở hữu nội dung

Mỗi bảng nên gắn đúng **một vùng sở hữu duy nhất**:

- `main_body`: thuộc nội dung chính.
- `appendix[n]`: thuộc phụ lục n.
- `header`/`footer`: vùng đầu/chân trang.
- `layout_form`: bảng dàn trang thuộc một thành phần thể thức được chỉ định.
- `unclassified`: chưa thể xác định an toàn; không tự động sửa.

**[BK]** Không được để một bảng đồng thời xuất hiện ở body và appendix; không bỏ qua bảng trong ô hoặc bảng lồng; lưu vị trí gốc và khả năng truy vết.

---

# PHẦN IV. BEST PRACTICE THIẾT KẾ THẨM MỸ

## 11. Năm tiêu chí chất lượng tối thiểu

1. **Đúng thể thức:** loại văn bản, lề, trang, phông, phụ lục và mẫu đúng nguồn.
2. **Dễ đọc:** cỡ chữ, tương phản, đệm ô, căn chỉnh theo loại dữ liệu.
3. **Cân đối:** tỷ lệ các cột bám vào độ dài và tầm quan trọng nội dung.
4. **Rõ phân cấp:** tiêu đề, dữ liệu, tổng cộng, ghi chú và nguồn được nhận biết dễ dàng.
5. **Ổn định:** tài liệu Word/PDF và bản in không làm mất chữ, tràn lề hoặc ngắt trang khó hiểu.

W3C nhấn mạnh cấu trúc bảng và mối liên hệ giữa ô tiêu đề với ô dữ liệu; Government Analysis Function nhấn mạnh sự đơn giản, hạn chế viền thừa, căn phải số liệu và ghi nguồn hợp lý. [S10]–[S12].

## 12. Hệ thống đường viền

**[KN]** Không mặc định bảng nào cũng phải có mọi đường kẻ. Chọn theo công năng:

**Kiểu A – Kẻ ô truyền thống (Formal Grid):**

- Đường viền ngoài: nét đơn 0,75 pt (giá trị preset đề xuất).
- Đường kẻ bên trong: nét đơn 0,5 pt.
- Màu: đen hoặc xám đậm đủ rõ khi in trắng đen.
- Tiêu đề cột: đậm, có đường phân tách rõ; có thể dùng nền trắng.
- Phù hợp danh sách, bảng phân công, đối chiếu từng ô và biểu mẫu thông thường.

**Kiểu B – Bảng thống kê tối giản (Statistical Minimal):**

- Nền trắng, ưu tiên đường phân tách ngang tại hàng tiêu đề và dòng tổng.
- Hạn chế đường dọc hoặc nét quá đậm nếu không giúp so sánh số liệu.
- Căn phải số liệu; tiêu đề của cột số nên căn tương ứng.
- Phù hợp bảng phân tích/nghiên cứu khi không tồn tại mẫu bắt buộc.

**Kiểu C – Giữ biểu mẫu chuẩn (Preserve Official Form):**

- Giữ nguyên mọi đường kẻ có ý nghĩa (cả nét đứt, viền đậm, ô gộp).
- Chỉ chỉnh thuộc tính được xác nhận không làm biến đổi ý nghĩa biểu mẫu.

**Không coi 0,5 pt và 0,75 pt là quy định của NĐ30/HD05.** Chúng là thông số preset điều chỉnh được. [S11].

## 13. Màu nền, độ tương phản và kiểu chữ

**[KN]** Ưu tiên **đen–trắng**, tránh dùng màu thương hiệu nổi, đổ bóng, gradient, vân nền và đường kẻ quá dày trong văn bản chính thức.

| Thành phần | Mặc định đề xuất | Tùy chọn có kiểm soát |
|---|---|---|
| Chữ ô | Đen `#000000` | Không dùng màu cảnh báo trừ mẫu yêu cầu |
| Nền bảng | Trắng `#FFFFFF` | — |
| Nền hàng tiêu đề | Trắng | Xám rất nhạt `#F2F2F2` nếu phù hợp |
| Viền | Đen hoặc xám đậm | Kiểu khác nếu mẫu bắt buộc |
| Tiêu đề cột | Đứng, đậm, không trang trí | Căn trái/giữa theo dữ liệu |
| Dòng tổng | Đậm, phân tách rõ | Nét trên hơi đậm hơn |
| Ghi chú | Tiết chế, nhất quán | Có thể nghiêng khi mẫu cho phép |

Với phiên bản dùng trực tuyến hoặc bản phát hành cần truy cập số, có thể tham khảo ngưỡng **tương phản chữ thông thường 4,5:1 theo WCAG**, nhưng đó **không phải ngưỡng được Nghị định 30/HD05 quy định riêng cho bảng Word**. Không dựa riêng màu sắc để biểu thị “đạt/không đạt”. [S12], [S13].

**Giải quyết xung đột tiêu chuẩn:** hướng dẫn Government Analysis Function có lời khuyên dùng phông không chân cho bảng trực tuyến, nhưng văn bản hành chính và Đảng tại Việt Nam có quy định Times New Roman; **phông chữ theo quy định Việt Nam được ưu tiên**.

## 14. Khoảng đệm trong ô, khoảng cách ô và chiều cao hàng

**[KN]** Preset mặc định đề xuất:

| Thuộc tính | Mức đề xuất | Rủi ro nếu áp dụng sai |
|---|---|---|
| Đệm trái/phải (`cell margins`) | 1,5–2,0 mm | Thu hẹp vùng chữ; tăng số dòng |
| Đệm trên/dưới | 0,8–1,2 mm | Hàng tăng cao, tràn trang |
| Khoảng cách giữa các ô (`cell spacing`) | 0 mm | Tạo khoảng hở lạ, làm đứt viền |
| Chiều cao hàng | Auto hoặc tối thiểu (`At least`) | Cấm dùng `Exactly` tùy tiện vì có thể cắt chữ |
| Căn dọc hàng tiêu đề | Giữa | Ô nhiều dòng có thể lệch thị giác |
| Căn dọc ô mô tả dài | Trên | Nội dung ngắn có thể kém cân nếu lạm dụng |

Đây là **thông số tham khảo** để tinh chỉnh trên tài liệu thực tế, không phải quy chuẩn pháp lý. Microsoft Word hỗ trợ trực tiếp AutoFit, Fixed Column Width, Cell Margins, Cell Spacing; không cần tự xây bộ máy dàn bảng mới. [S08].

## 15. Tối ưu độ rộng cột

**Lưu ý nâng cấp V3:** phân loại “mức ưu tiên độ rộng” bên dưới là điểm khởi tạo theo *hình thức nội dung*, **không được hiểu là độ ưu tiên nghiệp vụ/ngữ nghĩa**. Quy trình xác định nội dung trọng tâm và phân bổ độ rộng bằng phép đo nằm tại Phần XIX (mục 70–79).

**[KN]** Không chia đều chiều rộng tất cả các cột nếu nội dung rất khác nhau. Hãy phân bổ ưu tiên:

- STT/mã ngắn: hẹp vừa đủ.
- Mô tả hoặc nội dung công việc: rộng nhất.
- Tên đơn vị/chủ trì: vừa, tránh bẻ tên thành quá nhiều dòng.
- Ngày hạn/tình trạng ngắn: hẹp nhưng đủ hiển thị.
- Cột số liệu: đảm bảo số, dấu âm, dấu thập phân và đơn vị không bị cắt.

**Ví dụ minh họa, không ràng buộc:** bảng 4 cột (STT / Nội dung / Đơn vị / Thời hạn) có thể bắt đầu với tỷ lệ **9% / 49% / 25% / 17%**, sau đó đo lại theo dữ liệu.

**Chiều rộng khả dụng:**

`W_vung_chu = W_trang - le_trai - le_phai`.

Với A4 dọc 210 mm:

- NĐ30: rộng khoảng **155–165 mm** tùy bộ lề 30–35 mm và 15–20 mm.
- HD05, mặt trước: **165 mm** (210 − 30 − 15).

Đây là phép tính theo vùng chữ lý thuyết; bảng có thụt lề, dấu đầu dòng, bố trí nổi, nested table hoặc độ rộng phân biệt theo section cần trừ phần chiếm dụng thực tế. **Không tự động xoay ngang** khi chưa kiểm tra căn cứ và tác động tới section.

## 16. Quy tắc căn ngang và căn dọc theo dữ liệu

| Loại dữ liệu | Căn ngang [KN] | Căn dọc [KN] | Lưu ý |
|---|---|---|---|
| STT, mã ngắn | Giữa | Giữa | Không đổi giá trị mã có số 0 đầu |
| Tên người, đơn vị | Trái | Trên/giữa | Phụ thuộc độ dài |
| Diễn giải, ghi chú dài | Trái | Trên | Tránh Justify tạo khoảng trắng lớn |
| Số nguyên | Phải | Giữa | Giúp so sánh chữ số |
| Số thập phân | Theo dấu thập phân hoặc phải | Giữa | Giữ dấu và độ chính xác |
| Tỷ lệ phần trăm | Phải | Giữa | Thống nhất số chữ số hiển thị |
| Giá trị tiền | Phải | Giữa | Đơn vị phải rõ |
| Ngày tháng | Giữa hoặc trái nhất quán | Giữa | Đừng tự đổi định dạng ngày |
| Hàng tiêu đề | Theo nội dung cột, thường giữa | Giữa | Không buộc căn giữa mọi tiêu đề dài |
| Tổng cộng | Theo loại dữ liệu, đậm | Giữa | Có đường kẻ phân biệt |
| Ô ký tên/xác nhận | Theo mẫu | Theo mẫu | Cấm áp quy tắc đại trà |

**[KN]** Không căn đều (Justify) mọi ô trong một bảng hẹp. Không buộc ô chứa số thụt đầu dòng. Với bảng có nội dung dạng khoản/điểm trong ô, kiểm tra ngữ cảnh trước khi áp dụng.

## 17. Quy tắc trình bày số liệu, đơn vị tính và dữ liệu thiếu

Theo Government Analysis Function, nên xếp số theo cột, căn phải, cùng mức chính xác; có đơn vị và nguồn rõ. [S11]. Trong tài liệu văn bản đã có nội dung, **các thay đổi giá trị phải do người dùng quyết định**, không được tự ý chuyển đổi:

- Không làm tròn số, chuyển dấu phân cách hàng nghìn/thập phân, đổi đơn vị đo hoặc định dạng phần trăm nếu chưa được phép.
- Không biến dấu `—`, `–`, `N/A`, ô trống thành số `0`; **khuyết dữ liệu khác với giá trị 0**.
- Số `01`, mã `0012`, ngày `01/02/2026`, số điện thoại và mã tài liệu có thể là dữ liệu chuỗi; không tự ép kiểu.
- Với bảng mới được soạn từ đầu, nên thống nhất số chữ số thập phân trong mỗi cột và đơn vị tại tiêu đề hoặc chú thích.
- Nếu có tổng và các phần có phép làm tròn, giải thích độ chênh thay vì âm thầm sửa số.

## 18. Tên bảng, đánh số, ghi chú và nguồn

**[KN]** Với bảng thống kê/báo cáo, cấu trúc thường hữu ích:

1. Đoạn giới thiệu hoặc dẫn chiếu tới bảng.
2. Tên bảng: ví dụ “Bảng 01. Tổng hợp kết quả thực hiện nhiệm vụ”.
3. Đơn vị tính hoặc thời kỳ (nếu cần).
4. Bảng dữ liệu.
5. Ghi chú, giải thích ký hiệu, nguồn thống kê.

**[KT]** Nên đặt tên bảng như một đoạn văn hoặc sử dụng tính năng *Insert Caption* của Word để thuận lợi cho danh mục bảng tự động, thay vì chèn hàng gộp vào nội bộ bảng chỉ để giả lập tiêu đề (trừ khi mẫu yêu cầu). [S09].

**[BK]** Không tự tạo tên bảng, nguồn hoặc thời kỳ chưa có. Khi cải tạo DOCX sẵn có, chỉ chuẩn hóa *cách trình bày* nội dung hiện hữu, không tự thêm kết luận hay nguồn giả định.

---

# PHẦN V. BẢNG DÀI NHIỀU TRANG, KHẢ NĂNG TIẾP CẬN VÀ ĐẦU RA IN ẤN

## 19. Lặp hàng tiêu đề trên trang tiếp theo

**[KT]/[KN]** Với bảng có hàng tiêu đề ở đầu và kéo dài qua trang, Word hỗ trợ **Repeat Header Rows** để lặp tiêu đề khi Word tự ngắt trang. Microsoft lưu ý tính năng này **không tự lặp tiêu đề khi người soạn chèn manual page break trong bảng**. Tiêu đề lặp thường chỉ thấy ở Print Layout hoặc khi in. [S07].

**Đề xuất:** nếu xác định đúng hàng tiêu đề và có kiểm tra an toàn, bật tính năng lặp cho các bảng dài. Không đánh dấu nhầm hàng tổng cộng hoặc hàng nhóm dữ liệu làm tiêu đề.

## 20. Ngăn tách hàng qua trang

**[KT]/[KN]** Dùng tính năng ngăn hàng tách qua hai trang (`cantSplit` trong WordprocessingML) **có điều kiện**:

- Hàng ngắn và có thể nằm trọn trong một trang: ưu tiên ngăn tách nếu bảng dễ đọc hơn.
- Hàng rất dài, chứa nhiều đoạn hoặc cao hơn vùng in: không ép ngăn ngắt máy móc; có nguy cơ nội dung không hiển thị theo ý định ở một số bộ kết xuất.
- Hàng có chiều cao cố định Exactly: đặc biệt kiểm tra việc cắt chữ.
- Đừng nhầm việc giữ *hàng* với việc giữ *bảng* trên một trang.

## 21. Giữ tiêu đề bảng gần bảng, phân trang hợp lý

**[KN]**

- Tránh để tên bảng ở cuối một trang còn toàn bộ bảng sang trang kế tiếp.
- Tránh tách ngay sau hàng tiêu đề mà trang đầu không có dữ liệu.
- Không thêm hàng trống chỉ nhằm đẩy nội dung xuống trang khác; dùng thuộc tính đoạn/ngắt trang phù hợp.
- Đặt bảng vào vùng có thể in, không dùng spacing âm, canh lề thiếu kiểm soát hoặc bảng floating khi không cần.
- Không cố ép một bảng quá dài lên một trang bằng cách giảm chữ và lề ngoài phạm vi cho phép.

## 22. Khi nào cân nhắc trang ngang

**[PL]/[KN]** Quy trình ra quyết định an toàn:

1. Xác định loại văn bản và có được phép trình bày ngang theo điều kiện tương ứng hay không.
2. Đo chiều rộng hiện tại, phát hiện ô chứa chuỗi không thể ngắt, ảnh hoặc cột dư.
3. Thử cải thiện hợp lý độ rộng, đệm ô, cách xuống dòng; vẫn giữ kích thước chữ hợp lệ.
4. Nếu cần, đề xuất dùng landscape tại **section phù hợp**, kèm dự kiến ảnh hưởng đến trang trước/sau.
5. Nếu không có điều kiện an toàn, đề xuất tách phụ lục hoặc tái cấu trúc bảng **chỉ khi người dùng chấp thuận và căn cứ cho phép**.

Không tự xoay ngang cả văn bản chỉ vì một bảng rộng. Thay đổi orientation có thể ảnh hưởng section break, header/footer và số trang.

## 23. Khả năng tiếp cận

**[KN]** Từ W3C, Section508.gov và Microsoft có các khuyến nghị:

- Bảng dữ liệu phải là bảng Word thực sự, không phải ảnh chụp bảng.
- Hàng tiêu đề phải được xác định có ý nghĩa, không chỉ tô đậm về hình thức.
- Giữ thứ tự đọc nhất quán (trái sang phải, từ trên xuống dưới nếu đây là chiều đọc của tài liệu).
- Hạn chế gộp/tách ô khi soạn **bảng mới** nếu không có lý do nghiệp vụ; biểu mẫu gộp ô hiện hữu phải được bảo toàn.
- Không dùng màu sắc làm dấu hiệu duy nhất; bảo đảm tương phản và đọc được khi in đen trắng.
- Dùng Word Accessibility Checker để phát hiện vấn đề, đồng thời kiểm tra bằng mắt và bản in.
- Với bảng quá phức tạp và nhu cầu accessibility nghiêm ngặt, cân nhắc tạo bản tài liệu/định dạng phù hợp phục vụ truy cập **không phá bản gốc**.

Đặc biệt, hướng dẫn Section 508 phân biệt **layout tables**, **simple data tables** và **complex data tables**; một bảng trông đẹp chưa chắc thân thiện với trình đọc màn hình. [S09], [S10], [S12].

## 24. Kiểm tra khi chuyển sang PDF hoặc in

**[KT]** Một file DOCX mở được **chưa đủ chứng minh** đã trình bày đúng. Cần kiểm tra ít nhất:

- Bảng không tràn lề, không cắt chữ, không mất hàng/cột khi kết xuất.
- Số trang không bị thay đổi ngoài phạm vi chấp nhận.
- Hàng tiêu đề và tổng cộng ở vị trí hợp lý.
- Phông Việt hiển thị đúng, không mất dấu.
- Viền và nền không biến mất hoặc thay sắc độ khó đọc khi in trắng đen.
- Biểu mẫu có vùng ký/đóng dấu không bị xô lệch.
- Với đầu ra PDF có yêu cầu accessibility, cân nhắc PDF gắn thẻ cấu trúc và kiểm tra bằng công cụ chuyên dụng, vì không phải phép xuất PDF nào cũng bảo toàn quan hệ bảng. [S09].

---

# PHẦN VI. LỖI THƯỜNG GẶP VÀ PHƯƠNG ÁN XỬ LÝ

## 25. Bảng phân loại lỗi

| Mã | Hiện tượng | Mức độ đề xuất | Cách xử lý |
|---|---|---|---|
| E01 | Sai loại căn cứ NĐ30/HD05/mẫu riêng | Chặn | Chọn đúng authority trước khi sửa |
| E02 | Bảng bị mất dữ liệu, thay đổi thứ tự | Chặn | Khôi phục, không xuất bản đã sửa |
| E03 | Gộp/tách ô bị thay đổi trái phép | Chặn | Bảo toàn cấu trúc gốc |
| E04 | Bảng trong phụ lục bị nhận là thân văn bản | Chặn | Phân vùng lại; one block–one owner |
| E05 | Số trang/phụ lục thay đổi sai | Chặn hoặc cao | Đối chiếu phụ lục và section |
| E06 | Bảng tràn vùng in/lề | Cao | Phát hiện độ rộng thực; đề xuất điều chỉnh |
| E07 | Cắt chữ/ảnh trong ô | Cao | Bỏ chiều cao Exactly không an toàn, nới bố cục |
| E08 | Phông chữ không phù hợp | Cần kiểm tra tuân thủ | Đối chiếu cấu trúc và mẫu |
| E09 | Cỡ chữ/giãn dòng không thống nhất | Cảnh báo | Chỉ sửa vùng và mẫu có căn cứ |
| E10 | Hàng tiêu đề không lặp qua trang | Khuyến nghị | Bật Repeat Header Rows nếu phù hợp |
| E11 | Hàng chia trang bất hợp lý | Cảnh báo | Kiểm tra `cantSplit`, chiều cao hàng |
| E12 | Tiêu đề bảng và bảng tách trang | Cảnh báo | Dùng Keep with next/cấu hình đoạn thích hợp |
| E13 | Viền quá dày, không nhất quán | Thẩm mỹ | Áp preset khi cho phép |
| E14 | Đệm ô quá nhỏ; chữ dính viền | Thẩm mỹ | Đặt đệm nhất quán và kiểm tra tràn |
| E15 | Tất cả cột rộng bằng nhau dù dữ liệu chênh lệch | Thẩm mỹ | Gợi ý chiều rộng theo nội dung |
| E16 | Số liệu căn trái, khó so sánh | Thẩm mỹ | Đề xuất căn phải, không sửa giá trị |
| E17 | Đổi `N/A`/ô trống thành 0 | Chặn | Khôi phục dữ liệu nguyên trạng |
| E18 | Nền/màu quá đậm hoặc thiếu tương phản | Thẩm mỹ/tiếp cận | Chuyển sang đơn sắc hoặc cảnh báo |
| E19 | Tự thêm tên bảng/nguồn không có trong gốc | Chặn | Không tạo nội dung nghiệp vụ |
| E20 | Chỉnh bảng layout như bảng số liệu | Chặn | Nhận diện vai trò bảng trước khi định dạng |

**Lưu ý:** Các cấp độ trong bảng là thiết kế kiểm soát chất lượng, không phải mức xử phạt hoặc phân loại vi phạm trong văn bản quy phạm.

## 26. Trường hợp đặc biệt cần “không sửa” hoặc yêu cầu xác nhận

- Bảng thuộc biểu mẫu pháp lý/chuyên ngành đã ban hành, dù kiểu viền không đẹp theo preset.
- Bảng có ô gộp nhiều tầng và nghĩa dữ liệu phụ thuộc chính ô gộp.
- Bảng chứa ảnh, chart, content control, bookmark, hyperlink, công thức, track changes, chữ ký, vùng điền dữ liệu.
- Bảng bị ngắt trang do section đặc biệt, có đầu/chân trang phụ thuộc section.
- Bảng có văn bản song ngữ hoặc nhiều hệ chữ.
- Bảng chứa thông tin cần giữ nguyên ký tự, vị trí, thứ tự cho đối chiếu hoặc nộp hồ sơ.
- Bảng của văn bản thuộc phạm vi bảo mật/ký số: chỉnh sửa phải đúng quyền và quy trình; không sửa tài liệu đã ký như thể đó là bản dự thảo.

---

# PHẦN VII. PRESET CHUẨN HÓA ĐỀ XUẤT

## 27. PRESET 01 – Formal Grid / Monochrome (mặc định khuyến nghị)

**Dành cho:** bảng công việc, danh sách, tổng hợp thông thường, báo cáo hành chính, văn bản của Đảng không có biểu mẫu riêng.

| Thuộc tính | Mặc định [KN] |
|---|---|
| Font | Times New Roman, tuân thủ bộ cỡ chữ theo loại văn bản/đơn vị |
| Text | Đen, kiểu đứng; heading đậm |
| Bảng | Căn trong vùng chữ, không tràn lề |
| Viền ngoài | Nét đơn 0,75 pt |
| Viền trong | Nét đơn 0,5 pt |
| Nền | Trắng |
| Đệm ngang | 1,5–2,0 mm |
| Đệm dọc | 0,8–1,2 mm |
| Cell spacing | 0 mm |
| Hàng | Auto/At least, không dùng Exactly đại trà |
| Tiêu đề cột | In đậm; căn giữa hoặc theo loại dữ liệu |
| Số | Căn phải |
| STT | Căn giữa |
| Diễn giải | Căn trái, căn trên nếu dài |
| Hàng tổng | In đậm, có đường phân tách hợp lý |
| Qua trang | Lặp hàng tiêu đề khi thích hợp; kiểm tra ngắt hàng |

**Quan trọng:** Chỉ áp dụng khi không xung đột mẫu hoặc quy định cụ thể; toàn bộ giá trị viền/đệm là **khuyến nghị thẩm mỹ**.

## 28. PRESET 02 – Statistical Minimal

**Dành cho:** bảng số liệu trong báo cáo tổng hợp, nghiên cứu, bản phân tích khi không có mẫu bắt buộc.

- Bảng nền trắng, ít đường kẻ; nhấn đường kẻ dưới tiêu đề và quanh tổng cộng.
- Các cột số căn phải; tiêu đề của cột số tương ứng.
- Đơn vị, thời gian và nguồn hiện diện khi đã được người biên soạn cung cấp.
- Giữ mức làm tròn và cách viết số trong dữ liệu gốc; không tự thao tác số.
- Chỉ thêm kiểu nền hàng xen kẽ khi có nhu cầu và đủ tương phản; mặc định không cần.

## 29. PRESET 03 – Preserve Official Form

**Dành cho:** bảng đã là mẫu chính thức, biểu mẫu kiểm tra–giám sát, mẫu thống kê cơ quan, bảng có trường điền và vùng ký.

- **Giữ nguyên:** hàng/cột, ô gộp, đường viền đặc thù, chiều cao cố định có chủ đích, vị trí ký, nội dung, chú thích, công thức và quan hệ liên kết.
- Kiểm tra và cảnh báo vấn đề hiển thị; **không áp các tối ưu làm thay đổi biểu mẫu**.
- Thay đổi nhỏ chỉ khi chỉ ra căn cứ và có xác nhận của người dùng.

## 30. Cơ chế quyết định preset

1. Có mẫu chính thức hoặc dấu hiệu biểu mẫu cần giữ nguyên? → `Preserve Official Form`.
2. Bảng dùng để dàn trang hoặc bố trí thành phần thể thức? → không áp preset dữ liệu.
3. Bảng thống kê thuần túy và người dùng muốn tối giản? → `Statistical Minimal`.
4. Bảng dữ liệu thông thường? → `Formal Grid`.
5. Vai trò chưa rõ? → **chỉ kiểm tra/cảnh báo**, không tự áp dụng.

---

# PHẦN VIII. ĐẶC TẢ QUY TẮC CHO BỘ KIỂM TRA DOCX

## 31. Nguyên tắc kỹ thuật

**[KT] REUSE FIRST:** Microsoft Word và WordprocessingML đã có các primitive quản lý bảng. Không cần tự tạo mô hình tài liệu mới khi chỉ cần chỉnh thuộc tính sẵn có. Microsoft Learn mô tả `w:tbl` (bảng), `w:tblPr` (thuộc tính bảng), `w:tblGrid` (lưới), `w:tr` (hàng), `w:tc` (ô). [S14].

Mục tiêu là một bộ engine xử lý bảng và **hai cấu hình authority riêng** (`ND30_TABLE`, `PARTY_HD05_TABLE`); các preset thẩm mỹ đặt ở lớp tùy chọn. Không nhân đôi engine chỉ vì có hai hệ quy định.

## 32. Danh mục quy tắc đề xuất

| Rule ID | Nhóm | Nội dung kiểm tra | Hành động đề xuất | Quyền sửa |
|---|---|---|---|---|
| LEG-01 | Pháp lý | Chọn đúng loại văn bản/bộ quy tắc | Chặn nếu không xác định | Không tự suy đoán |
| LEG-02 | Pháp lý | Khổ giấy/vùng trình bày theo authority | Báo sai khác | Cần xác nhận nếu đổi section |
| LEG-03 | Pháp lý | Phông chữ/màu theo thành phần thể thức | Đối chiếu | Chỉ vùng cho phép |
| LEG-04 | Pháp lý | Điều kiện chuyển ngang khi có bảng | Gợi ý có căn cứ | Không tự áp dụng |
| LEG-05 | Pháp lý | Phụ lục dùng đúng hệ số và tiêu đề | Kiểm tra | Không tự đổi số |
| SEG-01 | Cấu trúc | Bảng thuộc body hay appendix hay layout | Phân loại | Không sửa nếu chưa chắc chắn |
| INT-01 | Bảo toàn | Nội dung từng ô và thứ tự đọc | Snapshot/diff | Bắt buộc giữ |
| INT-02 | Bảo toàn | Ô gộp và bảng lồng | Structural diff | Bắt buộc giữ |
| INT-03 | Bảo toàn | Ảnh, link, content controls, field | Structural diff | Bắt buộc giữ |
| LAY-01 | Bố cục | Tràn vùng chữ | Đề xuất độ rộng | Có xác nhận |
| LAY-02 | Bố cục | Chiều cao Exact gây cắt chữ | Cảnh báo | Có xác nhận |
| PAG-01 | Phân trang | Tiêu đề bảng tách khỏi bảng | Gợi ý Keep with next | Có xác nhận |
| PAG-02 | Phân trang | Lặp tiêu đề qua trang | Gợi ý tblHeader | Có xác nhận |
| PAG-03 | Phân trang | Chia hàng không hợp lý | Gợi ý cantSplit có điều kiện | Có xác nhận |
| VIS-01 | Thẩm mỹ | Nét viền không đều | Áp preset | Có xác nhận |
| VIS-02 | Thẩm mỹ | Đệm ô quá nhỏ | Áp preset | Có xác nhận |
| VIS-03 | Thẩm mỹ | Cột thiếu cân đối | Gợi ý tự tối ưu | Có xác nhận |
| VIS-04 | Thẩm mỹ | Căn số không phù hợp | Gợi ý căn theo dữ liệu | Có xác nhận |
| ACC-01 | Tiếp cận | Không có tiêu đề có ý nghĩa | Cảnh báo | Không tự viết nội dung |
| ACC-02 | Tiếp cận | Độ tương phản/màu | Cảnh báo | Có xác nhận |
| OUT-01 | Chất lượng | Đầu ra mở lại và render đúng | Verification | Chặn xuất khi hỏng |

**Cách lưu rule:** `{id, authority, category, severity, scope, applicability, expected, evidence, confidence, fixPolicy, verification}`. Cần ghi rõ nguồn nào là [PL], nguồn nào là [KN].

## 33. Quy trình xử lý tài liệu khuyến nghị

```text
DOCX đầu vào
    ↓
Nhận diện loại văn bản + căn cứ áp dụng
    ↓
Trích xuất source blocks từ DOCX (không làm mất bảng/bảng lồng)
    ↓
Phân vùng: header/metadata/body/signature/recipients/appendices/unclassified
    ↓
Nhận diện bảng + phân loại vai trò + bảo toàn provenance
    ↓
Kiểm tra quy định pháp lý và kiểm tra chất lượng hiển thị
    ↓
Đề xuất preset/phép sửa có phạm vi, hiển thị diff
    ↓
Người dùng chọn quy tắc và phê duyệt
    ↓
Chỉ chỉnh các thuộc tính được cho phép trong DOCX
    ↓
Mở lại DOCX, so sánh cấu trúc + nội dung + render/print layout
    ↓
Báo cáo và xuất tệp đã chỉnh
```

**Không thực hiện:** thay toàn bộ bảng bằng HTML rồi dựng lại DOCX từ đầu, làm phẳng bảng lồng, sửa đồng loạt bảng dàn trang, hoặc thay đổi các vùng đã được chứng minh ổn định nhưng không thuộc phạm vi công việc.

## 34. Danh mục thuộc tính WordprocessingML nên xét khi triển khai

| Thuộc tính/nhóm | Công dụng | Yêu cầu an toàn |
|---|---|---|
| `w:tblPr`, `w:tblW` | Kiểu và rộng toàn bảng | Giữ thuộc tính không được sửa |
| `w:tblGrid`, `w:gridCol` | Lưới và chiều rộng cột | Không làm sai lưới ô gộp |
| `w:tblBorders`, `w:tcBorders` | Viền bảng và ô | Tránh ghi đè viền đặc thù |
| `w:tblCellMar`, `w:tcMar` | Khoảng đệm trong ô | Kiểm tra chiều cao mới |
| `w:tblLayout` | Chế độ layout cố định/tự động | Không đổi đại trà |
| `w:trPr`, `w:trHeight` | Thuộc tính/chiều cao hàng | Không gây cắt chữ |
| `w:tblHeader` | Hàng tiêu đề lặp | Chỉ gắn cho hàng đầu phù hợp |
| `w:cantSplit` | Ngăn ngắt hàng qua trang | Không áp cho hàng quá cao |
| `w:gridSpan`, `w:vMerge` | Gộp ngang/dọc | **Bất biến nếu chỉ định dạng** |
| `w:shd` | Nền ô | Không đưa màu thừa |
| `w:jc`, `w:vAlign`, thuộc tính đoạn | Căn ngang/dọc | Theo vai trò và kiểu dữ liệu |

Bảng thuộc tính trên là **hướng nghiên cứu tích hợp**, không phải tuyên bố hệ thống nào đã được triển khai hoặc kiểm thử. Khi hiện thực cần kiểm tra schema thực tế, cascade style và khả năng tương thích Word. [S14].

## 35. Đề xuất giao diện kiểm tra/áp dụng

Với mỗi bảng nên hiển thị:

- **Vị trí:** thân văn bản / phụ lục số mấy / bảng dàn trang / chưa xác định.
- **Trạng thái:** đúng quy định, cần kiểm tra, cảnh báo thẩm mỹ, lỗi toàn vẹn.
- **Căn cứ:** tên nguồn + phần/mục liên quan hoặc nhãn “khuyến nghị thẩm mỹ”.
- **Đề xuất:** thuộc tính hiện tại → thuộc tính mục tiêu và tác động dự kiến.
- **Xem trước:** bảng trước/sau trên trang thực tế.
- **Quyền áp dụng:** chỉ được sửa thuộc tính nằm trong phạm vi đã được cho phép.
- **Kết quả:** diff, lỗi được khắc phục, cảnh báo còn lại, bằng chứng mở lại DOCX.

Tuyệt đối không ghi “sai Nghị định 30” chỉ vì viền của bảng là 1 pt thay vì preset 0,5 pt.

---

# PHẦN IX. ĐÁNH GIÁ CHẤT LƯỢNG VÀ NGHIỆM THU

## 36. Mô hình chấm điểm thẩm mỹ tham khảo

Chỉ chấm điểm **sau khi đạt điều kiện bất biến**: không mất nội dung, không phá cấu trúc, không vi phạm quy định bắt buộc.

| Tiêu chí | Trọng số đề xuất |
|---|---:|
| Bố cục và phân trang | 25 |
| Khả năng đọc | 25 |
| Đường viền và cân đối | 20 |
| Nhất quán kiểu chữ và khoảng trắng | 15 |
| Tiêu đề, số liệu, ghi chú, nguồn | 15 |
| **Tổng** | **100** |

| Điểm | Mức chất lượng gợi ý |
|---|---|
| 90–100 | Rất tốt |
| 80–89 | Tốt |
| 65–79 | Cần tối ưu thêm |
| Dưới 65 | Cần rà soát đáng kể |

**Lưu ý:** thang điểm **không** phải tiêu chuẩn pháp lý, không thay thế kiểm tra tài liệu thực tế. Một bảng đạt điểm cao nhưng bị mất số liệu **không được nghiệm thu**.

## 37. Checklist nghiệm thu thực hành

### A. Căn cứ và phạm vi

- [ ] Đã xác định loại văn bản, authority, thời điểm áp dụng.
- [ ] Đã xác định bảng thuộc thân văn bản hay phụ lục.
- [ ] Đã kiểm tra biểu mẫu chuyên ngành nếu có.
- [ ] Đã phân biệt tiêu chí pháp lý với preset thẩm mỹ.

### B. Nội dung và cấu trúc

- [ ] Số lượng và thứ tự bảng đúng.
- [ ] Mỗi bảng thuộc đúng một vùng sở hữu.
- [ ] Không thiếu/thừa nội dung hoặc đổi thứ tự ô.
- [ ] Cấu trúc hàng/cột và merged cells không thay đổi ngoài phạm vi.
- [ ] Ảnh, trường dữ liệu, liên kết, bảng lồng được giữ nguyên.
- [ ] Số liệu, dấu phân cách, ngày, mã và dữ liệu thiếu được giữ nguyên.

### C. Tuân thủ trình bày

- [ ] Khổ giấy, lề, hướng trang hợp lệ.
- [ ] Phông chữ và cỡ chữ theo loại tài liệu/thành phần.
- [ ] Số và tiêu đề phụ lục đúng hệ quy định.
- [ ] Không tự động áp quy tắc của đoạn văn cho tất cả ô bảng.

### D. Thẩm mỹ và đọc hiểu

- [ ] Bảng không tràn vùng in.
- [ ] Chữ không sát viền và không bị cắt.
- [ ] Độ rộng cột phù hợp ý nghĩa và độ dài dữ liệu.
- [ ] Tiêu đề rõ, dữ liệu dễ đối chiếu, số căn hợp lý.
- [ ] Viền và nền tiết chế, nhất quán.
- [ ] Bảng in trắng đen vẫn rõ, không dựa riêng màu sắc.

### E. Phân trang và đầu ra

- [ ] Tiêu đề bảng không lạc sang trang khác.
- [ ] Bảng qua trang có tiêu đề cột lặp khi phù hợp.
- [ ] Hàng không bị chia hoặc ép chiều cao một cách sai lệch.
- [ ] Mở lại DOCX không xuất hiện lỗi hay thay đổi ngoài phạm vi.
- [ ] Bản xem trước/in hoặc PDF phù hợp (nếu thuộc phạm vi nghiệm thu).

## 38. Ma trận kiểm thử theo phạm vi ảnh hưởng (blast radius)

| Nhóm thay đổi | Kiểm tra bắt buộc trực tiếp | Kiểm tra hồi quy có điều kiện |
|---|---|---|
| Viền/nền | Diff định dạng đúng bảng, không đổi content | Render nếu có border conflict |
| Đệm ô | Không cắt nội dung; độ cao hợp lệ | Bảng dài/trang kế tiếp |
| Cột/rộng bảng | Không tràn vùng in, không phá ô gộp | Section/bảng lồng |
| Font/paragraph trong ô | Không mất run, field, dấu tiếng Việt | Đoạn lồng/danh sách |
| Lặp hàng tiêu đề | Lặp đúng hàng đầu trên page break tự động | Print Layout/PDF |
| Ngăn tách hàng | Không cắt hàng dài | Trang có nhiều bảng |
| Xoay ngang section | Trình bày và số trang của section liên quan | Header/footer, trang liền kề |
| Bảng thuộc phụ lục | Không đổi số và owner | Footer/số trang phụ lục |

**Nguyên tắc:** tái sử dụng các bài kiểm tra và bằng chứng đã PASS của phần không bị tác động; không chạy toàn bộ hệ thống hoặc viết lại test cũ một cách máy móc.

## 39. Điều kiện nghiệm thu “PASS”

Một thay đổi chỉ được coi là đạt khi: **(a)** xác định đúng căn cứ và phạm vi; **(b)** thuộc tính mục tiêu được sửa đúng theo xác nhận; **(c)** nội dung và cấu trúc bất biến PASS; **(d)** DOCX mở lại thành công; **(e)** bố cục liên quan không phát sinh lỗi nghiêm trọng; **(f)** có báo cáo before/after với lỗi/cảnh báo còn lại. Đối với các chỉnh sửa nhạy cảm về phân trang phải có bằng chứng kết xuất, không chỉ kiểm tra XML.

---

# PHẦN X. LỘ TRÌNH ÁP DỤNG VÀ KIẾN NGHỊ

## 40. Các ưu tiên triển khai

**P0 – Tuân thủ và bảo toàn**

- Xác định authority và mẫu áp dụng.
- Phân loại bảng dữ liệu, bảng dàn trang, biểu mẫu, bảng phụ lục.
- Trích xuất/giữ nguyên cấu trúc bảng và nội dung.
- Kiểm tra tràn lề, mất nội dung, lỗi phân trang nghiêm trọng.
- Xây dựng kết quả cảnh báo có căn cứ và kiểm chứng mở lại.

**P1 – Trình bày ổn định, đẹp hơn**

- Chuẩn hóa viền, đệm ô, căn ngang/dọc theo preset được duyệt.
- Cân đối cột, hàng theo nội dung và vùng chữ thực tế.
- Lặp tiêu đề bảng dài, khắc phục tiêu đề lạc trang và ngắt hàng bất hợp lý.
- Có xem trước và tùy chọn áp dụng theo bảng.

**P2 – Nâng cao**

- Đánh giá thẩm mỹ theo tiêu chí.
- Cảnh báo khả năng tiếp cận và nguồn/đơn vị tính chưa rõ.
- Kiểm tra trực quan trước/sau và xuất báo cáo diff tự động.

## 41. Kiến nghị tổng hợp

1. **Một bộ máy xử lý DOCX, nhiều cấu hình quy tắc:** `ND30_TABLE`, `PARTY_HD05_TABLE` và khi thực sự cần mới bổ sung cấu hình văn bản quy phạm/pháp luật chuyên ngành.
2. **Một trách nhiệm – một nguồn chân lý:** quy định pháp lý đến từ nguồn quy định đang có hiệu lực; cấu trúc bảng đến từ DOCX gốc; các preset thẩm mỹ là cấu hình người dùng.
3. **Mặc định đơn sắc và trang trọng:** nền trắng, đen, Times New Roman, viền mảnh nhất quán, dữ liệu được căn hợp lý.
4. **Không “cải tạo cho đẹp” biểu mẫu chính thức:** preservation thắng aesthetic.
5. **Tối ưu bố cục an toàn trước khi xoay ngang hoặc chia bảng:** đảm bảo phù hợp quy định riêng của hệ văn bản.
6. **Lưu provenance và verification:** ai yêu cầu sửa, bảng nào, thuộc tính gì, căn cứ gì, kết quả kiểm tra nào PASS/FAIL.
7. **Chỉ thêm dependency hoặc code mới khi chứng minh rõ thành phần hiện có không đáp ứng:** tái sử dụng khả năng chính thức của Word/OOXML và code dự án đã có trước.

---


# PHẦN XI. NÂNG CẤP V2 — KIẾN TRÚC QUY TẮC, MỤC TIÊU VÀ RANH GIỚI TỐI ƯU

## 42. Những hạn chế được khắc phục so với bản 1.0

Bản V1 đã nhận diện căn cứ pháp lý, ba preset và các tiêu chí thẩm mỹ. Để **định dạng bảng trên tệp DOCX thực tế** đạt chất lượng cao hơn, cần bổ sung tám lớp kiểm soát chưa được lượng hóa đầy đủ:

1. **Định dạng hiệu dụng (effective formatting)**: hiểu sự chồng lớp giữa kiểu bảng, kiểu đoạn, kiểu ký tự, ngoại lệ hàng và định dạng trực tiếp; không chỉ đọc thuộc tính trực tiếp của một ô.
2. **Hình học chính xác**: tính vùng chữ theo section, trang chẵn/lẻ, bảng lồng, chiều rộng lưới, đệm ô và ràng buộc nội dung.
3. **Mô hình lưới bất quy tắc**: nhận diện ô chiếm nhiều cột/hàng, ô bị bỏ trống theo vị trí lưới, tiêu đề nhiều tầng, bảng nằm trong ô; không ép thành ma trận chữ nhật giả.
4. **Bố cục nhiều trang**: quyết định lặp tiêu đề, giữ hàng, liên kết chú thích, kiểm soát ngắt trang và tác động đến section.
5. **Giới hạn chỉnh sửa**: phân cấp tự sửa / chỉ gợi ý / buộc xác nhận / không sửa, đặc biệt đối với biểu mẫu và tài liệu đã ký.
6. **Kiểm chứng hai tầng**: đối chiếu cấu trúc DOCX và đối chiếu hình ảnh/bố cục thực tế; không nhầm tệp mở được với chất lượng trình bày đã đạt.
7. **Lựa chọn preset dựa vào loại bảng**: bảng phân công không giống bảng số liệu, bảng đối chiếu nhiều tầng hoặc bảng dàn trang.
8. **Kiểm soát hồi quy có phạm vi**: xác định từng bảng được sửa và thành phần gián tiếp ảnh hưởng, không chạy lại tùy tiện mọi thứ.

### 42.1. Định nghĩa "tối ưu" theo thứ tự ưu tiên

Thứ tự ưu tiên **không phải tối ưu đa mục tiêu bằng cách đánh đổi ngang hàng**:

`(A) legal/form authority > (B) content & package integrity > (C) readability & printable geometry > (D) visual consistency > (E) compactness`.

Nếu lựa chọn đẹp hơn đòi hỏi vi phạm A hoặc B, hệ thống **phải từ chối lựa chọn đó**. Chỉ so sánh ứng viên thuộc tập hợp đã đáp ứng A và B. Tính thẩm mỹ vì vậy là bài toán tối ưu có ràng buộc, không phải thay toàn bộ bảng để đạt một mẫu hình lý tưởng.

### 42.2. Trạng thái xử lý chuẩn

| Trạng thái | Định nghĩa | Kết quả phù hợp |
|---|---|---|
| `COMPLIANT` | Có đủ căn cứ, không phát hiện lỗi pháp lý/biểu mẫu thuộc phạm vi kiểm tra | Giữ nguyên hoặc tối ưu tùy chọn |
| `OPTIMIZABLE` | Bảng an toàn để nâng cấp một số thuộc tính trình bày | Cho chọn preset và xem trước |
| `REVIEW_REQUIRED` | Phân loại chưa chắc chắn, có mâu thuẫn giữa ưu tiên, thiếu trình kết xuất | Gợi ý; không tự sửa |
| `LOCKED` | Mẫu biểu bảo vệ, tài liệu đã ký, vùng đặc thù hoặc yêu cầu không can thiệp | Giữ nguyên |
| `UNSUPPORTED` | Cấu trúc OOXML/đối tượng nhúng chưa xử lý tin cậy | Báo rõ giới hạn |
| `VERIFICATION_FAILED` | Sau sửa có sai khác nội dung, cấu trúc hoặc kết xuất nghiêm trọng | Rollback, không giao đầu ra như đã đạt |

**Không đồng nhất:** `UNKNOWN` không phải `COMPLIANT`; bản render chưa được xem không được ghi nhận `VISUAL_PASS`.

## 43. Nguồn quy tắc và phương pháp phân xử xung đột

Mỗi thuộc tính phải có **một authority ở mỗi tầng**, kết hợp theo thứ tự:

1. Văn bản pháp lý điều chỉnh *loại văn bản thực tế* (`ND30`, `PARTY_HD05`, hoặc hệ khác): giá trị bắt buộc, ngoại lệ và phạm vi áp dụng.
2. Mẫu/biểu mẫu có thẩm quyền được chỉ định: quy tắc cụ thể của bảng/ô nếu có, không tự thay thế bởi preset.
3. Ràng buộc bảo toàn tài liệu do người dùng xác nhận: vùng bị khóa, đối tượng chữ ký, cấu trúc ngữ nghĩa.
4. Yêu cầu tùy chọn của người dùng: ví dụ bảng thống kê dùng Statistical Minimal.
5. Preset tối ưu chung: chỉ được dùng cho thuộc tính còn tự do sau bốn tầng trên.

**Ví dụ phân xử:** bảng biểu có màu nền và kích thước hàng định sẵn ở một phụ lục bắt buộc. Không được áp `Formal Grid` ghi đè nền/chiều cao của mẫu, dù preset mặc định của ứng dụng là đơn sắc. Với hai bảng cùng nội dung nhưng thuộc hai tài liệu khác hệ, cỡ chữ và giãn dòng phải lấy từ đúng nguồn quy tắc, không lấy từ tên preset.

**Căn cứ hiệu lực chính:** NĐ30/2020 Phụ lục I [S01–S03]; HD05-HD/VPTW Phần II, các Mục I, II, IV [S05–S06]. Những nhận định về UI, thuật toán và preset trong phần XI–XVIII đều là **đề xuất [KN]/[KT]**, không diễn giải như quy định pháp lý.

# PHẦN XII. HÌNH HỌC TRANG, ĐỘ RỘNG VÀ PHƯƠNG PHÁP TỐI ƯU CỘT

## 44. Cách tính kích thước dùng được

### 44.1. Không lấy một con số A4 cố định cho mọi trang

Phải lấy thông tin từ **section chứa bảng**, không suy ra từ thiết lập của section đầu hoặc từ đoạn văn đầu tiên. Cần xét khổ giấy, xoay dọc/ngang, lề, kiểu in hai mặt, gutter, thụt đoạn/bảng, bảng nằm trong ô khác, bố trí floating và vùng chữ thực tế.

Các công thức nền:

```
W_page = chiều rộng trang (mm) tại section chứa bảng
W_text = W_page - left_margin - right_margin - gutter_effective
W_usable = W_text - table_indent - nested_container_constraints
W_inner(c) = W_col(c) - cell_padding_left - cell_padding_right - border_effect
```

`border_effect` chỉ là phần chiếm dụng hình học thực tế của đường viền/spacing, không được tự trừ cố định như một số mm bất biến. Với bảng lồng, `W_usable` bị giới hạn bởi **ô cha**, không phải chiều rộng giấy A4. Với bảng dàn trang nổi, cần phân tích vùng đặt đối tượng thay vì áp công thức đoạn thông thường.

Ví dụ **chỉ theo vùng chữ**, A4 dọc 210 mm: ND30 có khoảng 155–165 mm tùy lề thực tế; HD05 mặt trước là 165 mm theo lề 30+15 mm. **Không coi 165 mm là chiều rộng cột tổng hợp bắt buộc** khi bảng thụt lề hoặc nằm trong ngữ cảnh khác.

### 44.2. Chuẩn đơn vị khi đọc/ghi OOXML

- `1 inch = 25,4 mm`.
- `1 pt = 1/72 inch`.
- `1 dxa/twip = 1/20 pt ≈ 0,0176389 mm`.
- `1 mm ≈ 56,6929 twip`.
- Với `w:tblW`, độ rộng loại `pct` biểu diễn theo đơn vị phần năm mươi của 1% (ví dụ 5000 ứng với 100%) **khi thuộc tính thực sự dùng loại `pct`**.
- `w:tblW` và `w:tcW` là **preferred width**, Word có thể vượt giá trị ưu tiên khi lưới hoặc chuỗi không ngắt dòng gây xung đột.

**Cấm** nhầm `pct` với `dxa`, hoặc so sánh trực tiếp độ rộng XML `w:w` khác đơn vị. Cần đổi về đơn vị thống nhất trước khi đối chiếu. Tài liệu Microsoft về `tblW` ghi rõ độ rộng ưu tiên và giới hạn từ layout/grid [S20].

## 45. Chiến lược tối ưu cột theo ràng buộc

### 45.1. Phân loại cột

> **Bổ sung V3:** Bảng sau chỉ nói về *khả năng cần thêm diện tích trình bày*, không phải mức độ quan trọng nghiệp vụ. Cột hạn hoặc định danh có thể có tầm quan trọng cao nhưng độ rộng hợp lý thấp. Xem mục 71–73 để tránh phân bổ mm tỷ lệ thuận theo ưu tiên ngữ nghĩa.


| Loại cột | Mức ưu tiên độ rộng | Đặc điểm / quyết định |
|---|---|---|
| STT | Thấp | Hẹp, nhưng đủ cho số lớn nhất và đệm ô |
| Mã, số văn bản, biển số, ID | Từ thấp đến trung bình | Không biến mã thành số; hạn chế bẻ mã |
| Tên cơ quan/cá nhân | Trung bình–cao | Ưu tiên không cắt tên, cho phép ngắt tại khoảng trắng |
| Nội dung diễn giải | Cao | Dành tỷ lệ lớn; hỗ trợ xuống dòng theo ngữ nghĩa |
| Ngày, hạn, thời gian | Thấp–trung bình | Tránh xuống dòng bất thường ở chuỗi ngày |
| Số liệu | Theo giá trị dài nhất | Căn phải; không làm tròn giá trị để vừa cột |
| Ký tên, dấu xác nhận | Theo mẫu | Không áp thuật toán phân chia tự động |
| Cột có ảnh/biểu tượng/đối tượng | Theo kích thước và neo của đối tượng | Không ép ảnh gây mất tỷ lệ hay mất nội dung |

### 45.2. Trình tự 6 bước giải bài toán độ rộng

1. Đo vùng chữ thực tế `W_usable` theo section/bảng lồng.
2. Phân tích từng cột: văn bản, từ dài nhất không thể ngắt, cỡ chữ hiệu dụng, đệm ô, hình ảnh và liên kết; xác định `min_width`, `ideal_width`, `max_width` nếu có.
3. Ràng buộc từ ô gộp: tổng các cột mà ô trải qua phải đủ để trình bày phần nội dung đó. Không được coi ô gộp thành những ô độc lập rồi tính hai lần.
4. Phân bổ độ rộng theo mức cần thiết và ưu tiên đọc hiểu; **không dùng mỗi số lượng ký tự** để suy ra mm vì phông, ký tự Việt, đậm/nghiêng, chữ số, ảnh và ngắt dòng ảnh hưởng đến bề rộng thật.
5. Thử các ứng viên (giữ nguyên; chỉnh đệm; cân đối lại cột; dùng layout cố định có kiểm chứng; cân nhắc trang ngang nếu hợp lệ), kiểm tra tràn trang, số dòng và phân trang.
6. Chọn ứng viên tối ưu chỉ trong số đã đạt tính toàn vẹn và phạm vi được phép; nếu không ứng viên nào đạt, báo `REVIEW_REQUIRED` thay vì ép cỡ chữ xuống quá thấp.

**Mục tiêu gợi ý** (không phải công thức luật): giảm số trường hợp tràn lề và cắt chữ trước; sau đó giảm dòng xuống bất hợp lý và thay đổi độ cao hàng quá lớn; cuối cùng tăng độ nhất quán, giảm khoảng trắng lãng phí. Nên dùng kết quả layout/render để đánh giá, không cố dự đoán chính xác chỉ từ nội dung XML.

### 45.3. Khi nào ưu tiên AutoFit và Fixed Layout?

| Trường hợp | Gợi ý | Điều kiện |
|---|---|---|
| Bảng mới, dữ liệu tương đối đơn giản | `AutoFit to Window` hoặc quản lý tỷ lệ tương đối | Kiểm tra sau khi nhập đầy đủ dữ liệu |
| Bảng có bố cục phải ổn định khi in | Fixed layout/column width **sau khi đo** | Nội dung đủ chỗ, không có chuỗi dài phá layout |
| Bảng biểu mẫu đã được ban hành | Preserve nguyên cấu hình | Chỉ sửa lỗi thực sự có căn cứ và được phép |
| Bảng với rất nhiều mô tả dài | Ưu tiên cột mô tả rộng, hàng Auto | Không hạ cỡ chữ đồng loạt |
| Bảng nhiều cột ít giá trị nhưng có tiêu đề dài | Xem lại cách xuống dòng tiêu đề, đề xuất landscape nếu đủ điều kiện | Không rút gọn nội dung tiêu đề tự động |
| Bảng có ô gộp phức tạp | Giữ cấu trúc, hạn chế sửa chiều rộng lưới | Kiểm chứng thực tế từng bảng |

Microsoft Word hỗ trợ `AutoFit Contents`, `AutoFit Window` và `Fixed Column Width`, cùng điều chỉnh cell margins/cell spacing [S08]. Việc đổi chế độ không đồng nghĩa chắc chắn bảng sẽ giữ độ rộng tuyệt đối khi nội dung xung đột [S20].

## 46. Quy tắc sửa bảng quá rộng theo thang can thiệp

| Bậc | Biện pháp | Chính sách |
|---|---|---|
| 0 | Giữ nếu vẫn nằm trong vùng chữ, không cắt chữ | Auto-pass |
| 1 | Giảm khoảng trống *quá dư*, chỉnh đệm ô trong ngưỡng preset | Gợi ý; sửa khi được phép |
| 2 | Phân bổ lại chiều rộng cột theo nội dung và ô gộp | Cần preview/approval |
| 3 | Điều chỉnh xuống dòng mềm bằng cơ chế layout, không thay đổi ký tự | Cần render xác nhận |
| 4 | Đổi sang trang ngang/section riêng nếu đúng thẩm quyền và khả thi | Cần phê duyệt riêng; kiểm tra section, header/footer, đánh trang |
| 5 | Đề xuất đưa bảng sang phụ lục hoặc chia bảng thành những bảng nhỏ | **Thay đổi cấu trúc văn bản**, không tự thực hiện |
| Cấm | Giảm phông xuống 8–10 pt, xóa cột, viết tắt nội dung, xoá dấu, đổi đơn vị, biến bảng thành ảnh | Không tự động |

Không tự chuyển bảng đang ở thân văn bản sang phụ lục: quyết định này liên quan cấu trúc, căn cứ và cách viện dẫn văn bản.

# PHẦN XIII. CHUẨN THẨM MỸ THEO VAI TRÒ BẢNG

## 47. Tám loại bảng và preset khuyến nghị

| Loại bảng | Nhận diện đặc trưng | Cách trình bày ưu tiên | Không được làm |
|---|---|---|---|
| `TASK_MATRIX` — phân công | STT; nhiệm vụ; đơn vị; thời hạn | Formal Grid; cột nhiệm vụ rộng; viền rõ | Tự đổi hạn/người phụ trách |
| `DATA_STAT` — thống kê | Chỉ tiêu, kỳ, giá trị, tổng | Statistical Minimal; căn số phải; nhấn tổng | Làm tròn số/sửa nguồn |
| `LEGAL_COMPARISON` — đối chiếu quy định | Nhiều mô tả, dẫn chiếu dài | Formal Grid nhẹ; căn trái; nhiều khoảng thở | Rút gọn dẫn chiếu |
| `SCHEDULE` — lịch | Ngày, giờ, địa điểm, nội dung | Formal Grid; ngày/giờ dễ quét; giữ ô nhóm | Hoán vị lịch hoặc đổi định dạng ngày sai nghĩa |
| `PERSONNEL_LIST` — danh sách | Tên, đơn vị, chức vụ | Formal Grid; ngắt tên nhất quán; lặp tiêu đề | Sắp xếp lại khi không được yêu cầu |
| `APPENDIX_REGISTER` — danh mục phụ lục | Mã, nội dung, ghi chú, nhiều trang | Formal Grid/Preserve; ổn định phân trang | Mất số thứ tự, vị trí phụ lục |
| `OFFICIAL_FORM` — biểu mẫu | Ô gộp, ô xác nhận, khung ký | Preserve Official Form | Tự chia/gộp ô, đổi border/nền quy định |
| `LAYOUT_TABLE` — bảng dàn trang | Không phải dữ liệu lưới; dùng để bố trí header/chữ ký | Giữ nguyên; xử lý theo chức năng thể thức | Áp preset bảng dữ liệu |

**Bảng với bố cục kỳ lạ/không rõ vai trò:** mặc định `REVIEW_REQUIRED` hoặc `Preserve`, không suy luận ép thành bảng thống kê.

## 48. Bộ design token khuyến nghị V2

Các trị số trong bảng là **giá trị bắt đầu để thử nghiệm**, cần tùy chỉnh theo cỡ chữ và mẫu; **không phải điều khoản bắt buộc**:

| Token | Formal Grid | Statistical Minimal | Official Form |
|---|---|---|---|
| `font.family` | Theo ND30/HD05/mẫu | Theo ND30/HD05/mẫu | Giữ theo mẫu |
| `font.size` | Theo loại văn bản và kiểu ô được phép | Kế thừa văn bản; không ép co chữ | Giữ theo mẫu |
| `text.color` | `#000000` | `#000000` | Theo mẫu |
| `background.body` | `#FFFFFF` | `#FFFFFF` | Theo mẫu |
| `background.header` | Trắng | Trắng (mặc định); xám nhạt tùy chọn | Theo mẫu |
| `border.outer` | 0,75 pt, solid | 0–0,5 pt tùy bảng | Giữ nguyên |
| `border.inner.h` | 0,5 pt, solid | 0,35–0,5 pt (nét chính) | Giữ nguyên |
| `border.inner.v` | 0,5 pt, solid | Có thể 0 pt khi không làm mơ hồ bảng | Giữ nguyên |
| `padding.x` | 1,5–2 mm | 2–2,5 mm | Giữ nguyên |
| `padding.y` | 0,8–1,2 mm | 1–1,5 mm | Giữ nguyên |
| `row.height` | Auto / tối thiểu nếu có lý do | Auto | Theo mẫu |
| `cell.spacing` | 0 | 0 | Giữ nguyên |
| `header.weight` | Bold | Bold | Theo mẫu |
| `total.weight` | Bold khi có tổng thật | Bold + đường kẻ phân tách | Theo mẫu |
| `alignment.numeric` | Right | Right | Theo mẫu |
| `alignment.longtext` | Left/Top | Left/Top | Theo mẫu |

**Ngoại lệ thị giác:** các bảng là biểu mẫu ký nhận, có nền phân biệt loại dữ liệu, hoặc đã phê duyệt trong mẫu thường **không được phép** bỏ màu/viền để tối giản. Nếu tài liệu chứa ký hiệu chức năng bằng màu, phải giữ ngữ nghĩa; chỉ gợi ý tăng tương phản khi có quyền sửa.

### 48.1. Tác động thực tế của đệm ô

Đệm ô quá nhỏ làm chữ sát viền; quá lớn làm bảng tăng nhiều trang. Với mỗi ô, hai chiều đệm cộng vào không gian cần thiết. Do đó, một thay đổi `padding.x=1,5 → 2,5 mm` có thể làm cột nội dung xuống thêm một dòng, tăng chiều cao hàng và số trang. Preset phải được **kiểm tra hậu quả**, không coi tăng padding luôn đẹp hơn.

### 48.2. Đường viền có ngữ nghĩa

- Bảng phân công hoặc bảng có nhiều ô tương quan ngang/dọc: đường viền đủ rõ giúp người đọc không nhầm ô.
- Bảng số liệu thuần có ít cột: viền ngang tại tiêu đề/tổng có thể đẹp và dễ so sánh hơn.
- Bảng có nhóm tiêu đề nhiều tầng: đường phân cách nhóm phải đủ rõ; không được xóa viền định ranh nhóm.
- Kiểm tra trùng nét, góc ghép, đường kẻ nhảy/đứt, và viền không nhất quán sau khi qua trang.
- Khi sử dụng cả `tblBorders` và `tcBorders`, cần xét kết quả hiệu dụng và quy tắc ưu tiên viền; sửa tất cả viền trực tiếp có thể phá style gốc.

## 49. Typography trong bảng: ưu tiên khả năng đọc

1. Phông chữ theo authority cho vùng nội dung; không tự đưa Arial/Calibri vì gợi ý quốc tế có thể mâu thuẫn hệ văn bản Việt Nam.
2. Dùng cỡ chữ của phần nội dung theo quy định làm **mốc đối chiếu**; nếu có bảng mẫu/đơn vị đặc thù, ưu tiên mẫu hợp lệ; tránh áp chặt quy định thụt đầu dòng và Justify cho ô dữ liệu ngắn.
3. Căn trái văn bản dài; căn phải số; căn giữa STT/ngày ngắn. Không dùng nhiều dấu cách hoặc tab để giả căn cột.
4. Tiêu đề cột có thể đậm; không tự viết hoa toàn bộ nếu văn bản gốc không như thế.
5. Tránh đổi độ giãn ký tự, `Fit Text`, Scale chữ hoặc nén ký tự để ép một tên dài vào ô nhỏ.
6. Nội dung ô có đoạn liệt kê/điểm/khoản phải giữ cấu trúc đoạn và numbering trong ô, không làm phẳng thành một chuỗi.
7. Với số thập phân/cột tiền: căn theo dấu thập phân khi thực sự hỗ trợ và có dữ liệu ổn định; nếu không, căn phải đồng nhất. Không tự thêm số 0 thập phân khi chưa được phép.
8. Không tự chèn dấu ngắt dòng cứng để “cân ô” nếu mục tiêu là sửa thuần định dạng.

## 50. Tiêu chuẩn nhìn trực quan để nghiệm thu bảng

| Dấu hiệu | Cách đánh giá bằng mắt / render | Ưu tiên |
|---|---|---|
| Nội dung không bị cắt | Chữ cuối trong ô hiện đầy đủ; không có chữ chồng lên viền | Bắt buộc |
| Không tràn vùng chữ | Viền bảng không vượt mép vùng in và đối tượng khác | Bắt buộc |
| Không trang gần như trống vì bảng | Kiểm tra hàng không tách, `keep-with-next`, page break | Cao |
| Cột quan trọng có đủ chỗ | Tên, mô tả, văn bản pháp lý không bị chia dòng vô lý | Cao |
| Dữ liệu cùng kiểu được căn giống nhau | Cột số, ngày, mã, tên có nhịp đọc rõ | Cao |
| Hàng tiêu đề rõ | Đậm, chiều cao đủ, không bị tách sai | Cao |
| Bảng dài dễ theo dõi | Nhận diện tiêu đề lặp/không lặp đúng theo mục tiêu DOCX/PDF | Cao |
| Viền nhất quán | Nét đơn, không loang hoặc dày đột ngột | Trung bình |
| Nhiều khoảng trắng thừa | Hàng cao quá mức/cột quá rộng so nội dung | Trung bình |
| Mật độ thông tin | Không quá chật hoặc quá loãng | Trung bình |

Không dùng “đạt thẩm mỹ” để thay thế việc đối chiếu nội dung, quyền sửa và căn cứ pháp lý.

# PHẦN XIV. BẢNG PHỨC TẠP, BẢNG LỒNG, BIỂU MẪU VÀ NGOẠI LỆ

## 51. Mô hình cấu trúc phải lưu giữ

Một bảng DOCX không nhất thiết là ma trận `rows × cols` hoàn chỉnh. Nó có **lưới bố cục** (`tblGrid`), ô có thể chiếm nhiều vị trí lưới (`gridSpan`/`vMerge`), có hàng bắt đầu muộn/kết thúc sớm, và có bảng khác trong ô. Tài liệu kỹ thuật của `python-docx` nhấn mạnh sự khác biệt giữa ô thật và ô bị bỏ trống; API `row.cells` có thể trình bày lặp dữ liệu của ô gộp để tạo ma trận nhìn giống chữ nhật [S22].

Khi kiểm tra cấu trúc:

- Ghi `table_id`, `story_part` (body/header/footer/footnote/endnote nếu được hỗ trợ), `section`, `parent_table`, `cell_id`, `row_path`, `grid_start`, `grid_span`, `vertical_merge_state`.
- Phân biệt **một ô vật lý** với nhiều vị trí lưới mà ô đó chiếm; dữ liệu không được nhân bản thành nhiều ô khi viết ra.
- Phân biệt vị trí lưới bỏ trống với ô rỗng thật.
- Với bảng lồng, ghi quan hệ cha/con và thứ tự xuất hiện giữa đoạn văn/ảnh/bảng trong một ô.
- Bảng thuộc phụ lục phải có provenance về `appendix_id`, không nhập chung body.
- Một bảng nằm trong header/footer có thể chỉ là cơ chế dàn trang; cần cho vào nhóm bảo toàn chức năng thể thức.

## 52. Các vùng bắt buộc bảo toàn trong thao tác format-only

| Thành phần | Vì sao quan trọng | Chính sách mặc định |
|---|---|---|
| `w:gridSpan`, `w:vMerge`, ô lược bỏ | Ngữ nghĩa nhóm và hình học bảng | Bất biến |
| Thứ tự block trong ô | Xác định nghĩa của văn bản, hình và bảng con | Bất biến |
| Content control `w:sdt` | Biểu mẫu/dữ liệu được ràng buộc | Bất biến |
| Field code/field result | Có thể sinh nội dung động | Không thay field/công thức |
| Bookmark, hyperlink, comment range | Vị trí liên kết/đánh dấu | Giữ nguyên |
| Track changes, move range | Trạng thái soát xét pháp lý/nghiệp vụ | Không tự accept/reject |
| Drawing/picture, relationship, anchor | Hình ảnh/biểu đồ ký hiệu | Giữ nguyên |
| Ô chữ ký, dấu, checkbox | Quy trình xác nhận | Preserve |
| Section, numbering, headers/footers | Ngữ cảnh phân trang và thể thức | Không sửa trừ khi phạm vi được duyệt |
| Bảng in mẫu, scan ảnh | Có thể không phải bảng Word thật | Không giả định sửa được như bảng dữ liệu |
| Tệp có chữ ký số/protection | Sửa có thể ảnh hưởng tính xác thực và khả năng kiểm chứng | Không tự thao tác; báo cần quy trình riêng |

Đặc biệt, **giữ nguyên văn bản nhìn thấy** chưa đủ: có trường hợp XML thay đổi làm mất field, reference hoặc nội dung ẩn. Verification cần đi xa hơn so với so sánh chuỗi text.

## 53. Phân loại rủi ro theo cấu trúc

| Cấp | Nhận diện | Tự động tối ưu |
|---|---|---|
| `R0 SIMPLE` | Bảng Word thật, không gộp, không bảng con, không đối tượng đặc biệt, nội dung rõ | Có thể cho sửa định dạng sau khi người dùng chọn |
| `R1 STRUCTURED` | Có gộp ô đơn giản/tiêu đề nhiều hàng nhưng phân tích được lưới | Chỉ thuộc tính an toàn; cần preview |
| `R2 COMPLEX` | Bảng lồng, ô lược bỏ, nhiều cấp, ảnh, field, text direction hoặc layout đặc biệt | Giữ cấu trúc; chỉ gợi ý hoặc giới hạn sửa |
| `R3 PROTECTED` | Mẫu bắt buộc, ký nhận, ký số, bảo vệ, tính toàn vẹn có nguy cơ | Preserve/khóa; không sửa tự động |
| `R4 UNKNOWN` | Markup Compatibility / phần tử lạ / lỗi parse | Không tự sửa; báo chưa hỗ trợ |

**Nguyên tắc fail-closed:** mức rủi ro cao hoặc thiếu bằng chứng → giảm quyền tự sửa; không tăng quyền vì mô hình phân loại có độ tự tin cao một cách chủ quan.

## 54. Word style cascade: nguồn gốc những lỗi “sửa rồi mà không đổi”

Nhiều bảng có `w:tblStyle` và các vùng định dạng có điều kiện như first row, first/last column, banded rows. Microsoft mô tả sự ưu tiên của định dạng có điều kiện (`tblStylePr`) và các lớp ghi đè theo vùng [S21]. Ngoài ra còn có `tblPrEx`, định dạng ô `tcPr`, đoạn `pPr`, ký tự `rPr` và các style kế thừa khác.

Do đó, trước một phép sửa:

1. Ghi nhận **giá trị hiện hữu hiệu dụng** (nếu có thể) và nguồn của thuộc tính (table style, row exception, direct cell, paragraph/run).
2. Xác định mục tiêu đổi **chỉ thuộc tính cụ thể** tại cấp thích hợp.
3. Không ghi đè tất cả `w:tcBorders`/`w:shd` cho mọi ô nếu một quy tắc style duy nhất có thể xử lý, và cũng không mặc định style đủ để thắng thuộc tính direct đang tồn tại.
4. Chỉ sửa style dùng chung khi chứng minh nó không ảnh hưởng bảng/vùng khác; nếu không, tạo cấu hình cục bộ hoặc yêu cầu người dùng quyết định.
5. Render lại; nếu hình thức không đổi hoặc lệch ngoài phạm vi, trả cảnh báo về nguồn xung đột.

**Không đưa ra “chuỗi ưu tiên tổng quát” thiếu kiểm chứng cho mọi thuộc tính OOXML**; từng họ thuộc tính có logic riêng và có thể khác giữa các bộ dựng tài liệu.

## 55. Bảng là hình ảnh, bảng quét và đối tượng nhúng

Đối với ảnh chứa bảng, Word không có `w:tbl` tương ứng để căn chỉnh ô. Không được nhận dạng ký tự từ ảnh rồi thay bằng bảng Word như một thao tác `format-only`; chuyển đổi OCR là nhiệm vụ khác, có rủi ro số liệu và đòi hỏi đối chiếu thủ công. Đối với bảng từ Excel nhúng, đồ thị hoặc đối tượng OLE, chỉ được can thiệp nếu có chức năng xử lý riêng, giữ được dữ liệu nguồn và liên kết. Khi chưa hỗ trợ thì báo `UNSUPPORTED`, không tuyên bố đã chuẩn hóa bảng.

# PHẦN XV. TỐI ƯU PHÂN TRANG, PRINT LAYOUT VÀ XUẤT PDF

## 56. Ma trận phân trang theo tình huống

| Tình huống | Giải pháp ưu tiên | Phép thử bắt buộc |
|---|---|---|
| Tiêu đề bảng là đoạn văn tách khỏi bảng | `keep-with-next` trên caption nếu phù hợp | Caption vẫn trước bảng, không kéo trôi cả cụm |
| Bảng có nhiều trang với header liên tục từ hàng đầu | Word `Repeat Header Rows` | Chỉ lặp các hàng đầu phù hợp, kiểm tra trang 2+ |
| Người dùng chèn manual page break trong bảng | Không hứa header tự lặp | Thông báo giới hạn chính thức của Word |
| Hàng ngắn vỡ qua hai trang | `cantSplit` chọn lọc | Không sinh trang trắng lớn/cắt chữ |
| Hàng dài hơn chiều cao còn lại hoặc một trang | Cho phép ngắt có kiểm soát | Nội dung đủ, không mất phần cuối |
| Hai bảng liền nhau khác nghĩa | Giữ ranh giới 2 bảng | Không nối bảng chỉ vì gần nhau |
| Bảng tiếp giáp chữ ký/phụ lục | Giữ khoảng cách/section theo mẫu | Không đẩy chữ ký sai vị trí |
| Phần bảng trong section landscape | Giữ header/footer/numbering đúng | Không ảnh hưởng section trước/sau |

Microsoft nêu rõ hàng tiêu đề lặp chỉ hoạt động với ngắt trang **tự động**, không hoạt động tương tự với ngắt trang thủ công [S07]. Không nên áp `cantSplit` cho toàn bảng mà chưa đánh giá chiều cao từng hàng.

## 57. Hai đầu ra phải có chính sách khác nhau: DOCX và PDF

Một vấn đề dễ bị bỏ sót: **bảng nhìn đúng khi in Word chưa đồng nghĩa PDF có gắn thẻ (tagged PDF) dễ tiếp cận**. Hướng dẫn Section508.gov về xuất PDF nêu lưu ý cụ thể đối với `Repeat Header Rows` khi đích là PDF, đồng thời yêu cầu bật document structure tags [S09]. Điều này cần được coi là khác biệt theo **định dạng đầu ra** và bộ chuyển đổi, không phải lý do tắt lặp tiêu đề cho tất cả DOCX.

Đề xuất kiểm tra riêng:

- `DOCX_PRINT`: lặp tiêu đề nếu đúng ngữ nghĩa và có bảng nhiều trang, xem Print Layout và bản in.
- `PDF_VISUAL`: nhìn hình ảnh từng trang sau chuyển đổi, kiểm tra không cắt ô, không chèn trang rỗng.
- `PDF_ACCESSIBLE`: kiểm tra thẻ bảng và hàng tiêu đề trong PDF thực tế bằng công cụ kiểm tra thích hợp; không suy ra accessibility chỉ từ DOCX hoặc từ cài đặt Word.
- Nếu thiếu công cụ PDF tagging/accessibility hoặc renderer, trả `NOT_VERIFIED`, không chấm `PASS`.

## 58. Kiểm soát orphan/widow và bảng ngắn ở cuối trang

Nên tránh tình trạng chỉ còn tên bảng trên trang trước, bảng bắt đầu trang sau; hoặc một hàng đơn lẻ cuối trang làm người đọc không hiểu nhóm dữ liệu. Biện pháp đề xuất là kiểm tra vùng trống còn lại và thuộc tính đoạn (`keepNext`, `keepLines`, `pageBreakBefore`, `widowControl`) theo **đoạn/hàng thích hợp**, không tự đặt một loạt `keepNext` cho mọi ô vì có thể tạo cụm không thể phân trang và đẩy nguyên bảng sang trang kế tiếp.

Quyết định tối ưu phải dựa trên hình ảnh đầu ra ở điều kiện tiêu chuẩn, không chỉ sự hiện diện của thuộc tính XML.

# PHẦN XVI. THUẬT TOÁN QUYẾT ĐỊNH, QUY TẮC KHAI BÁO VÀ PHÊ DUYỆT

## 59. Luồng quyết định chuẩn cho từng bảng

```text
1. FIND  : Tìm bảng Word vật lý trong tất cả phần tài liệu được hỗ trợ.
2. LOCATE: Xác định body / appendix / header / footer / cell-nested / unknown.
3. CLASSIFY: Data table / Official form / Layout table / Object image / Unknown.
4. RESOLVE AUTHORITY: ND30 hoặc HD05 hoặc mẫu chuyên ngành hoặc chưa rõ.
5. SNAPSHOT: Content, OOXML topology, relationships, styles, section references.
6. CHECK: Legal and form rules → document integrity risk → layout → visual.
7. PROPOSE: Tạo một hoặc nhiều phép sửa tối thiểu, chỉ thuộc phạm vi cho phép.
8. PREVIEW: Render các ứng viên và diff theo từng bảng; ghi rõ chưa kiểm chứng nếu không render.
9. APPROVE: Người dùng chọn mức sửa. Không tự chấp thuận khi thiếu quyền.
10. PATCH: Chỉnh các thuộc tính đã duyệt, bảo toàn package và nguồn authority.
11. VERIFY: Mở lại, diff cấu trúc và nội dung, kiểm tra render/print.
12. EXPORT/ROLLBACK: Chỉ xuất với mức kết quả đúng; thất bại thì phục hồi.
```

Mô hình này cho phép nhiều bảng trong cùng một DOCX có chính sách khác nhau: bảng ở body tự tối ưu, bảng biểu mẫu locked, bảng lồng review, bảng chữ ký preserve.

## 60. Chính sách xử lý theo cấp độ tác động

| Chính sách | Ý nghĩa | Ví dụ |
|---|---|---|
| `REPORT_ONLY` | Chỉ phát hiện và cung cấp bằng chứng | Bảng chưa có tiêu đề hoặc bảng chứa ảnh scan |
| `SAFE_IF_APPROVED` | Chỉ sửa định dạng đơn giản khi được duyệt | Căn phải số, chỉnh đường viền từ preset |
| `PREVIEW_REQUIRED` | Bắt buộc có render trước/sau | Phân phối lại độ rộng cột, đổi padding đáng kể |
| `STRUCTURAL_APPROVAL` | Thay đổi cấu trúc/vùng văn bản phải được chấp thuận riêng | Section ngang, chuyển bảng sang phụ lục |
| `NEVER_FORMAT_ONLY` | Không làm trong chức năng định dạng bảng | Xóa hàng/cột, sửa giá trị, gộp/tách ô, OCR chuyển ảnh thành bảng |

Đề xuất kỹ thuật: chỉ dùng các bộ phân loại bằng quy tắc xác định (tên cột, vị trí bảng, OOXML) cho các quyết định có thể quyết định chính xác; với ngữ nghĩa khó, trợ lý AI chỉ hỗ trợ gợi ý và giải thích. **Quyền sửa, validation, so sánh XML, thứ tự hàng và giá trị số liệu phải dùng logic xác định**, không giao AI tự quyết.

## 61. Mẫu mô tả quy tắc (đề xuất, không phải schema đã triển khai)

```yaml
id: TABLE-PAG-001
version: 2
name: Repeat the true initial header rows
authority: RECOMMENDATION
scope: table
applicability:
  classification: DATA_TABLE
  risk_max: R1
  header_at_beginning: true
  rows_span_pages: confirmed_by_renderer
checks:
  - no_manual_break_within_table
  - approved_for_docx_output
proposal:
  property: w:tblHeader
  target: contiguous_initial_header_rows_only
fix_policy: PREVIEW_REQUIRED
verification:
  - ooxml_topology_unchanged
  - visible_text_unchanged
  - header_repeat_verified_on_page_2
```

**Cảnh báo:** đoạn YAML minh họa cách diễn đạt rule, không khẳng định đã có API, thư viện hay schema này trong bất cứ repository nào.

## 62. Bảng quyết định theo độ tự tin (confidence)

| Độ chắc chắn | Ví dụ chứng cứ | Phương thức xử lý |
|---|---|---|
| Xác nhận trực tiếp (`EXACT`) | `w:tbl` có cấu trúc đơn giản, rõ source part; mẫu hợp lệ đã chỉ định | Có thể đưa vào danh sách phép sửa được xét |
| Cao nhưng có suy luận (`HIGH`) | Tiêu đề rõ; cột số ổn định; không có merge đặc biệt | Gợi ý và preview |
| Trung bình (`MEDIUM`) | Bảng có ô gộp nhiều tầng/tiêu đề khó xác định | Review; không áp sửa hàng loạt |
| Thấp (`LOW/UNKNOWN`) | Bảng dàn trang không rõ, chữ ký, XML lạ | Preserve; cần người dùng chỉ định |

Độ tin cậy dùng để **giảm** quyền tự sửa; không dùng các tỷ lệ % tự nghĩ ra để hợp thức hóa thay đổi nguy hiểm.

# PHẦN XVII. KIỂM THỬ THEO PHẠM VI, BẰNG CHỨNG VÀ ĐIỀU KIỆN NGHIỆM THU

## 63. Bộ tình huống tối thiểu nên có

| ID | Trường hợp thử | Kết quả kỳ vọng |
|---|---|---|
| T01 | Bảng 3×3 đơn giản, đủ vùng chữ | Chỉnh preset, không đổi dữ liệu |
| T02 | Bảng phân công nhiều mô tả tiếng Việt dài | Ưu tiên cột nội dung, không cắt chữ |
| T03 | Cột mã `001`, `0009`, số điện thoại | Giữ nguyên ký tự và số 0 đầu |
| T04 | Bảng có số âm, phần trăm, dấu thập phân | Căn số nhưng không đổi giá trị |
| T05 | Bảng có STT tới 3 chữ số | Cột STT đủ rộng, không bẻ chữ số |
| T06 | Hàng/cột tiêu đề có gộp ngang (`gridSpan`) | Giữ sơ đồ gộp, viền/độ rộng hợp lệ |
| T07 | Gộp dọc (`vMerge`) nhiều hàng | Không nhân bản nội dung, không phá merge |
| T08 | Hàng có ô đầu/cuối bị lược bỏ | Không coi ô lược bỏ là ô trống thật |
| T09 | Bảng con trong một ô + đoạn văn trong ô | Bảo toàn thứ tự block và quan hệ cha/con |
| T10 | Bảng có ảnh/biểu tượng trong ô | Không thay ảnh/anchor, không cắt ảnh |
| T11 | Bảng dài hơn 2 trang có hàng tiêu đề đầu | Header có thể lặp đúng khi Word tự phân trang |
| T12 | Bảng có manual page break | Không tuyên bố sai rằng header được tự lặp |
| T13 | Một hàng dài hơn trang | Không ép `cantSplit` gây mất nội dung |
| T14 | Hàng có `trHeight` Exactly gây cắt chữ | Báo lỗi, sửa có kiểm chứng nếu được duyệt |
| T15 | Bảng landscape giữa hai trang portrait | Không đổi section/header/footer/đánh trang ngoài phạm vi |
| T16 | Bảng trong phụ lục ND30 nhiều phụ lục | Giữ numbering La Mã; không nhập vào body |
| T17 | Bảng trong phụ lục HD05 nhiều phụ lục | Giữ numbering Ả-rập; không nhập vào body |
| T18 | Bảng dùng để dàn đầu văn bản/chữ ký | Không áp preset bảng dữ liệu |
| T19 | Biểu mẫu gộp ô, dấu xác nhận, checkbox | Preserve hoàn toàn nếu không có phép sửa được duyệt |
| T20 | Table Style xung đột với direct cell format | Chỉ sửa đúng thuộc tính; hình thức ra đúng và không ảnh hưởng nơi khác |
| T21 | Bảng có field/hyperlink/bookmark/comment | Không hủy relationship hoặc đối tượng |
| T22 | Track changes / document protection | Không tự accept changes/không tự gỡ khóa |
| T23 | OOXML `mc:AlternateContent` hoặc unknown part | Không làm mất nhánh/part; từ chối nếu không bảo toàn chắc chắn |
| T24 | Bảng chứa chuỗi không có dấu cách dài | Cảnh báo overflow, không tự cắt/xóa chuỗi |
| T25 | Bảng nhỏ cuối trang + caption | Không để caption mồ côi |
| T26 | Xuất PDF sau DOCX | Kiểm tra ảnh từng trang và thẻ bảng nếu yêu cầu accessibility |
| T27 | Không có engine render | Kết quả `VISUAL_NOT_VERIFIED`, không giả PASS |
| T28 | Áp cùng một preset hai lần | Idempotence: không phát sinh thay đổi ngoài dự kiến lần 2 |
| T29 | Tệp mã hóa hoặc không thể mở lại | Fail-closed, không có file kết quả giả hợp lệ |
| T30 | Bảng đã đạt yêu cầu | Không sửa vô ích, không tăng số trang |

Đây là **danh mục đề xuất**, không phải các test đã tồn tại hoặc đã PASS.

## 64. Bằng chứng cần lưu theo từng bảng

1. `table_id`, đường dẫn part, vị trí trong body/appendix, section tương ứng.
2. Fingerprint nội dung trước/sau: không chỉ concatenated text mà có thứ tự block và phân biệt ô vật lý.
3. Snapshot topology: số hàng, số ô vật lý, grid span, vMerge, nested parents.
4. Danh sách thuộc tính đã đổi và giá trị trước/sau; ghi rõ lý do/rule/authorization.
5. Kết quả kiểm tra quan hệ package (image, hyperlinks, footnotes, comments, fields nếu có).
6. Số trang/bounding boxes/tràn lề nếu renderer xác nhận; đánh dấu thiếu bằng chứng nếu không thể đo.
7. Hình ảnh trước/sau vùng bảng thay đổi, kết quả đối chiếu bố cục, lỗi còn lại.
8. Tổng kết `PASS`, `PASS_WITH_WARNINGS`, `NOT_VERIFIED`, `FAIL` với tiêu chí minh bạch.

## 65. Điều kiện từ chối cấp giấy chứng nhận chất lượng

Không được kết luận `PASS` khi có một trong các tình huống:

- Text, số liệu, công thức, thứ tự block hoặc số ô vật lý thay đổi ngoài phạm vi.
- Ô gộp dọc/ngang bị thay đổi; ảnh/field/relationship biến mất.
- Vi phạm biểu mẫu bắt buộc hoặc thay đổi nguồn authority.
- Tệp không mở lại được, DOCX package hỏng hoặc mất part thiết yếu.
- Có vùng chữ bị cắt hoặc tràn lề mà ảnh render xác nhận, dù điểm thẩm mỹ cao.
- Tuyên bố kiểm chứng bằng Word/PDF nhưng chỉ mới kiểm tra XML.
- Không có quyền sửa khi chính sách yêu cầu approval.

Khi không có renderer: vẫn có thể đạt **structural verification** cho phép sửa hẹp, nhưng phải ghi rõ `VISUAL_NOT_VERIFIED`; không thể đồng thời tuyên bố bảng đã tối ưu thẩm mỹ hoàn toàn.

# PHẦN XVIII. HƯỚNG DẪN THỰC HÀNH VÀ KẾ HOẠCH ÁP DỤNG ƯU TIÊN REUSE

## 66. Checklist thủ công trong Microsoft Word

Quy trình này hữu ích khi biên tập trực tiếp, không cần viết công cụ:

1. Bật `View Gridlines` để phân biệt ô thật và đường kẻ hiển thị; kiểm tra có ô gộp/lồng/ô dài hay không.
2. Vào `Layout > Margins` và `Size` xem khổ giấy/lề theo loại văn bản; xác định bảng thuộc section nào.
3. Chọn bảng, kiểm tra `Table Properties > Table` và `AutoFit`; không click `Distribute Columns` hàng loạt khi cột có vai trò khác nhau.
4. Điều chỉnh bằng `Cell Margins` để văn bản không sát viền; tránh tăng padding quá nhiều.
5. Trong `Table Properties > Row`, kiểm tra height và chế độ Exactly; xử lý bằng Auto/At least khi cần và được phép.
6. Dùng `Repeat Header Rows` khi bảng dữ liệu dài có tiêu đề thực sự ở những hàng đầu; không áp nếu hàng đầu là ô mẫu trang trí hoặc ngắt thủ công khiến kỳ vọng sai.
7. Chọn `Table Design > Borders and Shading` để thống nhất nét viền; tránh tô nền nhiều màu không cần thiết.
8. Căn giữa STT, căn trái diễn giải, căn phải số liệu; không biến định dạng thành thao tác sửa giá trị.
9. Chuyển sang `Print Layout` và xem tất cả trang có bảng; không chỉ xem trang đầu.
10. Nếu PDF là đầu ra: xuất và kiểm tra riêng PDF, đặc biệt ở điểm qua trang và bảng có tiêu đề lặp.
11. Lưu bản gốc; đối chiếu nội dung trước/sau nếu có sửa hàng loạt.

## 67. Đánh giá tái sử dụng giải pháp hiện có trước khi xây công cụ

| Lựa chọn | Giá trị tái sử dụng | Giới hạn & quyết định |
|---|---|---|
| **Microsoft Word (native UI)** | Có AutoFit, cell margins, row settings, repeat headers, table styles, print preview | Ưu tiên với chỉnh tài liệu đơn lẻ; cần thao tác/kiểm chứng thủ công [S07][S08] |
| **Open XML SDK (.NET)** | API strongly typed, tài liệu chuẩn hóa WordprocessingML | Hữu ích nếu dự án có .NET; không thêm runtime khi chỉ cần vá ít XML trong stack khác [S14][S20] |
| **python-docx (Python)** | API bảng, hàng, ô; tài liệu giải thích merged/omitted cells và nested tables | Dùng nếu đã có Python; với các trường hợp OOXML đặc biệt có thể cần cấp XML; không giả định roundtrip toàn bộ loại DOCX [S22] |
| **docx4j (Java)** | Thư viện làm việc với OOXML, khả năng phân tích DOCX theo Java | Chỉ cân nhắc khi dự án dùng Java/đã có dependency; cần audit license/feature/version thực tế trước chọn |
| **Apache POI XWPF (Java)** | API đọc/sửa bảng DOCX trong Java | Tương tự: không thêm stack Java chỉ để sửa bảng ít thuộc tính |
| **Thao tác OOXML bằng thư viện ZIP/XML đã có** | Thay đổi rất nhỏ, tránh migrate và giữ cấu trúc | Có thể phù hợp nếu mã hiện hành đã làm việc ở mức package; bắt buộc kiểm soát namespace, markup compatibility, relationships và zip safety |

**Chưa có audit mã nguồn repository ở nhiệm vụ này**: bảng trên là lựa chọn tham khảo, **không phải kiến nghị thêm dependency cụ thể**. Cần audit source hiện hành, AGENTS.md, module DOCX, processor, tests và các cấu hình đã được chứng minh hoạt động trước khi chọn cách tích hợp. Tránh tạo engine/registry/serializer thứ hai.

## 68. Giai đoạn hoàn thiện gợi ý — không mở rộng tùy tiện

| Giai đoạn | Phạm vi nhỏ nhất | Điều kiện hoàn thành |
|---|---|---|
| P0-A | Audit các công cụ/capability bảng hiện có và tài liệu tham chiếu | Bảng thành phần nào reuse/extend, file nào bị ảnh hưởng |
| P0-B | Bảo toàn topology + text + DOCX package khi sửa 1–2 thuộc tính bảng đơn giản | Test targeted mở lại, diff đạt |
| P1-A | Preset Formal Grid trên bảng đơn giản và bảng có ô gộp đơn giản | Chọn đúng bảng, không chạm layout/form |
| P1-B | Cân đối độ rộng và phân trang trên vài bảng đại diện | Render trước/sau, ít nhất một bảng nhiều trang |
| P2 | Các loại bảng phức tạp, kiểm tra accessibility và PDF tùy nhu cầu thật | Test theo blast radius + phê duyệt của người dùng |

Không triển khai thêm hệ OCR, PDF renderer, vector search, AI layout engine hoặc dịch vụ trung gian nếu chưa có yêu cầu và bằng chứng thiếu năng lực thực sự. Với thao tác thuần kiểm tra/định dạng bảng, các primitive của Word/OOXML và dependency sẵn có thường là điểm xuất phát phù hợp nhất.

## 69. Đặc tả đầu ra được coi là tối ưu

Đối với **một bảng** được định dạng thành công, báo cáo kết quả nên nói rõ:

> Đã áp dụng `Formal Grid` / `Statistical Minimal` trên bảng X thuộc body/phụ lục; thay đổi các thuộc tính A, B, C sau khi được phê duyệt; bảng nằm trong vùng chữ, không cắt nội dung; văn bản, thứ tự ô, cấu trúc gộp, ảnh và liên kết không đổi; tệp DOCX mở lại hợp lệ; kiểm tra bố cục: PASS bằng [tên renderer] hoặc NOT_VERIFIED nếu chưa có.

Đó là **mẫu phát biểu nghiệm thu**, không phải bằng chứng rằng bất kỳ tệp cụ thể nào đã được chỉnh sửa.

---

# PHẦN XIX. XÁC ĐỊNH NỘI DUNG TRỌNG TÂM ĐỂ QUYẾT ĐỊNH ĐỘ RỘNG CỘT — CHUYÊN ĐỀ V3

> **Trạng thái chuyên đề:** [KN]/[KT] – thuật toán thiết kế và chính sách đề xuất, **không phải** bộ định mức pháp lý của Nghị định 30/2020/NĐ-CP hay Hướng dẫn 05-HD/VPTW. Phần này kế thừa Phần IV, mục 15 và Phần XII, mục 44–46. Các ngưỡng, trọng số và phép đo là *khởi điểm hiệu chỉnh*, chưa được kiểm định trên một corpus DOCX đại diện.
>
> **Phạm vi sử dụng:** quyết định **độ rộng cột trong bảng Word đã có**, không tự ý thay đổi thứ tự cột, tiêu đề, giá trị hay vị trí bảng. Chỉ áp dụng cơ chế chọn chiều rộng cho bảng dữ liệu mà cấu trúc và quyền sửa đã được xác nhận. Biểu mẫu chính thức/ô ký/bảng dàn trang áp dụng chính sách bảo toàn.

## 70. Kết quả research: độ dài nội dung khác với giá trị thông tin

### 70.1. Bốn kết luận cần đưa vào thuật toán

1. **Thông tin trọng tâm được xác định bởi *tác vụ của người đọc*, không phải độ dài ô.** Nghiên cứu Nielsen Norman Group về bốn tác vụ dữ liệu nhấn mạnh cột đầu nên giúp định danh bản ghi bằng ngôn ngữ dễ hiểu, những cột liên quan nên được đặt gần nhau và thứ tự cột phản ánh tầm quan trọng với người đọc [S33]. Tài liệu VA.gov khuyến nghị xác định cùng người phụ trách nội dung những trường quan trọng để người đọc hiểu bảng, nhất là khi diện tích hiển thị hạn chế [S34]. *Đây là nguyên lý UX, không phải quy tắc bắt buộc phải đổi thứ tự cột DOCX có sẵn.*
2. **Thông tin rất quan trọng có thể chiếm ít không gian.** Ví dụ: *Hạn hoàn thành* hoặc *Kết quả* chỉ dài vài ký tự nhưng không được xuống dòng gây nhập nhằng; *Ghi chú* có thể dài mà vẫn chấp nhận nhiều dòng. Độ ưu tiên ngữ nghĩa và độ rộng yêu cầu phải được tính thành **hai đại lượng riêng**.
3. **Bộ dàn trang phải xét tối thiểu/bề rộng ưu tiên theo font và điểm ngắt.** ISO/IEC 29500 và tài liệu OOXML phân biệt thuật toán fixed và AutoFit, độ rộng tối thiểu sau ngắt dòng so với độ rộng không ngắt [S30]–[S31]. Microsoft hỗ trợ AutoFit Contents/Window và Fixed Column Width [S08]. Các giá trị `w:tblW`, `w:tcW` là **preferred width**, không bảo đảm chiều rộng cuối cùng không thay đổi [S20], [S29].
4. **Mục tiêu chính là hỗ trợ đọc, đối chiếu, ra quyết định; không lấp kín trang bằng mọi giá.** Government Analysis Function phân biệt bảng *demonstration* dùng để làm rõ thông điệp và bảng *reference* phục vụ tra cứu chi tiết; căn phải số và nhóm thông tin liên quan giúp đối chiếu hiệu quả [S11]. Nhiều dòng trong ô mô tả có thể hợp lý nếu phần còn lại của bảng trở nên dễ đọc hơn.

### 70.2. Những suy luận sai cần loại bỏ

| Cách suy luận sai | Vấn đề | Nguyên tắc thay thế |
|---|---|---|
| Cột nhiều chữ nhất phải rộng nhất | Một ghi chú rất dài có thể lấn cột nhiệm vụ/hạn | Xác định mục đích + chi phí xuống dòng |
| Cột quan trọng nhất phải rộng nhất | Mã hồ sơ quan trọng nhưng chỉ cần đủ chỗ, không nên lãng phí | **Ưu tiên bảo vệ** khác **nhu cầu mm** |
| Cỡ chữ nhỏ thì cần ít chỗ hơn | Thu nhỏ toàn bảng dễ trái quy định, khó đọc | Cố định font hợp lệ, tối ưu ràng buộc chiều rộng |
| Tiêu đề dài quyết định toàn bộ chiều rộng | Có thể xuống dòng tiêu đề hợp lý, dữ liệu mới là phần chiếm đa số | Đo cả header + phân phối giá trị dữ liệu |
| Đếm ký tự tiếng Việt là đủ | Độ rộng glyph, đậm/nghiêng, tổ hợp dấu, chữ số khác nhau | Đo theo font/run và bộ kết xuất, đếm ký tự chỉ là ước lượng |
| Dàn đều 100% chiều rộng vùng chữ luôn đẹp | Bảng ít dữ liệu có thể bị kéo giãn vô ích | Cho phép bảng hẹp hơn vùng chữ nếu phù hợp thể thức |
| Lặp giá trị ô gộp để đo từng cột | Nhân đôi sức ép chiều rộng | Ràng buộc **tổng chiều rộng các cột** của ô gộp |
| AutoFit cho kết quả tối ưu ngữ nghĩa | AutoFit chủ yếu phản hồi hình học và nội dung | Kết hợp ưu tiên ngữ nghĩa + đo thực tế + nghiệm thu |

## 71. Xác định “trọng tâm” qua tác vụ người đọc

### 71.1. Phân loại mục tiêu bảng trước khi xếp hạng cột

| Loại mục tiêu | Người đọc cần làm | Cột thường mang trọng tâm | Cột thường co giãn linh hoạt |
|---|---|---|---|
| **LOOKUP** – Tra cứu | Tìm đúng hồ sơ/người/đơn vị | Tên/định danh + dấu hiệu phân biệt | Diễn giải, ghi chú |
| **ACTION** – Điều hành | Biết việc phải làm, ai làm, khi nào | Nội dung công việc, trách nhiệm, hạn, trạng thái | Ghi chú, diễn giải phụ |
| **COMPARE** – So sánh | So sánh các năm/nhóm/đơn vị | Nhãn chỉ tiêu, số liệu, đơn vị tính, biến động | Ghi chú ngoại lệ |
| **DECISION** – Quyết định | Chọn phương án hoặc xử lý ngoại lệ | Tiêu chí quyết định, rủi ro, trạng thái, kiến nghị | Diễn giải cơ sở phụ nếu có |
| **SUMMARY** – Tổng hợp | Đọc kết quả/tổng số/chênh lệch | Chỉ tiêu, tổng cộng, kết quả chính | Phần diễn giải thêm |
| **COMPLIANCE** – Kiểm tra tuân thủ | Đối chiếu đúng điều kiện/quy định | Tiêu chí, mức yêu cầu, kết quả đánh giá, bằng chứng | Ghi chú không bắt buộc |
| **FORM** – Biểu mẫu bắt buộc | Điền và xác nhận theo mẫu | **Do mẫu quy định, không suy tự do** | Không tự xác định |

**Quy tắc ưu tiên nguồn để xác định mục tiêu:** (1) người dùng chọn rõ mục tiêu sử dụng; (2) loại biểu mẫu và quy định gắn với bảng; (3) tiêu đề/caption và đoạn giới thiệu liền trước, có provenance; (4) cấu trúc tiêu đề cột và nhãn hàng; (5) phân bố dữ liệu thực tế; (6) nếu vẫn không rõ, chọn `UNKNOWN` và **không xác lập cột trọng tâm với độ tin cậy cao**.

Không dùng tên cột một cách đơn lẻ để kết luận mục tiêu. “Kết quả” trong bảng nghiên cứu có thể là số, trong bảng theo dõi công việc có thể là trạng thái, trong bảng kiểm tra pháp lý có thể là kết luận đạt/không đạt.

### 71.2. Bản đồ vai trò cột (column role map)

| Vai trò | Dấu hiệu nhận diện | Bảo vệ hiển thị | Co giãn |
|---|---|---|---|
| `ROW_IDENTIFIER` | Tên, mã, địa danh, tên đối tượng dùng tìm hàng | Không cắt/không làm mơ hồ danh tính; mã dài không tách tùy tiện | Trung bình |
| `PRIMARY_CONTENT` | Việc phải làm, nội dung trọng tâm, chỉ tiêu chính | Đủ rộng để quét được nội dung và tránh số dòng quá nhiều | Cao khi có văn bản dài |
| `OWNER_ACCOUNTABLE` | Cơ quan chủ trì, người/đơn vị chịu trách nhiệm | Không làm tên bị nát thành nhiều dòng ngắn | Trung bình |
| `DEADLINE` | Hạn, mốc, thời gian | Cố gắng giữ mỗi giá trị ngày trên một dòng | Thấp sau khi đạt mức tối thiểu |
| `MEASURE` | Giá trị tiền, %, số lượng, kết quả định lượng | Giữ nguyên dấu/độ chính xác/đơn vị, căn phải | Thấp–trung bình |
| `STATUS_DECISION` | Trạng thái, kết luận, đạt/không đạt | Không bị che, không mơ hồ; ưu tiên khi mục tiêu ACTION/DECISION | Thấp–trung bình |
| `NARRATIVE_SUPPORT` | Ghi chú, diễn giải phụ, căn cứ bổ sung | Cho xuống dòng; không để chiếm hết vùng chữ | Cao về khả năng co hẹp |
| `STRUCTURAL_INDEX` | STT, số mục | Đủ rộng để giữ chữ số không đứt | Thấp |
| `FORM_RESERVED` | Ô nhập, ô ký, ô dấu, khung được quy định | Giữ nguyên theo mẫu | Khóa |

**Phân biệt hai thuộc tính:** `semantic_priority` xác định **thiệt hại nếu khó đọc**; `expansion_need` xác định **được lợi bao nhiêu khi cấp thêm 1 mm**. Một cột hạn chót có thể có priority rất cao nhưng expansion_need bằng 0 sau khi đủ chứa ngày.

### 71.3. Thang điểm ưu tiên ngữ nghĩa (heuristic nội bộ)

Nếu chưa có cấu hình nghiệp vụ, sử dụng thang 0–5 cho từng tiêu chí; cách tính dưới đây **chỉ là gợi ý khởi tạo**, cần hiệu chỉnh và kiểm định.

| Tín hiệu | Trọng số | Câu hỏi kiểm tra |
|---|---:|---|
| Mức liên quan đến nhiệm vụ người đọc `T` | 30% | Không thấy cột này có trả lời được câu hỏi của bảng không? |
| Khả năng nhận diện/định danh `I` | 20% | Cột có giúp xác định đúng hàng/đối tượng không? |
| Đóng góp diễn giải/so sánh `M` | 20% | Thiếu cột này có gây hiểu sai số liệu hoặc kết quả không? |
| Thiệt hại nghiệp vụ khi đọc nhầm `R` | 20% | Sai hạn, sai cơ quan, sai kết luận có gây hậu quả không? |
| Tần suất người đọc cần quét cột `F` | 10% | Khi tra cứu thường xuyên có phải nhìn cột này không? |

Công thức quy đổi thành 100 điểm: `P_i = 20 × (0.30 T_i + 0.20 I_i + 0.20 M_i + 0.20 R_i + 0.10 F_i)`.

- `P ≥ 80`: **trọng tâm**; được ưu tiên chống xuống dòng bất hợp lý và giữ mức đọc hiểu rõ.
- `60 ≤ P < 80`: **quan trọng**; không bóp hẹp tới mức khó đọc.
- `40 ≤ P < 60`: **hỗ trợ thiết yếu**; được co giãn có điều kiện.
- `P < 40`: **bổ trợ**; ưu tiên xuống dòng nếu cần tiết kiệm chiều rộng, nhưng vẫn phải đọc được.

Không được biến các ngưỡng trên thành kết luận pháp lý hoặc dùng `P` làm tỷ lệ phân bổ mm. Với `FORM_RESERVED`, độ rộng là **khóa cứng**, dù `P` thấp. Đối với `DATE/ID`, độ rộng sàn là ràng buộc trước khi tối ưu, dù `P` thấp. Trong mọi trường hợp, cấm để điểm máy tự động ghi đè mức ưu tiên do người dùng đặt.

### 71.4. Độ tin cậy của quyết định

- **HIGH:** mục tiêu được người dùng chọn hoặc biểu mẫu xác lập; các cột nhận diện rõ và không xung đột.
- **MEDIUM:** suy từ tiêu đề/caption và header, dữ liệu thống nhất, không vướng cấu trúc đặc biệt.
- **LOW:** bảng nhiều cấp/đa nghĩa, không có tiêu đề, dữ liệu dị biệt, ngữ cảnh thiếu hoặc nhiều cột không tên.

`LOW` ⇒ chỉ trình bày đề xuất, không tự tối ưu. `MEDIUM` ⇒ cần xem trước và xác nhận. `HIGH` ⇒ vẫn chỉ được sửa nếu có authorization cho đúng phạm vi; mọi thay đổi cần render verification. Điểm tin cậy là **đánh giá có thể giải thích**, không phải xác suất được hiệu chỉnh, trừ khi có số liệu kiểm định.

## 72. Đo “nhu cầu chiều rộng” độc lập với tầm quan trọng

### 72.1. Không lấy số ký tự làm đơn vị hình học

Đối với mỗi ô, đo hoặc ước lượng bằng **độ rộng trình bày của các text run trong font hiệu dụng** (tên font, cỡ chữ, đậm/nghiêng, ký tự và glyph), cộng tác động của: cell padding, border, indent, ký tự đặc biệt/tab, xuống dòng có sẵn, liên kết/field, số và hình/đối tượng trong ô. Với tiếng Việt, ký tự Unicode có thể có dạng tổ hợp và font fallback; vì vậy thuật toán chỉ đếm ký tự/cụm từ *không đủ* để chứng nhận độ rộng.

Nếu chưa có renderer Word tương thích: phép đo font bên ngoài chỉ dùng để **sàng lọc ứng viên**. Khi cần xác nhận đạt/không tràn, phải dùng bằng chứng kết xuất thật; nếu thiếu, trả `VISUAL_NOT_VERIFIED`.

### 72.2. Tập đặc trưng cần đo cho từng cột

| Biến | Ý nghĩa | Cách sử dụng |
|---|---|---|
| `hard_floor_i` | Mức rộng tối thiểu giữ nội dung không được phép ngắt + padding + đối tượng | Ràng buộc cứng nếu giá trị có thể xác minh |
| `soft_floor_i` | Mức rộng có thể chấp nhận khi text xuống dòng hợp lý | Không phải cam kết chuẩn pháp lý |
| `preferred_i` | Mức rộng đủ tốt để số dòng và chiều cao hàng hợp lý | Đích tối ưu mềm |
| `cap_i` | Mức trần hữu ích; mở rộng nữa ít cải thiện đọc hiểu | Tránh cấp rộng lãng phí |
| `P_i` | Ưu tiên ngữ nghĩa theo mục tiêu bảng | Trọng số thiệt hại khi khó đọc |
| `wrap_profile_i(w)` | Số dòng ước lượng theo các ứng viên chiều rộng `w` | Tính chi phí khi tăng/giảm mm |
| `risk_flags_i` | Mã dài, ngày, chữ ký, ảnh, field, ô gộp, bảo vệ | Chặn hoặc tăng mức phê duyệt |

**Khuyến nghị thống kê nội dung:** không cấp chiều rộng cột theo giá trị dài nhất một cách mù quáng. Với đoạn văn có thể ngắt, đo các phân vị độ rộng/chiều cao ở `P50`, `P90` và `P95` của các hàng thực tế; nhưng **không dùng phân vị để bỏ qua bất kỳ giá trị bắt buộc phải hiển thị nguyên vẹn nào**. Hàng ngoại lệ dài bất thường phải được cảnh báo riêng. Phân vị là kỹ thuật thiết kế đề xuất, không phải thông số ISO/OOXML.

`hard_floor_i` có thể lớn hơn toàn bộ vùng chữ nếu xuất hiện URL/mã không được bẻ hoặc hình ảnh quá rộng. **Không tự coi đó là lý do để xóa/ký tự xuống dòng mã.** Khi không có nghiệm an toàn, trả `REVIEW_REQUIRED` cùng danh sách ô gây xung đột.

### 72.3. Đặt mục tiêu số dòng khác nhau theo vai trò

| Vai trò | Kỳ vọng ban đầu [KN] | Ghi chú |
|---|---|---|
| STT, ngày ngắn, trạng thái ngắn, số thông thường | 1 dòng nếu khả thi | Nếu không vừa, yêu cầu xem xét bố cục |
| Mã, số văn bản, định danh | 1 dòng; không ngắt tại điểm không được phép | Bảo toàn ký tự/định dạng |
| Tên cơ quan, người, địa danh | Thường 1–2 dòng | Tránh mỗi dòng chỉ 1–2 từ vụn |
| Nội dung nhiệm vụ/công việc | Thường 2–4 dòng, tùy độ dài thực | Không cắt bớt câu |
| Ghi chú/nội dung hỗ trợ dài | Có thể nhiều hơn | Tránh đẩy chiều cao hàng cực đoan |
| Tiêu đề cột | Thường 1–2 dòng | Có thể dài hơn nếu bắt buộc |

Các khoảng 1–2/2–4 dòng chỉ để khởi tạo thuật toán. Đối với cột diễn giải dài, một ô có thể cần 6–10 dòng hợp lệ; không đặt `maxLines` để **cắt** dữ liệu như trong giao diện web.

## 73. Mô hình tối ưu phân bổ chiều rộng theo trọng tâm

### 73.1. Ràng buộc bất khả xâm phạm

Giả sử bảng có `n` cột lưới thực `w_1 … w_n`, vùng hữu dụng `W`. Ứng viên chỉ được xét khi:

1. `w_i ≥ hard_floor_i` với những ràng buộc cứng đã xác nhận; ràng buộc không chắc chắn phải ghi trạng thái.
2. `sum(w_i) ≤ W` (trừ khi có bố cục theo mẫu/bảng nổi được phép với logic khác).
3. Với mỗi ô gộp trải qua các cột `a … b`: `sum(w_a … w_b) ≥ merged_content_floor` theo ràng buộc nội dung của **ô thực**, không nhân bản nội dung qua ô lưới.
4. Không thay đổi grid topology, thứ tự ô, nội dung, ký tự, định dạng con số, công thức, hyperlink, field, ảnh hoặc phạm vi không được phép sửa.
5. Không thay đổi kích thước chữ/lề/hướng trang để hợp thức hóa một nghiệm nếu quy tắc pháp lý và sự cho phép không bảo đảm.
6. Các cột đã khóa theo mẫu, người dùng hoặc thành phần dàn trang là **không gian cố định** (`locked_width_i`).

Nếu `sum(hard_floor_i)` cộng các điều kiện ô gộp tạo hệ vô nghiệm: trả `NO_FEASIBLE_LAYOUT`; đề xuất bước xử lý theo Mục 46 chứ không ép bảng bằng giá nào cũng vừa.

### 73.2. Hàm mục tiêu thiết kế (heuristic — không phải đặc tả Word)

Một cách đánh giá ứng viên `w`:

```
Cost(w) =
    α × Σ[ semantic_priority_i × wrap_discomfort_i(w) ]
  + β × Σ[ row_height_excess_r(w) ]
  + γ × Σ[ numeric_or_identifier_break_penalty_i(w) ]
  + δ × Σ[ header_fragmentation_i(w) ]
  + ε × Σ[ |w_i - original_width_i| / W ]
  + ζ × wasted_space_penalty(w)
```

- `wrap_discomfort`: số lần ngắt/độ khó đọc, phạt mạnh khi dòng quá ngắn hoặc chia ngắt tên/mã; không đánh đồng *bất kỳ* xuống dòng nào cũng xấu.
- `row_height_excess`: xét **chiều cao hàng lớn nhất** trong các ô mỗi hàng, không cộng lặp chiều cao từng ô như thể là các hàng riêng.
- `numeric_or_identifier_break_penalty`: rất lớn hoặc được chuyển thành ràng buộc cứng với định danh, giá trị số/đơn vị cần hiển thị nguyên vẹn.
- `header_fragmentation`: phạt tiêu đề cột bị chia thành nhiều dòng lẻ, nhưng không cho tiêu đề dài đẩy tất cả dữ liệu vào cột hẹp.
- `original_width` penalty: giữ mức thay đổi nhỏ, có thể rollback; được ưu tiên tăng lên khi bảng vốn đã đẹp.
- `wasted_space`: giảm tỷ lệ cột được nới ra nhưng không cải thiện việc đọc.

Các hệ số `α...ζ` **không được cố định tùy tiện thành chuẩn chung**. Phải thử nghiệm, ghi bản cấu hình và hiệu chỉnh theo nhóm bảng. Chi phí chỉ xếp hạng các ứng viên **đã đạt mọi ràng buộc cứng**.

### 73.3. Cách giải dễ triển khai, ưu tiên reuse

**Phương án khả thi trước:** dùng các primitive đọc đo chiều rộng, wrap và cập nhật `w:tblGrid`/`w:tcW` mà bộ xử lý hiện tại đã có, trước khi xem xét solver. Quy trình đề xuất:

```text
INPUT: table, section_geometry, legal_profile, user_authorization
1  classify table; if FORM_RESERVED/LAYOUT/UNSUPPORTED -> PRESERVE_OR_REVIEW
2  extract real grid, merged constraints, effective styles, values, caption/context
3  infer reading task and column roles from deterministic rules + user override
4  measure hard_floor, soft_floor, preferred, optional cap and wrap curves
5  if existing layout passes quality gates -> KEEP_EXISTING
6  allocate required floors; check W, locked widths and all merged constraints
7  propose candidates by increasing widths where *marginal benefit per mm* is highest
8  shrink only eligible flexible columns, never breach hard floors
9  compare costs, penalties, number of pages and width change against baseline
10 preview candidate in compatible renderer; reject if overflow/clipping/new harm
11 require scope-specific approval; apply minimum format-only properties
12 reopen DOCX; compare content/topology/relationships and final render
OUTPUT: KEEP_EXISTING / PROPOSED / REVIEW_REQUIRED /
        NO_FEASIBLE_LAYOUT / VISUAL_NOT_VERIFIED / PASS
```

**Giải thích bước 7 (water-filling/greedy có kiểm chứng):** chia phần rộng còn lại thành các bước nhỏ theo độ chính xác dàn trang phù hợp (thí dụ 0,5–1 mm cho giai đoạn khảo sát, **không phải chuẩn bắt buộc**), giả lập tăng 1 bước cho các cột còn đủ điều kiện; tính mức giảm `Cost` trên mỗi mm; cấp cho cột có lợi ích biên lớn nhất. Khi mọi lợi ích thấp hoặc bảng đã hợp lý thì dừng, **không ép lấp toàn bộ `W`**. Với ô gộp và tương tác giữa cột, greedy có thể kẹt cực trị cục bộ; dùng so sánh nhiều ứng viên hoặc phương pháp tối ưu chính xác hơn *nếu* bộ kiểm thử cho thấy cần thiết.

**Trình tự ưu tiên quyết định:** bảo vệ cột bắt buộc → đảm bảo các nhãn/giá trị quan trọng đọc được → cấp không gian có lợi ích biên cao → giảm chiều cao hàng vô ích → hạn chế thay đổi so với bản gốc → kiểm chứng render. Không cấp mm theo `P_i/sum(P)`.

### 73.4. Nút chặn tự động

| Điều kiện | Hành vi an toàn |
|---|---|
| Đã đạt hình thức tốt, không tràn | `KEEP_EXISTING`; không sửa chỉ vì thuật toán có nghiệm điểm cao hơn chút ít |
| Định danh/giá trị cốt lõi bị cắt hoặc xuống dòng khó hiểu | Đề xuất tăng đúng cột đó trước |
| Tổng sàn cột lớn hơn W | `NO_FEASIBLE_LAYOUT`; không thu nhỏ font trái quy định |
| Bảng có ô gộp/lồng mà solver chưa hiểu topology | `REVIEW_REQUIRED`; không làm phẳng lưới |
| Mục tiêu bảng/ưu tiên cột còn mơ hồ | Giữ nguyên hoặc trình bày đề xuất chờ xác nhận |
| Bảng biểu mẫu được phê duyệt | `PRESERVE_OFFICIAL_FORM` |
| Chỉ có XML sau sửa, chưa có render | `VISUAL_NOT_VERIFIED` |
| Thay width làm tăng số trang/đẩy chữ ký không mong muốn | So sánh phương án; từ chối ứng viên nếu ảnh hưởng vượt phạm vi |

## 74. Ví dụ phân bổ theo trọng tâm – số liệu minh họa, chưa nghiệm thu

### 74.1. Bảng theo dõi nhiệm vụ

**Mục tiêu:** Lãnh đạo muốn đọc được *công việc nào*, *ai phụ trách*, *khi nào đến hạn*. `W_usable = 165 mm` chỉ là giả định minh họa tương ứng một cấu hình A4 dọc, **không áp cho mọi section**.

| Cột | Ý nghĩa | Ưu tiên nghĩa (minh họa) | Đề xuất khởi đầu | Lý do |
|---|---|---:|---:|---|
| STT | Định vị trong bảng | 35/100 | 12 mm | Ít chữ; đủ cho chỉ số lớn nhất |
| Nội dung công việc | Thông tin hành động chính | 95/100 | 72 mm | Dài và chứa nội dung quyết định |
| Đơn vị chủ trì | Trách nhiệm | 85/100 | 41 mm | Tên riêng, cần tránh ngắt vụn |
| Hạn hoàn thành | Thời điểm | 90/100 | 24 mm | Rất quan trọng nhưng ngắn; ưu tiên 1 dòng nếu phù hợp font |
| Ghi chú | Thông tin phụ | 30/100 | 16 mm | Có thể xuống dòng, không được cắt chữ |
| **Tổng** |  |  | **165 mm** | Chỉ là ứng viên cần đo/render kiểm chứng |

Điểm then chốt: **Hạn hoàn thành có độ ưu tiên nghĩa cao hơn Đơn vị nhưng được cấp ít mm hơn**, vì nhu cầu trình bày nhỏ hơn. Nếu giá trị ngày thực tế, padding hoặc font khiến 24 mm không đủ, phải điều chỉnh nghiệm thay vì tuyên bố “24 mm là chuẩn”. Nếu cột Ghi chú trở thành 8–10 dòng/hàng và kéo dài quá nhiều trang, phải tăng chi phí đó trong hàm mục tiêu, không cố giữ 16 mm.

### 74.2. Bảng so sánh thống kê

| Cột | Yêu cầu | Điều kiện được coi là tốt |
|---|---|---|
| Chỉ tiêu | Nhận diện nhóm cần so sánh | Không bẻ mỗi chữ thành một dòng; đủ rộng cho tên chỉ tiêu |
| Năm 2024 | Số liệu | Căn phải, không thay đơn vị/độ chính xác |
| Năm 2025 | Số liệu | Độ rộng tương đương cột 2024 nếu cùng định dạng dữ liệu |
| Thay đổi | Chỉ số so sánh chính | Không tách dấu +/- khỏi số, đơn vị phải rõ |
| Ghi chú | Ngoại lệ/nguồn | Cho phép xuống dòng, không lấn phần số liệu |

**Nội dung trọng tâm:** cặp cột 2024/2025 và *Thay đổi* giúp so sánh, nhưng độ rộng không nhất thiết lớn hơn cột nhãn *Chỉ tiêu*. Ưu tiên giảm khoảng cách quét mắt giữa các số và giữ hàng tổng cộng liên tục. Không tự sắp xếp lại các cột trong tài liệu đã có.

### 74.3. Bảng danh bạ/tra cứu

**Trường trọng tâm** thường là tên đơn vị/người, địa bàn và thông tin phân biệt đúng đối tượng; mã ngắn có thể quan trọng về pháp lý nhưng nên hẹp vừa đủ. Một ô địa chỉ dài không nhất thiết được nhận toàn bộ vùng còn lại nếu bảng chủ yếu dùng tra cứu tên và số liên hệ. Không được loại bỏ phần địa chỉ chỉ để giảm số trang.

### 74.4. Bảng biểu mẫu cố định, ký xác nhận hoặc nhiều tầng tiêu đề

Ưu tiên ngữ nghĩa **không cho phép** thay tỷ lệ cột mẫu. Với `FORM_RESERVED`, `gridSpan`, `vMerge`, ô trống có chức năng, vùng xác nhận/ký, giải pháp mặc định là `PRESERVE` hoặc `MANUAL_REVIEW`. Muốn chỉnh, cần căn cứ mẫu, quyền sửa và proof chính xác cho *mỗi* cấu trúc liên quan. Bảng nhiều tầng tiêu đề chỉ tối ưu trên **lưới thật** và phải đáp ứng các ràng buộc span; không chia độ rộng căn cứ số lượng ô nhìn thấy ở một hàng.

## 75. Áp dụng theo 3 mức can thiệp thay vì một thao tác “AutoFit”

| Mức | Phạm vi | Có thể tự động? | Minh chứng bắt buộc |
|---|---|---|---|
| **L0 – Preserve** | Bảng đã đọc tốt, biểu mẫu, bảng dàn trang, hoặc không đủ thông tin | Không thay đổi | Audit lý do giữ nguyên |
| **L1 – Safe suggestion** | Đề xuất cột cần nới/thu, không thay cấu trúc; đưa mm/% minh họa | Có thể tự tạo **đề xuất**, không áp vô điều kiện | Vai trò cột, nhu cầu mm, rủi ro, độ tin cậy |
| **L2 – Approved format-only** | Cập nhật độ rộng trong giới hạn quyền sửa, không đổi dữ liệu/ô gộp/section | Chỉ khi được phép và đo kiểm | Snapshot trước/sau + render + reopen |

**Không thuộc L2:** thay thứ tự cột, đổi tên tiêu đề, rút gọn nội dung, thêm/tách bảng, đổi chữ ký, đổi hướng trang làm ảnh hưởng section, đổi đơn vị/số liệu. Những thao tác này là thay đổi cấu trúc/biên tập, đòi hỏi yêu cầu độc lập.

## 76. Reuse First: nghiên cứu thực hành và thư viện hiện có

| Nguồn | Thành phần tái sử dụng về mặt ý tưởng | Giới hạn / quyết định |
|---|---|---|
| **Microsoft Word/OOXML** [S08], [S20], [S29]–[S31] | AutoFit, fixed width, preferred widths, layout grid và ràng buộc min/max content | **Authority cho dàn trang DOCX**; xem là điểm xuất phát, cần render thực tế |
| **python-docx** [S22], [S38] | Cách hiểu grid, merged/omitted cells; đọc cấu trúc bảng | Không tự thay engine của dự án; chỉ tham khảo đặc tả nếu stack không phải Python |
| **Rich (Textualize)** [S35] | Các tham số `min_width`, `max_width`, `ratio`, `no_wrap`, đo nội dung và thu cột có điều kiện | MIT; engine cho terminal, **không có nghĩa là renderer Word/OOXML**; chỉ tái sử dụng pattern |
| **PrettyTable** [S36] | `min_width`, `max_width`, căn cột, width theo header/content | BSD-3-Clause; bảng ký tự terminal; không thêm dependency vào DOCX chỉ vì thuật toán tương tự |
| **W3C CSS Tables Level 3** [S32] | Hệ khái niệm min-content/max-content, phân phối không gian khả dụng | Là mô hình Web/CSS, **không được coi là thuật toán Word** |
| **NN/g – Data Tables** [S33], **VA.gov** [S34] | Tác vụ người đọc, định danh, ưu tiên thông tin | Chỉ là UX evidence, không thay quy định/mẫu hành chính Việt Nam |

**Quyết định khuyến nghị:** chỉ tích hợp chức năng có sẵn của bộ xử lý DOCX/renderer; dùng các thư viện và nghiên cứu ở trên làm chuẩn so sánh/ý tưởng **chứ không thêm solver/framework/dependency mới trước khi có bằng chứng thiếu năng lực**. Nếu phải viết code, chỉ bổ sung policy/adapter tính độ rộng cho cột trên cấu trúc hiện có, không dựng một parser hay renderer DOCX thứ hai. Chưa audit repo/HEAD cụ thể trong phạm vi lần cập nhật tài liệu này, do đó **không tuyên bố** rằng hệ thống hiện tại đã có hoặc đã thiếu các capability nêu trên.

## 77. Mô hình bằng chứng và giải thích quyết định cột

Mỗi đề xuất tối ưu phải có thể truy vết:

```yaml
# Ví dụ dữ liệu giải thích (đặc tả, KHÔNG phải schema đang triển khai)
table_id: "body/table-03"
objective: "ACTION"
objective_confidence: "HIGH"
usable_width_mm: 165.0
layout: "candidate_fixed_after_measurement"
columns:
  - column: 1
    header: "Nội dung công việc"
    semantic_role: "PRIMARY_CONTENT"
    priority_score: 95
    initial_width_mm: 60.0
    hard_floor_mm: 30.0
    proposed_width_mm: 72.0
    reasons:
      - "Chứa hành động chính"
      - "Bố cục ban đầu xuống dòng quá nhiều"
  - column: 3
    header: "Hạn hoàn thành"
    semantic_role: "DEADLINE"
    priority_score: 90
    initial_width_mm: 18.0
    hard_floor_mm: null  # chưa đo đủ để chứng nhận
    proposed_width_mm: 24.0
    reasons:
      - "Nên đọc ngày trên một dòng nếu renderer xác nhận đủ chỗ"
constraints:
  preserve_text: true
  preserve_merge_topology: true
  no_section_change: true
approval_required: true
verification: "VISUAL_NOT_VERIFIED"
```

Các cột minh họa ở YAML không phải tập đủ của bảng ví dụ mục 74.1; đây chỉ là một bản ghi giải thích rút gọn. Không cho phép engine biến trường `hard_floor_mm: null` thành 0 mm hoặc kết luận đề xuất hợp lệ khi chưa có dữ liệu đo.

Đầu ra gợi ý người dùng gồm: **tại sao cột được ưu tiên**, cột nào bị thu hẹp, **giảm/tăng mm bao nhiêu**, thay đổi số dòng/số trang dự kiến, cảnh báo và ảnh trước–sau. Người dùng phải có khả năng **giữ nguyên**, **chỉnh tay ưu tiên cột**, hoặc **từ chối** đề xuất.

## 78. Kiểm thử riêng cho lựa chọn cột trọng tâm và điều kiện PASS

### 78.1. Bộ test đề xuất bổ sung T31–T52

| ID | Tình huống | Kết quả kỳ vọng |
|---|---|---|
| T31 | Cột ghi chú dài nhất nhưng không phải nội dung trọng tâm | Không tự cấp lớn nhất chỉ dựa số ký tự |
| T32 | Cột hạn chỉ có ngày nhưng nghiệp vụ rất quan trọng | Độ ưu tiên cao; chiều rộng vừa đủ, ưu tiên 1 dòng |
| T33 | Cột định danh `0000001234` dài, không có dấu cách | Không thay số 0, không cắt/mất mã |
| T34 | Tiêu đề cột dài nhưng tất cả giá trị rất ngắn | Cho phép cân nhắc xuống dòng header; không lãng phí cả cột |
| T35 | Một ô ngoại lệ gấp 20 lần dữ liệu bình thường | Dùng phân vị để khởi tạo nhưng giữ đầy đủ ngoại lệ, cảnh báo nếu không vừa |
| T36 | Nội dung tiếng Việt có dấu tổ hợp và run đậm/nghiêng | Đo theo font hiệu dụng; không tuyên bố mm chuẩn chỉ từ số ký tự |
| T37 | Hai cột số cùng đơn vị/năm, số chữ số khác nhau | Giữ khả năng so sánh và căn phải; không làm tròn |
| T38 | Bảng ACTION đặt mục tiêu theo người dùng khác bảng LOOKUP | Mapping ưu tiên thay theo mục tiêu; không đổi dữ liệu |
| T39 | Bảng chưa có tên, header mơ hồ | `LOW` confidence và `REVIEW_REQUIRED/KEEP_EXISTING` |
| T40 | Bảng được user đánh dấu cột A là tối quan trọng | Giữ override người dùng trước heuristic |
| T41 | Bảng ô gộp ngang spanning 3 cột | Ràng buộc tổng mm, không nhân bản text ô gộp |
| T42 | Gộp dọc/ô lược bỏ, lưới không đều | Không làm phẳng bảng để đo hoặc áp width |
| T43 | Bảng có ảnh, mã QR, đối tượng không thể co | Không ép đối tượng hay làm sai tỷ lệ |
| T44 | Tổng `hard_floor` lớn hơn W | `NO_FEASIBLE_LAYOUT`, không ép thu cỡ chữ |
| T45 | Một bảng vốn đang đẹp và không tràn | `KEEP_EXISTING`, idempotent |
| T46 | Đề xuất cải thiện wrap nhưng làm tăng số trang ngoài mong muốn | Không chấp nhận nếu mục tiêu và giới hạn không cho phép |
| T47 | Word AutoFit khác kết quả sơ bộ HTML/CSS | Word render là bằng chứng quyết định khi đầu ra là DOCX Word |
| T48 | Không có môi trường render Word tương thích | `VISUAL_NOT_VERIFIED`, không cấp PASS thẩm mỹ |
| T49 | Có biểu mẫu pháp lý, vùng ký và ô nhập | Không áp thuật toán căn tự do; preserve |
| T50 | Cột numeric 1 dòng, narrative nhiều dòng có bố cục cân | Không gượng ép số dòng bằng nhau |
| T51 | Người dùng chỉ phê duyệt bảng số 3 | Không sửa bảng số 1, 2, 4 và style dùng chung |
| T52 | Chạy tối ưu hai lần trên cùng cấu hình | Lần 2 không phát sinh layout churn |

### 78.2. Tiêu chí nghiệm thu V3

- **Hard gates PASS:** không mất/đổi nội dung, thứ tự cell, topology, công thức/field, đối tượng, biểu mẫu; không vi phạm cài đặt pháp lý/authority; không clipping/overflow trong bản render kiểm chứng.
- **Visual gates PASS:** cột quan trọng đọc được, số/ID/ngày hiển thị rõ, xuống dòng có chủ đích, bảng không tăng số trang một cách không kiểm soát, phù hợp phong cách hành chính/Đảng.
- **Algorithm evidence:** lưu `objective`, `column_roles`, `P_i`, `hard_floor`, `preferred`, `w_original`, `w_new`, risk và giải thích từng sửa đổi; riêng bảng phức tạp phải có snapshot grid spans.
- **Regression scope:** chỉ thử lại bảng/section thực sự thay đổi và hợp đồng ảnh hưởng trực tiếp; tận dụng các phép thử không bị ảnh hưởng đã PASS; không tự mở khóa core/đổi engine.
- **Công bố mức chứng cứ:** khi chỉ có đề xuất chưa có renderer, đánh dấu `PROPOSED_NOT_VERIFIED`; không tuyên bố đã đạt tối ưu hay đã triển khai tính năng.

## 79. Khuyến nghị cuối cùng về chiến lược tối ưu độ rộng

**Định nghĩa thực dụng:** cột được coi là đã tối ưu khi **rộng đủ để giữ ý nghĩa và đọc tốt các dữ liệu quan trọng, không chiếm thêm không gian mà lợi ích thị giác không tương xứng, và việc phân bổ không làm xấu các cột khác hoặc ảnh hưởng bố cục trang**.

1. Xác định **người đọc muốn làm gì** trước khi xem độ dài cột.
2. Bảo vệ **cột nhận diện, cột điều hành, cột so sánh, cột đánh giá** theo từng mục đích; nhưng cấp mm theo **nhu cầu hình học và lợi ích biên**, không theo điểm ngữ nghĩa tuyệt đối.
3. Cho phép **cột hỗ trợ nhiều chữ xuống dòng** nhưng không cắt nội dung; không “hy sinh” cột nào tới mức khó đọc.
4. Tối ưu trên **lưới Word thực + section thực + định dạng hiệu dụng**, không trên ma trận text đã làm phẳng.
5. Nếu không có nghiệm tuân thủ và dễ đọc, ưu tiên **báo cần xem xét** thay vì sửa trái phép định dạng, đổi số liệu, rút chữ hoặc xoay trang ảnh hưởng cấu trúc.
6. Ưu tiên **không sửa nếu chưa chứng minh cần sửa**. Đầu ra cuối phải được mở lại, kiểm chứng cấu trúc và kết xuất trực quan.

---


# PHẦN XX. NÂNG CẤP V4 — CHẤT LƯỢNG QUYẾT ĐỊNH, TỐI ƯU TOÀN BẢNG VÀ NGHIỆM THU BẰNG CHỨNG

> **Phạm vi phần bổ sung:** Kế thừa Phần I–XIX và các phụ lục của V3. Phần này không thay thế căn cứ pháp lý, không ấn định thông số thẩm mỹ thành nghĩa vụ bắt buộc và không khẳng định thuật toán đã được triển khai. Các công thức, ngưỡng và ví dụ dưới đây là **đặc tả thiết kế/khuyến nghị [KN]/[KT]**, cần được kiểm định trên DOCX và bộ kết xuất đích. Đối với tài liệu đã có bố cục tốt, kết quả tối ưu hợp lệ nhất có thể là **không thay đổi gì**.

## 80. Phân tích khoảng trống của V3 và quyết định cải tiến

V3 đã tách `semantic_priority` khỏi `expansion_need`, có ràng buộc `hard_floor`, xét ô gộp và yêu cầu render verification. V4 bổ sung lớp ra quyết định **toàn bảng/toàn trang** để khắc phục sáu khoảng trống thực tiễn:

| Khoảng trống cần lấp | Vì sao ảnh hưởng kết quả? | Bổ sung V4 |
|---|---|---|
| Đánh giá từng cột riêng lẻ | Tăng 5 mm cho cột A có thể buộc cột B thu hẹp; tổng số dòng tăng | Đánh giá **đồng thời** toàn bộ vector độ rộng |
| Đếm dòng trên từng ô | Chiều cao hàng phụ thuộc ô cao nhất; giảm dòng ở ô không chi phối hàng có thể không ích lợi | **Row bottleneck** và đánh giá chiều cao hàng |
| Chỉ ước lượng tổng chiều cao bảng | Bảng còn tương tác với caption, section, page header/footer, bảng trước/sau | Đánh giá **phân trang toàn vùng bị ảnh hưởng** |
| Xếp hạng điểm số thẩm mỹ | Một thay đổi nhỏ có thể gây clipping hoặc đổi số trang | **Hard gate + thứ tự ưu tiên quyết định**, rồi mới chấm điểm mềm |
| Diễn giải `HIGH/MEDIUM/LOW` như độ tin cậy tự nhiên | Không có tập kiểm định nên mức đó chưa phải xác suất chính xác | Tách **độ chắc chứng cứ** và **rủi ro thay đổi** |
| Tối ưu nhiều lần gây layout churn | Sai số làm tròn, style cascade, AutoFit có thể khiến độ rộng dao động | Chuẩn twip, mức cải thiện tối thiểu, **idempotence** |

**Sửa cách hiểu:** `P_i` là mức quan trọng của thông tin, không phải tỷ lệ chiều rộng. `hard_floor` là điều kiện chưa chắc đo chính xác được bằng font engine khác Word. Số trang ít hơn **không phải luôn tốt hơn** nếu phá bố cục, cấu trúc phụ lục hoặc khả năng đọc. [S41]–[S45].

## 81. Xác định trọng tâm bằng chứng cứ và tác vụ đọc: phương pháp có thể giải thích

### 81.1. Bốn câu hỏi phải trả lời trước khi đổi độ rộng

1. **Người đọc đang giải quyết tác vụ gì?** Tra cứu ai/cái gì; tìm người chịu trách nhiệm; tìm hạn xử lý; so sánh số liệu; đọc kết luận; hay điền mẫu?
2. **Dữ liệu nào không thể đọc sai?** Mã, ngày, số tiền, trạng thái, đơn vị, tiêu chí quyết định và điều kiện pháp lý.
3. **Đâu là nội dung chiếm không gian nhưng có thể xuống dòng?** Diễn giải, ghi chú, căn cứ dài, địa chỉ; không mặc định coi tất cả văn bản dài là ít quan trọng.
4. **Phần nào đang quyết định chiều cao hàng và thời điểm ngắt trang?** Kiểm tra từng hàng sau khi đo, không chỉ xét cột tổng quát.

Đề xuất cấu trúc bằng chứng `taskEvidence` (không phải schema triển khai):

```yaml
taskEvidence:
  document_kind: ADMINISTRATIVE | PARTY | OTHER | UNKNOWN
  table_kind: ACTION | LOOKUP | COMPARE | SUMMARY | DECISION | FORM | UNKNOWN
  task_source: USER_OVERRIDE | OFFICIAL_FORM | CAPTION_CONTEXT | HEADER_STRUCTURE | DATA_PROFILE | UNKNOWN
  source_location: "định danh vị trí trong tài liệu, không sao chép nội dung bí mật"
  column_role_evidence:
    - column: 1
      role: STRUCTURAL_INDEX
      why: "tiêu đề STT; dữ liệu nguyên ngắn"
    - column: 2
      role: PRIMARY_CONTENT
      why: "nội dung hành động phải thực hiện"
  evidence_grade: EXPLICIT | INFERRED_STRONG | INFERRED_WEAK | UNRESOLVED
  layout_risk: LOW | MEDIUM | HIGH | BLOCKED
```

**Quy tắc quan trọng:** `evidence_grade` nói về **căn cứ nhận định**, `layout_risk` nói về **khả năng gây tác động ngoài ý muốn**. Hai thuộc tính khác nhau; không gom vào một con số confidence. Chẳng hạn người dùng chỉ rõ “cột Hạn là trọng tâm” (`EXPLICIT`), nhưng bảng có ô gộp phức tạp (`HIGH`) thì vẫn phải trình duyệt trước khi đổi độ rộng.

### 81.2. Cách phân xử khi các dấu hiệu xung đột

Thứ tự ưu tiên: **biểu mẫu/điều kiện bắt buộc** → **yêu cầu rõ của người dùng** trong giới hạn pháp lý → **tiêu đề bảng và đoạn giải thích có provenance** → **cấu trúc nhiều hàng tiêu đề** → **phân bố dữ liệu**. Không dùng mô hình ngôn ngữ làm nguồn chân lý cho các phép tính hình học, kiểm tra luật, tính toán số cột hoặc kiểm tra tính nguyên vẹn.

Bảng nhiều cấp phải lấy nhãn theo **đường dẫn tiêu đề** (ví dụ `Kế hoạch > 2025 > Giá trị`), tránh nhìn một nhãn `2025` rồi kết luận mọi cột thuộc nhóm có ý nghĩa như nhau. Nếu không dựng được quan hệ nhãn do ô gộp bất thường, đưa bảng vào `REVIEW_REQUIRED`, không cho thay đổi tự động.

### 81.3. Cột trọng tâm không nhất thiết là cột lớn nhất

| Vai trò | Thông tin được bảo vệ | Cách cấp không gian |
|---|---|---|
| Hạn xử lý | Nguyên giá trị ngày, dễ quét theo hàng | Đủ một dòng trong khả năng; sau đó **dừng mở rộng** |
| Số tiền/số liệu | Dấu, chữ số, đơn vị và căn phải | Đủ nguyên trị và tiêu đề hợp lý; không cấp thêm khi hết lợi ích |
| Tên/cơ quan | Không chia vụn, không làm nhầm đối tượng | Đủ cho nhịp đọc thường 1–2 dòng; ưu tiên so với ghi chú |
| Nội dung hành động | Đủ ngữ cảnh để hiểu việc, không mơ hồ | Nhận phần dư nếu giảm được chiều cao hàng đáng kể |
| Ghi chú phụ | Đọc trọn vẹn nhưng có thể xuống dòng | Thường nhận diện là **nguồn có thể co**, không cắt chữ |
| Cột theo mẫu đã duyệt | Khớp hình thức và không gian dành cho nhập/ký | **Khóa width**; không áp tối ưu tự do |

Tài liệu UX về bảng khuyến nghị xác định tác vụ người đọc và đặt định danh có ý nghĩa ở vị trí dễ tìm; đây là cơ sở ưu tiên thông tin, không phải quy tắc sắp xếp lại cột trong tài liệu hành chính đã ban hành. [S45].

## 82. Tối ưu phải xét nút thắt của hàng và tác động phân trang

### 82.1. Chiều cao hàng là `max`, không phải tổng chiều cao các ô

Với hàng `r`, đặt `h_{r,i}(w)` là chiều cao dự kiến của ô bắt đầu/chiếm vùng cột `i` ở vector width `w`. Với hàng thông thường, mô hình sàng lọc:

\[
\widehat H_r(w) \approx \max_i h_{r,i}(w) + \operatorname{rowOverhead}_r.
\]

Trong hàng chứa ô gộp dọc, ô lồng bảng, chiều cao cố định hoặc trường dữ liệu, công thức trên chỉ là **ước lượng**, phải chuyển sang xử lý theo quan hệ row-span/nhóm hàng hoặc render thật. Tổng chiều cao bảng ước lượng `\widehat H_{table}` chịu ảnh hưởng padding, đường viền, spacing, yêu cầu giữ cùng hàng và cấu hình style; **không thể chỉ bằng `Σ ký tự/cột`**.

Ví dụ minh họa: một hàng có ô Nội dung cao 4 dòng và ô Ghi chú cao 8 dòng. Nếu tăng độ rộng Nội dung làm giảm từ 4 còn 3 dòng nhưng Ghi chú vẫn 8 dòng, chiều cao hàng **không giảm**. Nếu cùng lượng mm đó chuyển sang Ghi chú để giảm 8 xuống 5 dòng, hàng có thể thấp đi đáng kể. Trọng số ưu tiên của Nội dung vẫn cao hơn, nhưng lợi ích hình học từ mở rộng nó ở thời điểm này thấp.

### 82.2. Thuật ngữ mới: `row_bottleneck` và `page_boundary_sensitivity`

- `row_bottleneck`: ô hoặc cụm ô thực đang quyết định chiều cao hàng; có thể có nhiều ô đồng mức.
- `marginal_height_gain(i, δ)`: chiều cao hàng/bảng giảm khi cấp thêm `δ` twip cho cột `i`, **sau khi thu lại từ cột khác hợp lệ**.
- `page_boundary_sensitivity`: ứng viên khiến hàng/caption gần ranh giới trang chuyển sang trang khác, làm thay đổi số trang hoặc làm tiêu đề rơi riêng.
- `page_critical_row`: hàng mà thay đổi cao vài mm khiến toàn bảng phân trang khác đáng kể.

Các chỉ số trên là **khái niệm chẩn đoán đề xuất**, không phải thuộc tính WordprocessingML.

### 82.3. Kiểm chứng bố cục không chỉ trong phạm vi bảng

Cần phân biệt ba vòng ảnh hưởng:

1. **Table local:** số dòng, cắt chữ, căn, width và kích thước từng hàng.
2. **Section local:** vị trí bảng, caption/đoạn trước và sau, header/footer, vùng in của section, cột trang, hướng trang, thay đổi vị trí ngắt trang.
3. **Document downstream:** thay đổi số trang có thể khiến phần ký, nơi nhận, phụ lục sau bảng hoặc tham chiếu số trang dịch chuyển. Không được tuyên bố các phần này không ảnh hưởng nếu chưa so sánh.

Tối ưu một bảng có thể được áp dụng phạm vi hẹp về **mã sửa**, nhưng phạm vi **kiểm tra render** phải mở rộng đến phần văn bản thực sự bị dịch chuyển sau bảng. Không cần chạy lại toàn bộ test hệ thống nếu không có dấu hiệu lan truyền; tuy nhiên không giới hạn việc kiểm chứng chỉ trong bounding box bảng khi các trang sau có thể thay đổi.

## 83. Bài toán chọn độ rộng: khả thi, có lợi, và ít xáo trộn

### 83.1. Cách tiếp cận hai tầng và nguyên tắc từ chối nghiệm

**Tầng 1 — Hard gates (bắt buộc):** đúng quy định/mẫu; giữ nội dung và cấu trúc; không clipping/tràn vùng cho phép; không bị sửa ngoài vùng; không thay đổi số liệu; không vi phạm khóa ô/cột/section; có sự cho phép áp dụng.

**Tầng 2 — Soft comparison (khi tất cả hard gates PASS):** đọc nhanh thông tin quan trọng, chiều cao hàng/bảng, số dòng khó đọc, độ nhất quán, số trang/hệ quả phân trang, độ lớn thay đổi so với gốc. Ứng viên thua bố cục gốc hoặc có lợi ích không đáng kể nên được giữ ở chế độ `KEEP_EXISTING`.

Không dùng một tổng điểm để bù trừ lỗi nghiêm trọng (ví dụ +20 điểm thẩm mỹ không thể bù -1 lỗi mất chữ). Nếu thiếu bằng chứng bản kết xuất, trạng thái là `VISUAL_NOT_VERIFIED`, không phải `PASS`.

### 83.2. Hàm mục tiêu theo thứ tự từ điển (lexicographic)

Thay vì mặc định gán trọng số cộng tuyến tính cho mọi tiêu chí, đề xuất dùng lớp ưu tiên:

1. `feasible(w)` — phải đạt toàn bộ hard gates; nếu không loại ngay.
2. `semantic_damage(w)` — tổn hại đối với giá trị, nhãn, thời hạn, định danh, nội dung quyết định.
3. `layout_damage(w)` — clipping, ngắt trang xấu, caption tách bảng, số trang tăng ngoài mục đích được duyệt.
4. `readability_cost(w)` — ngắt dòng vụn, quá nhiều dòng, tương phản và cân đối.
5. `change_cost(w)` — tổng độ dịch width so với gốc, số ô/cột cần chỉnh; ưu tiên thay đổi ít.

Với hai ứng viên cùng đạt hard gates và được coi là tương đương ở các bậc ưu tiên cao, dùng điểm số có trọng số **chỉ trong bậc cùng mức**, có công bố hệ số, không tự suy từ tên vai trò cột.

Một khung chấm điểm mềm minh họa để thử nghiệm (không quy phạm):

```text
semantic_damage = SUM over critical values [penalty_if_ambiguous_or_fragmented]
row_layout_cost = SUM over rows [overheight_penalty + row_break_penalty]
page_cost = [orphan_caption, orphan_header, unexpected_new_page, downstream_shift]
visual_cost = [awkward_wrap, ragged_cells, inconsistent_padding, wasted_whitespace]
change_cost = SUM abs(new_twips[i] - old_twips[i]) + affected_property_count
```

**Hiệu chuẩn:** không ấn định các trọng số/định mức thành tiêu chuẩn chính thức khi chưa có dữ liệu render và đánh giá của người biên tập. Không dùng mục tiêu giảm số trang tuyệt đối: bảng hai trang dễ đọc có thể tốt hơn bảng một trang bị ép sít hoặc giảm cỡ chữ trái chuẩn.

### 83.3. Pareto frontier và quy tắc chọn ứng viên

Không một tiêu chí đơn lẻ luôn thắng. Một ứng viên có thể giảm một trang nhưng tăng 40% thay đổi độ rộng; ứng viên khác giữ số trang và cải thiện cột trọng tâm. Duy trì một tập nhỏ các nghiệm **không bị lấn át (Pareto)** theo `semantic_damage`, `page_cost`, `readability_cost`, `change_cost`; nếu ứng viên A không kém B ở mọi tiêu chí và tốt hơn ít nhất một tiêu chí, loại B.

Chỉ trình người dùng tối đa **2–3 phương án có sự khác biệt thực chất** (ví dụ: Giữ nguyên; Cân đối nhẹ; Ưu tiên nội dung công việc), không đưa danh sách hàng chục tỷ lệ khó giải thích. Số `2–3` là đề xuất UI, không phải quy định Word.

## 84. Cách tìm ứng viên hiệu quả, không cần solver hoặc dependency mới

### 84.1. Giới hạn đầu vào trước khi tìm nghiệm

`effective_page_width` phải tính theo section **đang chứa bảng**, kiểu trang dọc/ngang, lề thực tế, bố trí nhiều cột, phần thụt bảng và thuộc tính table-positioning khi có. Vùng `W` không luôn bằng `pageWidth − leftMargin − rightMargin` nếu có cột văn bản, table indent, table floating, text wrapping hay bảng lồng trong ô.

Đọc đúng cấu trúc lưới thực (`tblGrid`, `gridCol`, `gridSpan`, `vMerge`, omitted leading/trailing cells), không nhân bản ô gộp thành các ô dữ liệu giả. `w:tblW` và `w:tcW` được hiểu là **preferred widths**; layout cuối cùng phải kiểm tra trong Word. [S41]–[S43].

### 84.2. Không để các phép đo giả gây khẳng định giả

Phân biệt ba loại số đo:

| Tín hiệu | Phương pháp | Được dùng để kết luận |
|---|---|---|
| `GEOMETRY_EXACT` | OOXML section/page/margin, locked widths, số grid columns | Ràng buộc cấu trúc và giới hạn hợp lệ theo đầu vào |
| `TEXT_ESTIMATED` | Font metrics/shaping không phải renderer Word | Tạo ứng viên, ước lượng xuống dòng; **không** cấp PASS hiển thị |
| `WORD_RENDER_VERIFIED` | Bản render thực tế từ Word/đích được chỉ định, so sánh trước–sau | Cấp PASS hiển thị trong môi trường kiểm chứng được ghi nhận |

Dữ liệu nhiều ký tự tiếng Việt có dấu tổ hợp, font fallback, kí hiệu đặc biệt hoặc trường nội dung động phải được xem là rủi ro đo sai cao hơn. Nếu `TEXT_ESTIMATED` bất định, cần tạo **khoảng ước lượng** thay vì một số mm chính xác giả.

### 84.3. Tìm kiếm cục bộ có giới hạn và khả năng dừng

Ưu tiên dùng engine đo và sửa có sẵn. Nếu thiếu bước chọn ứng viên, chỉ thêm một bộ tìm kiếm xác định nhỏ:

```text
INPUT: table_original, page_context, legal_profile, explicit_constraints, permission

A. Audit topology + ownership + table kind.
B. BLOCK: official/locked/unsupported/unknown section geometry -> preserve or review.
C. Baseline: record effective widths + original render status + affected pages.
D. Construct hard constraints from locked values, non-breakable content,
   images/objects and true merged spans (do not duplicate merged cell text).
E. Generate small candidate set from:
   - original layout (always include)
   - minimal change to fix actual overflow
   - role-aware width allocation
   - bounded pairwise swaps of width between eligible columns
   - allowed AutoFit comparison, if that feature is available and safe.
F. Normalize candidates to integer twips and deduplicate width vectors.
G. Reject candidates violating hard constraints; measure/estimate the rest.
H. Rank by semantic safety, row bottleneck, page effects, readability,
   and finally amount of change; keep only nondominated candidates.
I. Verify promising candidates with target renderer, compare to baseline.
J. If no verifiable and materially better candidate -> KEEP_EXISTING or REVIEW.
K. Apply only authorized table-local formatting; reopen DOCX; validate again.
OUTPUT: decision, reason, per-column explanation, source evidence, verification state
```

**Pairwise width swap:** đổi `δ` twip từ cột `j` có thể co sang cột `i` có lợi ích; đây là phép thay đổi chiều rộng bảng **không tăng tổng W**. Bước khảo sát 0,5–1 mm chỉ là tham số thử nghiệm, nên chuyển sang integer twips trước khi ghi OOXML. Nếu mọi đổi nhỏ đều không có lợi, thử một số đổi lớn hơn có giới hạn để vượt ngưỡng chuyển dòng; không dùng tìm kiếm vô hạn hoặc thuật toán ML chỉ vì bài toán nghe phức tạp.

### 84.4. Số học chiều rộng và tránh rung lắc

- 1 point = 20 twips; 1 inch = 1440 twips; 1 mm xấp xỉ 56,6929 twips. Nên giữ số đo **nguyên twips** khi tối ưu/ghi DOCX.
- Khi phân bổ tỷ lệ tạo phần thập phân, làm tròn có kiểm soát và phân phối số dư theo các cột đủ điều kiện, không ghi width làm tổng vượt `W`.
- Cột đã khóa giữ nguyên số đo gốc, không làm tròn lại. Đối với bảng dùng `pct`, đọc đúng cơ chế `pct` trước khi chuyển sang mm; không giả định mọi width đều dùng `dxa`.
- Nếu một lần chạy nữa trên cùng dữ liệu, cùng profile, cùng renderer mà vẫn đề nghị sửa lại nhưng không có lợi ích được kiểm chứng, phải coi là **layout churn** và dừng.
- Bảng vốn đã đẹp: giữ nguyên `tblLayout`/AutoFit đã sử dụng; không buộc đổi sang fixed để hợp thức hóa thuật toán nếu điều đó làm tài liệu kém ổn định khi sửa tiếp.

## 85. Xử lý chuỗi khó ngắt, tiêu đề nhiều tầng và định dạng số

### 85.1. Phát hiện `unbreakable` theo ngữ cảnh, không theo regex duy nhất

Các giá trị như `20/10/2026`, `Số: 15/QĐ-UBND`, `00123`, số tiền, mã hồ sơ, đường dẫn, địa chỉ email và cụm từ có nonbreaking space cần cách xử lý khác nhau. Quy tắc xác định điểm ngắt phải căn cứ **kiểu dữ liệu + ngữ cảnh + font/render**, không cắt đơn giản tại `/`, `-`, dấu chấm hoặc dấu cách. Với số có `0` đầu, không chuyển thành kiểu số làm mất `0`.

Phân loại xử lý:

| Dạng nội dung | Chiến lược ban đầu | Điều kiện không tự can thiệp |
|---|---|---|
| STT, mã ngắn, ngày | Ưu tiên một dòng khi khả thi | Không thêm kí tự/ngắt dòng vào dữ liệu |
| Tên tổ chức, địa danh | Giữ cụm nhận diện dễ đọc; cho xuống dòng tại khoảng trắng thật | Không dùng phép tách mã làm gãy tên |
| Số tiền, tỷ lệ | Căn phải, giữ chính xác dấu và chữ số | Không làm tròn, đổi đơn vị, sửa locale |
| URL/email/mã dài | Đánh dấu `hard_to_wrap`; cân nhắc layout khác | Không chèn dấu cách hoặc chia thành nhiều text run làm thay đổi liên kết |
| Tiêu đề nhiều tầng | Tính ràng buộc width cho **khoảng cột được gộp** | Không đẩy cả width của tiêu đề gộp vào từng cột |
| Trường dữ liệu động/field | Ước lượng có cảnh báo; render kiểm chứng | Không biến field thành plain text |

### 85.2. Chuỗi phân tích không được tự thay nội dung gốc

Nếu bộ máy gợi ý điểm ngắt hoặc tách nhãn phục vụ đo hình học thì đó là mô hình **tạm thời phục vụ mô phỏng**. Chỉ áp dụng độ rộng/căn/đệm ô được cho phép vào OOXML; không ghi các kí tự `\n`, soft hyphen, zero-width space, nonbreaking-space mới vào nội dung gốc trừ khi người dùng yêu cầu rõ và kiểm tra tác động.

### 85.3. Ô gộp đặt bất đẳng thức trên tập cột

Nếu ô hợp nhất nằm trên cột 2–4, điều kiện tối thiểu là `w2 + w3 + w4` đáp ứng bề rộng nội dung ô (đã tính padding, border, khoảng trống cần thiết). Với `vMerge`, nội dung có thể chi phối **nhiều hàng**, nên không áp dụng công thức `max` của một hàng độc lập rồi tuyên bố PASS. Không thay thứ tự, số lượng hoặc quan hệ các ô thực.

## 86. Thiết kế thử nghiệm đánh giá ứng viên: đo ảnh hưởng thực tế

### 86.1. Baseline là chuẩn đối chứng bắt buộc

Không thể khẳng định “tối ưu hơn” chỉ vì bảng mới vừa chiều rộng. Mỗi bảng cần ít nhất hai quan sát: **gốc** và **ứng viên** dưới cùng môi trường (Word version/render target, font có sẵn, hệ điều hành khi ảnh hưởng, cỡ trang, thiết lập print). Tránh so sánh bản gốc render bằng engine A và bản mới bằng engine B.

Bộ chỉ số tham khảo:

| Nhóm | Chỉ số | Quy định phân xử |
|---|---|---|
| Tính toàn vẹn | Text/structure/relationship digest, order cell, merges | Phải bất biến ngoài phần cho phép |
| Tuân thủ | Legal/mẫu/profile assertions | Không được vi phạm |
| Bố cục | Overflow/clipping, ngoài vùng in, dòng bị che | `0` lỗi được xác minh |
| Trọng tâm | Tình trạng wrap cột hạn, mã, đơn vị, nội dung hành động | Không được kém đi ở giá trị trọng yếu |
| Hàng | `row_bottleneck`, số hàng bị đẩy sang trang, hàng ngắt bất hợp lý | So sánh với gốc; thay đổi phải giải thích |
| Trang | Trang của caption, bảng, chữ ký, phụ lục kế tiếp | Không gây tác động xấu ngoài phê duyệt |
| Thẩm mỹ | Đồng nhất viền/đệm/căn/spacing, mật độ chữ | Review kết hợp máy và người |
| Mức sửa | Số cột đổi, tổng absolute twips, OOXML nodes touched | Ít nhất có thể mà vẫn đạt mục tiêu |

Nếu không có bộ kết xuất kiểm chứng: đánh dấu `UNVERIFIED_LAYOUT`; không thay thế bằng lời khẳng định “đã đẹp”.

### 86.2. Kiểm tra bố cục nhiều trang có điều kiện

Render và so sánh các trang chứa bảng, trang liền trước/sau và **mọi trang downstream thực sự dịch chuyển**. Nếu pipeline có cách phát hiện vùng tác động chính xác, chỉ mở rộng đến vùng đó; nếu không có, phải tăng mức độ kiểm tra trước khi tuyên bố không ảnh hưởng đến nơi nhận, chữ ký hoặc phụ lục ở cuối tài liệu.

**Bảo mật dữ liệu:** đối với giải pháp không cho lưu nội dung DOCX, log chỉ lưu ID tạm trong phiên, số đo, mã lỗi và digest phù hợp; không ghi trích đoạn bảng, số liệu nhạy cảm, ảnh trang hoặc file nguồn vào storage/log ngoài phạm vi được cho phép. Bằng chứng trực quan có thể được xử lý trong phiên và xóa khi kết thúc; cần đánh giá chính sách lưu trữ trước triển khai.

### 86.3. Nhãn nghiệm thu mới

- `PASS_VERIFIED`: hard gates đạt, render kiểm chứng đạt, không đổi ngoài phạm vi.
- `KEEP_EXISTING`: bố cục gốc đã đạt hoặc phương án mới chưa có cải thiện đáng kể.
- `PROPOSED_AWAITING_APPROVAL`: ứng viên khả thi nhưng chưa được phê duyệt.
- `REVIEW_REQUIRED`: thiếu chắc chắn, bảng nhiều tầng, rủi ro hoặc thay đổi phạm vi lớn.
- `NO_FEASIBLE_LAYOUT`: ràng buộc không có nghiệm trong khổ/lề/hướng trang và quyền cho phép hiện tại.
- `UNVERIFIED_LAYOUT`: chưa có phép kiểm chứng bản kết xuất phù hợp.
- `REJECTED_REGRESSION`: ứng viên làm xấu đi tiêu chí trọng yếu hoặc dịch chuyển phần ngoài phạm vi.

Các nhãn là ngôn ngữ đặc tả V4, chưa phải API hay database hiện hữu. Không tuyên bố `PASS_VERIFIED` khi chỉ có XML parse hợp lệ.

## 87. Ba ca phân tích quyết định minh họa (không phải kết quả Word đã đo)

### 87.1. Bảng giao việc 5 cột trong vùng chữ 155 mm

**Giả định minh họa:** `STT | Nội dung công việc | Đơn vị | Hạn | Ghi chú`, bảng A4 dọc và vùng hữu dụng **giả định** 155 mm. Đây chỉ là bối cảnh giả lập, không thay cho `W` thực lấy từ section.

| Cột | Gốc giả định (mm) | Ứng viên A (mm) | Ứng viên B (mm) | Giải thích |
|---|---:|---:|---:|---|
| STT | 10 | 10 | 10 | Đã đủ chứa chỉ số; không nới |
| Nội dung công việc | 35 | 50 | 56 | Cột trọng tâm, nhiều chữ |
| Đơn vị | 23 | 28 | 31 | Giữ tên cơ quan dễ đọc |
| Hạn | 17 | 20 | 20 | Hạn quan trọng nhưng chỉ cần đủ một dòng |
| Ghi chú | 70 | 47 | 38 | Cho phép xuống dòng nếu không gây cao quá mức |
| **Tổng** | **155** | **155** | **155** | Không vượt W |

**Không chọn ngay B chỉ vì Nội dung rộng hơn.** Nếu phần lớn hàng bị chi phối bởi Ghi chú cao 6–8 dòng, thu Ghi chú xuống 38 mm có thể làm bảng dài hơn, đẩy chữ ký sang trang. Cần render cả A, B và bản gốc; chọn phương án **không phá bố cục**, đạt đọc hiểu tốt nhất với thay đổi ít nhất.

### 87.2. Bảng số liệu 7 cột

Cột “Chỉ tiêu” dài hơn cột số, nhưng cột số tiền hoặc tỷ lệ có thể đòi **mức sàn cứng** (đủ dấu trừ, dấu phân cách, phần trăm, đơn vị). Khi mỗi cột số đã vừa, phần rộng bổ sung nên ưu tiên cột Chỉ tiêu. Tuy nhiên không được tự gộp các cột chỉ vì nhiều cột hẹp; phải giữ lưới thống kê và các phép so sánh theo hàng.

Nếu hệ ràng buộc vô nghiệm, gợi ý lần lượt: rà lại việc bố trí ô/cột đã đúng chưa; lựa chọn bảng ngang khi điều kiện pháp lý cho phép; chia thành phụ lục/mục phù hợp theo phê duyệt; hoặc yêu cầu chỉnh sửa cấu trúc được cho phép. Không ép thu nhỏ chữ hoặc bỏ cột tự động.

### 87.3. Bảng hai tầng tiêu đề và ô ký

Với tiêu đề cấp 1 “Tình hình năm 2025” gộp ba cột và dòng cuối có vùng xác nhận, cần giữ nguyên các spans. Tối ưu width theo nhãn cấp thấp (`Kế hoạch`, `Thực hiện`, `Tỷ lệ`) nhưng kiểm tra tiêu đề cấp 1 trên **tổng ba cột**. Vùng xác nhận/ô ký và các điều khoản biểu mẫu là khóa. Nếu chưa hỗ trợ cả `gridSpan` và `vMerge`, chuyển `PRESERVE/REVIEW`, không ghi width mới.

## 88. Chuẩn đầu vào/đầu ra tối thiểu cho bộ quyết định cột

Bên dưới là **mẫu dữ liệu đặc tả**, không đồng nghĩa yêu cầu phải tạo service mới:

```yaml
width_decision_v4:
  table_locator: {part: "word/document.xml", table_path: "body/tbl[3]"}
  owner_region: "BODY | APPENDIX[n] | OTHER"
  legal_profile: "ND30_TABLE | PARTY_HD05_TABLE | TEMPLATE_OVERRIDE"
  selected_task: "ACTION"
  evidence_grade: "EXPLICIT"
  layout_risk: "MEDIUM"
  geometry:
    coordinate_unit: "twip"
    page_section_resolved: true
    usable_width_twips: 8787  # ví dụ minh họa ~155 mm, không phải giá trị chung
    layout_mode: "FIXED | AUTOFIT | UNKNOWN"
  columns:
    - {index: 1, role: "STRUCTURAL_INDEX", locked: false, old_twips: 567}
    - {index: 2, role: "PRIMARY_CONTENT", locked: false, old_twips: 1984}
  structural_risk: ["GRIDSPAN_PRESENT"]
  candidates:
    - {id: "ORIGINAL", status: "REFERENCE"}
    - {id: "A", status: "AWAITING_RENDER_VERIFICATION"}
  selected_action: "KEEP_EXISTING | PROPOSE | REVIEW | BLOCK"
  proof:
    source_integrity: "PENDING"
    renderer: "NONE"
    visual_result: "UNVERIFIED_LAYOUT"
    out_of_scope_changes: 0
```

**Lưu ý:** `table_path` đơn giản không đủ để nhận diện chắc chắn mọi bảng lồng nhau; khi triển khai cần dùng định danh nội bộ ổn định của bộ trích xuất sẵn có và đường dẫn part phù hợp, không tự phát minh một registry song song. Nếu phải lưu `table_locator`, đó là tham chiếu tạm có phạm vi phiên, không phải thông tin định danh dùng qua các lần upload.

Các trường `old_twips`/`usable_width_twips` ở ví dụ là giá trị minh họa, không cam kết tổng cộng đúng khi mới hiển thị hai trong năm cột; bộ kiểm thử phải kiểm tra tổng width của danh sách đầy đủ.

## 89. Bộ kiểm thử bổ sung V4 — 28 tình huống T53–T80

> **Toàn bộ đều là ca thử ĐỀ XUẤT, chưa được chạy trên DOCX thực tế.** Tiếp nối 52 ca T01–T52 của V3; chọn kiểm thử theo phạm vi module bị ảnh hưởng, không bắt buộc chạy hồi quy toàn hệ thống.

| ID | Tình huống | Tiêu chí kỳ vọng |
|---|---|---|
| T53 | Cột được ưu tiên rất cao nhưng ngày chỉ cần 20 mm | Không cho thêm mm sau khi đã đủ và không cải thiện |
| T54 | Cột ít ưu tiên đang quyết định chiều cao 80% hàng | Thuật toán vẫn xét lợi ích mở rộng cột đó |
| T55 | Tăng cột A 5 mm làm cột B bị chia thêm 2 dòng | Không chọn sai dựa trên lợi ích cục bộ của A |
| T56 | Đổi width chỉ làm ô 4 dòng thành 3 trong hàng có ô khác 9 dòng | Không báo giảm chiều cao hàng khi không có |
| T57 | Giảm cao một hàng khiến caption và bảng bớt chia trang | Ghi nhận lợi ích tại page boundary, không chỉ số dòng |
| T58 | Bảng đẹp rồi nhưng thuật toán tìm ra 0,2% điểm tăng | `KEEP_EXISTING`, không churn |
| T59 | Chạy cùng tài liệu lần thứ hai | Giữ nguyên width/render, idempotent |
| T60 | Làm tròn width theo tỷ lệ tạo tổng vượt W | Tổng integer twips vẫn không vượt W |
| T61 | Cột locked nằm cạnh cột cần mở | Không thay width cột locked hoặc cấu trúc bảng |
| T62 | Mọi cột được khóa nhưng vẫn còn tràn | `NO_FEASIBLE_LAYOUT` hoặc REVIEW; không ép font |
| T63 | Bảng có section 2 cột văn bản | W lấy theo vùng thực, không lấy toàn chiều ngang A4 |
| T64 | Bảng floating có text wrapping | Không xử lý theo công thức bảng inline khi chưa hỗ trợ |
| T65 | Bảng lồng trong ô bảng ngoài | W dựa trên ô chứa và padding/spacing thực |
| T66 | `tblW` kiểu phần trăm kết hợp grid twips | Không coi số phần trăm là trực tiếp mm |
| T67 | Merged header phủ 3 cột | Áp ràng buộc tổng span, không nhân 3 nội dung |
| T68 | `vMerge` kéo qua nhiều hàng | Không đo chiều cao các hàng một cách độc lập rồi PASS |
| T69 | Trường dữ liệu ngày đang hiển thị giá trị động | Không chuyển field thành text, luôn so sánh render |
| T70 | Mã `00123` và định dạng số đặc thù | Không mất số 0 hoặc đổi kiểu dữ liệu |
| T71 | URL dài và hyperlink | Không chèn ký tự/ngắt làm hỏng link |
| T72 | Tiếng Việt có dấu tổ hợp và chữ Latin trộn | Không tin tuyệt đối độ rộng dựa trên số ký tự |
| T73 | Candidate render bằng engine khác baseline | Không so sánh như cùng điều kiện |
| T74 | Bản DOCX mở được, XML hợp lệ nhưng clipping | FAIL visual, không `PASS_VERIFIED` |
| T75 | Bảng được sửa và đoạn nơi nhận cuối văn bản dịch sang trang khác | Kiểm tra downstream và báo tác động |
| T76 | Bảng không có caption, header mơ hồ | Không xác lập tác vụ với chứng cứ cao |
| T77 | Người dùng ưu tiên cột Hạn nhưng là biểu mẫu khóa | Biểu mẫu thắng, không sửa |
| T78 | Nhiều ứng viên tương đương | Chọn ít thay đổi hơn, hoặc giữ gốc |
| T79 | Dữ liệu nhạy cảm và chính sách không lưu file | Không ghi nội dung/ảnh trang vào log ngoài phạm vi |
| T80 | Thay đổi thuộc tính style dùng chung làm bảng khác biến đổi | FAIL phạm vi; yêu cầu sửa cục bộ hoặc review |

**Metamorphic tests nên ưu tiên sau đó:** đổi thứ tự hàng dữ liệu không làm thay đổi nhận diện vai trò nếu cột giống nhau; thêm một dòng ngoại lệ dài không được làm mất ràng buộc của giá trị không ngắt; làm rỗng cột ghi chú không được khiến cột này giành hết width; tăng W hợp pháp không được gây clipping mới; chạy lặp không làm phát sinh biến động width; thay đổi tên biểu mẫu được khóa không được thay quy tắc ưu tiên mẫu. Đây là tiêu chí bổ trợ, chỉ đưa thành test tự động nếu hành vi/contract thực tế cần khóa.

## 90. Ma trận hành động theo mức rủi ro và quyền can thiệp

| Chế độ | Điều kiện điển hình | Hành động cho phép |
|---|---|---|
| `PRESERVE` | Bảng biểu mẫu, vùng ký, bảng lồng không hiểu cấu trúc, quá nhiều khóa | Không đổi width/structure; chỉ cảnh báo |
| `LIGHT_TOUCH` | Bảng thường, chỉ có vấn đề spacing/viền/căn, không tràn | Tối ưu những thuộc tính riêng được phép, không đụng width |
| `WIDTH_PROPOSAL` | Bảng thường, xác định vai trò rõ, cần cân đối cột | Tạo tối đa 2–3 ứng viên, bắt buộc xem trước |
| `LAYOUT_REVIEW` | Không đủ W, cần xoay trang/đổi section/chia phụ lục | Không sửa tự động; có quyết định người dùng và kiểm chứng toàn vùng |
| `BLOCK` | Thiếu quyền, không hiểu topology, lỗi parse, mã nhúng/field không bảo đảm | Ngừng sửa, cung cấp lý do và vùng bị ảnh hưởng |

Một quy tắc có **rủi ro cao** nhưng mục tiêu người dùng quan trọng không đồng nghĩa được phép tự động sửa. Không dùng thuật toán để vượt quyền phê duyệt hoặc ranh giới nguồn quy tắc pháp lý.

## 91. Tái sử dụng và phương án triển khai tối thiểu

### 91.1. Những thành phần nên ưu tiên tái sử dụng

- **Microsoft Word native**: AutoFit Contents/Window, Fixed Column Width, Cell Margins, Repeat Header Rows và tùy chọn row break. Đó là tính năng thực, nhưng hành vi kết xuất vẫn cần kiểm chứng. [S42], [S44].
- **Office Open XML / Open XML SDK** hoặc thư viện DOCX đã có sẵn trong dự án: `tblPr`, `tblGrid`, `tcPr`, `trPr`, `tblLayout` và các relationship. Không sao chép động cơ Word, không tự viết layout engine mới nếu nhu cầu chỉ là chọn một tập ứng viên width hợp lệ. [S41], [S43], [S46].
- **Các dự án nguồn mở đã xem ở V3** như `python-docx` giúp hiểu mô hình bảng, Rich/PrettyTable cung cấp một số pattern về min/max width và wrap; chúng không phải bộ kết xuất DOCX thay thế Word. Việc tích hợp thư viện mới phải có bằng chứng thiếu capability ở local/dependency/native; không thêm chỉ vì có ví dụ đẹp.

### 91.2. Thứ tự triển khai đề xuất cho dự án hiện hữu

1. Audit code/parser/table model/current tests; xác định **authority** đang dùng và các contract đã chứng minh.
2. Tái sử dụng extraction và topology recognition hiện có; nếu chưa có, chỉ thêm phần tối thiểu để phát hiện grid/merge đúng.
3. Bổ sung `taskEvidence`, `row_bottleneck` và bộ sinh ứng viên width **thuần deterministic**, không tạo service/registry phụ.
4. Tích hợp một cơ chế preview/render/QA có sẵn; không tự viết trình render Word. Thiếu renderer thì chỉ xuất proposal, không công bố nghiệm thu visual.
5. Chạy các ca liên quan trên fixture thật, ghi before/after ở phạm vi kiểm chứng; nếu hợp đồng cũ không đổi, tận dụng evidence đã PASS.
6. Chỉ mở rộng khi xuất hiện lỗi tái hiện được hoặc nhóm tài liệu chưa hỗ trợ; mọi thay đổi phải cô lập, có thể rollback.

**Ngoài phạm vi V4:** commit, push, deploy, nâng cấp production, migration hoặc thay đổi Core. Đây là tài liệu tiêu chuẩn và nghiên cứu, chưa phải hoạt động triển khai mã nguồn.

## 92. Bảng tiêu chí nghiệm thu V4 đủ để giao cho bộ phận phát triển

| Mã gate | Yêu cầu nghiệm thu | Bằng chứng cần có | Kết luận khi thiếu |
|---|---|---|---|
| G01 | Chọn đúng profile pháp lý/mẫu | Record nguồn + phạm vi | `REVIEW_REQUIRED` |
| G02 | Phân loại đúng dạng bảng/vị trí | Table owner + topology | `BLOCK/REVIEW` |
| G03 | Không đổi nội dung, số liệu, quan hệ | Semantic/structural diff | `FAIL` |
| G04 | Không đổi tài sản/field/relationship | Package diff + object check | `FAIL` |
| G05 | Width fit với vùng thực và span | Geometry verification | `NO_FEASIBLE_LAYOUT` |
| G06 | Không có text clipped/overflow | Target renderer compare | `UNVERIFIED_LAYOUT` hoặc `FAIL` |
| G07 | Cột trọng tâm không kém hơn gốc | Task-aware before/after | `REJECTED_REGRESSION` |
| G08 | Row/page impacts có thể chấp nhận | Page diff in affected region | `REVIEW_REQUIRED/FAIL` |
| G09 | Không làm xấu bảng khác hoặc vùng ký | Scope/downstream comparison | `FAIL` |
| G10 | Lợi ích đủ rõ so với độ lớn thay đổi | Candidate rationale + baseline | `KEEP_EXISTING` |
| G11 | Áp dụng trong phạm vi được duyệt | Permission + change manifest | `BLOCK` |
| G12 | Chạy lại không làm width dao động | Idempotence test | `FAIL` |

**Hoàn thành nghiên cứu ≠ hoàn thành triển khai.** Chỉ báo `PASS_VERIFIED` cho một tài liệu cụ thể sau khi G01–G12 thích hợp đã được kiểm chứng; với quy tắc không áp dụng, ghi `N/A` có lý do, không tự động đổi thành PASS.

## 93. Kết luận và ưu tiên hành động của V4

1. **Thay đổi lớn nhất:** chuyển bài toán từ *chia mm theo độ dài và tầm quan trọng cột* sang *tối ưu có giới hạn theo hàng, bảng, trang và tác vụ đọc*, giữ bản gốc làm đối chứng.
2. **Không tăng độ phức tạp vô cớ:** chỉ thêm `taskEvidence`, bộ sinh ứng viên hữu hạn và kiểm chứng trước/sau vào pipeline hiện có, không viết lại renderer hay triển khai một solver lớn.
3. **Thẩm mỹ không phải chỉ là điểm số:** quyết định phải giải thích được lợi ích, vùng ảnh hưởng, độ tin cậy của phép đo và lý do giữ nguyên/từ chối.
4. **Chuẩn nghiệm thu:** đúng quy định + không mất nội dung + bảng dễ đọc hơn/không kém hơn + không phát sinh phân trang xấu + chỉ sửa đúng chỗ đã được phép.
5. **Trạng thái nghiên cứu tại 20/10/2026:** hoàn thành đặc tả trên giấy; cần audit mã dự án cụ thể, mẫu DOCX và kết xuất Word thật mới có thể đánh giá chất lượng implementation.


---

# PHẦN XXI. NÂNG CẤP V5 — QUY TRÌNH RA QUYẾT ĐỊNH CÓ THỂ THỰC THI, ĐO ĐƯỢC VÀ AN TOÀN ĐỐI VỚI DOCX

> **Phạm vi:** Đây là chuyên đề bổ sung cho Phần I–XX (V1–V4), **không thay thế** quy định pháp lý hoặc preset đã trình bày. V5 nhằm biến nghiên cứu về nội dung trọng tâm và độ rộng cột thành **hợp đồng đầu vào/đầu ra, thuật toán chọn phương án, bằng chứng nghiệm thu và chính sách xử lý bất định**. Đây vẫn là **đặc tả nghiên cứu**, chưa phải thành phần đã triển khai hay thuật toán được chứng minh tối ưu toàn cục. Toàn bộ tỷ lệ/ngưỡng ví dụ là cấu hình thử nghiệm, không phải định mức pháp luật. Ký hiệu [PL]/[BM]/[KN]/[KT]/[BK] giữ nguyên.

## 94. Rà soát khoảng trống V4 và mục tiêu riêng của V5

| Khoảng trống của V4 | Rủi ro nếu chưa làm rõ | Quyết định V5 |
|---|---|---|
| Mức độ quan trọng cột chưa có hợp đồng chứng cứ tối thiểu thống nhất | Phân loại nhầm `Ghi chú` là phụ, dù chứa điều kiện quyết định | Thêm **task brief**, đường dẫn chứng cứ, trạng thái chưa xác định, quyền override |
| Nhiều điểm số và hàm mục tiêu đề xuất nhưng chưa có quy tắc dừng cụ thể | Chỉnh cột liên tục dù không cải thiện khi in | Thêm **giữ nguyên mặc định**, ngưỡng cải thiện được đo, idempotence |
| Thiếu mô hình tách trạng thái hình học và kết xuất | Tính toán hợp lệ bị hiểu sai thành bản Word đã đạt | **Ba mức bằng chứng** XML/geometry → renderer → PDF/print |
| Phân trang có thể ảnh hưởng vùng ký và các section tiếp theo | Kiểm tra trong bảng PASS nhưng văn bản cuối bị xô lệch | Xác định phạm vi render dựa trên biến động thực tế (affected pages) |
| Các biểu mẫu có cột nhìn giống dữ liệu nhưng phục vụ chỗ trống ký/điền | Tự co cột được coi là dư thừa | Thêm **form geometry locks** và cơ chế phát hiện vùng ký |
| Bản đầu vào dùng track changes, content controls, alternate content | Save có thể thay đổi nội dung chưa định xử lý | Chặn theo capability đã kiểm chứng, so sánh OPC parts/relationships |
| Chưa có bộ nhãn nghiệm thu phân biệt thiếu dữ liệu với lỗi thật | Báo FAIL oan hoặc PASS quá sớm | Quy định `PASS`, `FAIL`, `REVIEW`, `UNVERIFIED`, `N/A`, `NO_OP` có chứng cứ |
| Các nguồn tham khảo trùng, một số phương pháp là khuyến nghị nghiên cứu | Nhầm thành cam kết kỹ thuật hoặc yêu cầu pháp lý | Thêm **bảng nguồn quy tắc và giới hạn chứng cứ** |

**Quy tắc ưu tiên:** Nếu V1–V4 có mô tả chấm điểm có thể dẫn tới tự động sửa nhưng V5 chưa đủ chứng cứ an toàn, ưu tiên chính sách V5: **không tự sửa**. V5 không làm thay đổi các chỉ số lề, cỡ chữ và bố cục pháp lý đã được viện dẫn; mọi kết luận pháp lý vẫn phải dựa vào văn bản gốc và mẫu được áp dụng.

## 95. Định nghĩa kết quả tối ưu và trường hợp không cần sửa

Định nghĩa một bảng `T` và vector độ rộng `w=(w1,...,wn)` theo **các cột lưới vật lý (grid columns)**, không phải số ô hiển thị. Bảng hiện có là `w0`. Một ứng viên `w'` chỉ được áp dụng nếu đồng thời:

1. Không vi phạm căn cứ pháp lý/mẫu/giới hạn quyền thao tác.
2. Toàn bộ nội dung, cấu trúc, liên kết, đối tượng và thuộc tính ngoài phạm vi cho phép được bảo toàn.
3. Đạt điều kiện hình học đối với trang/section/ô chứa và không có lỗi render mới.
4. Không làm giảm khả năng nhận biết nội dung trọng tâm, không làm mất tính phân biệt dữ liệu.
5. Lợi ích đo được vượt **mức cải thiện tối thiểu đã cấu hình**, hoặc khắc phục một lỗi hiện hữu rõ ràng.
6. Nếu hai ứng viên không phân biệt được bằng chứng đáng tin cậy, chọn **ít thay đổi hơn**, cuối cùng chọn **giữ nguyên**.

`NO_OP_VALID` là kết quả hoàn toàn hợp lệ; không được xem là công cụ thất bại chỉ vì số cột đã sửa bằng 0. Một hồ sơ kiểm tra có thể PASS với hành động `KEEP_EXISTING` khi bảng gốc đã tốt hoặc ứng viên không chứng minh được lợi ích.

Phân biệt rõ **tối ưu cục bộ theo bộ ứng viên đã khảo sát** với tối ưu toàn cục: chiến lược tìm kiếm hữu hạn **không chứng minh** đã tìm ra bố cục đẹp nhất trong mọi khả năng của Word.

## 96. Hợp đồng nhận diện nội dung trọng tâm (Column Intent Contract)

### 96.1. Task brief phải có trước khi chấm cột

`table_intent` có các thành phần:

- `reader_task`: `IDENTIFY`, `TRACK_ACTION`, `COMPARE_VALUES`, `EXPLAIN`, `FILL_FORM`, `APPROVE_SIGN`, `UNKNOWN`.
- `critical_fields`: các vai trò/danh tính cột cần ưu tiên **giữ nguyên khả năng nhận biết**, không nhất thiết ưu tiên thêm mm.
- `context_provenance`: người dùng chỉ định; mẫu bắt buộc; tiêu đề bảng/đoạn gần bảng; quan hệ tiêu đề nhiều tầng; phân bố dữ liệu; hoặc chưa biết.
- `ambiguity`: ghi rõ những phương án giải thích cạnh tranh; không lấp khoảng trống bằng phỏng đoán.
- `locked_columns`/`locked_spans`: nhận từ mẫu hoặc sự phê duyệt; không suy ra quyền sửa từ mức độ ưu tiên.

**Nguồn xác định trọng tâm, theo thứ tự:** mẫu chính thức áp dụng → hướng dẫn rõ ràng của người dùng **trong phạm vi mẫu cho phép** → caption/văn bản nói rõ tác vụ → tiêu đề nhóm+cột → đặc trưng nội dung → mặc định `UNKNOWN`.

Ví dụ: cột `Kết quả` chứa các giá trị `Đạt/Không đạt` trong bảng kiểm tra là trọng tâm cho quyết định. Cột `Căn cứ` có thể là thông tin giải thích, nhưng nếu bảng phục vụ kiểm định pháp lý thì `Căn cứ` cũng trở thành trọng tâm; không suy từ riêng tên cột.

### 96.2. Bộ dấu hiệu phân loại tối thiểu

| Nhận diện | Bằng chứng khả dụng | Không được suy diễn |
|---|---|---|
| Mã/STT | Tiêu đề, dạng mã liên tục, chiều dài ít biến động | Tất cả chuỗi ngắn đều kém quan trọng |
| Định danh hàng | Tên đối tượng/đơn vị, nội dung nhận diện chính | Cột đầu tiên luôn là định danh |
| Hạn/trạng thái | Tiêu đề, giá trị ngày/tình trạng, ngữ cảnh công việc | Cứ cột Hạn thì phải rộng nhất |
| Số liệu | Kiểu giá trị, ký hiệu đơn vị, nhãn nhóm | Có thể chuyển đổi/viết lại số cho đẹp |
| Diễn giải | Đoạn chữ dài, xuống dòng có nghĩa | Mọi đoạn dài có thể co không giới hạn |
| Phê duyệt/ký | Nhãn ký, xác nhận, dấu, ô trống có vai trò | Ô trống là dữ liệu dư có thể xóa/co |
| Tiêu đề nhiều cấp | Quan hệ `gridSpan`, `vMerge`, nhãn nhóm | Đếm ô vật lý như các cột độc lập |

Không sử dụng AI để thực hiện phép đo hình học hay quyết định permission/hard gate. AI (nếu có) chỉ đóng vai trò **gợi ý phân loại hoặc giải thích**, và phải xuất căn cứ để người dùng xác nhận khi chưa chắc chắn. Các bước xác định số ô, đọc mô hình lưới, kiểm tra luật và so sánh nội dung vẫn là deterministic logic.

### 96.3. Hai điểm số tuyệt đối không được trộn

- `criticality`: mức thiệt hại nếu thông tin trở nên khó đọc hoặc dễ nhầm. Có thể cao dù cột rất hẹp.
- `expandability`: độ lợi của việc cấp thêm một đơn vị chiều rộng xét trên số dòng, độ cao hàng và khả năng quét bảng.

Ưu tiên cấp chiều rộng theo **lợi ích biên đã kiểm chứng**, sau khi mỗi cột đạt ngưỡng khả năng đọc bắt buộc theo vai trò. Không chia độ rộng theo tỷ lệ trực tiếp của điểm `criticality`.

## 97. Hình học thực: bảng không luôn có một vùng 155–165 mm

Đo chiều rộng khả dụng theo ngữ cảnh cụ thể, không lấy một hằng số cho cả tài liệu:

```text
section.page_width
section.left_margin / right_margin
section.columns / column_spacing
section.orientation
section.mirrored_or_two_sided_layout
containing_cell_available_width (nếu nested)
table_indent / table_alignment / floating_position / text_wrap
cell_margins / cell_spacing / border contributions
paragraph_indent / relevant object constraints
=> admissible_table_region
```

Phân biệt:

1. **Trang A4 dọc bình thường:** lề theo profile pháp lý hiện hành; tính lại từ section thực tế.
2. **In hai mặt với lề mặt trước/mặt sau:** Hướng dẫn 05-HD/VPTW, phần II.IV.4.1–4.2 xác định lề trang mặt trước 30 mm trái/15 mm phải, mặt sau 15 mm trái/30 mm phải. Tổng vùng chữ không đổi nhưng **vị trí tương đối với mép giấy thay đổi**. Không tự hiểu chiều rộng đủ là đã bảo đảm bố trí mặt chẵn/lẻ. [S50].
3. **Section hai cột / nhiều cột:** lấy vùng cột thích hợp, không lấy toàn vùng chữ của trang.
4. **Bảng lồng nhau:** lấy chiều rộng ô cha sau khi xét đệm/viền và cấu trúc span.
5. **Bảng floating hoặc quanh chữ:** cần đo vùng đặt thực, và nếu capability chưa hỗ trợ thì `REVIEW`, không coi bảng inline.
6. **Bảng ngang (landscape):** chỉ đề xuất sau khi chứng minh các phương án trong trang hiện tại không phù hợp; thay đổi orientation/section không thuộc hành động chỉnh width thông thường.

**Giới hạn mô hình:** Phép tính OOXML/twips là kiểm tra hình học đầu vào. Kích thước hiển thị có thể chịu chi phối của font, Table Style, `tblLayout`, cell widths, grid, hộp chứa và phiên bản Word. Bởi vậy không gọi `GEOMETRY_PASS` là `RENDER_PASS`. [S51], [S52].

## 98. Mô hình đo chiều rộng và chiều cao theo mức tin cậy

### 98.1. Tầng đo M0–M3

| Tầng | Phương pháp | Có thể kết luận | Không được kết luận |
|---|---|---|---|
| `M0_SOURCE` | Đọc cấu trúc OOXML và các thuộc tính đã khai báo | Ràng buộc, quyền sửa, width khai báo | Chữ chắc chắn không bị cắt |
| `M1_ESTIMATE` | Đo chuỗi bằng font phù hợp, đo ngắt dòng/ô gộp ước lượng | Lọc ứng viên bất khả thi hiển nhiên | Đã đạt bố cục Word thực tế |
| `M2_RENDER` | Mở/kết xuất bản gốc và ứng viên bằng cùng renderer/phiên bản/font | So sánh hình học và khả năng đọc theo môi trường đó | Mọi phiên bản Word đều giống nhau |
| `M3_TARGET` | Kiểm tra thêm đầu ra đích: in, PDF/tagged PDF khi thuộc yêu cầu | Tính đạt theo kênh phát hành đã kiểm | Các kênh chưa kiểm đều đạt |

Định dạng nội dung tiếng Việt cần xem xét glyph, dấu kết hợp, phông thay thế, chữ đậm/nghiêng và ký tự khó ngắt. Đếm số ký tự hoặc dùng độ dài chuỗi như một phép đo mm là không đủ. Với dữ liệu thập phân, chuỗi có nhiều số 0, mã dài, tên file, URL hoặc ngắt dòng thủ công, cần chính sách riêng về ngắt/không ngắt; tuyệt đối **không thay đổi chính chuỗi gốc** nếu tác vụ chỉ là định dạng.

### 98.2. Hàm chi phí ở cấp hàng/bảng

Đặt `h(r,c,w)` là chiều cao sau render của nội dung ô/cụm ô tương ứng tại vector `w` và `H(r,w)` là chiều cao hàng (có thể chịu ảnh hưởng các row-spans). Bảng không phải tổng độc lập của chiều cao từng ô, nên:

```text
bottleneck_rows(w) := những hàng mà nội dung cao nhất quyết định chiều cao
height_gain(candidate) := H_table(baseline) - H_table(candidate)
critical_readability_loss(candidate) := mức giảm khả năng đọc các cột trọng tâm
boundary_change(candidate) := dịch chuyển trang/caption/đoạn liền kề
```

Chỉ ước lượng `H` để xếp ứng viên ban đầu; **số dòng/thay đổi trang được công bố là sự thật chỉ sau kiểm tra render**. Cột ít quan trọng về nội dung vẫn có thể là cột cần nới nếu chính nó quyết định phần lớn chiều cao bảng và việc nới đó không làm giảm các cột quan trọng.

## 99. Thuật toán đề xuất: sàng lọc → ứng viên ít thay đổi → nghiệm thu

Quy trình 11 bước, tận dụng parser/Word/OOXML/renderer hiện có:

1. **Identify authority:** loại văn bản, hiệu lực văn bản, mẫu bắt buộc, section và chủ sở hữu bảng (`body`/`appendix`/`layout`/`nested`).
2. **Capture baseline:** chụp topology, XML/relationships thuộc phạm vi, vector width, tình trạng khóa và các trang ảnh hưởng (nếu có renderer).
3. **Decide eligibility:** bảng cố định/đang theo dõi thay đổi/bảng trong đối tượng phức tạp/chữ ký không được tự động tối ưu.
4. **Determine task:** nhận diện vai trò cột với provenance; thiếu chứng cứ => `REVIEW` thay vì cấp width bừa.
5. **Compute region:** xác định width tính bằng twips theo section + containment; mọi cột khóa và `gridSpan` là ràng buộc.
6. **Measure M0/M1:** tính giới hạn tối thiểu khả dụng/ước lượng lợi ích mở rộng; chọn hàng thắt cổ chai.
7. **Generate few candidates:** trước tiên `ORIGINAL`, sau đó chỉ 2–3 ứng viên ở các nhóm cột thực sự có tác động; cộng trừ width từ cột được phép co, tổng twips chính xác.
8. **Filter hard constraints:** bỏ ứng viên vi phạm locks/span/layout/legal/preservation hoặc phải sửa ngoài phạm vi được duyệt.
9. **Render and compare (nếu khả dụng):** cùng renderer, fonts, settings; đo cả ảnh hưởng caption, ranh giới trang và vùng sau bảng.
10. **Choose lexicographically:** không suy giảm critical fields → không tràn/cắt → không hồi quy phân trang → dễ đọc hơn rõ rệt → thay đổi ít nhất; khi bất định, giữ gốc.
11. **Produce decision report:** `KEEP_EXISTING`, `PROPOSE`, `REVIEW`, `BLOCK` hoặc `APPLIED_VERIFIED` theo chứng cứ. Chỉ trạng thái cuối khi thực sự áp dụng và kiểm chứng.

### 99.1. Pseudocode tham khảo — không phải code ứng dụng

```text
function proposeTableWidth(table, task, constraints, capabilities):
    original = inspect(table)
    if not eligible(original, constraints, capabilities):
        return BLOCK_OR_REVIEW(reason, original)

    feasible = [original]
    for candidate in localCandidates(original, task, constraints, limit=3):
        if hardConstraintsHold(candidate):
            feasible.append(candidate)

    if not capabilities.sameTargetRenderer:
        return REPORT_ONLY(feasible, renderStatus="UNVERIFIED")

    evaluated = renderCompare(feasible, affectedRegion)
    accepted = [c for c in evaluated if c.passesAllHardGates]
    if not accepted:
        return KEEP_OR_REVIEW(original, reason="NO_VERIFIED_IMPROVEMENT")

    best = lexicographicChoose(accepted, tieBreak="MIN_CHANGE")
    if best.benefitIsNotMaterial or best.layoutRiskIsUnresolved:
        return KEEP_EXISTING(original)
    return PROPOSE(best, evidence=best.proof)
```

**Không cấy thêm solver/AI workflow/microservice/vector DB** để giải bài toán nhỏ này nếu không có số liệu chứng minh nhu cầu. Một lần mở Word native hoặc có sẵn renderer để so sánh cuối cùng có giá trị hơn việc viết lại cơ chế bố cục không tương đương Microsoft Word.

### 99.2. Tránh dao động và sửa quá mức

- Làm tròn cuối cùng theo **twips nguyên**, không sửa qua nhiều lần mm → pt → twips.
- Thiết lập **deadband** cho khác biệt width/chiều cao nhỏ hơn sai số renderer; ngưỡng phải được hiệu chỉnh bằng fixture thật, **chưa có con số chuẩn**.
- Ứng viên không có lợi ích đáng kể hoặc bằng nhau theo độ chính xác quan sát được => chọn baseline.
- Sau khi áp dụng cùng preset lần thứ hai, diff thuộc tính định dạng mục tiêu bằng 0 hoặc giống hệt trạng thái đã nghiệm thu (`idempotence`).
- Không sửa `styles.xml` dùng chung để phục vụ chỉ một bảng nếu gây tác động đến bảng khác; ưu tiên override đúng chỗ hoặc không sửa.

## 100. Quy tắc bảo toàn gói DOCX và những tính năng dễ gây hồi quy

`format-only` có nghĩa là không chỉ giữ **text** mà giữ **mối liên hệ ngữ nghĩa và cấu trúc của gói DOCX**, tối thiểu:

| Nhóm | Bất biến/cách kiểm |
|---|---|
| Nội dung hiển thị | Văn bản, số liệu, dấu, whitespace có ý nghĩa, thứ tự đọc, định dạng số có ý nghĩa |
| Bảng | Số bảng, đường dẫn owner, thứ tự bảng, số hàng/cột lưới, `gridSpan`/`vMerge`, ô lồng, hàng/cột ẩn theo cấu trúc |
| Đối tượng và tham chiếu | Ảnh, hyperlink, chart, footnote/endnote, bookmark, caption/ref, field code/formula, shape và relationship ID |
| Tài liệu quản trị | Section, số trang, metadata có liên quan, header/footer, protected ranges, content controls, tracked changes |
| Tương thích | `mc:AlternateContent`, các namespace và relationship chưa hiểu, macro/embedding có chính sách nhận/từ chối rõ ràng |
| Phạm vi sửa | Chỉ các nút/thuộc tính đã duyệt; không ghi lại toàn bộ gói theo cách phá những phần chưa hỗ trợ |

Microsoft cảnh báo quá trình preprocessing Markup Compatibility có thể loại các nhánh nội dung không được chọn, và **khi lưu chỉ còn markup sau preprocessing**. Vì vậy, tài liệu có `AlternateContent` không được âm thầm chạy qua phép mở–ghi lại gây mất nhánh khi yêu cầu chỉ sửa độ rộng bảng; cần chứng minh công cụ hiện có bảo toàn, nếu không hãy từ chối hoặc chuyển review. [S53].

Nếu tài liệu có **Track Changes**, không tự động chấp nhận/từ chối revision hay đồng nhất văn bản đã xóa với văn bản đang hiển thị. Microsoft phân biệt inserted/deleted/moved markup; nếu bộ so sánh không hỗ trợ trạng thái thay đổi, trả `REVIEW_REQUIRED`. [S54].

**Không nên định nghĩa một giá trị hash ZIP duy nhất là chứng cứ duy nhất về bất biến:** phần ZIP có thể được đóng gói lại hợp lệ dù payload XML không đổi. Cần so sánh nội dung XML/OPC ở mức semantic/canonical phù hợp và các binary part trong phạm vi, đồng thời báo rõ những khác biệt được phép và không được phép.

## 101. Kiểm chứng kết xuất và cách đọc kết quả đúng

### 101.1. Ma trận so sánh đối chứng

| Bằng chứng | Gốc | Ứng viên | Quy tắc kết luận |
|---|---|---|---|
| Trích xuất nội dung và cấu trúc | Snapshot | Snapshot | **Mọi khác biệt ngoài whitelist phải giải trình hoặc FAIL** |
| Vùng bảng và cột | Width/indent/locks | Width/indent/locks | Tổng width hợp lệ, không xâm phạm locked span |
| Hình ảnh render | PNG/PDF trang liên quan | Cùng settings | Không clipping, tràn, đè chữ, lệch các thành phần không liên quan |
| Row bottleneck | Số dòng/chiều cao thực | Đo lại | Không tuyên bố lợi ích nếu hàng vẫn bị chi phối như cũ |
| Caption, ký, phụ lục | Trang/vị trí trong tài liệu | Trang/vị trí tương ứng | Không tách rời gây khó đọc hoặc phá mẫu |
| Kết xuất đích | Word Desktop/PDF/In | Word Desktop/PDF/In | Chỉ xác nhận đúng kênh đã kiểm |

**Pixel diff không phải bằng chứng duy nhất.** Những khác biệt anti-aliasing, font/hinting, số trang cập nhật hoặc metadata có thể gây sai khác nhiều pixel mà không phải lỗi; đồng thời ảnh gần giống vẫn có thể che mất field hoặc hyperlink. Dùng đồng thời semantic diff, kiểm tra layout vùng quan tâm và duyệt hình khi cần.

### 101.2. Chính sách chấp nhận theo kênh

- `DOCX_OPENED`: file mở được, **chưa tương đương** bảng được trình bày tốt.
- `XML_CHECKED`: kiểm tra gói và thuộc tính hợp lệ, **chưa chứng minh** bố cục.
- `WORD_DESKTOP_VERIFIED`: có bằng chứng trong cấu hình Word/version/fonts được công bố; không ngoại suy cho mọi máy.
- `PDF_VERIFIED`: có bằng chứng cho PDF của bộ chuyển đổi cụ thể; không mặc nhiên tương đương Word native.
- `ACCESSIBILITY_REVIEWED`: kiểm tra cấu trúc đơn giản, hàng tiêu đề và khả năng đọc; nếu xuất tagged PDF, đánh giá tag riêng.

Microsoft Support lưu ý `Repeat Header Rows` chỉ hiển thị ở chế độ Print Layout hoặc khi in và không lặp qua ngắt trang thủ công trong bảng. Vì vậy, chỉ nhìn thuộc tính `tblHeader` chưa đủ để khẳng định trên mọi trang đã xuất hiện tiêu đề lặp. [S55]. Với đầu ra PDF có yêu cầu tiếp cận, hướng dẫn Section 508 còn cảnh báo cần kiểm tra riêng chính sách header rows/tagged PDF; **không bảo đảm từ việc DOCX hiển thị đúng sang cấu trúc PDF đúng**. [S56].

## 102. Ma trận phân xử tự sửa, đề xuất và từ chối

| Đặc điểm bảng | Hành động mặc định | Lý do |
|---|---|---|
| Bảng dữ liệu đơn giản, layout ổn, không lỗi rõ | `KEEP_EXISTING` | Tránh thay đổi không đem lại lợi ích |
| Bảng đơn giản tràn vùng chữ, có đủ renderer và không khóa | `PROPOSE_WIDTH` | Có thể kiểm chứng ứng viên trước khi áp dụng |
| Bảng 2+ cấp tiêu đề, gộp ngang hiểu rõ | `PROPOSE_WITH_REVIEW` | Phải kiểm ràng buộc trên nhiều cột và phụ thuộc header |
| Bảng có gộp dọc hoặc bảng lồng sâu | `REVIEW_REQUIRED` | Chiều cao hàng không độc lập; mô hình phải chứng minh hỗ trợ |
| Biểu mẫu cố định có vùng điền/ký | `PRESERVE_FORM` | Hình học biểu mẫu là một phần chức năng |
| Tài liệu `mc:AlternateContent`, tracked changes chưa hỗ trợ | `BLOCK_UNSUPPORTED` | Không thể chứng minh bất biến khi round-trip |
| Vùng chữ không đủ cho tất cả ngưỡng cột | `NO_FEASIBLE_LAYOUT` | Không ép cỡ chữ/phá mẫu; gợi ý trang ngang hoặc phụ lục sau xác nhận |
| Có lỗi renderer, thiếu phông, thiếu baseline | `UNVERIFIED` | Không khẳng định đã đạt chuẩn thẩm mỹ |
| Cần đổi orientation/section | `REVIEW_REQUIRED` | Vượt phạm vi thao tác đổi width thông thường |
| Bảng chứa thông tin mật và công cụ cần tải lên renderer khác | `BLOCK_OR_LOCAL_REVIEW` | Không chuyển dữ liệu khỏi phạm vi xử lý được cho phép |

## 103. Hệ thống chỉ số chất lượng: tránh thưởng sai hành vi

Nên thu thập các chỉ số sau trên **bộ fixture được phép sử dụng**, tránh dùng tài liệu thật chứa thông tin nhạy cảm để test.

| Mã | Chỉ số | Mục đích | Cách tránh hiểu sai |
|---|---|---|---|
| Q01 | `content_integrity_rate` | Tỷ lệ ca giữ đúng nội dung/relationship | Mục tiêu bắt buộc 100% cho ca được tuyên bố PASS |
| Q02 | `layout_failure_rate` | Tỷ lệ ca phát sinh clipping/overflow/overlap | Không che bằng điểm thẩm mỹ trung bình |
| Q03 | `critical_field_legibility` | Tỷ lệ cột trọng tâm đọc rõ | Phải có rubric và người đánh giá khi không tự đo chắc |
| Q04 | `page_regression_count` | Số ca tác động phân trang không được duyệt | Đổi trang không tự động là lỗi; xét mục đích |
| Q05 | `change_minimality` | Mức sửa thuộc tính khác nhau so với gốc | Không thưởng `NO_OP` nếu lỗi gốc còn nguyên |
| Q06 | `idempotence_pass_rate` | Không phát sinh diff khi lặp preset | Phải đo trên file sau lần áp dụng thứ nhất |
| Q07 | `review_precision` | Tỷ lệ cảnh báo thực sự đáng review | Không tối ưu bằng cách tự ý bỏ cảnh báo |
| Q08 | `render_coverage` | Tỷ lệ ca có đo kết xuất đích | Tách riêng `UNVERIFIED`, không cộng vào PASS |
| Q09 | `decision_trace_coverage` | Quyết định có lý do, nguồn, tác động, bằng chứng | Ẩn dữ liệu nhạy cảm khỏi log lâu dài |
| Q10 | `human_preference_rate` | Người thẩm định thích bản ứng viên hơn | Không thay điều kiện đúng pháp lý và bảo toàn |

**Rubric chấm mắt người (đề xuất thử nghiệm, 5 tiêu chí 0–2 điểm):** đọc được giá trị trọng tâm; tiêu đề rõ; khoảng trắng và viền hài hòa; không có hàng quá cao không cần thiết; dòng/bảng liên tục hợp lý khi lật trang. Chỉ dùng để so sánh các ứng viên đã PASS hard gates; người đánh giá không cần biết tên thuật toán để hạn chế thiên lệch. Nếu điểm ngang nhau hoặc khó phân biệt, giữ nguyên.

## 104. Bộ mẫu đánh giá và thiết kế thực nghiệm tối thiểu

Tận dụng tối đa T01–T80 đã được đề xuất ở V1–V4. Không tạo 80 mẫu mới nếu đã có fixture tương đương, có bằng chứng PASS và contract không đổi. Đối với V5, ưu tiên **10 nhóm đại diện**:

| Nhóm | Đặc tính dữ liệu | Kết quả cần quan sát |
|---|---|---|
| F01 | Bảng công việc 4–6 cột; hạn là cột trọng tâm | Cột hạn được bảo vệ, cột diễn giải vừa đủ |
| F02 | Bảng thống kê có đơn vị và số thập phân | Căn số dễ so sánh, không đổi chính xác dữ liệu |
| F03 | Bảng danh bạ tên dài, mã ngắn | Mã không mất số 0; tên không bị chia vụn |
| F04 | Bảng phụ lục >2 trang | Lặp header đúng với ngắt tự động, không nhầm manual break |
| F05 | Tiêu đề 2–3 tầng, `gridSpan` | Đủ width cho nhóm tiêu đề và các cột con |
| F06 | `vMerge`, hàng dài, ghi chú rất dài | Không ước lượng sai chiều cao, không cắt nội dung |
| F07 | Bảng lồng trong cột hoặc ô | Không đo theo chiều rộng A4 toàn trang |
| F08 | Biểu mẫu vùng ký/điền có ô trống | Giữ nguyên hình học mẫu |
| F09 | Tiếng Việt Unicode kết hợp, URL, mã dài | Đo/hiển thị đúng, không chèn ngắt tùy tiện |
| F10 | DOCX có tracked changes/AlternateContent/field | Bảo toàn hoặc chặn rõ ràng, không làm mất markup |

Mỗi fixture cần các phiên bản **gốc, vấn đề quan sát được, hướng xử lý được phép, trạng thái kỳ vọng, điều kiện PASS, file/ảnh trước-sau nếu có renderer**. Nên có một mẫu **đã tốt từ đầu** để chứng minh bộ tối ưu biết chọn `NO_OP`. Tuyệt đối không dùng dữ liệu nhạy cảm/tài liệu thật để kiểm thử nếu chưa có quyền và cơ chế bảo vệ phù hợp.

## 105. Ca kiểm thử mới T81–T96 — chỉ cho hành vi hoặc contract V5 bổ sung

> Đây là **16 tình huống kiểm thử đề xuất**, chưa được chạy. Các trường hợp trùng contract T01–T80 phải reuse fixture/evidence, không nhân đôi test vô ích.

| ID | Điều kiện mới | Kết quả kỳ vọng |
|---|---|---|
| T81 | Bảng vốn đã tốt, mọi ứng viên chỉ lợi hơn dưới mức sai số đo | `NO_OP_VALID` và giải thích giữ nguyên |
| T82 | User ưu tiên `Căn cứ`, tiêu đề gợi ý `Kết quả` | Ưu tiên user nếu hợp pháp, nhưng vẫn bảo vệ giá trị quyết định |
| T83 | Hai vai trò cột cạnh tranh mà không có task brief rõ | `REVIEW_REQUIRED`; không tự chọn trọng tâm với chứng cứ giả |
| T84 | Một số ô phục vụ chữ ký nhưng nội dung hiện đang trống | Form lock, không co/tách/xóa ô |
| T85 | Văn bản Đảng in hai mặt, lề mặt sau trái/phải đảo | Định vị đúng từng mặt/section; không chỉ kiểm tổng width |
| T86 | Word 365 render khác Word phiên bản khác với cùng DOCX | Chỉ tuyên bố đạt trên cấu hình đã đo, không phổ quát hóa |
| T87 | Không có renderer Word, nhưng XML geometry khả thi | `GEOMETRY_CHECKED`, không được báo `RENDER_PASS` |
| T88 | Ảnh render pixel khác do anti-aliasing nhưng nội dung/layout tương đương | Không FAIL mù quáng theo pixel diff |
| T89 | Caption hoặc vùng chữ ký bị dịch sang trang mới sau sửa cột | `REJECTED_REGRESSION` hoặc người dùng review tác động |
| T90 | Mở/lưu với Markup Compatibility preprocessing làm mất nhánh không chọn | Chặn hoặc FAIL bất biến gói |
| T91 | DOCX có tracked changes mà parser chỉ thấy văn bản đã hiển thị | Không chấp nhận/xóa revision; `REVIEW_REQUIRED` |
| T92 | DOCX mở được và XML hợp lệ nhưng bảng render có dòng bị che | `LAYOUT_FAIL`, không PASS chung |
| T93 | Chạy lại preset hai lần với cùng renderer | Diff lần hai bằng 0 theo phạm vi đã duyệt |
| T94 | Người dùng yêu cầu PDF/UA hoặc tagged PDF | Có gate PDF accessibility riêng; không chuyển PASS từ Word |
| T95 | Một ứng viên giảm 1 trang nhưng khiến mã/số khó đọc | Loại ứng viên dù số trang ít hơn |
| T96 | Thay đổi một `Table Style` dùng chung khiến bảng khác đổi viền/width | FAIL blast radius; sửa cục bộ hoặc giữ gốc |

**Kết quả tổng:** V1–V4: T01–T80; V5 bổ sung T81–T96 → **96 kịch bản kiểm thử được mô tả/đề xuất**. Con số này **không có nghĩa 96 bài test đã được tự động hóa hoặc chạy PASS**.

## 106. Mẫu biên bản quyết định định dạng một bảng

Bản ghi đầu ra không được chỉ trả `new widths`; phải giải thích tại sao. Ví dụ **schema tham khảo**, chưa phải API hoặc cấu trúc đã triển khai:

```yaml
version: V5-PROPOSAL
source:
  document_kind: PARTY
  rule_profile: PARTY_HD05
  official_template: NONE
  section_orientation: PORTRAIT
  renderer: NONE
  print_mode: TWO_SIDED
  sensitive_data_policy: DO_NOT_PERSIST

table:
  locator: 'ephemeral in-session identifier'
  kind: ACTION
  owner: BODY
  task: TRACK_ACTION
  evidence: HEADER_STRUCTURE
  ambiguity: []

baseline:
  width_twips: [510, 2760, 1900, 1220, 1200]  # tổng 7590
  rendered: false

constraints:
  locked_grid_columns: []
  gridspan_constraints: []
  target_width_twips: 7590  # minh họa, KHÔNG phải giá trị A4 mặc định

candidate:
  width_twips: [510, 2890, 1770, 1220, 1200]  # tổng 7590
  hard_gates: PENDING_RENDER
  measured_benefit: NOT_AVAILABLE

decision:
  action: REPORT_ONLY
  result: UNVERIFIED_LAYOUT
  reason: 'No target renderer evidence; cannot assert improvement'
  modifications_performed: 0
```

Một tài liệu có thể có nhiều bảng thuộc các owner khác nhau; mỗi quyết định gắn với một bảng và section/part cụ thể. Hồ sơ không được lưu toàn bộ nội dung bảng vào log chỉ để giải thích lựa chọn width; ưu tiên mã vai trò, số liệu tổng hợp đã loại nội dung nhạy cảm, fingerprint cục bộ theo chính sách.

## 107. Lộ trình dùng báo cáo V5 để thực thi thực tế mà không xây lại hệ thống

### 107.1. Bước audit trước khi viết mã

1. Xác định dự án/nhánh/HEAD thực tế và các contract đã `PASS/LOCKED`.
2. Tìm module DOCX parser, table topology, capability gateway/permission, preview, save/download, so sánh before/after, fixture và CI hiện có.
3. Kiểm tra có quyền sử dụng Microsoft Word native/Office.js hoặc renderer tương đương nào trong môi trường đích; không giả định trình duyệt có engine dàn trang Word.
4. Lập bảng `REUSE LOCAL → EXTEND LOCAL → REUSE DEPENDENCY/API → OFFICIAL/NATIVE → OSS → MINIMUM NEW CODE`, ghi bằng chứng `FOUND/MISSING/UNKNOWN`.
5. Nếu cơ chế đọc và sửa bảng đang ổn, chỉ thêm **policy, chứng cứ, chặn rủi ro** và các hook nhỏ trong đường đi đã có; không tạo implementation song song.

### 107.2. Phân kỳ tối thiểu có điều kiện

| Giai đoạn | Công việc | Gate để chuyển bước |
|---|---|---|
| P0-A | Audit, catalog các bảng, đo khả năng bảo toàn parser/OOXML | Biết rõ capability và ca không hỗ trợ |
| P0-B | `NO_OP`, phân loại role, kích thước vùng in, locks, các cảnh báo | Không thay nội dung, kết quả quyết định deterministic |
| P0-C | Sinh 2–3 đề xuất width **không ghi file**; xem lý do và bằng chứng | Đối chứng gốc rõ, ngưỡng/giới hạn có thể kiểm |
| P1-A | Áp dụng có xác nhận vào bản sao và package diff | Không mất nội dung/topology/relationship |
| P1-B | Renderer comparison khi khả dụng; xử lý vùng downstream | Đạt gate visual trong môi trường đã công bố |
| P2 (chỉ nếu chứng minh cần) | Calibrate ngưỡng, UI preview trước-sau, benchmark đa dạng | Lợi ích thực tế vượt chi phí và không tăng blast radius |

Nếu không có Word renderer/preview đáng tin cậy, có thể vẫn giao **báo cáo phân tích và đề xuất** nhưng **không được gọi là tự động tối ưu bảng đã nghiệm thu**.

### 107.3. Điều kiện nghiệm thu V5

- **G-PROFILE:** đúng chế độ văn bản, mẫu và thời điểm áp dụng.
- **G-INTENT:** trọng tâm cột có bằng chứng; bất định được báo, không tự dựng câu trả lời.
- **G-TOPOLOGY:** lưới/cột/ô gộp/bảng lồng được nhận đúng hoặc bị chặn đúng.
- **G-INTEGRITY:** dữ liệu, đối tượng, relationship và những phần ngoài phạm vi không thay đổi.
- **G-GEOMETRY:** phân bổ twip khớp giới hạn từng section/điều kiện khóa.
- **G-RENDER:** không tràn/cắt/xô lệch ngoài kiểm soát khi đã yêu cầu kiểm Word thực tế.
- **G-PAGE:** caption, tiêu đề, chữ ký, phụ lục và section downstream không bị hỏng.
- **G-DECISION:** lợi ích so baseline có thể giải thích; khi không chứng minh, chọn NO_OP/REVIEW.
- **G-IDEMPOTENCE:** áp dụng lại không làm phát sinh diff ngoài ý muốn.
- **G-SCOPE:** chỉ dùng quyền đã được xác nhận; không đẩy tài liệu/lưu ảnh/trích đoạn sang nơi không được phép.

### 107.4. Kết luận chuyên đề V5

**Độ rộng tốt nhất không phải vector chiều rộng được tính ra nhiều chữ số nhất**. Đó là phương án thỏa điều kiện bắt buộc, thể hiện đúng thông tin trọng tâm, dùng hợp lý không gian trang, không tạo dòng/hàng/trang bất thường, bảo toàn tài liệu và có bằng chứng thực tế. Khi chưa có đủ dữ liệu hoặc bằng chứng render, **không thay đổi** là quyết định chuyên nghiệp hơn một can thiệp không được kiểm chứng.

**Trạng thái tại 20/10/2026:** V5 mới hoàn thành ở cấp **nghiên cứu và đặc tả định dạng**. Bộ kịch bản, thuật toán, ngưỡng và checklist ở đây chưa đồng nghĩa có công cụ thực thi, fixture đã đo hoặc nghiệm thu trên Microsoft Word thật.

# PHẦN XXII. NÂNG CẤP V6 — QUY TRÌNH HIỆU CHỈNH, BENCHMARK TÁI LẬP VÀ NGHIỆM THU TỐI ƯU BẢNG

> **Tính chất:** Đây là phần **đặc tả nghiên cứu/đề xuất [KN][KT][BK]**, không phải bộ định dạng đã triển khai và cũng không phải tiêu chuẩn có hiệu lực pháp lý. Kế thừa các phần I–XXI. Chỉ tạo phép kiểm mới cho khoảng trống thực sự chưa được bao phủ; tái dùng toàn bộ phép kiểm và kết quả đã PASS nếu hợp đồng hành vi không thay đổi. Căn cứ nguồn kỹ thuật và khả năng tiếp cận: [S58]–[S65].

## 108. Khoảng trống thực chất của V5 và phạm vi V6

V5 đã nêu được *khi nào* nên xem xét chỉnh độ rộng cột, *tại sao* phải giữ gốc trong nhiều trường hợp và *bằng chứng* cần có. Để một nhóm phát triển có thể triển khai rồi nghiệm thu khách quan, vẫn cần xác định **cách tổ chức mẫu chuẩn, cách chọn ngưỡng, cách đo lợi ích, cách xử lý dao động kết xuất và hợp đồng không gây hồi quy**.

V6 tập trung sáu kết quả:

1. **Fixture độc lập với implementation:** mô tả tình huống, quyền sửa, oracle và môi trường, không lấy chính thuật toán đang thử làm đáp án chuẩn.
2. **Thước đo ở cấp hàng/bảng/trang và cột trọng tâm:** tách chỉ số kỹ thuật đo được khỏi chấm thẩm mỹ chủ quan.
3. **Quy tắc hiệu chỉnh ngưỡng:** không lựa chọn 0,5 mm, 1 trang hay 5% lợi ích như hằng số “chuẩn” khi chưa có thực nghiệm; tiền định quy trình đo và phê chuẩn.
4. **Quy tắc quyết định bảo thủ, có giới hạn không chắc chắn:** chỉ APPLY khi hard gates PASS, lợi ích vượt ngưỡng đã hiệu chỉnh và bằng chứng đủ độ tin cậy.
5. **Ma trận nghiệm thu tối thiểu:** chứng minh cả ba hành vi `APPLY`, `KEEP_EXISTING`, `REVIEW/BLOCK`, tránh một hệ thống chỉ giỏi sửa hoặc chỉ giỏi từ chối.
6. **Bộ hồ sơ bàn giao:** JSON manifest, bảng chấm ứng viên, mã lý do và checklist review có thể được tái sử dụng mà không buộc tạo framework mới.

**Ngoài phạm vi:** viết lại parser/renderer hiện có; thay đổi Locked Core; thay mẫu văn bản chính thức; tạo dịch vụ AI mới; chuẩn hóa nội dung/số liệu; xây infrastructure/DB phục vụ benchmark; tuyên bố Microsoft Word render giống hoàn toàn Word Online, LibreOffice và các phiên bản khác.

## 109. Mô hình quyết định hai tầng: hợp lệ trước, chất lượng sau

### 109.1. Tầng A — Hard gates không được đánh đổi

Ứng viên chỉ được xếp điểm khi vượt **tất cả** cổng áp dụng:

| Gate | Bằng chứng yêu cầu | Kết quả khi không đạt |
|---|---|---|
| A01 `AUTHORITY` | Profile đúng văn bản, section, mẫu/biểu mẫu có hiệu lực, quyền sửa đã xác định | `REVIEW` hoặc `BLOCK` |
| A02 `SCOPE` | Chỉ thay thuộc tính cho phép; không sửa Core/part khác | `REJECT` |
| A03 `STRUCTURE` | Số bảng, owner, hàng, grid columns, physical cells, spans, nesting, thứ tự block phù hợp baseline | `REJECT` |
| A04 `CONTENT` | Text/runs/whitespace có nghĩa, số liệu, ảnh, field, bookmark, hyperlink, relationships bất biến | `REJECT` |
| A05 `SIGNATURE/PROTECTION` | Không có chữ ký số hay khóa bảo vệ bị ảnh hưởng; chữ ký số hợp lệ không được vô hiệu hóa | `BLOCK` |
| A06 `GEOMETRY` | Vùng in của section/cell, các cột bị khóa, width sum và ảnh hưởng indent được kiểm | `REJECT` |
| A07 `VISUAL` | Không xuất hiện clipping/overlap/đè nội dung; kiểm cùng renderer mục tiêu nếu quyết định dựa vào layout | `UNVERIFIED` hoặc `REJECT` |
| A08 `READABILITY` | Mã, ngày, số, trường quyết định và tiêu đề vẫn phân biệt/đọc đúng | `REJECT` |
| A09 `DOWNSTREAM` | Không gây tác động ngoài phạm vi được duyệt tới caption, chữ ký, footnote và section kế tiếp | `REVIEW` hoặc `REJECT` |
| A10 `OUTPUT` | File mở lại được; gói OPC và chế độ phát hành đích đạt gate tương ứng | `REJECT` |

**Bổ sung cần ưu tiên:** tài liệu có chữ ký số. Microsoft ghi nhận tài liệu được ký số sẽ trở thành chỉ đọc nhằm ngăn thay đổi. Sửa và xuất một bản khác có thể phá tính xác thực của chữ ký, vì vậy không được coi thay đổi định dạng là an toàn đối với tài liệu đã ký. [S59]. Kiểm tra ngay từ lúc inspect; **không** đề xuất vô hiệu chữ ký hoặc bỏ bảo vệ để tiếp tục.

**Lưu ý:** validator OOXML xác nhận lỗi theo cấu trúc/schema trong phạm vi công cụ hỗ trợ, **không chứng minh** văn bản hiển thị đẹp hay không bị cắt; render gate là một phép kiểm khác. [S58].

### 109.2. Tầng B — Lexicographic ranking sau hard gates

Thứ tự lựa chọn mặc định (có thể điều chỉnh dưới profile, nhưng không thay thứ tự cổng A):

1. Bảo vệ trường trọng tâm `critical_visibility` và các ngưỡng tối thiểu của từng vai trò cột.
2. Giảm lỗi bố cục tồn tại từ baseline; không khuyến khích việc “thu ngắn bảng” nếu làm mất khả năng đọc.
3. Giảm số hàng bị ngắt vụn, số chỗ khó đọc, tổng chiều cao/pagination **trên phần vùng ảnh hưởng**, không tối ưu riêng một ô.
4. Giữ nhất quán preset, tỷ lệ khoảng trắng và đường viền tương ứng loại bảng.
5. Chọn phương án ít thay đổi `L1` theo twips, ít thay thuộc tính và ít động chạm các phần tử nhất.
6. Nếu hòa hoặc bằng chứng chưa vững: chọn `KEEP_EXISTING`.

Các điểm thẩm mỹ là tiêu chí **xếp hạng ứng viên đã an toàn**, không phải điểm thưởng để bù vi phạm pháp lý, thay đổi dữ liệu hay phá chữ ký.

## 110. Thiết kế bộ benchmark có thể tái lập

### 110.1. Một fixture cần lưu những gì?

Mỗi fixture là **một nguồn DOCX được phép sử dụng** cộng với một manifest chứa dữ kiện tối thiểu cần thiết. Không bắt buộc tạo lại file nếu đã có fixture dự án và bằng chứng tương ứng.

| Trường | Bắt buộc? | Ý nghĩa |
|---|---|---|
| `fixture_id` | Có | Mã ổn định, không tiết lộ nội dung |
| `fixture_version` | Có | Phiên bản mẫu được khóa khi chấm |
| `source_sha256` | Có | Hash của file gốc để tránh nhầm mẫu; không dùng thay checksum content |
| `source_provenance` | Có | `SYNTHETIC`, `PUBLIC_LICENSED`, `AUTHORIZED_PRIVATE` |
| `table_locator` | Có | Quan hệ part + chỉ mục bảng + owner path trong fixture |
| `document_profile` | Có | `ND30`, `PARTY_HD05`, `SPECIAL_FORM`, `UNKNOWN` |
| `legal_template_lock` | Có | Mẫu chính thức và trường/cột bị khóa |
| `reader_task` | Có | Tác vụ người đọc đã được phê chuẩn trong fixture |
| `critical_columns` | Có, có thể rỗng | Cột trọng tâm và bằng chứng lựa chọn |
| `allowed_changes` | Có | Whitelist thuộc tính format-only được phép thay |
| `renderer_target` | Có nếu chấm hiển thị | Word/phiên bản/build, hệ điều hành, khổ trang, font |
| `baseline_observations` | Có | Lỗi/thế mạnh của bảng gốc, độc lập với ứng viên |
| `expected_decision_class` | Có | `APPLY_CANDIDATE`, `KEEP_EXISTING`, `REVIEW`, `BLOCK` |
| `acceptance_oracles` | Có | Điều kiện đọc được, bảo toàn, vùng in, trang, đặc tính đặc biệt |
| `owner_approval` | Khi dùng file thật | Bằng chứng quyền dùng file/phạm vi xử lý |

Không đưa tài liệu riêng tư vào git, log, báo cáo hoặc kho benchmark công khai. `sha256` của file cũng có thể là metadata nhạy cảm trong một số ngữ cảnh: chỉ lưu trong phạm vi cho phép, có chính sách vòng đời; ưu tiên fixture dữ liệu tổng hợp.

### 110.2. Ma trận tối thiểu để chọn mẫu

Không cố nhân tích Descartes tất cả chiều vì sẽ bùng nổ. Chọn **pairwise + các ca nguy hiểm trọng điểm**, tái sử dụng fixture đã có:

| Chiều | Nhóm đại diện | Cần ưu tiên |
|---|---|---|
| Authority | NĐ30 / HD05 / mẫu chuyên ngành / chưa xác định | Mỗi hệ một trường hợp có ràng buộc khác nhau |
| Bảng | Hành động / thống kê / danh bạ / nhiều cấp / form / layout / nested | Chọn theo rủi ro và tần suất thực tế |
| Chiều rộng | Vừa / thiếu nhẹ / thiếu nghiêm trọng / vô nghiệm | Có baseline tốt + trường hợp không được sửa |
| Nội dung | Ngắn / dài / Unicode tiếng Việt / URL, mã không ngắt / số thập phân | Ít nhất một ca text width không bằng số ký tự |
| Trang | Dọc / ngang / nhiều section / in hai mặt / nhiều trang | Có case ranh giới caption, chữ ký |
| OOXML | AutoFit / Fixed / gridSpan / vMerge / omitted cells / style cascade | Chú ý ô vật lý và inherited style |
| Mức rủi ro | Mẫu cố định / Track Changes / AlternateContent / có chữ ký số | Phải biết chặn hoặc cảnh báo chính xác |
| Renderer | Sẵn có / thiếu / khác phiên bản/font | Không cộng nhầm `UNVERIFIED` vào PASS |

**Tỷ lệ mẫu khuyến nghị để bắt đầu thử nghiệm (chưa phải chuẩn cứng):** khoảng 1/3 mẫu baseline vốn tốt, 1/3 mẫu có cải thiện hợp lệ, 1/3 mẫu cần review/block. Chỉ điều chỉnh sau khi biết phân bố bảng thực tế; không dùng phân bố benchmark để giả định tỷ lệ lỗi trên tài liệu người dùng.

### 110.3. Khóa tập hiệu chỉnh và tập nghiệm thu

- **Calibration set:** dùng để chọn ngưỡng, sửa lỗi thực thi và quan sát phương sai.
- **Holdout acceptance set:** đóng băng trước khi chọn ngưỡng, dùng đánh giá cuối. Khi phát hiện bug ở holdout, ghi bug và ca tái hiện; chỉ mở lại bài đo sau khi khai báo thay đổi, không âm thầm điều chỉnh ngưỡng cho vừa kết quả.
- **Adversarial set:** các bảng góc cạnh hoặc chưa hỗ trợ, tiêu chí chính là phản ứng chặn an toàn.
- Đặt `dataset_revision`, `manifest_revision`, `renderer_fingerprint`, `rule_profile_revision`. Đối chiếu cùng revision khi so sánh hai kết quả.

## 111. Các phép đo hữu ích và giới hạn diễn giải

### 111.1. Định nghĩa phép đo, phân biệt proxy với truth

| Chỉ số | Cách đo/đánh giá | Tầng tin cậy | Không suy diễn |
|---|---|---|---|
| `overflow_count` | Vùng bounding box thật so với vùng khả dụng (nếu có khả năng đo đáng tin) | M2/M3 | Không dùng riêng `tblW` chứng minh không tràn |
| `clipped_cell_count` | Kiểm nhận cắt/che chữ khi render và đối chiếu content | M2/M3 | Pixel diff thô không đủ |
| `critical_unreadable_count` | Review các trường trọng tâm theo rubric có hướng dẫn | M2 + human | Độ dài string không phải độ dễ đọc |
| `row_fragment_count` | Số hàng bị chia gây khó theo dõi trên bản in đích | M2/M3 | Không phải mọi chia hàng đều là lỗi |
| `header_context_loss` | Mất tiêu đề và ngữ cảnh trên các trang tiếp | M2/M3 | `tblHeader` có mặt chưa chắc mọi ca đều lặp |
| `table_page_footprint` | Vùng/chiều cao/số trang bảng chiếm trong section | M2/M3 | Ít trang hơn chưa chắc tốt hơn |
| `downstream_displacement` | Vị trí các khối ngay sau bảng và trang/section bị tác động | M2/M3 | Dịch trang hợp lệ có thể được duyệt |
| `style_consistency` | Đối chiếu những thuộc tính được phép với preset | M0/M2 | Không ghi đè biểu mẫu |
| `width_change_L1` | Tổng trị tuyệt đối chênh lệch độ rộng các cột lưới (twips) | M0 | Ít đổi width không đồng nghĩa đẹp |
| `reader_preference` | Cặp ảnh trước/sau, đánh giá mù có rubric | Human/M2 | Không được thắng hard gates |

### 111.2. Cảnh báo đặc biệt với phép đo ở cấp hàng

Với hàng không gộp dọc, `H_row` phụ thuộc chủ yếu ô có chiều cao chi phối. Khi có `vMerge`, một cụm ô có thể trải nhiều hàng, nên không thể gán đơn giản toàn bộ chiều cao cụm vào riêng một hàng. Do đó dùng dữ liệu render (nếu có), giữ quan hệ row-span thực, **không** dùng tổng độc lập số dòng từng ô để khẳng định bảng sẽ giảm chiều cao bao nhiêu.

### 111.3. Xử lý sai số và thay đổi renderer

Không đặt `pixel-diff = 0` làm điều kiện duy nhất, vì anti-aliasing, font rasterization và cách khử răng cưa có thể thay đổi. Thay vào đó, kiểm đồng thời:

1. Diff cấu trúc/ký tự/bất biến phạm vi sửa: *phải* đạt.
2. Các vùng ảnh hưởng: đường biên bảng, nội dung trọng tâm, tiêu đề, khối ngay sau bảng.
3. Kết quả đo không ổn định: chạy lại đối chứng trong **cùng môi trường**; nếu baseline chính nó dao động thì đánh dấu `MEASUREMENT_UNSTABLE`.
4. Renderer khác: công bố là **môi trường khác**; không gộp số liệu vào mẫu cùng fingerprint.

Microsoft chỉ mô tả kiểm tra Open XML theo schema; Word bảo đảm tính năng lặp hàng tiêu đề cho trường hợp phù hợp và ghi nhận ngoại lệ ngắt trang thủ công. [S58], [S61]. Không có một API Microsoft được xác minh ở đây có thể cam kết đo chính xác đầy đủ layout Word của mọi file trong mọi môi trường, vì vậy **phải audit capability thực tế** trước khi đặt các chỉ số M2 bắt buộc.

## 112. Ngưỡng hiệu chỉnh và kiểm chứng lợi ích thực sự

### 112.1. Không mã hóa sớm các ngưỡng tùy ý

V5 đề xuất “lợi ích vượt mức tối thiểu” nhưng chưa chứng minh con số nào là hợp lý. V6 quy định cách hiệu chỉnh thay vì phát minh chuẩn:

1. Chốt renderer/font/page settings và chọn calibration set có baseline tốt, baseline xấu, baseline vô nghiệm.
2. Đo lại baseline nhiều lượt để ước lượng biến thiên kỹ thuật của chỉ số quan sát; không cần đo hàng loạt nếu phép đo vốn deterministic đã được chứng minh.
3. Tạo ít ứng viên từ thuật toán đã có, bao gồm phương án giữ nguyên làm đối chứng.
4. Người thẩm định đánh giá cặp baseline–candidate **không biết phương án nào do hệ thống sinh**; thứ tự A/B đảo ngẫu nhiên trong nghiên cứu nếu phù hợp.
5. Chọn `minimum_meaningful_improvement` đủ lớn để vượt sai số đo và được đánh giá là dễ đọc hơn trên tập hiệu chỉnh. Lưu quyết định chọn ngưỡng cùng version.
6. Khóa ngưỡng **trước** khi chạy holdout; không sửa ngưỡng dựa vào kết quả holdout nếu vẫn tuyên bố đó là kiểm chứng độc lập.
7. Nếu dữ liệu không chứng minh cải thiện ổn định, mặc định `REPORT_ONLY` hoặc `KEEP_EXISTING`.

Các giá trị 0,5 pt đường kẻ, 1,5 mm đệm ô, 5% lợi ích, 1 trang giảm hay 90/100 điểm **không trở thành quy định pháp lý** chỉ vì được ghi vào preset hoặc báo cáo. Ngưỡng phải gắn với `(metric_id, unit, renderer_fingerprint, fixture_revision, calibration_method, approved_by)`.

### 112.2. Quy tắc lợi ích và quyết định theo khoảng bất định

Với thước đo lỗi (càng nhỏ càng tốt), đặt `benefit = cost_baseline - cost_candidate` sau khi chuẩn hóa theo cùng phạm vi. Nếu ứng viên có khoảng bất định `[b_low, b_high]`:

- `b_low > threshold` **và** tất cả hard gates PASS ⇒ có thể `PROPOSE_APPLY` (chưa tự ý sửa khi chưa có quyền).
- `b_high <= threshold` ⇒ `KEEP_EXISTING` nếu baseline đã hợp lệ; nếu baseline lỗi chưa khắc phục ⇒ `REVIEW`/`NO_FEASIBLE_LAYOUT`.
- Khoảng cắt qua threshold ⇒ `UNDECIDED_REVIEW`; không tuyên bố chắc chắn cải thiện.
- Không có renderer ⇒ **không suy ra** khoảng lợi ích layout thực; giữ quyết định ở mức `M0/M1`.

**Không bắt buộc bootstrap/phương pháp thống kê nặng** cho mọi tài liệu; chọn cách đo phù hợp phạm vi dữ liệu và mức lặp thực tế. Mục đích là chống việc quyết định từ sai số đo hoặc khác biệt kết xuất không có ý nghĩa.

## 113. Quy tắc phân bổ width ở mức thực thi và minh họa kiểm tra toán học

### 113.1. Bài toán dưới đơn vị nguyên twips

Giả sử một bảng có `n` grid columns, tổng vùng phân bổ nội bộ sau xét indent/spacing là `W` twips. Chọn `w_i` nguyên không âm và `l_i <= w_i <= u_i`:

```text
Σ(w_i) = W                      # bảo toàn tổng độ rộng phân bổ
w_i = w0_i nếu locked(i)        # cột bị khóa không thay đổi
Σ(w_i for i in span) >= L_span # ngưỡng tối thiểu đối với một nhóm gridSpan
hard_gates(w) = PASS           # dữ liệu/structure/form/renderer
```

Nếu có chính sách không sử dụng hết vùng in, thay `Σw_i=W` bằng `Σw_i<=W` và thêm penalty cho khoảng trống thừa; **không tự động kéo rộng tất cả bảng đến mép vùng in**. Nếu chọn bảng lồng, `W` phải được tính từ ô chứa thực. Các mức `l_i`, `u_i` là ràng buộc *được xác định/hiệu chỉnh*, không phải kết quả AI tự đoán.

### 113.2. Ví dụ cân đối 5 cột (giả lập để chứng minh logic, chưa render)

| Vai trò | Baseline (mm) | Ứng viên (mm) | Nhận xét |
|---|---:|---:|---|
| STT | 11 | 11 | Khóa |
| Nội dung nhiệm vụ | 78 | 72 | Có thể xuống dòng hợp lý nếu không làm hàng cao hơn |
| Người phụ trách | 36 | 41 | Tăng chỗ hiển thị tên không thể cắt |
| Hạn | 22 | 23 | Bảo vệ ngày tháng |
| Kết quả | 18 | 18 | Giữ đủ giá trị trạng thái |
| **Tổng** | **165** | **165** | Bảo toàn tổng, chỉ minh họa phân phối |

Chưa thể gọi ứng viên này “tối ưu” vì **chưa có** dữ liệu đo số dòng/chiều cao của ô `Nội dung nhiệm vụ` sau khi bớt 6 mm hoặc khả năng đọc cột `Người phụ trách` được cải thiện thực. Nếu nội dung nhiệm vụ tăng thêm một dòng ở nhiều hàng, ứng viên có thể xấu hơn; quy trình cần đo cả hai. Không dùng ví dụ này làm tỷ lệ cột mặc định cho tất cả bảng.

### 113.3. Tie-break và tính lặp lại

Khi hai ứng viên đạt tương đương theo ngưỡng hiệu chỉnh:

1. Ưu tiên baseline nếu baseline không có lỗi.
2. Nếu baseline có lỗi cần sửa, chọn ứng viên sửa **ít ô/cột/thuộc tính** hơn.
3. Nếu bằng nhau, chọn `Σ|w_i-w0_i|` nhỏ hơn.
4. Cuối cùng chọn thứ tự ổn định theo `candidate_id` để kết quả deterministic; không cần AI làm trọng tài.
5. Chạy lại sau khi áp dụng; nếu engine đã ổn định mà file bị thay đổi tiếp khi cùng cấu hình ⇒ báo `NON_IDEMPOTENT`.

## 114. Bốn loại oracle và mức nghiệm thu có thể công bố

| Oracle | Loại kết luận được phép | Không được thay thế |
|---|---|---|
| O1 `STRUCTURAL` | Có giữ nội dung, topology, package, chỉ sửa thuộc tính whitelist? | Kiểm tra bố cục Word |
| O2 `SEMANTIC` | Các cột trọng tâm/giới hạn đã xác định đúng, có chứng cứ? | Tuyên bố vẻ đẹp bằng mắt người |
| O3 `VISUAL_TARGET` | Có đọc được, không cắt/tràn/đè, ngắt trang phù hợp trên renderer được kiểm? | Bảo toàn relationship nếu không xét O1 |
| O4 `HUMAN_REVIEW` | Bản nào dễ đọc hơn theo rubric, có bất đồng không? | Điều kiện pháp lý và tính hợp lệ package |

**Công bố trạng thái chuẩn:**

- `PASS_STRUCTURAL_ONLY`: đạt O1/O2; thiếu O3. Không gọi là tối ưu hiển thị hoàn thành.
- `PASS_TARGET_RENDER`: đạt O1/O2/O3 trong môi trường công bố.
- `PASS_USER_ACCEPTED`: qua O1/O2/O3 và phê duyệt nếu workflow yêu cầu.
- `PASS_PDF_TARGET`: vượt cổng riêng cho đầu ra PDF yêu cầu; không tự suy từ Word.
- `NO_OP_VALID`: baseline hợp lệ/không có ứng viên tốt hơn được chứng minh.
- `UNVERIFIED`: không đủ chứng cứ cho loại kết luận được yêu cầu.
- `FAIL/ROLLBACK`: bất kỳ hard gate bắt buộc thất bại.

**Một bản Word và một bản PDF là hai vật chứng khác nhau.** Với yêu cầu tiếp cận tài liệu phi web, hướng dẫn WCAG2ICT (W3C Group Note, 11/12/2025) chỉ giúp diễn giải nguyên tắc; đây là tài liệu **informative, không đặt ra chuẩn tuân thủ mới**. Chính W3C ghi nhận một số nội dung như bảng dữ liệu có thể cần bố cục hai chiều, và khả năng reflow phụ thuộc định dạng/trình đọc. [S60].

## 115. Tổ chức kiểm định thực tế, người đánh giá và tránh thiên lệch

### 115.1. Ma trận phương pháp phù hợp quy mô

| Mục tiêu | Phương pháp đủ dùng | Điều không cần làm nếu không có nguy cơ |
|---|---|---|
| Thuộc tính chỉ thay trong một bảng | Diff part XML liên quan + đối chiếu checksum đối tượng | Test lại mọi module ứng dụng |
| Dữ liệu/quan hệ không mất | Snapshot invariant được phép + mở lại DOCX | Chuyển toàn bộ DOCX qua hệ cơ sở dữ liệu mới |
| Chọn width tốt hơn | Paired baseline/candidate trên cùng renderer | Đánh giá trên nhiều OS nếu sản phẩm chỉ hỗ trợ một renderer đã công bố |
| Thẩm mỹ | 2 người đánh giá khi đủ nguồn lực; làm mù nguồn A/B; ghi bất đồng | Dùng điểm AI thay cho người và hard gates |
| Tình huống chưa hỗ trợ | Kiểm có `BLOCK/REVIEW` rõ và không ghi file | Ép xây thêm subsystem để auto-fix |

**Hướng dẫn rubric đề xuất (mỗi tiêu chí 0–2, không có ý nghĩa pháp lý):** (a) đọc được thông tin quyết định; (b) không có cột mất cân đối dễ thấy; (c) ngắt dòng và chiều cao hàng hợp lý; (d) phân trang giữ ngữ cảnh; (e) kiểu viền/khoảng trắng trang trọng. Không chấm nếu hard gate đã FAIL. Người đánh giá phải nhìn cùng kích thước zoom hoặc bản in chuẩn; mẫu có dữ liệu giả lập không được biến thành bằng chứng tính đúng nghiệp vụ thực tế.

### 115.2. Quy tắc xử lý bất đồng

- Hai người thống nhất ứng viên hơn baseline và O1–O3 PASS: đủ điều kiện `PROPOSE_APPLY` khi threshold đã phê chuẩn.
- Một người thích baseline, một người thích ứng viên: `INCONCLUSIVE` → giữ nguyên hoặc review; không lấy trung bình làm bằng chứng chắc chắn.
- Cùng đánh giá tốt nhưng ứng viên làm thay đổi phân trang ngoài phạm vi duyệt: hard gate thắng, `REJECT/REVIEW`.
- Có bất đồng liên quan mẫu pháp lý, chuyên viên phụ trách mẫu được ưu tiên xác nhận **điều kiện hợp lệ**, không dùng vote thẩm mỹ để thay nguồn authority.

## 116. Ma trận xử lý lỗi và quản lý kết quả không áp dụng

| Mã lý do | Tình trạng | Hành động an toàn | Có sửa DOCX không? |
|---|---|---|---|
| `R_SIGNED` | Có chữ ký số | `BLOCK`, bảo toàn bản gốc; hướng dẫn thao tác theo quy trình ký hợp lệ bên ngoài | Không |
| `R_LOCKED_FORM` | Biểu mẫu/ô ký/kích thước khóa | `PRESERVE_FORM` | Không |
| `R_UNSUPPORTED_MARKUP` | `AlternateContent`, revision hoặc object chưa bảo toàn được | `BLOCK`/`REVIEW` | Không |
| `R_NO_RENDERER` | Không có phép đo đầu ra đích | `REPORT_ONLY`, nêu mức M0/M1 | Không sửa tự động theo tiêu chí “đẹp hơn” |
| `R_UNDERCONSTRAINED` | Thiếu task/critical columns/authority | `REVIEW` | Không |
| `R_NO_FEASIBLE` | Tổng ngưỡng tối thiểu vượt vùng in | `NO_FEASIBLE_LAYOUT`, đề xuất phương án khác cần duyệt | Không |
| `R_NO_MATERIAL_GAIN` | Có ứng viên nhưng lợi ích dưới ngưỡng/sai số | `KEEP_EXISTING` | Không |
| `R_VISUAL_REGRESSION` | Mất chữ/ngắt trang/đè nội dung mới | `REJECT`, rollback | Không phát hành bản ứng viên |
| `R_PACKAGE_DIFF` | Thay đổi ngoài whitelist hoặc mất relationship | `REJECT`, rollback | Không phát hành |
| `R_RENDER_DIVERGENCE` | Hai môi trường đích cho kết quả khác | `REVIEW`, thu hẹp phạm vi tuyên bố | Chỉ khi chính sách đích cho phép |

Một báo cáo tốt phải nói rõ cả *vì sao không sửa*. Điều này ngăn phần mềm ép mọi bảng vào preset và làm biến dạng những bảng vốn đúng.

## 117. Bộ kiểm thử bổ sung V6 (T97–T108), tái dùng 96 ca trước đó

> **12 tình huống mới được ĐỀ XUẤT**, chưa thực thi. Không tạo 12 test vật lý mới nếu fixture và contract hiện có đã bao phủ; đây là danh mục kiểm tra khoảng trống V5, dùng dedup theo intent/expected behavior.

| ID | Thay đổi/ngoại lệ cần chứng minh | Oracle kỳ vọng |
|---|---|---|
| T97 | File DOCX đã có chữ ký số, yêu cầu format-only | `BLOCK`, bản gốc không bị sửa, có `R_SIGNED` |
| T98 | OOXML schema PASS nhưng một ô mất chữ khi in | O1 PASS riêng; O3 FAIL; kết quả chung không PASS |
| T99 | Mẫu baseline đẹp, thử ba ứng viên đều chỉ đổi dưới mức ngưỡng | `NO_OP_VALID`; log quyết định không ghi nội dung thật |
| T100 | Ứng viên A giảm chiều cao 10% nhưng mất ngữ cảnh cột quyết định | Hard gate readability FAIL; không chọn A |
| T101 | Một cột tăng width nhưng hàng cao nhất chuyển từ cột khác sang cột này | Đánh giá H hàng sau render, không tối ưu từng cột độc lập |
| T102 | Hai ứng viên khác biệt nhỏ hơn dao động baseline render | `MEASUREMENT_UNSTABLE`/`UNDECIDED_REVIEW` |
| T103 | Calibration chọn threshold, holdout cho kết quả trái dự đoán | Ghi FAIL/không đạt; không sửa threshold ngầm |
| T104 | Bảng dữ liệu có ô bị thiếu ở đầu/cuối hàng và ô gộp | Bản đồ physical grid đúng; không điền ô không tồn tại |
| T105 | Tài liệu public sample nhưng license không cho phân phối sửa đổi | Không đưa fixture vào bộ công khai trái quyền sử dụng |
| T106 | Cùng profile chạy tối ưu hai lần trên DOCX đã áp dụng | Không có thay đổi thứ hai ngoài dữ liệu môi trường được phép |
| T107 | Xuất DOCX và tagged PDF, DOCX pass nhưng thẻ bảng PDF sai | Không tuyên bố `PASS_PDF_TARGET` |
| T108 | Ứng viên chạm Table Style dùng chung và gây tác động bảng khác | Fail `SCOPE`; đổi cục bộ hoặc giữ gốc |

**Thống kê cập nhật:** T01–T96 của V1–V5 được **giữ nguyên**; V6 bổ sung danh mục T97–T108, tổng cộng **108 kịch bản được đặc tả**. Đây **không phải** 108 phép thử đã chạy hoặc 108 fixture phải được viết mới. Không dùng số lượng ca để thay bằng chứng thực nghiệm.

## 118. Hợp đồng báo cáo kết quả — bản giao việc tối thiểu

Một quyết định định dạng tối thiểu cần cung cấp:

```yaml
schema_version: 'table-decision-v6-proposal'  # draft, chưa triển khai
fixture_or_session_id: 'ephemeral-id'
legal_profile: 'PARTY_HD05'
owner_path: 'word/document.xml > body > table[2]'
table_kind: 'ACTION'
reader_task: 'TRACK_ACTION'
critical_columns:
  - {grid_col: 3, role: 'DEADLINE', provenance: 'reviewed-header'}
locks:
  signed_document: false
  official_form: false
  fixed_grid_columns: [0]
renderer:
  status: 'NOT_AVAILABLE'
  fingerprint: null
baseline:
  width_twips: [624, 4422, 2041, 1707, 562]
  structural_oracle: 'PASS'
proposal:
  width_twips: [624, 4309, 2154, 1707, 562]
  change_scope: ['w:tblGrid', 'w:tcW-if-consistent']
  render_oracle: 'NOT_EVALUATED'
  expected_gain: 'UNKNOWN'
decision:
  action: 'REPORT_ONLY'
  status: 'UNVERIFIED'
  reason_codes: ['R_NO_RENDERER']
  changes_applied: 0
```

Chú ý: số twips trong ví dụ là dữ liệu minh họa không đại diện cho lề A4 hay width đích cụ thể. `w:tcW-if-consistent` chỉ là chú giải phạm vi xét sửa, **không phải chỉ thị có thể thay mọi `w:tcW` mà không phân tích gridSpan, style và precedence**. Không ghi snapshot toàn bộ cell text vào audit log nếu không có căn cứ nghiệp vụ và quyền lưu trữ.

**Biên bản nghiệm thu từng bảng** nên có: nguồn quy định, ảnh/section trước sau nếu có, contract reader task, trạng thái từng gate, tên và fingerprint renderer, kết quả đo và sai số, quyết định/ý kiến xác nhận, thời điểm đo, checksum bản đầu/cuối, phạm vi file/part sửa. Khi không có Word target renderer, biên bản phải hiện nổi bật `UNVERIFIED_RENDER`; không dùng lời khẳng định “đã tối ưu thẩm mỹ”.

## 119. Audit reuse trước khi đưa đặc tả V6 vào phần mềm

Thứ tự tiếp cận bắt buộc:

1. Audit HEAD/nhánh và bản AGENTS.md/tracker thực tế của repo đích **nếu nhiệm vụ được giao là triển khai**; báo cáo V6 này tự thân không phải bằng chứng đã audit code tại HEAD hiện hành.
2. Tìm bảng/OOXML parser và cách giữ physical grid/spans. Tài liệu chính thức `python-docx` nêu rõ ô gộp, ô thiếu và bảng lồng làm mất giả định ma trận chữ nhật; không nên lặp lại lỗi này ở lớp đo width. [S63].
3. Tìm sẵn snapshot/invariant/rollback renderer, phép so sánh PDF, quyền người dùng, preset và test đã PASS. Tận dụng trực tiếp các thành phần hiện hữu; không tạo oracle, state hay registry song song.
4. Kiểm capability: nếu library chỉ parse DOCX, không ghi nhận nó là Word render engine. Nếu thư viện thay text bằng cách gán chuỗi có nguy cơ mất runs/paragraph cấu trúc, không dùng API đó cho tác vụ format-only; tài liệu `python-docx` xác nhận đặt `cell.text` thay nội dung hiện có bằng paragraph/run mới. [S64].
5. Ghi matrix `REUSE LOCAL / EXTEND LOCAL / DEPENDENCY / OFFICIAL NATIVE / MATURE OSS / ADAPTER / MINIMUM NEW CODE` cùng bằng chứng hiện có. Nếu có module hoạt động tốt không bị ảnh hưởng, giữ nguyên và dùng test/evidence đã PASS.
6. Chỉ khi chưa có cơ chế đo/so sánh khả dụng mới nghiên cứu OSS liên quan với số liệu về maintenance/license/security/dependencies; **không** chọn thêm một converter PDF hay framework document khác chỉ để “tối ưu bảng”.
7. Tạo thử nghiệm nhỏ có thể rollback, ví dụ **chỉ đề xuất width không ghi file**, sau đó kiểm thực trên 2–3 fixture đại diện trước khi mở rộng phạm vi.

### 119.1. Bộ tiêu chí quyết định có nên bổ sung dependency

| Tiêu chí | Câu hỏi phải trả lời |
|---|---|
| Khả năng reuse | Hiện tại đã có helper/API tương đương chưa? |
| Compatibility | Có đọc/ghi OOXML gốc mà giữ `AlternateContent`, styles, relationships, tracked revisions không? |
| Render fidelity | Đo có cùng layout với bản Microsoft Word mục tiêu không, hay chỉ là ước lượng? |
| License | License cho phép mục đích sử dụng, phân phối và môi trường dự án không? |
| Security | Có xử lý offline/không chuyển file nhạy cảm qua bên thứ ba không? |
| Dependency cost | Phải kéo theo engine/fonts/native binary không? |
| Operational cost | Có làm tăng kích thước app, tài nguyên, chi phí cloud và tính khó debug không? |
| Maintenance | Có maintainer, test, releases, API stability thực tế không? |
| Rollback | Có cô lập được module phụ trợ và hoàn nguyên khi lỗi không? |

Kết quả đánh giá nếu thiếu dữ liệu phải để `UNKNOWN`, không biến dự đoán thành chứng cứ. V6 không chỉ định một package mới bắt buộc.

## 120. Definition of Done và thứ tự nghiệm thu đề xuất

| Mốc | Điều kiện được gọi là hoàn tất | Chưa đủ nếu chỉ có |
|---|---|---|
| D0 — Spec | Có source/rule/risk/contract/oracle/status rõ ràng | Danh sách thẩm mỹ chung chung |
| D1 — Fixture | Mẫu đại diện có quyền sử dụng, manifest, baseline, expected class độc lập, checksum | Một vài file DOCX ngẫu nhiên |
| D2 — Decision | Quyết định deterministic, chứng minh `KEEP/REVIEW/BLOCK/APPLY` hợp lý, không sửa ngoài scope | Thuật toán luôn chọn ứng viên mới |
| D3 — Integrity | Sau ghi mở lại DOCX, O1 PASS 100% trên **những ca được tuyên bố hỗ trợ và đã chạy**, có rollback khi fail | Chỉ file không báo lỗi ZIP |
| D4 — Layout | O3 có bằng chứng trên Word/renderer đích đã công bố, không hồi quy ảnh hưởng | XML width đúng hoặc PDF converter khác hiển thị đẹp |
| D5 — Acceptance | Holdout với quy tắc đã khóa; đánh giá người dùng nếu cần; báo cáo PASS/FAIL/UNVERIFIED độc lập | Tự thay threshold sau khi thấy kết quả |

**Các lối thoát chấp nhận được:** `NO_OP_VALID`, `REVIEW_REQUIRED`, `UNSUPPORTED_BLOCKED` vẫn có thể là hành vi đúng cho những ca tương ứng. Không bắt toàn bộ file được áp preset. Tuy nhiên, nếu sản phẩm cam kết **tối ưu tự động** bảng thường, cần có ca APPLY thực sự chứng minh được lợi ích; chỉ ra cảnh báo chưa đủ để tuyên bố đạt năng lực đó.

### 120.1. Chốt các ưu tiên P0/P1/P2 theo blast radius

- **P0:** Hard gates, signed/locked detection, physical-grid integrity, `KEEP_EXISTING`, no-op idempotence; báo cáo mức bằng chứng trung thực.
- **P1:** Benchmark đã có manifest, quyết định width hữu hạn, diff-before/after và render theo môi trường đích được hỗ trợ.
- **P2:** Calibrate trọng số thẩm mỹ, so sánh người dùng và đánh giá khác phiên bản/thiết bị khi có nhu cầu thực tế.

Đây là **ưu tiên triển khai đề xuất**, không phải kết quả đã thực thi. Chỉ chạm những thành phần thực sự cần thay đổi sau audit. Không commit/push/deploy/migrate sản xuất theo một yêu cầu “hoàn thiện báo cáo” đơn thuần.

## 121. Kết luận chuyên đề V6

Bản V6 hoàn thiện logic từ **“biết đề xuất độ rộng cột”** sang **“biết chứng minh có nên thay đổi độ rộng cột hay không”**. Trọng tâm thực tế là:

- Không phá nguồn authority, biểu mẫu, chữ ký số, content và physical-grid topology.
- Chỉ ưu tiên cột khi chứng minh được tác vụ người đọc và giới hạn width, không cấp width chỉ vì cột có nhiều chữ.
- Coi cả baseline `KEEP_EXISTING` là ứng viên cạnh tranh bình đẳng; ưu tiên ít đổi khi chất lượng tương đương.
- Quyết định layout chỉ dựa vào **đầu ra đã đo** của renderer được công bố; XML/schema PASS không phải Word-layout PASS.
- Hiệu chỉnh ngưỡng trên calibration set, khóa trước holdout và lưu môi trường/bằng chứng để tái lập.
- Báo cáo rõ điều kiện `APPLY`, `KEEP`, `REVIEW`, `BLOCK`, `UNVERIFIED`; không ngụy tạo nghiệm thu từ đề xuất.

**V6 đủ làm bộ yêu cầu thiết kế, audit và kế hoạch kiểm chứng; chưa phải bằng chứng phần mềm định dạng bảng đạt tối ưu hoặc đạt 108 ca kiểm thử.**

---

# PHẦN XXIII. NÂNG CẤP V7 — ĐẶC TẢ VẬN HÀNH ĐỂ QUYẾT ĐỊNH, CĂN CHỈNH VÀ NGHIỆM THU ĐỘ RỘNG CỘT

> **Tình trạng:** đặc tả nghiên cứu bổ sung ngày 20/10/2026; chưa có bằng chứng đã triển khai engine, benchmark hay render Word trên tài liệu thực tế. Phần này bổ sung các contract và quy tắc ra quyết định còn thiếu của V6; **không thay thế hoặc phát sinh hệ thống xử lý song song**. Ký hiệu [PL]/[BM]/[KN]/[KT]/[BK] giữ nguyên từ đầu báo cáo. Tài liệu kỹ thuật chính thức mới đối chiếu: [S66]–[S77].

## 122. Audit khoảng trống còn lại: tiêu chí chỉ có tên chưa đủ để vận hành

| Khoảng trống của V6 | Rủi ro thực tế | Nội dung V7 bổ sung | Ranh giới với V6 |
|---|---|---|---|
| `critical_columns` mô tả nhưng chưa có hợp đồng phát hiện tin cậy | Đoán sai cột có thể làm co trường thông tin chính | Bậc bằng chứng, mức tin cậy và quy tắc abstain | Kế thừa mô hình vai trò V3, không tạo classifier bắt buộc |
| Có hard gates nhưng chưa có precedence khi hai gate mâu thuẫn | Cùng bảng nhận hai quyết định trái nhau | Máy trạng thái quyết định và độ ưu tiên reason code | Tái sử dụng gate A01–A10, không nhân đôi authority |
| `preferred width` có thể hiểu nhầm là chiều rộng thật | XML PASS nhưng bảng Word tràn vùng in | Phân biệt đề xuất geometry với đo renderer đích | Mở rộng V4–V6, không thay renderer |
| Chưa quy định cách so sánh bảng có nhiều ô gộp khi đổi grid | Tính hai lần độ rộng một ô trải qua nhiều cột | Mô hình khoảng liên tiếp trên grid + chính sách khóa | Không viết lại parser nếu đã có physical-grid map |
| Viền nhìn không giống thuộc tính viết trực tiếp | Style cascade/xung đột viền ô khiến kết quả khó dự đoán | Khảo sát `tblLook`, `tblStylePr`, `tcBorders`, spacing trước khi sửa | Không bổ sung style mới cho toàn tài liệu |
| Có báo cáo mức đo nhưng chưa nêu hợp đồng danh mục metric | Nhầm proxy chiều rộng với kết luận dễ đọc | Metric catalog, đơn vị, oracle, tình trạng `N/A` | Kế thừa O1–O4, M0–M3 |
| Ngưỡng lợi ích chưa rõ xử lý sai số & tính ổn định | Cứ tối ưu nhiều lần lại dịch cột | Quy tắc dominance, materiality, tie-break, idempotence | Không tuyên bố ngưỡng mặc định là luật |
| Các phép thử mới có nguy cơ trùng test cũ | Tăng số lượng test nhưng không tăng độ phủ | Traceability từng ca T109–T124 đến contract mới | Dùng fixture/test hiện hành nếu đã bao phủ |

**Quyết định kiến trúc V7:** Không tạo engine `TableOptimizerV7` độc lập. V7 là lớp đặc tả cho pipeline hiện hữu: `inspect → resolve authority/locks → suggest → preview → approve → patch → verify`. Nếu dự án chưa có bước nào thì chỉ bổ sung tối thiểu bước thiếu sau audit source. Đặc tả này không phải bằng chứng đã đọc HEAD của một repo cụ thể.

## 123. Hợp đồng nhận diện tác vụ người đọc và cột trọng tâm

### 123.1. Chỉ kết luận từ chứng cứ đủ mạnh

**Các lớp bằng chứng theo mức độ ưu tiên**, không cộng điểm trực tiếp để thay cho kiểm tra:

1. `EXPLICIT_USER`: người dùng chỉ định cột cần nổi bật, thời hạn, kết quả, đối tượng hoặc mục tiêu đọc bảng.
2. `OFFICIAL_FORM`: mẫu ban hành/mẫu đã duyệt xác định cột khóa, nhóm cột, quy cách.
3. `DOCUMENT_CONTEXT`: tiêu đề bảng, tiêu đề mục, đoạn dẫn trước bảng và chú thích chỉ rõ mục đích mà không cần diễn giải tùy tiện.
4. `HEADER_AND_TYPE`: tiêu đề cột cùng kiểu dữ liệu đủ rõ (STT, đơn vị, nhiệm vụ, hạn chót, trạng thái, giá trị...).
5. `DISTRIBUTION_ONLY`: chỉ dựa độ dài, tần suất, loại dữ liệu — **không** đủ tự khẳng định cột nào quyết định nghiệp vụ.

`semantic_priority` và `minimum_readable_width` là **hai đại lượng khác nhau**: cột hạn chót có ưu tiên cao nhưng nhu cầu width nhỏ; cột diễn giải dài có thể cần width lớn nhưng ưu tiên thấp hơn. Không dùng `text.length` hoặc diện tích ô làm proxy duy nhất cho trọng tâm. Không diễn giải nội dung bí mật bằng API bên ngoài nếu không được phép.

### 123.2. Trạng thái quyết định cột

| Trạng thái | Cơ sở | Quyền máy được phép thực hiện |
|---|---|---|
| `CONFIRMED` | Người dùng xác nhận hoặc mẫu có authority | Giữ constraint theo đúng định nghĩa; vẫn cần render gate |
| `GROUNDED` | Tiêu đề và ngữ cảnh độc lập cùng hỗ trợ một ý nghĩa | Đề xuất, cho phép người dùng xem trước/đổi trọng tâm |
| `AMBIGUOUS` | Tiêu đề trùng nghĩa, ô gộp đa cấp, kết quả phân loại xung đột | Không tự sửa width dựa trên vai trò; yêu cầu review |
| `UNKNOWN` | Thiếu header/ngữ cảnh hoặc dữ liệu chỉ là mã | Chỉ đưa ra khuyến nghị hình học không xâm lấn; mặc định giữ |
| `LOCKED` | Biểu mẫu chính thức/đối tượng đặc thù cố định | Chỉ chẩn đoán; không đổi geometry |

**Nguyên tắc chống suy diễn:** Nếu bảng có cột `Kết quả`, thuật toán không được tự kết luận đó là cột quan trọng nhất trong mọi báo cáo. Nếu có hai `Ngày` ở các nhóm tiêu đề, phải giữ rõ parent header; nếu không resolve chắc chắn phải `AMBIGUOUS`. **Không cần AI** cho header có quy tắc nhận diện xác định; nếu AI được sử dụng chỉ làm gợi ý không mang quyền pháp lý và người dùng được quyền bác bỏ.

### 123.3. Hợp đồng dữ liệu nhỏ nhất

```yaml
reader_task:
  type: 'TRACK_PROGRESS'              # controlled vocabulary trong profile, không suy luận tự do
  provenance: 'DOCUMENT_CONTEXT'
  evidence_refs: ['caption', 'preceding_paragraph']
  certainty: 'GROUNDED'
columns:
  - grid_interval: [0, 1]             # nửa kín: [start, end); cột thứ 0
    role: 'ORDINAL'
    certainty: 'GROUNDED'
    preserve_whole_tokens: true
  - grid_interval: [1, 2]
    role: 'TASK_DESCRIPTION'
    certainty: 'CONFIRMED'
    preserve_whole_tokens: false
  - grid_interval: [2, 3]
    role: 'OWNER'
    certainty: 'GROUNDED'
    preserve_whole_tokens: true
  - grid_interval: [3, 4]
    role: 'DEADLINE'
    certainty: 'CONFIRMED'
    preserve_whole_tokens: true
policy:
  fallback: 'KEEP_EXISTING'
  allow_auto_write: false
```

`certainty` là trạng thái bằng chứng, không được hiểu là xác suất 0–1 đã hiệu chỉnh. Không lưu nội dung từng ô trong audit log chỉ vì có hợp đồng này.

## 124. Mô hình hình học khả thi trên grid vật lý

### 124.1. Định nghĩa width và đơn vị

Ký hiệu: `W` là chiều rộng vùng được phép cấp cho bảng sau khi trừ lề section, `tblInd` (nếu liên quan), bố trí wrap/floating, vùng chứa bảng lồng và ràng buộc biểu mẫu. `w_i` là chiều rộng **đề xuất** cho grid column `i`, biểu diễn dưới dạng twips nguyên (1 twip = 1/1440 inch, tương đương khoảng 0,017639 mm). Không làm tròn sang mm trong phép cộng nội bộ.

Ràng buộc đề xuất cơ bản:

```
for each grid column i:
    min_width[i] <= w[i] <= max_width[i]
sum(w[i]) <= available_width
for each protected / merged interval [a,b):
    sum(w[a:b]) respects that cell's interval constraints
for each frozen column i:
    w[i] == baseline_width[i]
```

Đây là **mô hình tìm ứng viên**, không phải hợp đồng Word sẽ render đúng bằng `w_i`. Theo tài liệu OOXML, `w:tblW` và `w:tcW` chỉ là *preferred width*: grid columns, widths khác và thuật toán dàn trang có thể ghi đè. Đặc biệt, `tblW pct` tương đối với vùng chữ của trang, trong khi `tcW pct` tương đối với bảng — không dùng cùng một mẫu số. [S72], [S73].

### 124.2. Physical grid khác bảng ma trận ô chữ nhật

- Một physical cell với `gridSpan = k` chiếm khoảng `[i, i+k)`; nó **không** phải `k` ô độc lập.
- `vMerge` làm quan hệ cùng cột kéo qua các hàng; không sao chép text ô đầu vào ô tiếp diễn.
- `gridBefore/gridAfter` (omitted cells) là các cột grid không có physical cell tương ứng ở một hàng; không tự tạo ô cho đầy hàng.
- Bảng lồng phải giải theo vùng chứa **của ô mẹ**, không lấy toàn bộ chiều ngang A4 làm ngân sách cho bảng con.
- Trong các bảng direction/indent/floating đặc thù chưa xác định được geometry, trả `REVIEW_REQUIRED` thay vì ước lượng chắc chắn.

Nếu không thiết lập được map `physical_cell → [grid_start, grid_end)`, chỉ chẩn đoán, **không ghi width**. Đặc biệt, với `gridSpan`, một constraint vi phạm của ô gộp có thể làm nhiều cột đồng thời không hợp lệ; không được tối ưu từng cột như hệ độc lập.

### 124.3. Không tự đồng nhất XML với vùng in

Ba phép đo khác nhau phải được ghi riêng:

| Phép đo | Giá trị | Giới hạn |
|---|---|---|
| `source_preferred_width` | XML `tblW/tcW/gridCol` + đơn vị + provenance | Không chứng minh pixel render |
| `predicted_width` | Đầu ra solver/ước lượng văn bản | Không chứng minh Word tuân theo |
| `measured_width` | Hộp bao của bảng/ô trên renderer mục tiêu | Gắn với renderer/font/printer/section cụ thể |

Không ghi một trường `table_width` duy nhất rồi sử dụng thay thế cho cả ba ý nghĩa. [S67], [S72], [S73].

## 125. Đo áp lực xuống dòng và lợi ích biên: không dùng số ký tự như độ rộng

### 125.1. Cách xác định “ô gây nút thắt hàng”

Với mỗi ứng viên width, ước lượng số dòng từng ô theo dữ liệu đầu vào hiện có và font metrics **nếu có nguồn đo đáng tin cậy**, sau đó dự báo chiều cao từng hàng theo ô có độ cao chi phối. Khi có render target, thay ước lượng bằng số đo đã lấy từ renderer.

```
cell_height_estimate(r,c,w) = line_count_estimate * effective_line_height + top_bottom_padding
row_height_estimate(r,w_vector) = max(cell_height_estimate of all physical cells in row r)
```

Đây chỉ là proxy; `Exactly`, chiều cao hàng tối thiểu, hàng gộp dọc, border, paragraph spacing, anchored objects và nhiều yếu tố khác có thể làm công thức trên sai. Gắn trạng thái `M1_ESTIMATE`, không báo là `M2_RENDER`.

**Điểm mới:** Cột có nhiều ký tự nhưng không phải nguồn quyết định chiều cao hàng ở đa số hàng thì mở rộng nó có thể không cải thiện chiều cao bảng. Ngược lại, việc lấy 3 mm từ cột A để nới cột B có thể làm cột A trở thành nút thắt mới. Vì vậy lợi ích biên phải tính trên **vector `w` toàn bảng**, không trên từng cột tách rời.

### 125.2. Bảo vệ token nguyên vẹn

Các chuỗi như số quyết định, ký hiệu văn bản, ngày theo định dạng đã phê duyệt, mã hồ sơ, địa chỉ mạng, số liệu và cụm có nonbreaking space/hyphen phải được nhận diện từ **bản gốc**, không tự thay mã Unicode, thêm hoặc xóa ký tự để bảng vừa cột. Word hỗ trợ nonbreaking space và nonbreaking hyphen; việc đổi chúng sẽ thay ngữ nghĩa xuống dòng của tài liệu. [S76].

Nếu token không thể ngắt lớn hơn mọi độ rộng cho phép, kết quả là `NO_FEASIBLE_WIDTH` hoặc gợi ý người dùng sửa **nội dung/mẫu** theo thẩm quyền, không tự ép font nhỏ hoặc đổi số liệu.

## 126. Style cascade, Table Look và xung đột đường viền: kỹ thuật tránh “XML đúng nhưng bảng xấu”

Bảng Word có nhiều lớp quyết định giao diện: styles của tài liệu, table style với conditional parts (first/last row, first/last column, banding, góc), table property exceptions, row/cell overrides, paragraph/run formatting và border resolution. `tblLook` điều khiển việc áp dụng các nhánh điều kiện; `tblStylePr` có thể đưa thuộc tính tế bào hoặc ký tự vào header. [S69], [S70].

**Quy tắc kiểm tra trước khi đổi thẩm mỹ:**

1. Thu thập `tblStyle`, `tblLook`, `tblPrEx`, `tblBorders`, `tcBorders`, cell spacing và thuộc tính của cell thực tế liên quan.
2. Phân biệt `property not specified`, `none`, và `nil` theo ngữ cảnh và phiên bản đặc tả. **Không** giả định mọi giá trị `none` và `nil` có cùng hành vi hiển thị; tài liệu Microsoft về xung đột border có những ghi chú tương thích. [S71].
3. Không sửa style dùng chung để “đẹp” một bảng nếu style đó còn áp dụng cho bảng khác; ưu tiên chỉnh cục bộ trong whitelist nhưng vẫn cần đo kết quả.
4. Không đặt viền từng ô hàng loạt nếu chưa xác định cách Word giải xung đột viền giữa hai ô kề nhau.
5. Nếu một preset mâu thuẫn với official form hoặc style được khóa, giữ style gốc, ghi `R_STYLE_LOCK`.
6. Đánh giá trên bản render, không suy rằng chỉ `w:sz=4` là tất cả đường kẻ sẽ hiển thị 0,5 pt.

Microsoft hướng dẫn người dùng thao tác Table Properties, Borders/Shading, Table Options để chỉnh margin, spacing và wrap; đây là cơ chế chính thức nên tận dụng trước khi thiết kế thuật toán thay thế. [S66], [S67].

## 127. Điều kiện an toàn liên quan hàng cao, phân trang và header nhiều tầng

| Rủi ro | Dấu hiệu kiểm tra | Hành động đề xuất |
|---|---|---|
| Hàng đặt chiều cao Exactly, chữ dài hơn khung | `trHeight` và render clipping | Chỉ đề xuất đổi sang `At least` nếu không khóa; xác nhận trước khi áp dụng |
| Hàng bị đẩy sang trang mới khi bật `cantSplit` | Dựa trên chiều cao thực tế | Không bật hàng loạt; giữ khi hàng quá dài không thể nằm một trang |
| Tiêu đề nhiều hàng không liên tiếp từ đầu bảng | `tblHeader` đặt rời rạc | Không tự tuyên bố header sẽ lặp; xem xét nhóm đầu liên tục |
| Bảng chứa ngắt trang thủ công | Page breaks/chia bảng | Không dựa duy nhất vào `tblHeader`; cần render kiểm chứng |
| Bảng một hàng/biểu mẫu ký rất cao | Mẫu và chiều cao nội dung | Không tự ép cả hàng trong một trang hoặc thu phông |

Microsoft nêu rõ hàng có chiều cao *Exactly* có thể ngăn tự mở rộng để hiện chữ; nên dùng *At least* khi mẫu cho phép. [S68]. Tài liệu Open XML cũng xác định `cantSplit` chỉ giúp đẩy hàng qua trang, không biến hàng dài quá trang thành hàng một trang; `tblHeader` chỉ có hiệu lực với chuỗi hàng đầu liên tục. [S74], [S75].

**Điều chỉnh cách chấm:** Việc giảm số trang bằng cách cắt chữ hoặc thu cỡ chữ trái authority phải FAIL, kể cả khi `page_count` giảm; giữ cùng số trang nhưng nhìn dễ đọc hơn có thể là cải thiện thực tế. Khi xuất PDF, kiểm tra đối tượng/trang PDF riêng, không suy từ PDF khác renderer rằng file Word đích PASS.

## 128. Quy trình tạo và tìm ứng viên hữu hạn, xác định, có thể rollback

**Bắt buộc giữ ứng viên gốc** `BASELINE` trong toàn bộ quá trình; luôn có đường lui. Thuật toán tìm kiếm không được biến thành hệ thống song song hoặc phụ thuộc một mô hình AI không giải thích được.

```text
INPUT: immutable baseline_doc, selected_table, section_geometry,
       resolved_form_locks, reader_task, supported_renderer, policy

1. SNAPSHOT original OPC part/rels, physical-grid map, content invariants.
2. CHECK authority / signatures / protections / known unsupported features.
   If blocked -> return BLOCK without mutation.
3. LOCATE printable geometry and ownership; UNKNOWN -> REPORT/REVIEW.
4. BUILD constraints for grid widths, merged intervals and locked cols.
   If infeasible -> NO_FEASIBLE_WIDTH (baseline preserved).
5. GENERATE finite deterministic candidate widths (baseline included):
   - use current widths when valid;
   - try local reallocation only between compatible unlocked columns;
   - respect integer twips and merged intervals;
   - dedup width vectors; cap search budget via config, not guessed law.
6. ESTIMATE cost and reject obviously invalid candidates (M1 proxy only).
7. PATCH each candidate IN A DISPOSABLE COPY with whitelisted attributes.
8. RUN structure/content/package oracle. Reject failing candidates.
9. RENDER surviving candidates with same target environment where available.
10. RUN visual & downstream oracle, compare against baseline and uncertainty.
11. RANK by legal/form gates -> readability -> layout -> minimal diff.
12. IF baseline ties or benefit isn't demonstrated -> KEEP_EXISTING.
13. IF candidate is superior AND policy authorizes -> request APPROVAL;
    apply approved patch atomically, reopen, verify again; else REVIEW.
14. ON any post-write failure -> rollback and mark REJECTED/UNVERIFIED.
OUTPUT: decision, reasons, evidence level, candidate summary, changed parts.
```

**Tính xác định:** cùng tài liệu, profile, source version, renderer fingerprint và đầu vào phải tạo ra danh sách ứng viên cùng thứ tự; nếu renderer dao động thì phải ghi độ dao động, không che dưới một kết quả PASS duy nhất. **Tính tối thiểu:** nếu hai ứng viên tương đương theo các ngưỡng đã hiệu chỉnh thì chọn ứng viên thay ít thuộc tính/twips hơn; nếu không hơn baseline rõ rệt, chọn baseline.

## 129. Máy trạng thái quyết định và thứ tự ưu tiên reason code

Để tránh phát biểu mâu thuẫn, mỗi bảng chỉ có **một quyết định xuất cuối** dưới cùng một source-of-truth của workflow. Các lỗi có thể nhiều nhưng quyết định cuối phải đơn trị:

| Trạng thái | Ý nghĩa | Có được ghi DOCX? |
|---|---|---|
| `BLOCKED` | Chữ ký số, biểu mẫu bảo vệ hoặc loại tài liệu ngoài hỗ trợ | Không |
| `REJECTED` | Ứng viên vi phạm hard gate; giữ bản gốc | Không phát hành ứng viên |
| `REVIEW_REQUIRED` | Thiếu authority, grid hoặc người đọc cần xác nhận | Không tự ghi |
| `UNVERIFIED` | Thiếu điều kiện đo cần cho claim bố cục | Chỉ xuất bản diagnostic nếu chính sách cho phép, không ghi “đã tối ưu” |
| `KEEP_EXISTING` | Baseline an toàn và không có ứng viên cải thiện có ý nghĩa | Không thay đổi |
| `APPROVED_APPLIED` | Người dùng cho phép, patch thực hiện và verify PASS | Có, với bằng chứng scope |

Thứ tự ưu tiên khi nhiều reason cùng xuất hiện: **bảo vệ pháp lý/chữ ký → bảo toàn cấu trúc/nội dung → lỗi package → thiếu authority/unknown → lỗi visual → thiếu phép đo → không có lợi ích**. Reason code có thể giữ nhiều mục, nhưng `primary_reason` chọn lý do chặn có hậu quả cao nhất; không lấy lỗi “no material gain” che sự hiện diện của chữ ký số.

Không nhập nhằng `NO_OP_VALID` với `UNVERIFIED`: `NO_OP_VALID` chỉ nói **không có thay đổi được thực hiện và hành vi giữ nguyên là đúng theo policy**, không chứng minh tài liệu nguồn đã đạt mọi chuẩn hình ảnh đích. Có thể có `KEEP_EXISTING + VISUAL_NOT_EVALUATED` với phạm vi tuyên bố rõ.

## 130. Metric catalog và cách đối chiếu trước/sau chống “tối ưu ảo”

| Metric ID | Đơn vị | Thu thập | Nghiệm thu / giải thích |
|---|---|---|---|
| `m_width_allocated` | twips | M0 | Width đề xuất; không là width thực |
| `m_grid_overflow` | boolean, mm | M2/M3 | Đo ranh vùng in; phụ thuộc target |
| `m_text_clipping` | count + vị trí | M2/M3 + review | Zero regression là hard gate |
| `m_critical_token_break` | count | M2/M3 + reviewer | Token trọng tâm không bị chia khó hiểu theo rubric |
| `m_row_fragmentation` | count | M2/M3 | Chỉ coi là lỗi nếu mất ngữ cảnh, không đếm mọi chỗ ngắt |
| `m_header_context_loss` | count | M2/M3 | Đánh giá đủ hàng header liên tiếp |
| `m_page_footprint` | pages, bounding boxes | M2/M3 | Ít trang chỉ là phụ, không vượt readability |
| `m_downstream_delta` | mm, page index | M2/M3 | Đánh giá caption, footnote, chữ ký vùng ảnh hưởng |
| `m_change_surface` | count parts/properties; L1 twips | M0 | Ưu tiên ít can thiệp khi ngang chất lượng |
| `m_render_repeatability` | median, range | M2/M3 | Phải đo baseline lại trước khi tuyên bố cải thiện |
| `m_effective_style` | table/row/cell | M0 + M2 | Đối chiếu style cascade/viền ở phiên bản đích |

`N/A`, `NOT_MEASURED`, `MEASURED` phải phân biệt; **không đổi `N/A` thành zero**. Không chấm các bảng chính thức vốn cấm chỉnh bằng rubric thẩm mỹ chung rồi coi điểm thấp là lỗi pháp lý. Nếu target không cung cấp bounding box tin cậy, metric liên quan mang trạng thái `UNAVAILABLE`, không tự suy từ kích thước ảnh chụp đã resize.

## 131. Đánh giá hiệu quả bằng ưu thế Pareto và ngưỡng hiệu chỉnh

Một ứng viên `C` có thể được gọi là **trội hơn baseline** khi:

1. Mọi hard gate áp dụng đều PASS.
2. Không metric trọng yếu nào suy giảm đáng kể ngoài ngưỡng đo đã thống nhất.
3. Có ít nhất một lợi ích thực sự có giá trị với tác vụ người đọc, vượt sai số và ngưỡng materiality đã hiệu chỉnh.
4. Thay đổi các phần không thuộc phạm vi đều bằng 0 (hoặc ngoại lệ được giải thích và phê duyệt theo contract).

**Không bắt buộc đặt trọng số cứng** như “mỗi mm = bao nhiêu điểm” khi chưa có benchmark. Nếu candidate A cho cột deadline dễ đọc hơn nhưng đẩy bảng sang trang mới, và B chỉ giảm trang nhưng làm gãy mã hồ sơ, hãy xét task/hard gate và đưa vào review khi không có phương án trội rõ. Khi có nhiều ứng viên không trội lẫn nhau, baseline vẫn là đối thủ hợp lệ; nếu không có căn cứ chọn, giữ nguyên.

`delta_observed = metric_candidate - metric_baseline` chỉ có giá trị khi cùng điều kiện Word build, font, phương pháp xuất/in, setup trang. Nếu mức cải thiện nhỏ hơn dao động render lặp lại, ghi `MEASUREMENT_UNSTABLE` hoặc `NO_MATERIAL_GAIN` tùy chứng cứ, **không** tuyên bố cải thiện.

## 132. Ví dụ định lượng với cột trọng tâm và điều kiện bất biến

Bảng hành động gồm 4 cột trên một vùng ngang khả dụng **minh họa** 165 mm (không áp dụng mặc định cho mọi section):

| Cột | Vai trò | Baseline (mm) | Ứng viên A (mm) | Lý do thử |
|---|---|---:|---:|---|
| STT | Nhận diện thứ tự | 12 | 12 | Giữ nguyên |
| Nhiệm vụ | Mô tả dài | 85 | 77 | Cho phép nhiều dòng hơn khi đủ đọc |
| Đơn vị thực hiện | Định danh | 36 | 43 | Giảm việc tên đơn vị bị chia khó hiểu |
| Hạn hoàn thành | Ra quyết định thời gian | 32 | 33 | Bảo vệ hiển thị ngày/tháng và tiêu đề |
| **Tổng cộng** | | **165** | **165** | Không tràn về tổng số học |

Ứng viên A mới là một **giả thuyết**. Chỉ chọn A nếu render xác nhận: (i) toàn bộ token quan trọng được đọc rõ; (ii) không tăng số hàng bị cắt/che; (iii) nút thắt chiều cao toàn bảng không xấu đi quá ngưỡng; (iv) caption, chữ ký và phụ lục lân cận không bị ảnh hưởng trái phép; (v) thay đổi được người dùng chấp thuận. Ngược lại `KEEP_EXISTING`.

**Phản ví dụ:** nếu hàng “Nhiệm vụ” có diễn giải rất dài và quyết định chiều cao, rút từ 85 xuống 77 mm có thể làm tăng 1 dòng ở nhiều hàng, khiến A xấu hơn. Do đó không có quy tắc “nhường 8 mm cho đơn vị” phổ quát. Tỷ lệ cột tốt được rút ra từ việc đo bố cục **thực tế**, không phải từ một bộ tỷ lệ cố định.

## 133. Contract ghi file dạng format-only và bằng chứng thay đổi

Đề xuất một `patch_manifest` nhỏ, dùng lại hệ audit/patch của dự án nếu đã có:

```json
{
  "schema_version": "table-format-v7-proposal",
  "document_profile": "PARTY_HD05",
  "source_identity": "sha256-of-authorized-source",
  "table_locator": "word/document.xml#body/table[2]",
  "operation": "SET_GRID_PREFERRED_WIDTHS",
  "requested_grid_widths_twips": [680, 4366, 2438, 1870],
  "allowed_part_paths": ["word/document.xml"],
  "allowed_property_paths": ["w:tblGrid/w:gridCol@w:w", "w:tcPr/w:tcW@w:w"],
  "requires_approval": true,
  "approval_status": "PENDING",
  "render_evidence": "NOT_AVAILABLE",
  "decision": "REVIEW_REQUIRED"
}
```

Ví dụ trên là schema minh họa, không thể chạy như lệnh patch. Vị trí bảng theo thứ tự chỉ số là locator tạm; với sản phẩm thật phải bảo đảm identity theo part/owner path/snapshot và chống tình trạng thay đổi bảng giữa inspect và apply (TOCTOU). `allowed_property_paths` chỉ mô tả phạm vi; **không** được ghi `tcW` đồng loạt nếu gridSpan/omitted cells/style làm dữ liệu mâu thuẫn.

**Quy định kiểm chứng sau ghi:**

- Reopen package; xác nhận các part/relationships **ngoài phạm vi** không đổi nội dung có nghĩa, không đánh đồng việc ZIP repack khác byte với hỏng tài liệu.
- So sánh những vùng content gốc theo bảo toàn ngữ nghĩa và OOXML topology; không tự chấp nhận Track Changes, gộp các run hay xóa bookmark/field.
- Recalculate/compare target layout bằng đúng renderer khi quyết định yêu cầu.
- Xác nhận xuất file vẫn giữ nhận diện authority, section geometry và chữ ký số không bị tác động (đối tượng có chữ ký đã bị BLOCK từ đầu).
- Nếu post-condition fail, xuất bản gốc hoặc báo lỗi có thể kiểm tra; **không bao giờ** công bố file lỗi là kết quả đã tối ưu.

## 134. Đặc tả giao diện duyệt kết quả — không biến suy luận thành thao tác âm thầm

Một bảng được hiển thị trong UI review với năm nhóm thông tin, có thể tái sử dụng panel hiện hữu:

| Nhóm UI | Phải hiện | Không được làm |
|---|---|---|
| Tình trạng bảng | `Đã phù hợp / Có đề xuất / Cần duyệt / Không hỗ trợ / Chưa kiểm chứng` | Hiện tất cả là “Tối ưu thành công” |
| Chứng cứ | Căn cứ quy định, mẫu, loại bảng, source và target renderer | Che giấu nguồn suy luận |
| Độ rộng | Chiều rộng gốc/đề xuất từng cột, đơn vị mm, cột bị khóa | Chỉ hiển thị % không có ngữ cảnh vùng in |
| Trực quan | Trước/sau cùng zoom/môi trường; nếu chưa render, gắn cảnh báo rõ | Dùng HTML canvas thay bằng “giống Word khi in” |
| Quyền quyết định | Giữ nguyên, duyệt ứng viên, hoặc báo lỗi/không áp dụng | Tự sửa mẫu/chữ ký/protected doc |

Không đưa nội dung DOCX riêng tư vào log debug, telemetry hay benchmark công khai. Không phát sinh persistent DOCX đầu vào/đầu ra/tạm trong hệ storage dự án nếu kiến trúc hiện hữu cấm; kiểm tra phương án xử lý ở cấp môi trường triển khai sau khi audit.

## 135. Bộ phép thử hợp đồng mới T109–T124 và truy vết

> 16 tình huống dưới đây là **ca kiểm tra đề xuất**, không đồng nghĩa 16 fixture/code test mới hoặc đã chạy. Chỉ tạo test mới nếu khả năng hiện tại thiếu bằng chứng cho behavior trực tiếp thay đổi. T01–T108 của V1–V6 giữ nguyên.

| ID | Trường hợp mới cần xác minh | Oracle / kết quả mong đợi |
|---|---|---|
| T109 | Tiêu đề `Kết quả` không có ngữ cảnh, hai cách hiểu đều hợp lý | `AMBIGUOUS`, không tự chọn cột trọng tâm |
| T110 | Người dùng chỉ định cột deadline nhưng dữ liệu ngày ngắn | Ưu tiên đọc deadline; không mặc định cấp width lớn nhất |
| T111 | `tblW pct` và `tcW pct` cùng biểu thị 50% | Tính đúng mẫu số khác nhau, không dùng chung W |
| T112 | Bảng có `gridSpan=3`, solver thử co 1 cột | Constraint kiểm khoảng 3 cột; không đếm ô 3 lần |
| T113 | Hàng có `gridBefore` và không có physical cell đầu | Không thêm ô giả, không làm lệch ID cột |
| T114 | Bảng lồng có ô mẹ chỉ rộng 42 mm | Tính available width theo ô mẹ, không theo A4 |
| T115 | Style `tblLook` đặt header đậm; direct formatting thiếu | Phát hiện effective style; không sửa nhầm bảng khác |
| T116 | Viền ô kề nhau `nil/none`, spacing 0 | Không suy từ raw border đơn lẻ, kiểm đúng kết xuất |
| T117 | Row height `Exactly` che chữ, mẫu không khóa | Cảnh báo và đề xuất At least; không tự sửa khi chưa duyệt |
| T118 | `cantSplit` trên hàng cao hơn cả trang | Không tuyên bố bảo đảm hàng nằm một trang |
| T119 | Hai header rows đầu liên tiếp, hàng 3 đánh header rời rạc | Chỉ nhóm hợp lệ được lặp; kết quả cần render |
| T120 | DOCX có nonbreaking hyphen trong mã quyết định | Không sửa ký tự để giảm width; token giữ nguyên |
| T121 | Candidate đẹp hơn chút ít dưới variance Word render | Chọn baseline/UNDECIDED; không khai cải thiện |
| T122 | Repack ZIP làm đổi bytes nhưng part không liên quan giữ nội dung | Không FAIL sai vì ZIP-level diff; semantic/part gate vẫn phải PASS |
| T123 | Thay style bảng dùng chung làm đổi bảng thứ hai | Scope FAIL, rollback ứng viên |
| T124 | Hai lần chạy cùng input/target mà width dao động | Phát hiện idempotence/determinism regression, không tự PASS |

**Định nghĩa traceability:** Mỗi T109–T124 gắn tối thiểu `requirement_id`, `fixture_ref/reuse`, `oracle`, `evidence_path`, `result` và `reviewer`. Những ca có oracle M2/M3 không thể tuyên bố PASS từ O1/XML-only. Các ca T01–T108 đã có bằng chứng PASS mà contract không đổi thì không cần chạy lại toàn bộ.

## 136. Kế hoạch áp dụng V7 theo REUSE FIRST và phạm vi ảnh hưởng

| Nhóm | Mục tiêu nhỏ nhất | Nguồn reuse ưu tiên | Bằng chứng kết thúc |
|---|---|---|---|
| P0-A | Khảo sát code hiện có, lock và grid map | Parser/OPC utils, quy tắc profile, snapshot & validator đã có | Bản audit đường dẫn file/symbol/test/pass hiện hành |
| P0-B | Chạy diagnostic-only trên bảng đại diện | Layout inspect/render đang dùng; không ghi DOCX | Bản đo M0, reason code, không sửa file |
| P0-C | Quy tắc UNKNOWN/AMBIGUOUS/BLOCK/KEEP | Workflow, panel review, approval existing | Hành vi không sửa an toàn trên ca rủi ro |
| P1-A | Candidate width hữu hạn cho bảng đơn giản | Grid measure, Word/OOXML, solver tối thiểu | O1/O2; candidate với phép đo M2 nếu target có sẵn |
| P1-B | Patch format-only và rollback | Patch engine, transaction, audit hiện hữu | Changed-part diff, reopen và render target PASS |
| P2-A | Thẩm mỹ nâng cao, thử nhiều môi trường | Preset, typography/render test đã tồn tại | Holdout, metric đáng tin, review người dùng |

**Chốt phạm vi:** Không viết lại phần xử lý DOCX gốc, không tạo một service AI để quyết định sorting/CRUD/validation, không tạo storage mới, không thay Core đang khóa nếu extension contract đã đủ. Tối ưu ở đây là **bổ sung một khả năng còn thiếu**, không phải xây lại subsystem. Việc triển khai chỉ bắt đầu sau khi người dùng giao nhiệm vụ trên repo đích; nghiên cứu hiện tại chưa sửa mã hoặc commit.

## 137. Definition of Done V7 — phân biệt đặc tả, bằng chứng và sản phẩm

| Cấp độ | Điều kiện xác nhận | Trạng thái thời điểm soạn V7 |
|---|---|---|
| `SPEC_READY` | Đã nêu decision contract, geometry, state/reason, metric, 16 ca thử, nguồn | **Có ở mức tài liệu** |
| `CODE_AUDITED` | Đọc HEAD và xác định reuse, gaps, test existing | **Chưa thực hiện trong nhiệm vụ này** |
| `DECISION_VERIFIED` | Chạy deterministic decision trên fixture đại diện, so baseline | **Chưa thực hiện** |
| `PATCH_INTEGRITY_PASS` | Thực thi patch DOCX thật, O1/O2/OPC PASS, rollback | **Chưa thực hiện** |
| `TARGET_RENDER_PASS` | Đo Word/renderer mục tiêu, O3 có bằng chứng, sai số được kiểm soát | **Chưa thực hiện** |
| `USER_ACCEPTED` | Người dùng duyệt giao diện và kết quả in của ca đại diện | **Chưa thực hiện** |

Không gọi V7 là “thuật toán đã tối ưu” hoặc “tuân thủ 100%” khi mới có đặc tả. Các ngưỡng, preset và số ca là **đề xuất**, không phải tiêu chuẩn pháp lý hoặc kết quả benchmark thực tế.

## 138. Kết luận V7: tối ưu là một quyết định có căn cứ, không phải phép co giãn cột

V7 cung cấp các thành phần còn thiếu để một implementer có thể chuyển từ bộ nguyên tắc sang contract vận hành: (1) biết bằng chứng nào chứng minh cột trọng tâm; (2) biết phép đo và constraint nào áp dụng cho bảng thường và phức tạp; (3) nhận diện khi style hoặc renderer phủ quyết đề xuất width; (4) chọn được `APPLY / KEEP / REVIEW / BLOCK / UNVERIFIED` với lý do; (5) đo được giá trị trước/sau mà không biến chỉ số proxy thành kết luận.

**Nguyên tắc chốt:** `No evidence → no automatic width rewrite.` Nếu chỉ có XML và ước lượng, hệ thống có thể đề xuất có điều kiện, **không** được tuyên bố đã tối ưu bản in Word. Nếu bảng là biểu mẫu được bảo vệ hoặc đầu vào đã ký, giữ nguyên. Nếu một giải pháp chỉ giảm số trang bằng cách phá khả năng đọc hoặc tác động phần không được sửa, loại. Nếu hai ứng viên tương đương, lấy phương án thay đổi ít nhất hoặc giữ baseline. Khi có quyền duyệt, có phép đo và bằng chứng đủ mạnh, mới áp dụng bản đã qua gate và có khả năng rollback.

---

# PHẦN XXIV. NÂNG CẤP V8 — TỪ ĐẶC TẢ ĐỘ RỘNG CỘT ĐẾN QUY TRÌNH TỐI ƯU CÓ THỂ NGHIỆM THU

> **Phạm vi V8.** Chuyên đề này không viết lại các quy tắc V1–V7. Nó đóng các khoảng trống còn lại giữa **đề xuất thuật toán** và **khả năng triển khai an toàn trong Microsoft Word**: đầu vào chuẩn, hình học trang thực, đo mức độ đọc được của nội dung tiếng Việt, hành động tối thiểu, hợp đồng quyết định, so sánh có kiểm soát, chẩn đoán ngoại lệ, dữ liệu kiểm thử và bằng chứng nghiệm thu. Các thông số và thuật toán trong Phần XXIV đều là **đề xuất kỹ thuật**, không phải quy định pháp luật. Chưa có bộ tối ưu được triển khai hay thử nghiệm kết xuất Word trong nhiệm vụ nghiên cứu này.

## 139. Kiểm toán V7: các điểm cần hoàn thiện trước khi triển khai

| Khoảng trống còn lại | Nguy cơ nếu không xử lý | Bổ sung V8 | Mức bằng chứng đích |
|---|---|---|---|
| Đối tượng tối ưu chưa khóa đầy đủ theo story/section | Chọn nhầm bảng ở footer, textbox, phụ lục | `table_identity`, `owner_path`, `section_identity` có kiểm tra thay đổi nguồn | O1/O2 |
| Chưa tách rõ hiện trạng renderer với tiêu chuẩn đề xuất | Thay bảng đúng đang hiển thị thành bảng tệ hơn | Lưu baseline, fingerprint font/Word/thiết bị/print | O3 |
| Ngưỡng “đẹp hơn” còn tổng quát | Cải thiện một ô nhưng làm xấu nhiều ô khác | Bộ chỉ số cấp ô–hàng–bảng–vùng lân cận; lexicographic gates | O3/O4 |
| Thiếu hợp đồng hành động giới hạn | Tối ưu độ rộng biến thành sửa màu/phông/chữ hoặc orientation | Allowlist thay đổi; hành động tăng mức rủi ro theo thứ tự | O1/O2 |
| Tiếng Việt chưa có hợp đồng đo chữ đủ rõ | Dùng đếm ký tự rồi báo width chính xác | Phân biệt grapheme, glyph, font thực và kết xuất | O3 |
| Mẫu in hai mặt, section nhiều cột, bảng nổi | Tính sai vùng cấp chỗ cho bảng | Geometry đủ điều kiện và `UNRESOLVED_GEOMETRY` | O1/O3 |
| Khả năng tương thích giữa các máy chưa được ghi nhận | Word trên máy khác xuống dòng khác | `target_environment_fingerprint` và chính sách portability | O3 |
| Acceptance ở mức danh sách, thiếu trace tới yêu cầu và mã lỗi | “PASS” không truy được lý do | Requirement → rule → fixture → oracle → evidence → decision | O1–O4 |

**Kết luận audit:** V8 không cần một thuật toán AI sinh bố cục mới. Cần **chuẩn hóa đầu vào/đầu ra và khả năng kiểm chứng** quanh bộ xử lý Word hiện hữu. Việc audit source thực tế của repo phải được thực hiện riêng trước giai đoạn triển khai, không suy luận rằng các primitive đã tồn tại.

## 140. Trật tự thẩm quyền và thứ tự ưu tiên tối ưu

Mọi yêu cầu đều phải phân giải theo thứ tự sau; không được sử dụng trọng số thẩm mỹ để bù cho một điều kiện bắt buộc thất bại:

1. **Quy định pháp lý áp dụng:** Nghị định 30/2020/NĐ-CP hoặc bộ Quy định 399-QĐ/TW, Hướng dẫn 05-HD/VPTW; phân biệt phạm vi văn bản chính/phụ lục, mặt trước/mặt sau.
2. **Biểu mẫu/chỉ dẫn cụ thể:** Mẫu ban hành hoặc yêu cầu trình bày được người có thẩm quyền chỉ định; không tự sửa bố cục biểu mẫu đã khóa.
3. **Bảo toàn tài liệu:** Nội dung, dữ liệu, bảng lồng, field, bookmark, review markup, chữ ký số, cấu trúc quan hệ package.
4. **Hình học và kết quả in:** Không tràn vùng hợp lệ, mất chữ, che số, đẩy sai chữ ký/phần phụ lục hoặc phá phân trang ngoài blast radius.
5. **Thông tin phục vụ tác vụ đọc:** Cột quan trọng dễ nhận diện, giá trị không bị ngắt mơ hồ, có thể so sánh dữ liệu thuận lợi.
6. **Thẩm mỹ, tính nhất quán và ít xáo trộn:** Viền, khoảng trắng, căn chỉnh, chi phí thay đổi nhỏ nhất.

**Tác vụ đọc là dữ liệu đầu vào, không phải suy luận chắc chắn từ độ dài cột.** Một cột `Kết quả` có thể biểu thị số liệu, trạng thái hoàn thành, hoặc phần ghi chú. Nếu chưa đủ chứng cứ xác định vai trò, đặt `SEMANTIC_AMBIGUOUS` và chỉ tối ưu hình học không cần biết ngữ nghĩa hoặc đề nghị người dùng chỉ rõ.

## 141. Định danh bảng và phạm vi tác động thật

Một bảng không thể được định danh ổn định chỉ bằng “bảng thứ 3 của tài liệu”. Khi người dùng chỉnh sửa bảng khác, chỉ số thay đổi. Đề xuất định danh tạm thời gồm `source_sha256`, `part_uri`, đường dẫn chứa (story/body/header/footer/footnote/textbox/appendix), vị trí cấu trúc, fingerprint topology và dấu mốc snapshot. Trước mỗi bước APPLY phải đối chiếu lại snapshot; khác biệt nguồn → `STALE_SOURCE`, không ghi.

Một **vùng ảnh hưởng** phải chứa tối thiểu: bảng đích, đoạn tiêu đề bảng trước nó, ghi chú/nguồn sau nó, các đoạn/bảng cùng trang có thể bị đẩy, vùng chữ ký/nơi nhận nếu lân cận và section break ảnh hưởng trực tiếp. Không cần so sánh mọi trang của tài liệu theo cách máy móc, nhưng phải so vùng lân cận liên quan đến thay đổi phân trang.

Microsoft xác định WordprocessingML gồm nhiều *story* (body, header/footer, comment, textbox, footnote/endnote...), do đó chỉ duyệt `document.xml` không có nghĩa đã kiểm mọi bảng trong file. [S79].

| Trạng thái locator | Hành vi |
|---|---|
| `STABLE` — định danh và topology khớp snapshot | Cho phép tiếp tục lập đề xuất |
| `RELOCATED_BUT_VERIFIED` — vị trí đổi, fingerprint vẫn duy nhất và nhất quán | Chỉ tiếp tục khi có contract định danh đã được kiểm thử |
| `AMBIGUOUS` — nhiều bảng giống nhau, không chỉ ra bảng đích | `REVIEW_REQUIRED` |
| `STALE_SOURCE` — tài liệu thay đổi từ lúc inspect | Dừng APPLY; yêu cầu inspect lại |

## 142. Hợp đồng đo nội dung tiếng Việt và token không được ngắt

Độ rộng đo theo số ký tự/code point là **proxy yếu** vì kích thước hiển thị phụ thuộc run, phông/font fallback, cỡ chữ, ký tự ghép dấu, kerning, kiểu đậm/nghiêng, hướng chữ và cách Word ngắt dòng. Hợp đồng đề xuất:

- Giữ **chuỗi nguồn nguyên vẹn**: không tự đổi NFC/NFD, không xóa U+00A0 (nonbreaking space), nonbreaking hyphen, tab, dấu xuống dòng, trường dữ liệu hoặc dấu thập phân. Có thể dùng dạng chuẩn hóa chỉ **trong bộ phân loại**, tuyệt đối không ghi trả lại thay đổi ấy khi hành động chỉ là định dạng.
- Đọc theo **run** khi xác định phông thực (kể cả run properties kế thừa); nhận diện các grapheme/cluster có dấu tiếng Việt, cụm “Điều 12”, “2026/HD-05”, số tiền, mã cơ quan, ngày tháng. Không giả định một grapheme tương đương một độ rộng cố định.
- Với văn bản có `w:br`, tab, field, hyperlink, `textDirection` hoặc tổ hợp Latin–ký hiệu, mức đo chỉ là `M1_ESTIMATE` cho tới khi có render đúng môi trường.
- Đo cả tiêu đề cột: chuỗi tiêu đề như `Ngày hoàn thành` có thể đòi chiều rộng hơn tất cả dữ liệu ngày. Không cố tối ưu để vừa giá trị mà làm vỡ tiêu đề bất hợp lý.
- Thiết lập `min_legibility_width` theo **token thiết yếu** và hành vi wrap hợp lệ đã quan sát, không theo cỡ chữ tối thiểu tùy tiện. Mọi token được bảo vệ nếu chưa hiển thị rõ phải kích hoạt hard gate, không được bỏ qua vì 95% ô khác đọc tốt.

Các văn bản đang dùng Times New Roman theo quy định chung nhưng cùng tên font chưa bảo đảm hệ thống có đúng face/phiên bản. Microsoft giải thích việc không có font hoặc chuyển tài liệu sang máy khác có thể thay đổi layout; nhúng font cũng chịu các giới hạn sử dụng và quyền nhúng. V8 **không đề xuất chèn font vào DOCX** như thao tác mặc định; ưu tiên fingerprint và thông báo thiếu font. [S83].

## 143. Hình học vùng trình bày: bổ sung các trường hợp chưa được tính đủ

Bắt đầu từ trang/section chứa bảng, xác định: khổ giấy thực, chiều dọc/ngang, lề, mirror margins và gutter nếu có, vùng chữ hữu dụng, cột báo/section nhiều cột, indentation, text wrapping, bảng nổi, ô mẹ của bảng lồng, cell spacing và cell margins. Không suy từ một cấu hình A4 mặc định cho toàn tài liệu.

`w:tblLayout` cho biết chế độ `fixed` hoặc `autofit`; không đồng nghĩa đo được chiều rộng thực bằng tổng `tcW`. Khi có bảng nổi, `w:tblpPr` có thể xác định vị trí của bảng; không được tính ngân sách của nó như bảng inline thông thường. Các thiết lập tương thích Word có thể làm hành vi layout khác; cần ghi fingerprint thay vì âm thầm đổi compatibility mode. [S81], [S84], [S82].

**Geometry contract:**

```text
GeometryContext = {
  target_section_id, page_w_twips, page_h_twips,
  margins_twips, gutter_twips, mirror_margins,
  text_column_or_container_w_twips,
  table_indent_twips, table_layout_mode,
  table_floating_position_status,
  cell_spacing_and_effective_margins,
  parent_cell_constraint_when_nested,
  print_side_if_relevant,
  geometry_confidence: VERIFIED | ESTIMATED | UNKNOWN
}
```

Đây là khung dữ liệu thiết kế, chưa phải schema đã triển khai. Khi gặp bảng nổi, nhiều cột, hướng chữ đảo, hoặc tổ hợp section chưa có phép đo tin cậy, kết quả mặc định là `UNRESOLVED_GEOMETRY`/`REVIEW_REQUIRED` chứ không tự cấp độ rộng toàn trang.

## 144. Xử lý các yếu tố Word có thể khiến kết quả khác kết quả tính toán

| Đặc điểm | Vì sao quan trọng | Quy tắc V8 |
|---|---|---|
| `w:tblLayout=fixed/autofit` | Chế độ bố trí thay đổi hành vi phân phối | Giữ mode gốc trừ khi được duyệt đổi; kiểm kết xuất [S81] |
| Compatibility mode trong `settings.xml` | Hành vi layout có thể phụ thuộc chế độ tương thích | Ghi nhận, không tự “nâng cấp” để sửa bảng [S82] |
| `tblpPr` và bảng nổi | Bảng có vị trí/wrap khác bảng nội tuyến | Không dùng solver inline mặc định [S84] |
| `gridBefore/gridAfter` | Hàng có các vị trí grid không có ô thật | Không tự thêm ô và không dịch dữ liệu [S85] |
| `tcMar`, `tblCellMar`, direction-aware `start/end` | Đệm ô hiệu dụng khác thông số raw một cấp | Resolve ở đúng mức áp dụng, không ghi chồng tùy tiện [S86] |
| `w:textDirection` | Cách dùng chiều ngang/dọc khác bình thường | Review nếu chưa hỗ trợ đúng [S87] |
| Hai bảng cùng style kề nhau | WordprocessingML có trường hợp xử lý như một bảng liên tiếp | Cẩn trọng nhận diện bảng/ranh giới và ảnh hưởng sửa [S89] |
| Font không có ở máy đích | Glyph metrics và ngắt dòng thay đổi | Yêu cầu phép đo đúng font hoặc đánh dấu renderer không tương đương [S83] |
| Header repeat và ngắt trang thủ công | Word không lặp header khi có ngắt trang thủ công trong bảng | Ghi chú giới hạn, không suy “PASS” từ một cờ XML [S80] |

**Quy tắc tối thiểu:** V8 chỉ nêu các dấu hiệu cần kiểm. Không bắt buộc tự viết một CSS-like cascade hoặc engine dàn trang riêng để tái hiện Word. Trước hết tận dụng parser, validator, UI Word và khả năng render sẵn có nếu audit dự án xác nhận.

## 145. Quy trình xác định cột trọng tâm: tín hiệu, xung đột, mức chắc chắn

Thay vì gán một nhãn duy nhất như `important=true`, mỗi cột có hồ sơ:

| Trường | Cách hiểu |
|---|---|
| `reader_task` | Người đọc dùng bảng để tra cứu, so sánh, phân công, phê duyệt hay đối chiếu biểu mẫu |
| `semantic_role` | STT / nhận diện / mô tả / ngày hạn / giá trị đo / trạng thái / giải thích / khác |
| `role_evidence` | Nhãn tiêu đề, loại token dữ liệu, ngữ cảnh caption và đoạn xung quanh, chỉ định người dùng |
| `priority_tier` | `MUST_READ`, `PRIMARY`, `SECONDARY`, `AUXILIARY`, `UNKNOWN` |
| `break_sensitivity` | Mức nguy hiểm nếu nội dung bị xuống dòng giữa token hoặc mất liên hệ cột–hàng |
| `width_pressure` | Nhu cầu không gian được đo/ước lượng, **không phải** tầm quan trọng ngữ nghĩa |
| `edit_lock` | Không cho phép rút rộng, đổi style, hoặc thay đổi theo mẫu |
| `evidence_level` | `USER_DECLARED`, `FORM_DEFINED`, `RULE_INFERRED`, `AMBIGUOUS` |

**Quy tắc chống tối ưu lệch:** `MUST_READ` không mặc định rộng nhất; chỉ phải được cấp đủ để đọc nhanh, không làm hỏng phần quan trọng khác. Hai cột cùng là `PRIMARY` được xử lý công bằng theo số trường hợp đọc không đạt, không ưu tiên cột có tiêu đề dài một cách máy móc. Các tín hiệu AI, nếu dùng để gợi ý vai trò, không được trở thành nguồn duy nhất có quyền thay đổi deterministic layout; khi không chắc thì cho người dùng duyệt.

## 146. Danh mục hành động tối thiểu, có thể giải thích và hoàn tác

Chỉ các hành động **format-only** đã được người dùng/phạm vi cho phép mới đưa vào candidate. Sắp theo mức can thiệp tăng dần:

| Mã hành động | Thay đổi | Điều kiện | Ngoài phạm vi tự động |
|---|---|---|---|
| `A0_KEEP` | Giữ nguyên bảng | Luôn tồn tại làm baseline | Không có |
| `A1_REBALANCE_WIDTH` | Phân phối lại preferred width/grid đã kiểm chứng | Bảng dữ liệu inline, geometry rõ, cột không khóa, O1/O2 PASS | Không đổi font/text/merge |
| `A2_ADJUST_CELL_MARGINS` | Đệm ô trong giới hạn preset được duyệt | Đã kiểm effective margin; không phải official form | Không thu đệm để tạo chữ sát viền |
| `A3_HEADER_REPEAT` | Đánh dấu hàng đầu liên tiếp cần lặp | Hàng tiêu đề rõ, bảng nhiều trang, đã duyệt | Không tạo hàng giả, không ngắt thủ công |
| `A4_SAFE_ROW_HEIGHT` | Đề xuất đổi `Exactly` sang `At least` | Đã phát hiện clipping, mẫu không khóa | Không sửa hàng ký/biểu mẫu đặc thù |
| `A5_BORDER_STYLE_LOCAL` | Chỉnh viền/nhấn tiêu đề cục bộ | Preset chọn, đo style cascade và xung đột | Không sửa shared style gây ảnh hưởng bảng khác |
| `A6_ORIENTATION_REVIEW` | Gợi ý trang ngang hoặc phụ lục | Bảng không thể bố trí an toàn theo dọc và quy định cho phép | Không tự thay section break, header/footer |

Các hành động có thể **đề xuất phối hợp** nhưng phải so với baseline; không thực hiện gói chỉnh sửa đồng loạt. Việc giảm cỡ chữ, nén ký tự, thay dấu câu, làm tròn số, chia bảng thành hai bảng vật lý hoặc xoay trang không bao giờ được tự động áp dụng trong preset tối ưu độ rộng V8.

## 147. Hàm mục tiêu và nguyên tắc không đánh đổi hard gates

Bài toán được xác định **theo thứ tự từ điển** (lexicographic optimization), không cộng tất cả giá trị thành một con số rồi hy sinh dữ liệu để được bảng ít trang:

```text
G0 — Hard gates: authority + protected form + content/OPC invariants +
                 geometry feasibility + zero new clipped/overlapped text.
     Candidate fail any G0 -> REJECT, regardless of visual score.

G1 — Task legibility: priority-weighted count/severity of unreadable
     essential tokens, unscannable keys, ambiguous row-to-column mapping.
     Prefer fewer severe failures; no deterioration of MUST_READ fields.

G2 — Layout stability: total affected-row heights, blank-space defects,
     page-break regressions, caption/nearby content displacement.
     Compare against baseline in same target renderer.

G3 — Aesthetic quality: alignment, whitespace balance, borders,
     header clarity, typography consistency; reviewer-specific.

G4 — Minimal intervention: changed table properties, total abs(delta twips),
     affected parts and rendered neighborhoods.
```

**Điểm mới so với chấm 100 điểm ở V1:** thang thẩm mỹ chỉ được dùng trong G3 khi G0/G1/G2 đã đạt; một bảng thiếu dữ liệu không bao giờ có thể đạt chỉ vì nền, viền đẹp. Với hai ứng viên có G1/G2 tương đương trong sai số đã hiệu chỉnh, dùng G4 để ưu tiên thay đổi nhỏ nhất; nếu candidate không chứng minh cải thiện đáng kể so baseline thì `NO_OP_VALID`.

Các chỉ số G1/G2 phải công bố **đơn vị và cách đo** (`count`, `mm`, `page`, `severity`, `render confidence`), không tạo ra một độ chính xác giả. Khi O3 chưa có, các chỉ số height/clip/page chỉ được gắn `predicted` chứ không `measured`.

## 148. Thí nghiệm định lượng minh họa: lợi ích của toàn hàng thay vì một cột

**Tình huống giả định**, không phải dữ liệu từ DOCX thực: bảng gồm STT, nội dung, đơn vị, hạn. Vùng in giả định 165 mm. Mẫu baseline `[12, 85, 36, 32]` mm; ứng viên A `[12, 77, 43, 33]` mm; ứng viên B `[12, 83, 38, 32]` mm. Cả ba có tổng **165 mm**.

Giả sử sau phép đo **độc lập, chỉ để minh họa**, ba hàng nội dung có độ cao dự kiến ở mỗi phương án như sau:

| Hàng | Baseline (mm) | A (mm) | B (mm) | Vì sao có thể khác |
|---|---:|---:|---:|---|
| 1 | 12 | 12 | 12 | Không phải nút thắt |
| 2 | 24 | 36 | 24 | A làm cột nội dung xuống thêm dòng |
| 3 | 20 | 20 | 20 | Không thay đổi nút thắt |
| **Tổng 3 hàng** | **56** | **68** | **56** | A tăng chiều cao **12 mm** dù cột đơn vị rộng hơn |

Nếu B cải thiện khả năng đọc `Đơn vị` mà không làm giảm khả năng đọc `Nội dung`, B **có thể** là ứng viên phù hợp hơn A, nhưng vẫn phải kiểm chứng O1/O2/O3 và ngưỡng thực nghiệm trước khi duyệt. Nếu sự cải thiện đó không vượt sai số hoặc không giải quyết nhu cầu người đọc, **giữ baseline**.

Ví dụ còn cho thấy: “tiết kiệm một dòng ở một ô” không có nghĩa “tiết kiệm một dòng của hàng”. Chiều cao hàng do nội dung cao nhất cùng các ràng buộc ảnh hưởng quyết định; cần tối ưu vector chiều rộng đồng thời thay vì quyết định từng cột độc lập.

## 149. Chính sách lựa chọn renderer và khả năng di chuyển giữa môi trường

| Mục đích kết quả | Renderer chứng cứ chính | Có thể khẳng định điều gì |
|---|---|---|
| Chỉ kiểm tra cấu trúc DOCX | Validator + OOXML inspector | Hợp lệ cấu trúc và bất biến đã được kiểm |
| Người dùng làm việc trên Word Windows | Chính build Word mục tiêu + font thực | Layout tại cấu hình đã kiểm, không phải mọi máy |
| Kết quả PDF xuất từ Word | Word → PDF bằng cùng cấu hình đích | PDF đã xuất phù hợp tại lần kiểm |
| LibreOffice preview hoặc browser canvas | Engine tương ứng | Chỉ layout trên chính renderer đó; không tự chứng nhận Word |
| Tài liệu chuyển máy in / máy làm việc khác | Chạy lại phép kiểm chọn lọc hoặc gắn portability warning | Không bảo đảm pixel-exact đa nền tảng |

Cần ghi trong evidence: sản phẩm/build, OS, nguồn render, khổ giấy/printer profile nếu có, font và tính sẵn có của font, chế độ tương thích, phiên bản nguồn, hash đầu ra, thời điểm kiểm. Không cần thu thập danh sách phần mềm cá nhân không liên quan. PDF không phải phép chứng minh rằng DOCX sẽ tái dàn trang giống hệt trên mọi máy.

Microsoft nêu khả năng font embedding giúp giữ layout khi chia sẻ, nhưng cũng có hạn chế và có thể ảnh hưởng quyền/licensing. Với Times New Roman, **không mặc định nhúng, sao chép hoặc phân phối font** như điều kiện tối ưu; cách an toàn trước hết là xác định font được sử dụng trên renderer đích. [S83].

## 150. Hợp đồng kiểm thử tối thiểu: rule, oracle, bằng chứng, trạng thái

Một bản ghi quyết định cần liên kết đầy đủ:

```json
{
  "schema_version": "table-optimization-v8-spec",
  "source_digest": "sha256:<redacted>",
  "document_profile": "ND30|PARTY_HD05|FORM_OVERRIDE|UNKNOWN",
  "table_identity": {"part_uri": "word/document.xml", "snapshot_key": "opaque-stable-key"},
  "reader_task": "track-deadline",
  "geometry_status": "VERIFIED",
  "font_status": "VERIFIED_IN_TARGET",
  "candidate": {"action": "A1_REBALANCE_WIDTH", "widths_twips": [680, 4365, 2438, 1871]},
  "locked_properties": ["content", "merge_topology", "section_properties"],
  "oracle_results": {"O1": "NOT_RUN", "O2": "NOT_RUN", "O3": "NOT_AVAILABLE", "O4": "NOT_RUN"},
  "target_environment_id": "renderer-fingerprint-placeholder",
  "changed_parts": [],
  "decision": "REVIEW_REQUIRED",
  "reason_codes": ["RENDER_NOT_VERIFIED"],
  "approved": false
}
```

Schema chỉ minh họa contract; không được nhầm đây là thông báo engine đã kiểm thử. Ghi nhớ nguồn nội dung thật chỉ trong phiên xử lý được cho phép; manifest không cần lưu văn bản từng ô hoặc hình xem trước. Giá trị `source_digest` không được coi là cách ẩn danh hoàn toàn đối với văn bản có nội dung dễ suy đoán.

**Reason codes bổ sung:** `STALE_SOURCE`, `UNRESOLVED_GEOMETRY`, `FONT_ENV_MISMATCH`, `LAYOUT_MODE_UNSUPPORTED`, `FLOATING_TABLE_REVIEW`, `NO_MATERIAL_GAIN`, `BASELINE_PREFERRED`, `RENDER_NOT_VERIFIED`, `SEMANTIC_AMBIGUOUS`, `TARGET_PAGINATION_REGRESSION`, `SIDE_EFFECT_OUT_OF_SCOPE`, `SIGNATURE_BLOCK`. Các mã này **đề xuất**; triển khai phải map vào registry/trạng thái đã có nếu phù hợp, không tạo một registry song song.

## 151. Ma trận nghiệm thu ưu tiên: phân biệt PASS cấu trúc với PASS trình bày

| Giai đoạn | Kiểm tra | Cơ chế reuse | PASS khi |
|---|---|---|---|
| O0 — tiền kiểm | Nguồn/mẫu/approval/risk | Auth/HITL/validator hiện có | Bảng được phép đề xuất và phạm vi đã rõ |
| O1 — cấu trúc | OPC, OOXML, relationships, topology, allowed-diff | Validator hiện hữu hoặc Open XML SDK phù hợp | Không phát sinh hỏng schema và vùng ngoài scope không bị đổi bất hợp lệ |
| O2 — nội dung | Text, data, fields, objects, bookmarks, merge, attachment refs | Source extractor/diff hiện có | Không mất, lặp, đổi thứ tự, thay nghĩa số liệu |
| O3 — hiển thị | Layout các ô quan trọng, overflow, clipping, pagination, vùng sau bảng | Renderer đích khi khả dụng | Không regression trong vùng ảnh hưởng, mức cải thiện có bằng chứng |
| O4 — người dùng | Đúng mục tiêu tra cứu, thẩm mỹ và khả năng duyệt trước in | UI review hiện có | Người dùng đánh giá/duyệt theo workflow đã có |

**Không được dùng Open XML validator như oracle kết xuất.** Microsoft mô tả validator để kiểm lỗi cấu trúc và schema, không phải công cụ xác nhận mọi ô đều nhìn đẹp khi in. [S78]. **Không được lấy HTML canvas mô phỏng làm oracle Word** trừ khi kết quả đó được chứng minh đồng nhất trong phạm vi tài liệu và môi trường mục tiêu.

## 152. Kiểm thử thay đổi có ý nghĩa và tính ổn định

- **So sánh có cặp:** một fixture gốc, cùng renderer, cùng font, cùng thiết lập và cùng vùng kết xuất cho baseline và từng candidate. Không so ảnh chụp ở hai mức zoom khác nhau.
- **Chênh lệch lặp lại:** nếu renderer không ổn định do pagination/font/cache, chạy lại những ca **bị ảnh hưởng** với cùng fingerprint để đo độ dao động; không đặt ngưỡng dựa trên một ảnh đơn lẻ.
- **Holdout:** tách bộ bảng dùng hiệu chỉnh ngưỡng khỏi bộ dùng kiểm chứng; không tuning theo đúng các file mang ra chứng minh kết quả.
- **Baseline-first:** không candidate nào đạt lợi ích đủ rõ → `NO_OP_VALID`, không bắt buộc sinh file sửa mới.
- **Regression budget:** thay đổi số trang không tự coi là xấu hoặc tốt; cần xem chữ ký, caption, khoảng trắng và dữ liệu bị cắt/đẩy ra sao.
- **Repeatability:** cùng source snapshot và profile → quyết định/manifest không đổi, trừ khác biệt môi trường được ghi nhận. Thử lần hai trên tài liệu đã tối ưu không tiếp tục dao động độ rộng.

V8 không đưa ra các ngưỡng “độ cao giảm ≥ 5%” hay “độ đẹp ≥ 90” như điều kiện luật định; ngưỡng materiality phải đo và hiệu chỉnh trên benchmark thực theo cách V6 đã quy định.

## 153. Bộ kiểm thử V8: T125–T144 (20 ca mới, không trùng T01–T124)

> Các tình huống dưới đây là **đặc tả ca kiểm thử mới**. Chưa tạo fixture Word, chưa chạy Word và chưa xác nhận PASS. Khi triển khai cần tái sử dụng test, fixture, screenshot hoặc audit đã có nếu đáp ứng contract; chỉ bổ sung fixture cho hành vi thực sự còn thiếu.

| ID | Điều kiện đầu vào | Kết quả mong đợi / oracle |
|---|---|---|
| T125 | Word có bảng trong textbox, body và footer | Locator phân biệt story; không chọn nhầm bảng |
| T126 | Người dùng sửa tài liệu sau bước inspect | `STALE_SOURCE`, không apply patch cũ |
| T127 | Cột tiếng Việt chứa tổ hợp dấu Unicode phức tạp | Không tự chuẩn hóa thay text; đo bằng renderer hoặc chỉ ước lượng |
| T128 | Mã hồ sơ có nonbreaking hyphen và NBSP | Giữ nguyên ký tự và hành vi token được bảo vệ |
| T129 | Font Times New Roman không có trên renderer | `FONT_ENV_MISMATCH`, không xác nhận O3 mục tiêu |
| T130 | `w:tblLayout=autofit`, ưu tiên độ rộng bất nhất | Không suy width thật từ XML; render hoặc review |
| T131 | Section nhiều cột, bảng ở cột hẹp | Ngân sách theo container, không dùng toàn chiều ngang A4 |
| T132 | Bảng nổi có `tblpPr` và text wrap | `FLOATING_TABLE_REVIEW` nếu engine chưa hỗ trợ |
| T133 | Mirror margins/gutter/in hai mặt | Xét mặt trang/section, không mặc định cùng lề hai phía |
| T134 | Padding được set ở style và override ở ô | Resolve effective padding, không sửa nhầm cấp |
| T135 | `w:textDirection` hiển thị chữ dọc | Không áp dụng bộ đo ngang cho ô này |
| T136 | Hai bảng cùng style đứng liền nhau | Không kết luận ranh giới render từ số lượng `tbl` đơn giản |
| T137 | Cột PRIMARY có chữ ngắn nhưng nhiều token quan trọng | Được cấp đủ đọc; không tự cho lớn nhất |
| T138 | Candidate giảm cao một ô nhưng làm tăng cao hàng khác | Đánh giá row/bảng, không chấp nhận vì lợi ích từng ô |
| T139 | Candidate giảm trang nhờ cắt chữ (`Exactly`) | Hard gate FAIL; không tối ưu ảo |
| T140 | Bảng tốt sẵn, các candidate dưới mức sai số | `NO_OP_VALID`, không ép viết file |
| T141 | Render baseline/candidate khác build Word | Không so sánh như cùng môi trường; `RENDER_NOT_VERIFIED` |
| T142 | Shared Table Style thay làm đổi bảng ngoài scope | `SIDE_EFFECT_OUT_OF_SCOPE`, rollback |
| T143 | Sau APPLY, người dùng chạy tối ưu lần hai | Idempotent; không dao động width |
| T144 | Chỉ có O1/O2 PASS, O3 không có | Xuất trạng thái đúng `STRUCTURE_ONLY/REVIEW`, không báo PRINT_READY |

**Traceability bắt buộc cho từng ca:** `requirement_id`, `source_fixture`, `expected_behavior`, `oracle`, `environment`, `result`, `evidence_reference`, `reviewer/approval`. Trường `result` ban đầu phải là `NOT_RUN`. Không tạo test dựa trên tài liệu công việc thật nếu đã có bộ QA riêng hoặc chưa được phép dùng dữ liệu đó.

## 154. Giao diện review dành cho người dùng Word: ngắn gọn nhưng đủ căn cứ

Đề xuất tận dụng panel review hiện có thay vì tạo giao diện độc lập:

| Dòng thông tin trong UI | Hiển thị mẫu | Hành động |
|---|---|---|
| Loại bảng | “Bảng phân công — 4 cột — thuộc nội dung chính” | Xem phân loại |
| Mục đích đọc | “Theo dõi hạn và đơn vị thực hiện” | Chọn/chỉnh nếu cần |
| Vấn đề | “Tên đơn vị đang xuống 3 dòng; bảng có nguy cơ kéo sang trang tiếp” | Xem ô liên quan |
| Đề xuất | “Điều chỉnh nhẹ cột Nhiệm vụ / Đơn vị; giữ nguyên font, văn bản và số liệu” | Xem trước/sau |
| Bằng chứng | “Đã kiểm cấu trúc”; “Chưa có xác nhận bản in Word” | Đọc chi tiết |
| Quyết định | “Giữ nguyên / Duyệt ứng viên / Hủy sửa” | Theo quyền HITL hiện có |

Giao diện phải có trạng thái trung thực: `Đã phù hợp`, `Có phương án đã kiểm`, `Cần duyệt`, `Không đủ bằng chứng`, `Mẫu được bảo vệ`, `Không hỗ trợ`. Không gắn nhãn “Tối ưu in ấn thành công” nếu mới hiển thị preview HTML.

## 155. Kế hoạch triển khai tối thiểu theo Reuse First và blast radius

| Đợt | Phạm vi nhỏ nhất | Audit/reuse ưu tiên | Tiêu chí nghiệm thu |
|---|---|---|---|
| D0 | Kiểm tra mã nguồn/HEAD/AGENTS/test và ranh giới authority | Module DOCX/OPC, source extractor, section parser, validator, capability/HITL hiện có | Bản đồ file–symbol–contract và gap, **không sửa code** |
| D1 | Ghi nhận geometry và reason code, chẩn đoán read-only | Parser/inspector hiện có | Các ca input unsupported trả REVIEW/BLOCK đúng, không mutation |
| D2 | Phân loại cột và width pressure trên bảng inline đơn giản | Rule engine/table model đã có | T125/T127/T137 và bất biến liên quan, không nhận dạng quá tự tin |
| D3 | Solver ứng viên hữu hạn, baseline luôn tồn tại | Algorithms/utilities nội bộ trước; sau đó API/thư viện chính thức phù hợp | T130/T138/T140; deterministic trên fixture |
| D4 | Patch format-only với approval & rollback | Transaction/diff pipeline hiện có | T126/T142/T143; O1/O2 và changed-parts PASS |
| D5 | Word-target render nghiệm thu theo ảnh hưởng | Renderer/test harness hiện có nếu xác minh được | T129/T131/T132/T139/T141/T144; O3 có chứng cứ |
| D6 | Thử nghiệm người dùng và khóa preset | UI review + tập benchmark holdout | Người dùng đánh giá, lỗi cần sửa được đóng bằng evidence |

**Không tự thêm dependency/renderer mới** chỉ để sinh điểm đẹp. Nếu không có Word renderer đích trong kiến trúc hiện tại, giai đoạn nghiên cứu/diagnostic và patch cấu trúc vẫn có thể tiến hành nhưng phải dừng trước lời khẳng định “khớp kết quả in Word”. Không commit/push/deploy/migrate khi chưa được giao quyền thực thi cụ thể.

## 156. Definition of Done V8 và ma trận trạng thái

| Kết quả | Bằng chứng tối thiểu | Trạng thái khi soạn V8 |
|---|---|---|
| `SPEC_V8_READY` | 19 mục bổ sung; hard gates; schema; bảng hành động; 20 ca thử; nguồn | **Đạt mức đặc tả tài liệu** sau kiểm tra nội dung |
| `RESEARCH_VERIFIED` | Dẫn đúng nguồn Microsoft và giới hạn diễn giải | Đã đối chiếu nguồn; không thay cho test Word |
| `CODE_AUDITED` | HEAD + source+ test hiện hành | **Chưa thực hiện** |
| `SOLVER_VERIFIED` | Benchmark số học/fixture có kết quả lặp lại | **Chưa thực hiện trong sản phẩm** |
| `INTEGRITY_PASS` | Diff DOCX thật, O1/O2 + reopen | **Chưa thực hiện** |
| `WORD_RENDER_PASS` | Word target O3, ảnh before/after cùng môi trường, không regression | **Chưa thực hiện** |
| `USER_ACCEPTED` | Duyệt kết quả ở giao diện/in thực tế | **Chưa thực hiện** |

**Nhắc lại các mức bằng chứng:** `SPEC_READY` không có nghĩa `CODE_READY`; XML hợp lệ không có nghĩa bản in đạt; 144 ca là *danh mục thử nghiệm được đề xuất*, không phải 144 phép thử đã chạy PASS.

## 157. Kết luận V8 và ranh giới nghiên cứu tiếp theo

V8 đã làm rõ ba trụ cột còn thiếu để tính toán độ rộng cột có giá trị sử dụng thực:

1. **Đúng chỗ:** xác định bảng, story, section, lề và vùng chứa thật; không dùng một phép chia mm toàn tài liệu.
2. **Đúng nội dung trọng tâm:** bảo vệ token thiết yếu, đo kết quả Word thay vì đếm chữ và không cho “cột quan trọng” đồng nghĩa “cột lớn nhất”.
3. **Đúng bằng chứng:** chỉ duyệt ứng viên hơn baseline sau khi hard gates, so sánh cùng renderer và đánh giá blast radius; cho phép `NO_OP_VALID` khi bản gốc đã đạt.

**Kiến nghị triển khai có giá trị cao nhất:** chuyển ngay sang *audit read-only source dự án đích + bộ fixture thử nghiệm nhỏ nhưng đa dạng*, không mở rộng nghiên cứu lý thuyết vô hạn. Dựa trên audit, chỉ bổ sung thiếu sót thật, bảo toàn toàn bộ code/test đã PASS và đối chiếu trực quan trên Word trước khi cho phép ghi file đã tối ưu.

# PHẦN XXV. NÂNG CẤP V9 — CHỐT QUY TẮC NGHIỆM THU, ĐO DỮ LIỆU THỰC VÀ GIẢM RỦI RO TỐI ƯU GIẢ

> **Phạm vi V9:** Phần này là bản hiệu chỉnh thực thi của V8, không thiết kế lại engine, không thay văn bản quy định và không thay thế 144 trường hợp thử đã đặc tả. Mục đích là phân biệt rõ **điều kiện xác nhận trước khi sửa, bằng chứng về lợi ích, mức chất lượng có thể tuyên bố, và điểm dừng nghiên cứu**. Các ca T145–T152 chỉ bao phủ hành vi/ngoại lệ chưa mô tả đầy đủ ở V8.
>
> **Tình trạng thực nghiệm:** Các ví dụ tính toán trong Phần XXV là dữ liệu giả lập để kiểm tra logic; chưa đo từ Microsoft Word hay từ tài liệu DOCX thật. Không chuyển bất kỳ ví dụ, contract hay ca thử chưa chạy thành chứng cứ PASS của sản phẩm.

## 158. Audit V8: kết quả đã có, giới hạn và thay đổi tối thiểu của V9

### 158.1. Các phần không cần mở lại

Đã kiểm tra cấu trúc tập tin V8: **24 phần chính, 157 tiểu mục từ 1–157, 89 mục nguồn [S01]–[S89] không trùng**, các tham chiếu nguồn đã định nghĩa đều hợp lệ ở mức văn bản Markdown. Các khối quy tắc về thẩm quyền, phân loại bảng, bảo toàn nội dung, `preferred width`, lưới vật lý, `G0–G4`, `O0–O4`, trạng thái REVIEW/KEEP và bộ ca T01–T144 vẫn được giữ nguyên.

Các hạng mục sau **không được coi là đã xác minh chỉ nhờ audit file MD**: hiệu quả thuật toán trên DOCX, khả năng tương thích Word Windows/Word Mac, tính ổn định phân trang, chất lượng PDF khi in, độ chính xác nhận diện cột trọng tâm và tỷ lệ người dùng chấp nhận phương án.

### 158.2. Những khoảng trống cần đóng, không nhân đôi subsystem

| Khoảng trống ở cấp vận hành | Rủi ro | Điều chỉnh V9 |
|---|---|---|
| Lẫn lộn đơn vị nhận diện chữ và điểm ngắt dòng | Đánh giá sai nhu cầu độ rộng của văn bản tiếng Việt | Tách `grapheme` → `break opportunity` → `actual rendered line` |
| Nhìn thấy đường lưới Word rồi coi như viền bảng in được | Bản DOCX nhìn có ô nhưng bản in thiếu viền | Tách `editing_gridlines` khỏi `effective_printed_borders` |
| Tối ưu từng bảng độc lập dù cùng họ bảng trong một văn bản | Kết quả không nhất quán về tỷ lệ, đệm và phân cấp thông tin | Thêm kiểm tra `document_table_family`, nhưng không sửa đồng loạt |
| Cột trọng tâm do máy dự đoán nhưng không thể giải thích | Cấp sai mm cho nội dung ít giá trị đọc | Yêu cầu hồ sơ bằng chứng, mức chắc chắn và cách giải quyết xung đột |
| Chiều cao ước lượng tốt nhưng không có render đích | Tuyên bố bảng tối ưu in ấn khi chưa đủ chứng cứ | Chuẩn phát hành `DIAGNOSTIC` / `STRUCTURE_VERIFIED` / `WORD_RENDER_VERIFIED` |
| Thêm ca thử liên tục nhưng không có file kiểm thử | Báo cáo dài hơn mà độ tin cậy không tăng | Đặt tiêu chuẩn **dừng mở rộng lý thuyết** và chuyển sang fixture thực tế |

**Không đề xuất đổi tên hay tạo registry/service mới.** Nếu dự án đã có capability, trạng thái, audit log hoặc metadata tương đương, chỉ map các trường cần thiết vào cơ chế hiện hữu.

## 159. Ma trận thẩm quyền: quyết định định dạng phải có nguồn và phạm vi

Trước khi tính độ rộng, phải ghi nhận mỗi bảng thuộc văn bản hành chính, văn bản Đảng hay mẫu đặc thù. Các bảng được phát hiện trong body, phụ lục, textbox, footer, bảng lồng không tự động có chung quyền sửa.

| Tình huống | Authority ưu tiên | Quyết định mặc định |
|---|---|---|
| Bảng dữ liệu trong thân văn bản hành chính | Nghị định 30/2020/NĐ-CP + mẫu chỉ định, nếu có | Có thể **đề xuất** tối ưu hình học/định dạng an toàn |
| Bảng trong phụ lục văn bản hành chính | Nghị định 30 + chỉ dẫn phụ lục + mẫu thực tế | Không thay tiêu đề/đánh số phụ lục; chỉ xét nội dung bảng nếu không khóa |
| Bảng trong văn bản Đảng thuộc phạm vi Hướng dẫn 05 | Quy định 399 + Hướng dẫn 05 + mẫu cụ thể | Chọn profile tương ứng; tôn trọng chiều trang, lề và thể thức |
| Biểu mẫu có bảng và vùng ký, xác nhận | Mẫu đã ban hành/được chỉ định | `PRESERVE_OFFICIAL_FORM` trừ thuộc tính được ủy quyền sửa |
| Bảng dàn trang đầu văn bản, chữ ký, nơi nhận | Quy định thành phần thể thức + bố cục tài liệu | Không áp preset bảng dữ liệu |
| Chưa xác minh loại văn bản hoặc mẫu áp dụng | Chưa có authority đáng tin | `REVIEW_REQUIRED`, không gắn nhãn “vi phạm pháp lý” |

Giữ phân loại `[PL]`, `[BM]`, `[KN]`, `[KT]`, `[BK]` từ V8. Các preset thẩm mỹ hoàn toàn là `[KN]`. Mỗi thông báo vi phạm pháp lý phải có **nguồn, thành phần, phạm vi và trạng thái hiệu lực**; thông báo “không đẹp” không được biến thành thông báo “sai Nghị định 30/Hướng dẫn 05”. [S01]–[S06].

## 160. Xác định cột trọng tâm theo tác vụ đọc — từ chứng cứ đến quyền thay đổi

### 160.1. Tối thiểu hóa suy đoán

Tạo một `reader_task` ở cấp bảng, không tự đặt mỗi cột một mức điểm tuyệt đối rồi chia width. Quy trình:

1. Trích xuất nhãn tiêu đề, tên bảng, đoạn giới thiệu/trích dẫn liền kề **ở chế độ read-only**.
2. Kiểm tra mô hình dữ liệu có thể xác định theo quy tắc: STT, tên chủ thể, mô tả, thời hạn, số liệu, tình trạng, ghi chú, nhóm tổng cộng.
3. Nhận diện hành động đọc chính: `LOOKUP`, `COMPARE`, `TRACK_DEADLINE`, `VERIFY_COMPLIANCE`, `APPROVE`, `FILL_FORM`, `UNKNOWN`.
4. Kết hợp bằng chứng: yêu cầu do người dùng chỉ định > cấu trúc biểu mẫu được xác nhận > tín hiệu nhãn/kiểu dữ liệu > suy đoán thống kê. Không có lý do để AI thay deterministic logic cho các trường hợp nhận diện chính xác.
5. Nếu bằng chứng xung đột, giữ `UNKNOWN`/`AMBIGUOUS` và hiển thị lựa chọn, không âm thầm trao ưu tiên.

| Vai trò | Độ rộng cần bảo vệ | Lợi ích khi cấp thêm chỗ | Trường hợp không nên mở rộng |
|---|---|---|---|
| Số hiệu, STT | Đủ để nhận diện trọn vẹn token | Thường thấp sau khi đã vừa | Thêm chỗ chỉ tạo vùng trống |
| Chủ thể/đơn vị | Đủ phân biệt các bản ghi quan trọng | Cao khi tên đang xuống dòng làm mất khả năng quét | Đã đọc rõ, mở rộng làm hỏng cột mô tả |
| Mô tả nội dung | Đủ số dòng vừa phải, giữ cụm từ có nghĩa | Có thể cao vì thường chi phối chiều cao hàng | Đã đạt mức tốt, mở rộng làm hỏng cột khác |
| Ngày hạn/tiến độ | Bảo vệ ngày và ký hiệu không bị cắt/mập mờ | Thấp sau ngưỡng nhận diện, dù rất trọng tâm | Không cần dài nhất bảng |
| Số liệu/đơn giá | Giữ dấu âm, phần thập phân, đơn vị | Cao nếu số khó so sánh | Mở rộng chỉ để tạo khoảng trắng lớn |
| Ghi chú | Đủ đọc và xuống dòng hợp lý | Thấp/trung bình tùy tác vụ | Không chiếm ưu tiên chỉ vì chữ dài |

**Cột trọng tâm = ưu tiên khả năng đọc, không đồng nghĩa cột phải rộng nhất.** Phân loại ngữ nghĩa không được quyền sửa số liệu, ký tự hoặc cấu trúc ô gộp.

## 161. Bổ sung chuẩn đo tiếng Việt: grapheme, điểm ngắt và dòng kết xuất là ba đại lượng khác nhau

### 161.1. Định nghĩa đúng để tránh sai số

- `code point`: đơn vị mã hóa ký tự, **không đại diện cho một độ rộng glyph cố định**.
- `extended grapheme cluster`: đơn vị ký tự cảm nhận của người đọc; có thể gồm nhiều code point, ví dụ ký tự Latin cộng dấu; tham chiếu Unicode UAX #29 [S91].
- `line-break opportunity`: vị trí có thể kết thúc dòng theo bộ quy tắc Unicode UAX #14; **không phải chỗ Word chắc chắn sẽ xuống dòng** [S90].
- `actual_line_break`: vị trí xuống dòng thật khi renderer dàn trang với font, run, lề, chiều rộng ô, indent và thuộc tính đoạn cụ thể.
- `rendered_block_height`: chiều cao thực tế của đoạn/ô/hàng sau khi Word kết xuất; không bằng số code point nhân một hệ số hằng.

Thứ tự phép đo: `(run + font + script + language + protected token + paragraph settings) → candidate break opportunities → estimated wrap → verified rendered lines`. Không chấm PASS bản in khi mới có `estimated wrap`.

### 161.2. Các chuỗi đặc biệt phải được bảo toàn nguyên vẹn

| Trường hợp | Ví dụ minh họa | Cách kiểm |
|---|---|---|
| Dấu tiếng Việt tổ hợp Unicode | Chữ gồm base + dấu kết hợp | Không cắt bên trong grapheme; không tự chuẩn hóa lại dữ liệu nguồn |
| Khoảng trắng không ngắt | `U+00A0`, NBSP | Không coi là dấu cách ngắt tự do |
| Dấu nối không ngắt | `U+2011` | Không thay bằng gạch ngang ASCII |
| Chuỗi ngày/số/mã | `20/10/2026`, `HD-05/2026` | Đánh giá token nguyên khối khi tác vụ cần tra cứu |
| Dòng xuống chủ ý | `w:br`, đoạn riêng trong ô | Không tính như Word tự ngắt; không xóa để tiết kiệm chỗ |
| Công thức, field, hyperlink | Giá trị hiển thị có thể khác text run gốc | Giữ đối tượng; chỉ đo/đối chiếu qua nguồn render tương ứng |

Unicode UAX #14 phân biệt cơ hội ngắt dòng với phép *line fitting* của ứng dụng; UAX #29 mô tả ranh giới grapheme. Chúng là tài liệu kỹ thuật Unicode, **không phải bằng chứng cho thuật toán dàn dòng cụ thể của Word**. Việc áp dụng trực tiếp mọi quy tắc ngắt dòng Unicode như bản sao Word là không đủ cơ sở. [S90], [S91].

## 162. Đường kẻ bảng: phân biệt vạch hỗ trợ chỉnh sửa và viền in thật

**Quy tắc làm rõ ưu tiên V9:** Nếu những phần trước của báo cáo chỉ nói kiểm ở *Print Layout*, khi mục đích là xác minh **viền sẽ xuất hiện trên bản in**, phải ưu tiên Word **Print Preview (File → Print)** hoặc PDF xuất từ Word trên chính môi trường mục tiêu. Chế độ chỉnh sửa Print Layout vẫn có thể hiển thị lưới hỗ trợ, nên một ảnh chụp màn hình đơn lẻ chưa đủ chứng minh viền in.

Word có tính năng `View Gridlines` để người dùng thấy giới hạn ô kể cả khi bảng không đặt đường viền. Microsoft nêu **gridlines không in ra**, khác với table borders [S92]. Do đó, công cụ kiểm tra không được kết luận "bảng có viền" chỉ vì ảnh chụp trong chế độ chỉnh sửa thấy một lưới màu nhạt.

| Tầng hiển thị | Bằng chứng | Điều có thể kết luận |
|---|---|---|
| OOXML trực tiếp (`tblBorders`, `tcBorders`) | Thuộc tính khai báo | Có khai báo, chưa chắc phản ánh toàn bộ viền hiệu dụng |
| Table Style/conditional borders | Table look, style override, cạnh kề, xung đột viền | Cần resolve hoặc dùng kết xuất; không xem raw cell property là đủ |
| Word Editing View/Gridlines | Ảnh màn hình Word có đường lưới | Chỉ kết luận hỗ trợ chỉnh sửa, **không phải viền sẽ in** |
| Word Print Preview/PDF xuất từ Word | Bản kết xuất có điều kiện nguồn, font, build rõ | Có thể xác minh viền **của chính bản kết xuất đó** |

**Acceptance mới:** Với preset `Formal Grid`, nếu người dùng yêu cầu viền in nhìn thấy, bằng chứng tối thiểu là viền in có thật trên Print Preview hoặc PDF xuất từ Word mục tiêu, không phải `View Gridlines` bật. Với preset `Statistical Minimal`, không được tự xem ít đường viền là sai quy định khi mẫu không ấn định lưới.

## 163. Nhất quán thẩm mỹ ở cấp tài liệu — không sửa mọi bảng theo một preset cứng

Một tài liệu có thể đồng thời chứa bảng phân công, thống kê, biểu mẫu và bố cục chữ ký. Tối ưu từng bảng riêng lẻ không đủ để bảo đảm sự hài hòa trên toàn tài liệu; nhưng áp cùng viền, cỡ chữ và padding cho mọi bảng lại có thể phá mẫu.

**Khái niệm `document_table_family` đề xuất:** nhóm **chỉ các bảng có cùng vai trò và cùng authority**, ví dụ nhóm bảng thống kê tương đương nhau trong thân báo cáo. Các thuộc tính có thể đánh giá độ nhất quán gồm: kiểu tiêu đề cột, độ đậm tiêu đề, đường viền cùng loại, căn chỉnh số liệu, đệm ô và cách trình bày dòng tổng. Không tự chuẩn hóa tỷ lệ cột giữa hai bảng nếu nhiệm vụ đọc hoặc nội dung khác nhau.

**Quy trình 4 bước:** phát hiện nhóm tương đương → tìm thiết lập đang ổn định được dùng nhất quán → đề xuất thay đổi cục bộ đối với bảng lệch chuẩn → chỉ ghi khi người dùng cho phép và kiểm chứng không ảnh hưởng các bảng chung style. Tránh sửa Table Style dùng chung nếu điều đó gây thay đổi ngoài phạm vi; chỉ cần cảnh báo khi không thể chứng minh patch cục bộ đủ an toàn.

Đây là lớp thẩm mỹ `[KN]`, không phải điều khoản pháp luật. Đối với official forms, nhóm tương đương là **đúng mẫu pháp lý**, không phải "trông gần giống".

## 164. Ngân sách độ rộng: chỉ cấp thêm khi có lợi ích, không ép bảng luôn phủ hết trang

Gọi `W_allow` là độ rộng tối đa hợp lệ của vùng chứa đã xác minh (section, column, indent, text wrapping, bảng lồng...). Mỗi cột có `min_i` và `max_i`/độ rộng mong muốn từ nội dung, cùng các khóa/ô gộp theo V7–V8.

**Điều kiện hình học:** `sum(w_i) <= W_allow`, đồng thời thỏa các khóa và constraint ô gộp. **Không áp `sum(w_i) = W_allow` cho mọi bảng**: một bảng danh sách ba cột ngắn có thể cân đối hơn khi đặt hẹp hơn vùng cho phép và căn trang theo mẫu. Phần không dùng tới không tự động bị coi là lỗi.

Chỉ thêm độ rộng nếu có lợi ích đã định nghĩa trước: giảm lỗi đọc token quan trọng, giảm chiều cao hàng thực bị nút thắt, tránh vỡ tiêu đề, cải thiện nhóm so sánh số liệu hoặc đáp ứng mẫu đã khóa. Lợi ích chỉ là ước lượng thì **không đủ để tuyên bố kết quả Word**.

**Điều kiện bất khả thi:** nếu tổng độ rộng tối thiểu vượt vùng hợp lệ, trả `NO_SAFE_INLINE_FIT`; gợi ý các lựa chọn có phê duyệt như trang ngang hoặc phụ lục nếu quy định cho phép. Không tự giảm phông, xóa đệm cần thiết, cắt số, sửa dữ liệu, tách bảng hay đổi orientation để “bắt buộc vừa”.

## 165. Ví dụ định lượng có thể kiểm tra toán học — ưu tiên lợi ích toàn hàng

Tình huống giả lập: bảng phân công có 4 cột `STT`, `Nội dung`, `Đơn vị`, `Hạn`; trang có `W_allow=165 mm`. Đây chỉ là **mô hình kiểm tra nguyên tắc**; chưa đọc bất kỳ DOCX hoặc đo Word nào.

| Phương án | STT | Nội dung | Đơn vị | Hạn | Tổng chiều rộng |
|---|---:|---:|---:|---:|---:|
| Baseline | 12 | 70 | 55 | 28 | 165 mm |
| Candidate B | 12 | 85 | 43 | 25 | 165 mm |
| Candidate C | 12 | 76 | 49 | 28 | 165 mm |

Giả sử các cột có sàn tạm tính `[12, 60, 35, 25] mm`, đều thỏa ở cả ba phương án. Với một tập ba hàng, **giả sử** kết quả đo lý tưởng hóa như sau, đơn vị mm:

| Hàng | Baseline | B | C | Diễn giải |
|---|---:|---:|---:|---|
| 1 | 14 | 14 | 14 | Không đổi |
| 2 | 42 | 28 | 28 | Mở rộng cột Nội dung giúp giảm chiều cao hàng |
| 3 | 28 | 42 | 28 | B co cột Đơn vị quá nhiều nên tạo nút thắt mới |
| **Tổng ba hàng** | **84** | **84** | **70** | C tiết kiệm giả định 14 mm so với baseline |

**Diễn giải đúng:** Không thể chọn B chỉ vì cột Nội dung rộng hơn. C có thể là ứng viên tốt hơn về *chiều cao lý thuyết*, nhưng chỉ được áp dụng nếu giữ nguyên số liệu, không gây ngắt sai trường trọng tâm, không hỏng hàng tiêu đề và render cùng Word mục tiêu xác nhận. Nếu 14 mm chỉ là dự đoán, hoặc C làm một ngày hạn bị cắt, kết quả vẫn có thể là `KEEP_EXISTING`.

Một bảng không phải lúc nào cũng cần phủ hết 165 mm: ví dụ bản ghi chỉ có STT/ngày/trạng thái đủ đọc trong 100 mm, nên giữ 100 mm nếu mẫu và toàn trang nhìn cân đối. V9 **không** đặt “tiết kiệm 14 mm” thành ngưỡng chung cho mọi bảng.

## 166. Phân định các oracle: điều gì đã được quan sát, điều gì chỉ là dự đoán

| Kiểu kết quả | Bằng chứng | Có thể công bố | Không được công bố |
|---|---|---|---|
| `SPEC_READY` | MD, nguồn, rule, test definitions | Đặc tả đã kiểm tra nội tại | Engine đã hoạt động |
| `ESTIMATED` | Phép tính geometry, dự đoán wrap/row | Ứng viên có vẻ khả thi để xem trước | Bản in đẹp hoặc không cắt chữ |
| `STRUCTURE_VERIFIED` | DOCX reopen, integrity/OOXML/relationship diff O1/O2 PASS | Bất biến cấu trúc/nội dung trong phạm vi kiểm | Pixel/Print Layout đúng |
| `WORD_RENDER_VERIFIED` | Cùng build Word/font và before/after O3 PASS | Trình bày đã đạt tại môi trường Word mục tiêu | Mọi bản Word/OS/printer đều giống |
| `USER_APPROVED` | Review xác định, phạm vi đã duyệt | Được người dùng chấp thuận phương án | Tự động đảm bảo mọi máy đều cho kết quả tương đương |

Không suy diễn từ `STRUCTURE_VERIFIED` sang `WORD_RENDER_VERIFIED`. Không dùng một ảnh HTML/CSS hoặc lưới Word Editing View thay cho xuất in. Khi chưa có Word renderer mà người dùng cần kết quả in đúng, hệ thống có thể cung cấp chẩn đoán và ứng viên để review, **không gắn trạng thái PRINT_READY**.

## 167. Điều kiện chấp nhận có thể kiểm thử: so baseline theo từng mục tiêu, không chấm điểm tùy ý

Áp dụng thứ tự đánh giá `G0–G4` của V8; V9 cụ thể hóa:

```text
ACCEPT(candidate):
  1. Same authorized source snapshot and verified table identity.
  2. Applicable legal/form rules satisfied; changed fields in allowlist.
  3. O1/O2 PASS on reopened output; content and topology invariants PASS.
  4. No new clipping, overlap, critical-token ambiguity, or forbidden
     downstream shift according to the required target render oracle.
  5. For claims of print-layout improvement: O3 PASS in the same target
     renderer environment, with paired baseline/candidate evidence.
  6. At least one predeclared user-relevant metric improves beyond the
     measurement uncertainty/materiality threshold calibrated beforehand.
  7. Higher-priority metrics do not get materially worse.
  8. No safer/equivalent candidate with a smaller patch has been preferred.
  ELSE KEEP / REVIEW / BLOCK with reason code; never silently fallback
  to a visually unverified APPLY.
```

Đối với **chỉ báo chẩn đoán**, có thể bỏ mục O3 nhưng phải ghi `UNVERIFIED_LAYOUT`; điều này không cấp quyền phát hành với tuyên bố “đạt chuẩn in”. Các ngưỡng vật chất (*materiality*) phải được định nghĩa theo benchmark và môi trường đo, không được vay mượn như một hằng số mang tính pháp lý.

Thước đo đề xuất cho một cặp baseline/candidate: số ô trọng tâm không đọc được (định nghĩa rõ), số token quan trọng bị cắt, số hàng có chiều cao không mong muốn, số trang vùng ảnh hưởng, số chỗ tách caption khỏi bảng, mức lệch style trong cùng nhóm và số thuộc tính bị sửa. **Không cộng các đại lượng khác đơn vị vào một điểm chất lượng chung để vượt hard gate**.

## 168. Mẫu bản ghi quyết định tối thiểu để tái lập và kiểm toán

```yaml
schema: table-layout-decision-v9-spec  # minh họa, không phải sản phẩm hiện có
source:
  fingerprint: '<sha256 của file nguồn, không công bố nếu nhạy cảm>'
  authority: ND30 | PARTY_HD05 | SPECIAL_FORM | UNKNOWN
  approval_scope: read_only | suggest | apply_approved
location:
  part_uri: word/document.xml
  table_locator: '<định danh xác minh tại thời điểm kiểm>'
  container: body | appendix | header | footer | nested | other
reader_task:
  type: TRACK_DEADLINE
  evidence: USER_DECLARED | FORM_DEFINED | RULE_INFERRED | AMBIGUOUS
geometry:
  status: VERIFIED | ESTIMATED | UNKNOWN
  maximum_width_twips: '<số nguyên khi đã xác minh>'
proposal:
  action: A0_KEEP | A1_REBALANCE_WIDTH | other_allowed_action
  target_widths_twips: []
  modified_property_allowlist: []
evidence:
  structure: NOT_RUN | PASS | FAIL
  content: NOT_RUN | PASS | FAIL
  render: NOT_AVAILABLE | NOT_RUN | PASS | FAIL
  target_renderer_fingerprint: '<khi có>'
  affected_neighborhood: []
  baseline_candidate_pair: '<tham chiếu phiên QA được phép lưu>'
decision:
  value: KEEP_EXISTING | REVIEW_REQUIRED | APPLY_APPROVED | BLOCKED
  reason_codes: []
  reviewer_approval: false
  rollback_source_snapshot: '<tham chiếu nội bộ, không lưu nội dung khi bị cấm>'
```

**Không yêu cầu tạo storage mới.** Nếu ứng dụng áp dụng chính sách không lưu DOCX đầu vào/đầu ra/tạm, manifest chỉ được tồn tại trong phạm vi xử lý và chính sách dữ liệu cho phép. Log lỗi không được ghi nội dung ô, thông tin cá nhân, dữ liệu mật hay bản chụp tài liệu trái phép. Dùng hợp đồng vốn có của dự án để lưu/đối chiếu trạng thái; không tự nhân đôi nguồn authority.

## 169. Ma trận lựa chọn thao tác khi cần tối ưu chất lượng bảng

| Vấn đề người dùng nhìn thấy | Ưu tiên đề xuất | Khi không được làm |
|---|---|---|
| Bảng đã đẹp, đọc tốt và nằm trong vùng hợp lệ | `A0_KEEP` | Không sửa chỉ để tạo file mới |
| Cột mô tả xuống quá nhiều dòng; còn độ rộng hợp lệ từ cột ít cần | `A1_REBALANCE_WIDTH` sau khi bảo vệ token trọng tâm | Không đổi khóa mẫu, ô gộp hoặc `W_allow` |
| Cột ngày/bộ phận bị cắt hoặc ngắt khó hiểu | Bảo vệ độ rộng sàn; khảo sát phân phối lại | Không giảm cỡ chữ, sửa chuỗi nguồn hoặc thay dấu |
| Ô sát đường viền | Xem `A2_ADJUST_CELL_MARGINS` trong preset có quyền | Không đặt padding bằng 0 chỉ để tiết kiệm |
| Bảng nhiều trang, hàng tiêu đề không lặp | Xem `A3_HEADER_REPEAT` khi hàng đầu đã xác định rõ | Không tạo tiêu đề giả/ngắt thủ công |
| Hàng `Exactly` che chữ | Gợi ý `A4_SAFE_ROW_HEIGHT` | Không sửa vùng ký hoặc biểu mẫu khóa |
| Bảng thấy lưới khi soạn nhưng in không có viền | Kiểm `effective_printed_borders`, chỉ đề xuất `A5` khi mẫu yêu cầu | Không dùng trạng thái View Gridlines làm oracle |
| Bảng không thể vừa an toàn trong section | `NO_SAFE_INLINE_FIT` → review trang ngang/phụ lục | Không tự chỉnh section và đầu/chân trang |
| Chỉ có kết quả ước lượng từ HTML/OOXML | `REVIEW_REQUIRED` nếu cần xác nhận bản in | Không báo `WORD_RENDER_VERIFIED` |

Chỉ các nhóm hành động A0–A6 đã có trong V8 được tái sử dụng. Các quy tắc trên là **cổng chọn hành động**, không phải yêu cầu xây thêm một subsystem mới.

## 170. Đánh giá toàn tài liệu: cân đối bảng và không phá bố cục xung quanh

Chất lượng một bảng không chỉ nằm trong hình chữ nhật của nó. Ở mỗi candidate cần định nghĩa *blast radius* hợp lý: caption trước bảng, ghi chú và nguồn số liệu sau bảng, số trang đã bị ảnh hưởng, bảng gần kề, chữ ký/nơi nhận nếu bị dịch và ranh giới section. Đặc biệt, ứng viên làm bảng thấp đi nhưng để lại một khoảng trống lớn hoặc đẩy caption mất liên kết với bảng có thể kém hơn baseline.

Trong tài liệu có nhiều bảng cùng vai trò, kiểm tra nhất quán về kiểu tiêu đề và khoảng cách **chỉ như một gợi ý độc lập**. Không áp đồng loạt cho bảng dàn trang, biểu mẫu in sẵn, bảng ký xác nhận hoặc bảng lồng mà không có căn cứ. Việc tạo một nhóm bảng tương đương không làm thay đổi source-of-truth pháp lý hoặc ownership của từng block.

**Quy tắc nghiệm thu theo phạm vi:** thay đổi chỉ thuộc `tblPr`, `tcPr` hoặc `trPr` của một bảng không bảo đảm chỉ bảng đó đổi layout. Nếu kết xuất cho thấy ảnh hưởng đến đoạn văn/chữ ký/khu vực kế tiếp, phải kiểm tra các vùng đó. Không test lại toàn bộ tài liệu một cách máy móc khi renderer và bằng chứng xác định được phạm vi ảnh hưởng nhỏ hơn; nhưng cũng không tuyên bố 'ngoài ảnh hưởng' khi chưa xác định được sự dịch trang.

## 171. Tám trường hợp thử mới T145–T152: chỉ cho khoảng trống thực sự của V9

**Tình trạng:** đặc tả `NOT_RUN`; không có DOCX fixture hoặc Word render đã chạy trong V9.

| ID | Đầu vào đặc trưng | Bằng chứng nghiệm thu / hành vi kỳ vọng |
|---|---|---|
| T145 | Ô có soft hyphen `U+00AD` và zero-width space `U+200B` ảnh hưởng cách xuống dòng | Không tự xóa/thay ký tự nguồn; ghi nhận cơ hội ngắt là dự đoán cho tới khi Word render |
| T146 | Chuỗi có cơ hội ngắt dòng Unicode nhưng Word renderer chọn dòng khác | Đặt nhãn `ESTIMATED` đến khi O3 kiểm; không kết luận theo UAX #14 rằng Word chắc chắn xuống dòng |
| T147 | Bảng trong Word Editing View thấy gridlines nhưng không có borders in | Kiểm đúng bản in/Print Preview hoặc PDF do Word xuất; không báo `PRINTED_BORDER_PASS` nhờ đường lưới |
| T148 | Bảng nhỏ hợp lệ, tổng width thấp hơn `W_allow` | Không kéo các cột ra cho đủ trang chỉ để tránh khoảng trống |
| T149 | Ba bảng: hai bảng thống kê tương đương, một biểu mẫu khóa | Gợi ý nhất quán đúng nhóm; không sửa biểu mẫu và shared style ngoài phạm vi |
| T150 | Cột trọng tâm “Hạn” đã đủ đọc; cột “Nội dung” quyết định chiều cao hàng | Không cấp hết phần dư cho “Hạn” chỉ vì điểm ưu tiên ngữ nghĩa cao |
| T151 | Cột mô tả được nới nhưng một cột khác tạo nút thắt hàng mới | Không chọn ứng viên dựa vào một ô; đánh giá tổng hàng và thay đổi phân trang |
| T152 | O1/O2 PASS, chưa có Word renderer, người dùng yêu cầu “khớp bản in” | Trạng thái `STRUCTURE_VERIFIED`/`REVIEW_REQUIRED`, không tuyên bố `WORD_RENDER_VERIFIED` |

Ca V8 T125–T144 vẫn giữ nguyên. Các ca T145–T152 chỉ cần fixture mới nếu không thể chứng minh yêu cầu bằng fixture, test hoặc bằng chứng đã tồn tại. Giữ `NOT_RUN` cho tới khi có file thử và kết quả quan sát tương ứng.

## 172. Điều kiện đóng đặc tả V9 và chuyển sang kiểm chứng thực nghiệm

### 172.1. Bộ kết quả đủ để giao phát triển

- [ ] Với từng profile ND30/HD05, điều kiện pháp lý/biểu mẫu được dẫn điều khoản đúng phạm vi; phần khuyến nghị không lẫn yêu cầu bắt buộc.
- [ ] Những quy tắc cho width có đầu vào `reader_task`, `column_role`, `geometry`, `locks`, font, renderer, `source_snapshot` và quyền sửa.
- [ ] Mỗi thay đổi có allowlist thuộc tính, hành vi khi bất khả thi, candidate baseline, reason code và rollback.
- [ ] Danh mục kiểm thử phân biệt `NOT_RUN`, `STRUCTURE_VERIFIED`, `WORD_RENDER_VERIFIED` và kết quả người dùng duyệt.
- [ ] Phần tích hợp thực thi phải audit code/primitive hiện hữu, không tạo hệ thống mới khi thành phần có sẵn đáp ứng.

### 172.2. Điều kiện **dừng mở rộng lý thuyết**

Không tăng phiên bản V10 chỉ vì có thêm ý tưởng thẩm mỹ. Trước hết cần ít nhất một *fixture corpus* gồm bảng hành chính, bảng Đảng, bảng số, bảng tiếng Việt dài, ô gộp, bảng nhiều trang và mẫu được bảo vệ **được phép sử dụng**, có baseline Word cụ thể. Từng lỗi phải gắn bằng chứng quan sát được. Chỉ khi benchmark cho thấy lỗi còn tồn tại, điều kiện chưa được mô tả hoặc nguồn quy định cập nhật, mới sửa/thêm quy tắc đúng phạm vi. Đây là hướng phù hợp với **REUSE FIRST, PRESERVE PROVEN WORK và blast-radius testing**.

### 172.3. Kết luận V9

- Mục tiêu không phải "mọi cột vừa trang" mà là **tối đa hóa khả năng đọc thông tin trọng tâm trong giới hạn bố cục hợp lệ**, không làm xấu toàn hàng, bảng, trang và văn bản.
- Tách bạch quy tắc pháp lý với thiết lập thẩm mỹ; tách dự đoán phép ngắt dòng với kết xuất Word; tách đường lưới chỉnh sửa với viền in thật.
- Giữ baseline khi không chứng minh được một phương án cải thiện an toàn và có ý nghĩa.
- Chỉ công bố mức nghiệm thu tương ứng bằng chứng đã có; **văn bản nghiên cứu V9 không phải bằng chứng bộ định dạng DOCX đã triển khai**.


# PHẦN XXVI. V10 — ĐÓNG KHOẢNG CÁCH GIỮA ĐẶC TẢ VÀ BẰNG CHỨNG THỰC NGHIỆM

> **Tính chất của phần này:** Bản cập nhật dựa trên **kiểm thử độc lập có thể tái lập**, không phải xác nhận rằng module DOCX của bất kỳ repository nào đã chạy. Những mẫu DOCX được tự tạo từ dữ liệu giả lập ngày 20/10/2026; không dùng dữ liệu cơ quan, tài liệu mật, hay mẫu biểu pháp lý thực. Bộ kết xuất thăm dò sử dụng **LibreOffice headless**, không phải Microsoft Word. Các kết luận phải mang nhãn môi trường tương ứng. Phần I–XXV, 152 tình huống đã đặc tả và phụ lục trước đây được giữ nguyên.

## 173. Kết luận kiểm toán V9 và thay đổi thực sự cần thiết

V9 đã mô tả khá đầy đủ các ràng buộc về pháp lý, bảng phức tạp, độ rộng ưu tiên, xử lý cột trọng tâm, tiêu chí O1–O4, và cơ chế `KEEP/REVIEW/APPLY`. Khoảng trống còn lại **không phải thiếu thêm thuật toán lý thuyết**, mà là thiếu: (a) file mẫu đầu vào được phép dùng, (b) cặp nguồn–ứng viên có thể chạy lại, (c) dấu vết phép đo trước/sau và (d) tiêu chí phân biệt xác minh trên LibreOffice với xác minh trên Word. V10 chỉ bổ sung những hạng mục này, không xây subsystem, rule registry, storage hay khả năng AI song song.

**Những nội dung V9 tiếp tục được coi là nguồn chuẩn của báo cáo:** các cổng **pháp lý, mẫu áp dụng và bảo toàn dữ liệu** cùng bắt buộc được kiểm tra trước tiêu chí `[KN]` (không coi đây là phép xếp hạng một chiều thay thế nguyên tắc pháp luật/mẫu); bảo toàn `source_snapshot`; tính toán trong lưới vật lý; không đánh đồng `semantic_priority` với `width_need`; không dùng XML hoặc điểm thẩm mỹ để xác nhận chất lượng in; giữ baseline khi không có lợi ích được chứng minh. Không nhân bản 152 ca thành một danh mục mới.

## 174. Bộ corpus thăm dò: tám fixture DOCX tự tạo, có thể chạy lại

Bộ mẫu kèm theo được tạo với **`python-docx 1.2.0`**, tài liệu DOCX dạng OPC/WordprocessingML, dữ liệu hoàn toàn tổng hợp. Mỗi file có SHA-256 trong `manifest.json`; mã sinh có trong `generate_fixtures.py`. Các mã F01–F08 là **mã dữ liệu kiểm chứng**, không phải mã kịch bản T153+.

| File | Thành phần cần kiểm | Lợi ích / nguy cơ cụ thể | Tình trạng |
|---|---|---|---|
| `F01_work_plan.docx` | 4 cột, công việc–đơn vị–thời hạn | Phân bổ width theo nội dung trọng tâm; nhận diện ngày hạn | Tạo, mở ZIP, render LO |
| `F02_statistics.docx` | Số liệu, tỷ lệ, căn phải | Giữ chính xác dấu phân cách, dấu âm/dương, thứ tự hàng | Tạo, mở ZIP, render LO |
| `F03_multipage.docx` | 46 hàng dữ liệu + hàng tiêu đề, cỡ chữ Đảng giả lập | Trang nhiều, lặp tiêu đề hàng đầu | Tạo, mở ZIP, render LO 6 trang |
| `F04_merged_headers.docx` | Tiêu đề hai tầng, ô gộp theo hàng/cột | Không phá cấu trúc `gridSpan`/`vMerge` | Tạo, mở ZIP, render LO |
| `F05_nested_long_tokens.docx` | Bảng con và mã hồ sơ dài | Không flatten bảng lồng hoặc tự sửa token | Tạo, mở ZIP, render LO |
| `F06_form_like.docx` | Biểu mẫu giả lập có ô trống và nơi ký | Ưu tiên `PRESERVE`; không coi là mẫu chính thức | Tạo, mở ZIP, render LO |
| `F07_landscape.docx` | Trang A4 ngang, 8 cột | Hình học theo section, không mượn width trang dọc | Tạo, mở ZIP, render LO |
| `F08_exact_height.docx` | Hàng chiều cao `Exactly` 7 mm, nội dung dài | Tái hiện một ca nội dung bị cắt khi kết xuất | Tạo, mở ZIP, render LO: lỗi thấy được |

**Ranh giới diễn giải:** Mặc dù F03 dùng cỡ chữ và cấu hình trang mô phỏng bối cảnh văn bản Đảng, đó **không** phải chứng nhận tuân thủ đầy đủ Quy định 399/Hướng dẫn 05. F06 không phải biểu mẫu đã ban hành. Những mẫu này không thay thế tài liệu thật được cấp quyền dùng để nghiệm thu.

### 174.1. Chứng cứ cấu trúc baseline

- Có **8/8 file DOCX** tạo thành công, qua `ZipFile.testzip()` và mở được bằng `python-docx`.
- Tổng số bảng cấp ngoài: **8**; riêng F05 có một bảng lồng, nâng tổng bảng vật lý được mô hình hóa trong tám mẫu lên **9**.
- Dữ liệu đầu vào có định danh, mô tả và bản băm SHA-256; một fixture chỉ đại diện một nhóm tình huống chính, không giả định bao phủ toàn bộ tài liệu thật.
- Đã kết xuất các fixture bằng LibreOffice headless và kiểm tra trang đầu đại diện bằng ảnh; F03 là **6 trang**, các fixture khác **1 trang** trong cùng môi trường thử.
- **Chưa thực hiện** Microsoft Word Windows/macOS, bản in máy in thật, so sánh nhiều font/môi trường và toàn bộ T01–T152. Không báo PASS các hạng mục đó.

## 175. Phát hiện thực nghiệm số 1: một DOCX hợp lệ vẫn có thể cắt chữ ở đầu ra

Đầu vào F08 chứa chuỗi đầy đủ trong ô thứ hai hàng dữ liệu, trong đó có cụm `Dòng ba vẫn phải được bảo toàn nguyên vẹn.`. Hàng dữ liệu có `w:trHeight` ở mức xấp xỉ 7 mm và `w:hRule="exact"`.

Quan sát **trên bản PDF do LibreOffice xuất**:

| Tiêu chí | Baseline F08 | Ứng viên F08-candidate |
|---|---|---|
| `w:hRule` | `exact` | `atLeast` |
| Giá trị `w:val` của `w:trHeight` | 397 twips (giữ nguyên) | 397 twips (giữ nguyên) |
| Có chuỗi `Dòng ba` trong phần văn bản trích từ PDF | **Không** | **Có** |
| Ảnh kết xuất | Nội dung vượt khỏi chiều cao hàng và bị che | Văn bản hiển thị đủ trong hàng được mở cao |
| Số trang PDF | 1 | 1 |
| Nội dung text của `w:t` trong DOCX | Có đầy đủ | **Giữ nguyên như nguồn** |
| Bảng/hàng/ô | 1 bảng, 2 hàng, 2 cột | **Không đổi** |
| ZIP part có nội dung byte thay đổi | — | Chỉ `word/document.xml` |

Tác động trực tiếp: **mở DOCX thành công, Open XML có chữ và thậm chí có cấu trúc hợp lệ không đủ để kết luận người nhận nhìn thấy toàn bộ nội dung**. Trong mẫu này, chỉ thay `exact` thành `atLeast` đã cải thiện kết xuất LibreOffice mà không đổi nội dung ô. Tuy nhiên, **không biến kết quả này thành luật sửa tự động mọi hàng `Exactly`**: biểu mẫu có vùng chữ ký, ô định vị, form cố định hoặc Word renderer khác vẫn cần chính sách riêng và xác nhận.

**Bằng chứng đã có:** ZIP integrity, tương đương chuỗi `w:t` nguồn–ứng viên, số bảng/hàng/ô được bảo toàn, PDF text extraction và ảnh kết xuất của F08 trước/sau. **Bằng chứng còn thiếu:** nghiệm thu cùng cặp file bằng Microsoft Word mục tiêu, hình học đầy đủ của các vùng lân cận trên Word, so sánh tất cả OOXML semantics trên một tập dữ liệu phức tạp và quyền sửa trên tài liệu thật.

## 176. Phát hiện thực nghiệm số 2: lặp tiêu đề qua sáu trang trong môi trường thử

F03 chứa một hàng tiêu đề được đánh dấu `w:tblHeader` và 46 hàng dữ liệu. Trên PDF do LibreOffice tạo, văn bản `STT` của hàng tiêu đề xuất hiện tại đầu **6/6 trang**; hàng dữ liệu cuối (46) vẫn có trên PDF. Đây là một quan sát cụ thể ở **LibreOffice**, không phải bằng chứng Word tương đương.

Microsoft quy định chức năng lặp hàng tiêu đề yêu cầu chọn hàng đầu tiên; bảng chỉ tự lặp khi phân trang tự động và tính năng không lặp nếu chèn ngắt trang thủ công bên trong bảng. Nên giữ T liên quan đến repeat-header ở hai mức: xác minh XML là mức cấu trúc; Word Print Layout/PDF xuất từ **Word mục tiêu** mới là mức nghiệm thu chất lượng in. Nguồn: [S07] `https://support.microsoft.com/en-us/word/repeat-table-header-on-subsequent-pages`.

## 177. Phân lớp trạng thái bằng chứng mới — tránh tự nâng hạng PASS

Để V9 và V10 không lẫn lộn, tất cả bản ghi thử phải nêu rõ `what_was_tested`, `what_was_not_tested`, và `environment`.

| Trạng thái | Chứng cứ tối thiểu | Điều **không** được kết luận |
|---|---|---|
| `FIXTURE_CREATED` | DOCX tồn tại, checksum, manifest | Không kết luận render hay tuân thủ luật |
| `PACKAGE_OPENED` | ZIP pass, parser đọc được | Không kết luận text hiển thị đủ |
| `CONTENT_DIFF_PASS` | So sánh nội dung/đối tượng theo scope xác định | Không kết luận tất cả OOXML part khác ngoài scope bất biến |
| `LO_RENDER_OBSERVED` | LibreOffice version, PDF/PNG, trang và vùng ảnh liên quan | Không tuyên bố `WORD_RENDER_VERIFIED` |
| `WORD_RENDER_VERIFIED` | Microsoft Word target build, font, print preview hoặc PDF xuất từ Word, cặp baseline–ứng viên | Không suy ra mọi môi trường Word đều giống nhau |
| `LEGAL_FORM_REVIEWED` | Mẫu và căn cứ đúng điều khoản, người kiểm có thẩm quyền | Không thay thế bằng ảnh đẹp |
| `DEPLOYMENT_PASS` | Kết quả tích hợp thật qua các gate của dự án | Không đồng nghĩa một fixture cô lập PASS |

Nguồn Microsoft nêu rõ Open XML SDK **không cung cấp chức năng dàn trang của Word**, không thay Office object model và không tự bảo đảm tài liệu hợp lệ chỉ vì sử dụng SDK; do đó phải giữ tách biệt validation và layout oracle. Nguồn mới: [S93] `https://learn.microsoft.com/en-us/office/open-xml/open-xml-sdk-design-considerations`.

## 178. Chuẩn đặc tả thử nghiệm có thể tái lập (`experiment_record`)

Mỗi phép thử hoặc ứng viên cần ghi theo cấu trúc nhỏ dưới đây; nếu dự án đã có report/log tương đương thì **map sang nguồn hiện có**, không cần tạo bảng CSDL hay event bus.

```yaml
record_version: table-qa-v10
case_id: F08
scenario: exactly_row_clipping
input_fingerprint: "<SHA-256 trong manifest>"
input_owner: synthetic_fixture
profile: ND30_EXAMPLE_NOT_LEGAL_CERTIFICATION
scope: word/document.xml, table[1], row[2]
change:
  property: w:trHeight/@w:hRule
  from: exact
  to: atLeast
  allowlist: ["w:trHeight/@w:hRule"]
  authorization: TEST_ONLY
structural_evidence:
  opc_integrity: PASS
  same_text_runs: PASS
  same_table_row_cell_topology: PASS
  changed_zip_parts: ["word/document.xml"]
render_evidence:
  engine: LibreOffice_headless
  baseline_pdf_contains_final_sentence: false
  candidate_pdf_contains_final_sentence: true
  baseline_pages: 1
  candidate_pages: 1
  word_target_status: NOT_RUN
status: LO_RENDER_OBSERVED
claim_scope: "Synthetic F08, only LibreOffice environment"
```

Trong tài liệu thật, tuyệt đối không ghi văn bản ô, ảnh nội dung nhạy cảm hoặc bản sao DOCX vào audit log trái với chính sách riêng tư. Dấu vết nêu trên chỉ là ví dụ dùng dữ liệu giả lập công khai trong bộ fixture.

## 179. Các quy tắc lựa chọn độ rộng đã đủ để chuyển từ nghiên cứu sang đo thực nghiệm

Không đặt thêm công thức tính điểm ngữ nghĩa hoặc ngưỡng cố định nếu chưa có kết quả benchmark. Khi tối ưu một bảng, sử dụng đầu vào tối thiểu:

1. `reader_task` xác nhận được (tra cứu/so sánh/theo dõi hạn/đối chiếu/phê duyệt);
2. `row/column-role` và ràng buộc tối thiểu của các token quan trọng;
3. `geometry` tính theo **đúng vùng chứa** (section, page orientation, nesting, indentation, floating position);
4. `hard locks` (mẫu bắt buộc, chữ ký, image/field, merge topology, dữ liệu, phông/cỡ chữ);
5. `baseline` và tập ứng viên hữu hạn, bao gồm cả **giữ nguyên**;
6. renderer mục tiêu, mức kiểm chứng và phạm vi ảnh hưởng.

Ví dụ minh họa để kiểm toán số học (không phải phép đo Word): trên vùng được phép 165 mm, bảng 5 cột có baseline `[10, 60, 35, 24, 36]` mm, ứng viên `[10, 75, 32, 25, 23]` mm, cả hai đều bằng **165 mm**. Việc cộng thêm 15 mm cho cột nội dung có thể cải thiện xuống dòng, nhưng giảm cột ghi chú 13 mm có thể tạo nút thắt chiều cao mới. **Chưa được chọn phương án** cho tới khi đánh giá nút thắt của các hàng, đoạn/caption lân cận và kiểm chứng kết xuất.

Nếu có nhiều ứng viên đạt hard gates, ưu tiên ứng viên ít thay đổi, giữ được thông tin trọng tâm và cho phép đọc nhanh. Không ép chiếm hết vùng in nếu bảng hiện tại đã phù hợp; không gán cột “Hạn” nhiều width chỉ vì đây là cột quan trọng.

## 180. Quy trình đo khi triển khai thật: tuần tự, có điểm dừng và không test lại toàn bộ máy móc

| Chặng | Đầu ra xác minh được | Điểm dừng |
|---|---|---|
| D0. Audit khả năng hiện hữu | Phần mềm, package, converter, parser, printer/render, unit test và contract đã có | Thiếu quyền hoặc không xác minh được baseline → không thay code |
| D1. Gắn fixture | Chạy F01–F08 qua pipeline hiện hữu **nếu có** | Không tạo đường xử lý DOCX song song |
| D2. Chọn lỗi tái hiện | Cặp baseline/output có lỗi nhìn thấy, scope và nguồn | Nếu không thấy lỗi → `NO_OP_VALID` |
| D3. Tạo sửa nhỏ nhất | Một tập thuộc tính được phép sửa, diff gói | Nếu thay trái phép → `BLOCKED` |
| D4. Kiểm cấu trúc và nội dung | OPC, XML topology, text/relationships/fields phù hợp scope | Một hard gate FAIL → rollback |
| D5. Kiểm kết xuất cùng renderer | Print Layout/PDF baseline–ứng viên, so các vùng bị ảnh hưởng | Không có renderer mục tiêu → không xác nhận chất lượng in mục tiêu |
| D6. Kiểm người dùng và mẫu | Cột trọng tâm dễ đọc, hình thức đủ trang trọng, đúng biểu mẫu | Chưa duyệt → chỉ đề xuất |
| D7. Chốt kết quả | Manifest, reason code, PASS/FAIL và đường rollback | Không tuyên bố triển khai khi chưa tích hợp |

**Ưu tiên chi phí thấp:** chạy đúng 8 fixture mới trước, sau đó chọn lại ca T01–T152 có hành vi/contract bị tác động và thêm fixture thật nếu có lỗi khác. Không chạy lại 152 ca chỉ để tạo con số PASS; không mở các phần `PROVEN/LOCKED` nếu không có bằng chứng lỗi hoặc phạm vi ảnh hưởng trực tiếp.

## 181. Định nghĩa nghiệm thu riêng cho thuật toán tối ưu độ rộng cột

Độ rộng có thể được công bố là **được tối ưu trên tài liệu và môi trường được kiểm** chỉ khi:

- `G0`: thẩm quyền, nội dung, merge topology, dữ liệu và quyền sửa **PASS**;
- không xuất hiện chữ bị cắt, đối tượng mất, bảng tràn vùng in hoặc chuyển trang gây hỏng thông tin;
- cột trọng tâm được xác định theo tác vụ có căn cứ, không phải do suy đoán thiếu kiểm chứng;
- phương án cải thiện ít nhất một chỉ số đã đặt trước **và không gây suy giảm đáng kể ở tiêu chí cao hơn**;
- kiểm kết xuất baseline–ứng viên trên cùng phiên bản renderer/font/config; nếu mục tiêu là Word thì không lấy LibreOffice thay Word;
- so cả hàng, bảng, trang và vùng trước/sau, không chỉ so chiều cao một ô;
- đủ quyền phê duyệt và có khả năng hoàn tác.

**Nếu dữ liệu đo còn thiếu:** kết quả chính xác là `NO_SAFE_DECISION` hoặc `REVIEW_REQUIRED`, không phải `FORMAT_SUCCESS`. Nếu bảng đã hợp lệ và không có phương án tốt hơn có bằng chứng, `NO_OP_VALID` là thành công **không thay đổi**.

## 182. Danh mục lỗi/rủi ro còn tồn tại sau V10

| ID | Vấn đề chưa có bằng chứng đủ | Hành động đúng tiếp theo |
|---|---|---|
| R10-01 | Chưa nghiệm thu các fixture bằng Microsoft Word đích | Chạy Word Windows/Word Mac nếu được yêu cầu; lưu fingerprint build/font |
| R10-02 | Chưa có corpus DOCX hành chính/Đảng thật được phép thử | Bổ sung mẫu vô danh hóa/được ủy quyền, tránh dữ liệu mật |
| R10-03 | Chưa có kết quả từ engine của dự án | Audit repo và chạy lại fixture trên pipeline hiện hữu trước khi lập thay đổi |
| R10-04 | Chưa có nhãn/đánh giá người đọc để hiệu chỉnh `semantic_priority` | Gắn nhãn tác vụ trên mẫu thật, đối chiếu đồng thuận người duyệt |
| R10-05 | Chưa đo tác động đến footer/chữ ký/phụ lục sau khi sửa width | Mở rộng blast radius theo kết quả phân trang thực |
| R10-06 | Chưa thử đặc tính font chữ trên nhiều môi trường | Khóa/ghi font fingerprint và ghi rõ renderer |
| R10-07 | Kiểm giữ nguyên text ở F08 chưa đại diện mọi đối tượng OOXML | Không suy rộng sang Track Changes, AlternateContent, hyperlink, field, drawing |
| R10-08 | Chưa biết ngưỡng cải thiện width thực sự có ý nghĩa | Hiệu chỉnh từ số liệu lặp lại, không đặt ngưỡng tùy tiện |

## 183. Các bước giao nhận tối thiểu và bằng chứng phải có

**Bộ giao nhận V10** gồm một báo cáo MD tích hợp, một ZIP benchmark riêng với 8 fixture nguồn, 1 ứng viên F08, manifest có SHA-256 và script tạo dữ liệu tổng hợp; kèm hướng dẫn đọc kết quả quan sát được. ZIP chỉ nhằm **tái lập nghiên cứu**, không phải phần mềm xử lý DOCX. `F08_candidate_atleast.docx` là một phép sửa minh họa bằng thư viện đã có, không phải một bước tự động đủ an toàn để áp dụng cho tài liệu bất kỳ.

Khi đưa vào repo thực tế, đầu ra tối thiểu của Executor nên là: phiên bản HEAD và module liên quan đã audit; fixture/case được tái sử dụng; danh mục file/symbol thực sự sửa; command/evidence PASS–FAIL; trạng thái Word render và giới hạn; không commit/push/deploy khi chưa được phê duyệt. Các kết quả này **chưa có trong V10** và không được tự điền như đã hoàn thành.

## 184. Quyết định chuyển giai đoạn và nguyên tắc dừng báo cáo lý thuyết

V10 đã chứng minh được **một vấn đề hiển thị cụ thể trên file tổng hợp và một phương án sửa tối thiểu có hiệu quả trong LibreOffice**, đồng thời xác nhận một trường hợp lặp tiêu đề bảng trên sáu trang. Điều đó mang giá trị mới so với V9 nhưng **không chứng minh** thuật toán tự phân phối độ rộng cột, tính pháp lý của biểu mẫu hay tính tương thích Word trên mọi thiết bị.

Do vậy, **không nên thêm phiên bản nghiên cứu chỉ để tăng số mục, ca thử hoặc nguồn**. Mọi bản bổ sung sau V10 phải có ít nhất một trong các căn cứ: (i) lỗi mới tái hiện bằng file thực tế, (ii) quy định có hiệu lực mới, (iii) hiệu chỉnh ngưỡng bằng benchmark, hoặc (iv) kết quả thử tích hợp thật. Khi chưa có, giữ V10 làm đặc tả tạm khóa và chuyển trọng tâm sang kiểm định đúng mục tiêu sản phẩm.




# PHẦN XXVII. V11 — THỰC NGHIỆM CÓ ĐỐI CHỨNG VỀ PHÂN BỔ ĐỘ RỘNG CỘT THEO NỘI DUNG TRỌNG TÂM

> **Phạm vi đóng góp mới:** V10 chứng minh một trường hợp xử lý chiều cao `Exactly`; V11 kiểm chứng trực tiếp các *phương án phân bổ độ rộng cột* trên **hai bảng DOCX tổng hợp F01 và F02** đã có trong corpus V10. Không bổ sung hàng loạt quy tắc chỉ vì mục tiêu tăng độ dài tài liệu. V11 đưa ra kết quả quan sát được bằng LibreOffice, có đối chứng chế độ dàn bảng, checksum, PDF, ảnh, kịch bản tái lập và cả kết quả **không nên chỉnh sửa**. Đây là thăm dò có kiểm soát, **không phải chứng minh thuật toán tối ưu toàn cục**, nghiệm thu Word hoặc một bộ xử lý production.

## 185. Điều kiện chuyển V10 sang V11: có khoảng trống thực nghiệm cụ thể

Ở V10, việc cột “Nội dung công việc” cần rộng hơn cột “STT” là một đề xuất hợp lý nhưng **chưa có đối chứng kết xuất** cho thay đổi width. V11 trả lời ba câu hỏi thực nghiệm: (1) một phương án phân bố theo tác vụ đọc có cải thiện khả năng đọc và chiều cao bảng không; (2) nới mạnh cột trọng tâm có thể làm xấu những cột khác đến mức nào; (3) khi phương án mới **không cải thiện**, có nên trả lại baseline hay không. Không dùng bộ mẫu tổng hợp để suy diễn là mọi văn bản hành chính/Đảng phải có các tỷ lệ đó.

Tái sử dụng fixture F01/F02 của V10; không tạo corpus song song, không chỉnh sửa kho mã nguồn ứng dụng, không commit, push hoặc triển khai. Công cụ phục vụ phép đo là `python-docx` để đọc, `lxml`/`zipfile` để patch thăm dò cấu trúc OPC, LibreOffice để kết xuất, PyMuPDF để đo đường kẻ và xác minh trích xuất, Pillow để tổng hợp ảnh QA.

## 186. Hợp đồng thực nghiệm, dữ liệu nguồn và biến được phép thay đổi

- **F01 — Bảng phân công nhiệm vụ:** 4 cột, 4 hàng (1 header, 3 dữ liệu), tổng chiều rộng khoảng 165 mm trên A4 dọc. Cột “STT” là mã nhận diện ngắn; “Nội dung công việc” mô tả dài; “Đơn vị thực hiện” trung bình; “Hạn hoàn thành” chứa ngày cần nhận biết nhanh.
- **F02 — Bảng thống kê:** 4 cột, 4 hàng, gồm “Chỉ tiêu”, “Năm 2024”, “Năm 2025”, “Tăng/giảm (%)”. Các giá trị số là dữ liệu căn phải. Mục tiêu là giữ được sự liên kết số liệu và tránh làm dài bảng do header không đủ chỗ.
- **Biến kiểm soát:** Cùng nguồn DOCX, cùng 165 mm tổng chiều rộng, cùng kiểu chữ, lề, số hàng, nội dung, thứ tự ô, đường viền, bản LO và phương pháp trích xuất.
- **Biến tác động:** Danh sách độ rộng theo cột trong các thuộc tính `w:tblGrid/w:gridCol`, `w:tcPr/w:tcW`, tổng bảng `w:tblW`, chế độ `w:tblLayout=fixed` của phương án thử. V11 không sửa chữ, số liệu, căn đoạn, viền hoặc phông.
- **Đối chứng chống nhiễu:** Bổ sung bản `fixed_equal`, đặt đủ bốn cột bằng nhau dưới `fixed` nhưng không đổi tỷ lệ. Ở cả F01 và F02, bản này có cùng chiều cao PDF đo được với bản gốc `auto`/mặc định. Vì vậy, trong **bộ mẫu này**, giảm chiều cao không thể giải thích chỉ bằng việc đổi `tblLayout`.

| Trường | Giá trị thử nghiệm | Tính pháp lý |
|---|---|---|
| Renderer | LibreOffice 25.2.3.2 | Chỉ là môi trường thử; không đại diện Microsoft Word |
| Đầu vào | 2 DOCX tổng hợp từ V10 | Không phải tài liệu thật hay mẫu hành chính chính thức |
| Phương án | 9 lượt kết xuất: 2 baseline, 2 fixed-equal, 5 phân bổ khác | Giá trị mm là minh họa có kiểm thử, không phải định mức của NĐ30/HD05 |
| Diện tích trang | A4 dọc, vùng rộng hữu dụng 165 mm | Kiểm theo geometry *của fixture*, không thay thế đọc từng section tài liệu thực |
| Chứng cứ | DOCX, PDF, PNG, `metrics.json`, SHA-256, script | Có thể kiểm tra và tái lập khi có phần mềm tương ứng |

## 187. Lập phương án: không đồng nhất “quan trọng” với “phải rộng nhất”

Đối với F01, chiều rộng tổng 165 mm được giữ nguyên và thử bốn cấu hình:

| Phương án | STT | Nội dung | Đơn vị | Hạn | Ý định |
|---|---:|---:|---:|---:|---|
| Bản gốc | 41,25 | 41,25 | 41,25 | 41,25 | Chia đều, tạo baseline |
| Cân đối | 14 | 76 | 38 | 37 | Cột nhận diện vừa đủ, nhiều không gian cho mô tả, giữ tên/đơn vị/ngày ở mức đọc được |
| Ưu tiên mạnh | 12 | 87 | 33 | 33 | Xem hiệu quả khi ưu tiên mô tả quá mức |
| Cực đoan | 10 | 105 | 25 | 25 | Kiểm chứng lỗi hồi quy khi thu hẹp quá mức nhiều cột |

Đối với F02: bản gốc 41,25 × 4; bản vừa phải `[60,35,35,35]`; bản nới quá mạnh nhãn `[75,30,30,30]`. Những phương án thử **không phải** đầu ra của mô hình AI hoặc công cụ tự động chọn nghiệm; chúng được lập thủ công để tách tác động. Đặc biệt, giá trị 14 mm cho STT của F01 chỉ đạt với nội dung/phông/renderer hiện tại, không được dùng làm cỡ tối thiểu cố định toàn hệ thống.

## 188. Phương pháp đo và phạm vi suy luận

Bộ đo đọc đường ngang của bảng từ các drawing paths trong PDF bằng PyMuPDF và sử dụng `H = y_last - y_first` (đơn vị điểm PDF); chuyển đổi `mm = pt × 25,4/72`. Cách đo này có hiệu lực cho **các bảng mẫu có đường kẻ đơn rõ ràng**, không thay thế thuật toán đo bảng bất kỳ, nhất là bảng không viền, đường kẻ đứt, bảng lồng hay nhiều trang.

Các tiêu chí được quan sát: số trang, chiều cao bảng, tình trạng xuống dòng của **tiêu đề và ô quan trọng**, sự hiện diện chữ qua PDF, ràng buộc tổng chiều rộng và hình ảnh kết xuất. Kiểm tra “16/16 ô tìm thấy trong PDF” là phép dò chuỗi sau khi bỏ khoảng trắng, có thể cho âm tính giả/dương tính giả nếu thứ tự text PDF bị thay đổi hoặc có nội dung trùng lặp; **không phải bằng chứng tổng quát về không cắt chữ**. Bảo toàn dữ liệu gốc được xác nhận riêng bằng so sánh toàn bộ chuỗi `w:t`, số hàng/ô, cấu trúc `gridSpan`/`vMerge` và diff part OPC. Kiểm tra trực quan đã thực hiện với ảnh của từng phương án thử.

## 189. Kết quả F01: phương án cân đối cải thiện có số đo

| Phương án | Cao bảng (pt) | Cao bảng (mm) | So với gốc | Tiêu đề/khả năng đọc | Quyết định nghiên cứu |
|---|---:|---:|---:|---|---|
| Gốc, AutoFit/mặc định | 205,40 | 72,46 | 0% | Tiêu đề nguyên, cột mô tả rất hẹp, xuống dòng nhiều | Baseline |
| Fixed-equal | 205,40 | 72,46 | 0% | Như bản gốc | Đối chứng, không có lợi ích |
| **Cân đối `[14,76,38,37]`** | **130,70** | **46,11** | **−36,37%** | Bốn nhãn tiêu đề vẫn một dòng; mô tả xuống dòng ít hơn | **Ứng viên tốt nhất trong tập đã thử** |
| Ưu tiên mạnh `[12,87,33,33]` | 145,60 | 51,36 | −29,11% | `STT` bị tách thành hai dòng; các header khác bị ngắt | Loại khi header một dòng là yêu cầu chất lượng |
| Cực đoan `[10,105,25,25]` | 145,60 | 51,36 | −29,11% | `STT`, “Đơn vị thực hiện”, “Hạn hoàn thành” đều xuống dòng | Loại vì hồi quy khả năng đọc |

**Phép tính chính:** `(205,40 − 130,70) / 205,40 × 100 = 36,37%` (làm tròn). Cả năm lượt F01 đều cho PDF 1 trang, 16/16 giá trị ô được phát hiện trong PDF và giữ nguyên tập chữ trong các source DOCX. Ảnh bản cân đối cũng cho thấy bốn header còn nguyên dòng; các bản ưu tiên quá mức khiến header bị chia. **Không suy rộng** kết quả 36,37% sang văn bản khác.

## 190. Kết quả F02: ví dụ NO_OP tốt hơn “làm đẹp”

| Phương án | Cao bảng (pt) | Cao bảng (mm) | So với gốc | Hiện tượng | Quyết định nghiên cứu |
|---|---:|---:|---:|---|---|
| Gốc AutoFit/mặc định | 85,80 | 30,27 | 0% | Header ở một dòng, số liệu căn phải | Giữ làm baseline |
| Fixed-equal | 85,80 | 30,27 | 0% | Không khác biệt có ý nghĩa | Không có lợi ích |
| Vừa phải `[60,35,35,35]` | 85,80 | 30,27 | 0% | Chiều cao không giảm; bố cục chưa chứng minh đẹp hơn | **Giữ nguyên**, tránh thay đổi vô ích |
| Nới nhãn `[75,30,30,30]` | 100,80 | 35,56 | +17,48% | `Tăng/giảm (%)` bị tách dòng | **Từ chối**, gây hồi quy |

Đây là phản ví dụ cần giữ trong bộ regression: dù cột mô tả/nhãn có thể được ưu tiên về mặt ngữ nghĩa, tăng width quá mức có thể làm header số liệu xuống dòng và khiến cả hàng tiêu đề cao hơn; do đó toàn bảng cao hơn. Mô hình không được áp đặt “cột nhiều chữ phải tăng width” nếu không có lợi ích được chứng minh.

## 191. Bằng chứng bảo toàn: thay đổi một OPC part, nhưng nhiều thuộc tính cùng thay đổi

Đối với mỗi bản ứng viên, diff nhị phân từng part cho thấy chỉ `word/document.xml` khác nguồn; toàn bộ part còn lại giữ nguyên bytes ở mức giải nén từng part. Chuỗi `w:t` theo thứ tự, bảng/hàng/ô, topology gộp/tách được đối chiếu bằng parser. **Không được tuyên bố** rằng “chỉ một thuộc tính độ rộng thay đổi”: các bản thử đã thay cả `w:tblLayout` sang fixed, `w:tblW`, `w:tblGrid`, `w:tcW`. Đối chứng fixed-equal hỗ trợ tách tác động của layout mode, nhưng không loại trừ mọi tương tác từ phần mềm kết xuất.

Các tình huống tracked changes, AlternateContent, digital signature, comment, field, drawing, Content Control **không có trong 2 fixture**, nên kết quả bảo toàn này không được dùng để mở khóa sửa những loại DOCX đó. Bản sửa không được coi là bản mẫu thể thức hành chính/Đảng đã hợp lệ. `python-docx` được dùng để đọc fixture; thay đổi thử nghiệm dùng patch cục bộ với `lxml`/`zipfile` trên gói ZIP, không xây dựng lại toàn bộ DOCX qua trình chuyển đổi trung gian.

## 192. Quy tắc cột trọng tâm có thể vận hành sau phép thử

Đề xuất biểu diễn mỗi cột bằng ít nhất năm nhóm thuộc tính độc lập:

| Nhóm | Trường gợi ý | Vai trò |
|---|---|---|
| Ngữ nghĩa | `role`, `reader_task`, `critical_token`, `priority_evidence` | Cho biết cột cần nhận biết thông tin gì và tại sao |
| Độ rộng | `content_min`, `header_min`, `preferred_range`, `max_width` | Ràng buộc cứng/mềm theo text/font/renderer |
| Hình học | `grid_interval`, `spans`, `container_width`, `cell_padding` | Đề phòng xung đột ô gộp, bảng lồng và lề |
| Kết xuất | `header_line_count`, `row_height`, `table_height`, `page_count`, `text_visibility` | Chỉ số quan sát để so ứng viên với baseline |
| Tin cậy | `evidence_level`, `locked`, `uncertainty`, `approved_actions` | Ngăn tự sửa vượt phạm vi được xác minh |

**Hợp đồng quan trọng nhất:** ưu tiên ngữ nghĩa không phải width need; cột “Hạn” ngắn nhưng cần đọc rõ một lần, cột STT phải đủ rộng cho header + giá trị, cột mô tả có thể xuống dòng; không cột nào được cấp width bằng cách làm hỏng header của cột khác. Với đa số bảng thông thường, chỉ nên tự đề xuất khi có nhãn cột tin cậy; khi nhãn là bảng nhiều tầng hoặc ô gộp thì dùng cơ chế đo trên grid vật lý đã đặc tả ở V7, không áp cứng ma trận 4 cột của F01.

## 193. Sàng lọc ứng viên bằng hard gates rồi mới tối ưu thẩm mỹ

Thứ tự bắt buộc ở mức đặc tả, cần kiểm chứng khi triển khai:

1. **G0 — Integrity/authority:** nguồn và kiểu bảng có quyền sửa, không mất byte/ý nghĩa dữ liệu, không làm sai biểu mẫu hoặc phạm vi được phép.
2. **G1 — Feasibility/geometry:** tổng width nằm trong vùng chứa, độ rộng cột tối thiểu đủ cho token bảo vệ, ô gộp và header được giữ.
3. **G2 — Readability:** không làm tăng số dòng header bắt buộc giữ một dòng, không che số liệu quan trọng, không phát sinh overlap.
4. **G3 — Pagination:** không tạo page count mới hoặc đẩy chữ ký/phụ lục sang trang nếu không có chấp thuận.
5. **G4 — Benefit:** chỉ so ưu thế chiều cao/khả năng đọc sau G0–G3; ưu tiên phương án đổi ít nhất trong các phương án hiệu quả tương đương.

`NO_OP_VALID` là một nghiệm chính thức. Bản F02 vừa phải là ví dụ: `Δheight = 0` và chưa có bằng chứng người đọc được lợi hơn, vì vậy chỉnh width sẽ tăng chi phí thay đổi mà không mang lại lợi ích xác minh. F01 ưu tiên mạnh/ cực đoan không được chấp nhận chỉ vì `Δheight < 0` bởi chúng gây xuống dòng tiêu đề. Với bảng không viền không được suy luận số đo chiều cao từ công cụ đo đường kẻ của V11; cần dùng oracle kết xuất thay thế.

## 194. Tìm kiếm nghiệm hữu hạn và ngưỡng cải thiện chưa được hiệu chỉnh

Lộ trình khuyến nghị khi tích hợp vào processor hiện hữu (không phải code thực thi V11):

```text
baseline = read_and_snapshot_existing_table()
if locked_or_unsupported: return KEEP_OR_REVIEW
candidates = [baseline]
for width_vector in bounded_width_grid:
    if not source_geometry_and_header_constraints(width_vector): continue
    proposal = patch_only_approved_properties(width_vector)
    if not integrity_reopen_diff(proposal): continue
    evaluation = render_same_engine_as_baseline(proposal)
    if not hard_gates(evaluation): continue
    candidates.append(evaluation)
return choose_pareto_minimum_change(candidates, calibrated_gain_threshold)
```

Đề xuất giới hạn số lượng ứng viên, kích thước bước thay đổi bằng twip nguyên, ngân sách render và điều kiện dừng sau khi không còn lợi ích đáng kể. Đối với ví dụ F01, chưa có kết quả tối ưu toàn cục hoặc nghiệm ổn định giữa các renderer, nên không được lấy `[14,76,38,37]` làm preset áp dụng trên mọi bảng. Đối với F02, nếu không có bằng chứng cải thiện thực, kết thúc bằng `KEEP_EXISTING` chứ không sinh thêm các ứng viên không cần thiết.

## 195. Hợp đồng chấp nhận của người dùng và kiểm soát hồi quy

Trước khi sửa, UI hoặc pipeline cần thông báo: bảng nào, thuộc `body` hay `appendix`, căn cứ áp dụng, cột được ưu tiên, vì sao ưu tiên, thuộc tính đề xuất đổi, mức bằng chứng và tác động phân trang. Với bảng mang định dạng khuôn mẫu, chữ ký, vùng nhập liệu hoặc nhiều đoạn tài liệu liên kết, chỉ được thay đổi khi mẫu/authority cho phép. Sau thay đổi, tái mở ZIP/DOCX, diff phần ngoài bảng, render so sánh, kiểm tra link/ảnh/số liệu, lưu lý do `ACCEPTED`, `NO_OP_VALID`, `BLOCKED`, `REVIEW_REQUIRED` hoặc `UNVERIFIED`.

**Ma trận nghiệm thu tối thiểu** dành cho phép đo width cần có: F01 thăm dò cải thiện; F02 giữ nguyên; một bảng đã tốt; một bảng có ô gộp; một bảng lồng; một bảng phụ lục; một bảng nhiều trang; một mẫu bảo vệ; một bảng chứa mã dài; một bảng khác phông hoặc renderer; một tài liệu có nhiều section. Tận dụng T01–T152 và F01–F08 hiện có. Không tự sinh ra 152 ca mới hoặc tuyên bố chúng PASS khi chưa chạy.

## 196. Hồ sơ tái lập kết quả V11 và oracle bắt buộc

Gói thực nghiệm `Table_DOCX_V11_Width_Experiment.zip` chứa `source/` (2 DOCX từ corpus V10), `docs/` (9 bản baseline/đối chứng/ứng viên), `pdf/` (9 kết xuất của LibreOffice), `images/` (9 ảnh trang), `metrics.json` (kèm hash, cấu hình mm, kết quả đo), `comparison_sheet.png`, `experiment_width.py`, `make_comparison.py`, `EXPERIMENT_RESULTS.md`.

Các trạng thái kiểm chứng:

| Oracle | Tình trạng V11 | Giới hạn |
|---|---|---|
| OPC part / bảng / chuỗi text | Đã so sánh bằng parser, 7 bản patch chỉ đổi `word/document.xml` | Chưa kiểm DOCX phức tạp có đối tượng đặc biệt |
| PDF LibreOffice | 9/9 DOCX đã kết xuất; PDF 1 trang; 16/16 ô tìm thấy theo phép dò thử nghiệm | Không phải Word và chưa kiểm OCR/hình ảnh trong tài liệu thật |
| Hình học bảng | Đã đo đường kẻ ngang 9/9 bảng; xem ảnh | Chỉ đáng tin trên mẫu có viền phù hợp; không thay thế đo ở Word |
| QA bằng mắt | Đã xem các bản đối chiếu, phát hiện header bị ngắt | Phán đoán thẩm mỹ mang tính ngữ cảnh; chưa có panel người dùng |
| Microsoft Word | **Chưa chạy** | Không thể tuyên bố WORD_RENDER_VERIFIED |
| Tích hợp module | **Chưa chạy** | Không có sản phẩm, PR, commit, deployment hoặc regression app |

## 197. Những giới hạn chưa thể kết luận

- Chỉ có **hai loại bảng đơn giản**; toàn bộ 9 phép render trên dữ liệu tổng hợp trong một môi trường. Không có suy luận thống kê đại diện, độ ổn định giữa các Word version hoặc hiệu quả với tài liệu thật.
- Không có kiểm tra đối với sự thay thế phông chữ, bảng gộp phức tạp, phần footer/chữ ký/phụ lục, section in hai mặt và bảng không viền. Không thể khẳng định một ngưỡng chiều rộng tối thiểu có hiệu lực phổ quát.
- Phép đo chiều cao dựa trên viền PDF; trích xuất văn bản PDF không có quyền thay thế kiểm chứng hiển thị, không thay thế đánh giá manual khi có token/hình/field đặc biệt.
- Bản `fixed_equal` kiểm soát một yếu tố nhiễu nhưng các thuộc tính `tblW/tcW/gridCol` vẫn liên quan nhau trong thuật toán dàn bảng; chưa có thiết kế nhân tố đầy đủ. Không chuyển *correlation* thành tuyên bố nhân quả phổ quát.
- Các giá trị mm và tỷ lệ 36,37%/17,48% là **kết quả trong phép thử này**, không phải mục tiêu KPI chung của hệ thống. Ngưỡng “đáng sửa” phải được hiệu chỉnh trên tập DOCX đại diện và phản hồi người dùng.

## 198. Quyết định chốt V11 và việc nên làm tiếp theo

**Đã có bằng chứng mới đủ điều kiện tạo V11:** trên F01, thay tỷ lệ cột theo vai trò giúp giảm độ cao so với baseline và fixed-equal; trên F02, bố cục vốn hợp lý không nên bị chỉnh nếu không có lợi ích, còn việc phân bổ quá mạnh có thể làm tăng chiều cao. Đây là các ví dụ đo được về **ý nghĩa của nội dung trọng tâm + ràng buộc đọc được + NO_OP_VALID**, lấp đúng khoảng trống mà V10 đã chỉ ra.

**Chưa đủ điều kiện nghiệm thu engine:** cần audit repo/processor hiện tại, reuse API, chạy bộ mẫu trên Microsoft Word tương thích với môi trường người dùng, mở rộng đúng phạm vi lỗi ảnh hưởng. Hành động tiếp theo không phải tạo V12 lý thuyết nếu không có bằng chứng mới, mà là đối chiếu kết quả Word trên F01/F02 và thử mở rộng sang F04/F05, rồi hiệu chỉnh bộ điều kiện quyết định. Không commit/push/deploy/migrate tài liệu hoặc kho mã nguồn theo mặc định.


# PHẦN XXVIII. V12 — KIỂM CHỨNG CHÉO THEO LOẠI BẢNG, TÍNH TRỌN VẸN HÀNG VÀ NGƯỠNG QUYẾT ĐỊNH

## 199. Mục tiêu và những khoảng trống thực sự của V11

Phiên bản V11 đã chứng minh trên dữ liệu tổng hợp F01 (bảng công việc) và F02 (thống kê) rằng tái phân bổ độ rộng có thể giảm chiều cao bảng đáng kể, nhưng phương án nào cũng có thể gây hiệu ứng phụ. V12 **không xây dựng formatter mới**, không tăng số lượng kịch bản T01–T152 chưa chạy. Để thu hẹp khoảng trống kiểm chứng, V12 dùng lại các fixture F03–F07 của V10, cấu trúc patch nhỏ đã thử trong V11, bổ sung phép đánh giá trang, ô gộp, bảng lồng, hàng bị tách và trường hợp không nên sửa.

Các câu hỏi được kiểm: (i) liệu cải thiện F01 có khái quát sang bảng dài/trang ngang; (ii) số trang ít hơn có che lấp lỗi phân trang; (iii) bảng có merged header/nested có thật sự cần chỉnh; (iv) việc chỉ thay các thuộc tính bảng có bảo toàn topology, nội dung và package; (v) lúc nào hệ thống cần từ chối ứng viên có kết quả định lượng tốt nhưng chất lượng đọc kém.

**Nguồn kỹ thuật dùng đối chiếu:** [S44] Repeat Table Header Rows, [S93] giới hạn Open XML SDK, [S95] preferred width và nguồn bổ sung [S98] `cantSplit`. Các ngưỡng và kết quả thực nghiệm không được xem là quy định của NĐ30 hoặc HD05.

## 200. Thiết kế thử nghiệm tái lập và nguồn dữ liệu

- F03: bảng dài 47 hàng (1 tiêu đề + 46 hàng dữ liệu) trong văn bản Đảng **giả lập**, A4 dọc, 3 cột; mục tiêu giữ cột STT đọc được và mở rộng cột mô tả.
- F04: tiêu đề hai tầng và các ô `vMerge`/`gridSpan`; mục tiêu không phá lưới vật lý khi chỉnh chiều rộng.
- F05: bảng lồng nhau và mã hồ sơ dài không thuận tiện ngắt dòng; mục tiêu bảo vệ mã và bảng con.
- F06: biểu mẫu giả lập có vùng ký; quyền mặc định là giữ nguyên mẫu, không tự áp preset thẩm mỹ.
- F07: bảng 8 cột trang A4 ngang; mục tiêu giảm chiều cao do cột diễn giải quá hẹp mà không làm vỡ tiêu đề ngắn.

Đã kết xuất 17 trường hợp gốc/ứng viên chính và một ứng viên giữ hàng ngắn riêng, tổng **18 DOCX/PDF**. Mỗi tệp nguồn tạo mới chỉ có dữ liệu tổng hợp. Thử nghiệm sử dụng **LibreOffice 25.2.3.2 520(Build:2)**, không phải Microsoft Word. Trong bộ chạy chính, patch chỉ vào `word/document.xml`; không tái tạo toàn bộ DOCX, không đổi style chung, không đổi section, không đổi font.

## 201. Thao tác patch tối thiểu phù hợp merged/nested

Tham khảo lại V11 rồi mở rộng phép đo sang lưới vật lý thay vì áp giả định `mỗi ô = một cột`. Với mỗi `w:tr`, xác định `gridBefore`, duyệt đúng các `w:tc` trực tiếp và đọc `w:gridSpan` nếu có. Khi đặt `w:tcW`, dùng **tổng độ rộng các grid column mà ô thật sự chiếm**, không gán kích thước của một cột đơn lẻ cho ô gộp. Bảng con không được tìm nhầm thành bảng ngoài; chỉ xử lý direct-child `w:tblGrid`, `w:tr`, `w:tc`. Các nhánh `w:vMerge`/`w:gridSpan` và cây bảng con phải giữ nguyên.

```text
physical_grid_widths = [w0, w1, ..., wn]
for physical_row in target_table.direct_rows:
    grid_index = row.gridBefore or 0
    for cell in physical_row.direct_cells:
        span = cell.gridSpan or 1
        cell.preferred_width = sum(physical_grid_widths[grid_index:grid_index+span])
        grid_index += span
    assert grid_index <= number_of_grid_columns
```

Đây là pseudocode kiểm chứng fixture, không phải một thuật toán an toàn đối với mọi DOCX: cần xử lý đầy đủ bảng nổi, `gridAfter`, width kế thừa, nội dung có thể thay thế theo phiên bản Word và các trường hợp tương thích trước khi áp dụng trong phần mềm.

## 202. Bảng dài F03: tác động theo số trang và giới hạn chỉ số giảm trang

| Ứng viên | Độ rộng (mm) | Số trang LO | Quan sát | Phân xử |
|---|---|---:|---|---|
| Gốc | 55–55–55 | 6 | Cột nội dung hẹp, bảng dài; hàng có thể chia trang | Baseline |
| Fixed Equal | 55–55–55 | 6 | Đối chứng: chỉ đổi layout không mang lại kết quả | Không chọn |
| Balanced | 16–102–47 | 4 | Giảm 2 trang (33.33%) nhưng còn hiện tượng chia hàng | **REVIEW** |
| Aggressive | 12–125–28 | 3 | Số trang ít hơn nhưng tiêu đề STT bị tách `ST`/`T` | **REJECT** |

Đặc biệt, bảng chỉ còn 3 trang **không tốt hơn** một cách tuyệt đối nếu đánh đổi khả năng đọc ở tiêu đề và cột tình trạng. Cần thực hiện `header_single_line` và `pagination_integrity` trước khi xét tiếp các metric số trang.

## 203. Kiểm chứng kết hợp độ rộng và phân trang hàng ngắn F03

Trên ứng viên Balanced 16–102–47 mm, thêm `w:cantSplit` vào 46 hàng dữ liệu **vì đã biết trước mỗi hàng trong fixture có thể nằm gọn một trang**. Kết quả LO: vẫn **4 trang**; hàng tiêu đề lặp trên **4/4 trang**; có **46/46 mã dòng dữ liệu** và **142/142 chuỗi `w:t`** xuất hiện trong văn bản PDF khi chuẩn hóa khoảng trắng để tìm. Quan sát đầu/cuối trang cho thấy các trang bắt đầu bằng bản ghi 1, 13, 25 và 37, không còn phần nối của hàng ngay sau tiêu đề.

- Bằng chứng này đủ để đánh giá **kết quả LO trên fixture F03**, không suy rộng thành Word-PASS.
- `cantSplit` không có nghĩa hàng dài hơn chiều cao một trang bị giữ nguyên bất kể nội dung: tiêu chuẩn OOXML cho phép hàng phải trải trang nếu thực tế không vừa. [S98].
- Không áp dụng `cantSplit` hàng loạt trong văn bản chưa đo chiều cao hàng; có thể khiến bố cục xấu hơn hoặc gây trang có khoảng trống lớn.
- Candidate kết hợp phải được xét riêng, không gộp việc thay width với ngắt hàng thành một hành động format-only không có quyền phê duyệt.

## 204. F04: bảo toàn tiêu đề hai tầng và ô gộp

| Phương án | Chiều cao quan sát | PDF chứa đủ text gốc | Topology |
|---|---:|---|---|
| Baseline 33×5 mm | 68,12 mm | 42/42 đoạn `w:t` | Gốc |
| Balanced 17–44–29–29–46 mm | 68,12 mm | 42/42 | Không đổi `gridSpan/vMerge` |
| Notes Focus 12–33–23–23–74 mm | 68,12 mm | 42/42 | Giữ XML nhưng cột STT thiếu không gian |

Kết luận: **không chọn chỉnh width chỉ vì tìm được phương án khác**. Với các cột tiêu đề gộp và bảng ngắn, lợi ích bằng 0 hoặc không đáng kể. Cho phép người duyệt chọn theo mục tiêu thị giác khi có yêu cầu, nhưng mặc định `NO_OP_VALID` nếu bảng gốc không lỗi.

## 205. F05: mã dài và bảng lồng — không tự thu cột mang token quan trọng

F05 có 2 cột ngoài và một bảng con nằm trong ô mô tả. Baseline cao **41,03 mm**. Hai cách tăng cột mã lên 102 mm hoặc tăng cột mô tả lên 100 mm không chứng minh được giảm chiều cao so với gốc; ở trường hợp ưu tiên mô tả, số dòng trích xuất còn tăng từ 11 lên 12. Tất cả ứng viên giữ cấu trúc bảng con và 9/9 đoạn `w:t` được trích xuất trong PDF.

Như vậy, không được mặc định cột có chuỗi dài là cột luôn cần cấp thêm width. Trước khi đổi width phải xét độ dài không thể ngắt, kích thước bảng con và khả năng hiển thị của cả hai vùng.

## 206. F06: bảo vệ biểu mẫu là một quyết định tối ưu hợp lệ

Bảng biểu mẫu tổng hợp F06 chứa hàng ký xác nhận; không có quy định nguồn cho phép tự thay đổi bố cục. **Không tạo ứng viên chỉnh chiều rộng.** Kiểm tra baseline mở/kết xuất được, nhưng không có kết luận rằng mẫu là biểu mẫu hành chính hoặc Đảng chính thức. Thao tác hợp lệ trong bộ thí nghiệm là `PRESERVE / NO_OP`, không coi đây là thất bại của thuật toán.

## 207. F07: bảng A4 ngang nhiều cột và ngưỡng tối thiểu cho tiêu đề

| Phương án | Độ rộng 8 cột (mm) | Chiều cao PDF (mm) | Nhận xét |
|---|---|---:|---|
| Gốc | 31,5 mm × 8 | 98.14 | Nội dung mô tả bị xuống nhiều dòng |
| Fixed Equal | 31,5 mm × 8 | 98.14 | Không cải thiện |
| Balanced | 15–25–45–71–20–20–20–36 | **45.40** | Giảm **53.74%**, giữ STT nguyên dòng |
| Description Focus | 12–21–37–95–18–18–18–33 | 50,69 | Tiêu đề STT bị tách thành ST/T → REJECT |

Cần đánh giá đồng thời 3 cấp: (i) độ rộng vừa đủ cho nhãn ngắn và năm; (ii) cột thông tin trọng tâm đủ không gian để hạn chế xuống dòng; (iii) không để cột phụ trợ bị bóp nhỏ quá mức. Ứng viên Balanced đạt kết quả tốt trên LO, nhưng **chưa chứng minh tính tối ưu toàn cục**: chỉ so sánh các ứng viên đã thử, chưa tìm toàn bộ miền nghiệm.

## 208. Chốt ma trận quyết định sau thí nghiệm

| Điều kiện | Quyết định | Căn cứ |
|---|---|---|
| Không cải thiện chất lượng đọc / số trang | `NO_OP_VALID` | F04, F05 |
| Mẫu có bố cục cố định, không có phép sửa được cấp quyền | `PRESERVE` | F06 |
| Ít trang hơn nhưng tiêu đề chính bị vỡ | `REJECT` | F03 Aggressive, F07 Description Focus |
| Giảm chiều cao và tiêu đề đọc tốt | `PROVISIONAL_CANDIDATE` | F07 Balanced |
| Giảm trang nhưng còn hàng bị tách gây khó đọc | `REVIEW_PAGINATION` | F03 Balanced |
| Cải thiện width + giữ hàng ngắn; không đổi trang | `PROVISIONAL_CANDIDATE` | F03 Balanced + `cantSplit` |
| Không có renderer đích Microsoft Word | `WORD_UNVERIFIED` | Tất cả các phương án |

Cần áp dụng **lexicographic gates** trước weighted-score: tính toàn vẹn tài liệu và pháp lý → rủi ro mẫu và quyền thay đổi → khả năng đọc tối thiểu → không tràn/cắt và phân trang → lợi ích đo được → thẩm mỹ và hạn chế độ lớn thay đổi. Điều kiện pháp lý không được hòa trộn thành điểm cộng bù trừ.

## 209. Sửa hạn chế của phép kiểm PDF text coverage

Ở một số bản F03, phương pháp tìm toàn bộ chuỗi `w:t` trong PDF sau khi xóa khoảng trắng đánh dấu thiếu một vài chuỗi, dù đủ mã bản ghi 1–46 và không quan sát mất dữ liệu: nguyên nhân khả dĩ là đoạn PDF trích xuất lẫn thứ tự cột hoặc bị chia phần. Không được từ “substring không tìm thấy” suy luận mất nội dung trên trang; cũng không được từ “mã dòng tìm đủ” suy ra **mọi ký tự khác** đều hiển thị chính xác.

Tài liệu cần báo cáo đồng thời: **(a)** signature `w:t` trước–sau, **(b)** topology + changed OPC parts, **(c)** PDF text coverage có phương pháp rõ, **(d)** render trực quan trang đầu/trang cuối và các vị trí nghi ngờ, **(e)** trạng thái chưa kiểm Word. Trường hợp F03 Balanced + giữ hàng ngắn đã đạt 142/142 `w:t` ở phép tìm PDF này, nhưng kết quả vẫn chỉ thuộc LO.

## 210. Kiểm chứng ngắt trang: từ số trang đến tính toàn vẹn bản ghi

Không dùng duy nhất `page_count`. Bộ chỉ số tối thiểu khi bảng nhiều trang:

```text
pages_count
repeat_header_pages / table_pages
record_id_coverage
row_split_detected
broken_short_header_labels
footer_signature_appendix_overlap
cell_text_xml_signature_preserved
image_or_field_integrity (when present)
```

Cần phát hiện dòng dữ liệu chỉ còn phần đuôi ở đầu trang mới. Với bảng lớn, người đọc cần biết ngay mỗi bản ghi thuộc số thứ tự/đơn vị nào. Nếu các hàng ngắn hoàn toàn có thể giữ trên một trang thì `cantSplit` có thể phù hợp, nhưng với hàng thật dài không ép giữ tuyệt đối. Microsoft Support chỉ xác nhận lặp tiêu đề trên các trang mới do ngắt trang tự động; không nên thay ngắt trang bằng `pageBreak` thủ công rồi kỳ vọng lặp tiêu đề. [S44], [S98].

## 211. Tái sử dụng trước khi tích hợp; phạm vi thay đổi nhỏ

Các phép thử đã tái sử dụng `python-docx` để đọc xác minh, `lxml` để patch chính xác một part, ZIP package API để giữ toàn bộ part khác, PyMuPDF để quan sát text/đường kẻ, LibreOffice để tạo PDF. **Không đưa các công cụ này thành dependency bắt buộc mới cho dự án** khi chưa audit engine DOCX đã dùng: mỗi tool có vai trò benchmark độc lập. Mọi tích hợp tương lai phải kiểm toán module, API, schema, fixtures và contract hiện có, bảo toàn các phần đã PASS; dùng một authority cho bảng và một pipeline xuất tài liệu.

Bộ thử nghiệm riêng gồm script tái lập, `metrics.json`, các DOCX/PDF thử, hình đối chiếu, `QA_RESULTS_V12.md`, manifest hash. Không sửa trực tiếp repo, không thêm service/queue/DB, không đòi đổi kiến trúc Core đã khóa.

## 212. Tiêu chí chốt V12 và phạm vi bằng chứng

**Đã thực hiện trên fixture tổng hợp:** patch và so sánh topology/chuỗi văn bản; 18 trường hợp DOCX/PDF kết xuất LO; F03 6→4 trang, F07 giảm khoảng 53,7% chiều cao; các đối chứng không thay đổi; thử 46 hàng `cantSplit` trên bảng nhiều trang và kiểm chứng còn 4 trang. **Chưa thực hiện:** Word Print Layout trên máy/phiên bản đích; hiệu chỉnh ngưỡng bằng tài liệu thật có phép sử dụng; kiểm PDF tagging/accessibility chuyên sâu; chạy 152 tình huống đặc tả; triển khai engine sản phẩm.

Quyết định: **V12 đạt mức nghiên cứu thực nghiệm trong môi trường LO tổng hợp; chưa đủ mức nghiệm thu triển khai.** Không tạo phiên bản V13 chỉ nhằm mở rộng số chương nếu chưa có một lỗi, mẫu, điều kiện pháp lý hoặc thí nghiệm mới có giá trị. Bước tới cần kiểm Microsoft Word và sau đó pilot rất hẹp trên đúng bộ xử lý DOCX hiện có.

---

# PHẦN XXIX. V13 — KIỂM ĐỊNH ĐỘ BỀN CỦA PHƯƠNG ÁN ĐỘ RỘNG CỘT VÀ CỔNG HÌNH HỌC TRƯỚC KHI ÁP DỤNG

> **Phạm vi bằng chứng V13:** 12 phép kết xuất DOCX→PDF cho hai nhóm F03, F07 dưới ba cấu hình cỡ chữ (gốc, +1 pt, +2 pt); thêm 2 phép thử lề F07 (mỗi lề trái/phải tăng 5 mm). Tất cả dữ liệu là mẫu giả lập, sử dụng LibreOffice trên cùng một môi trường. V13 **không** chứng minh tương thích Microsoft Word, không chạy lại 152 ca T01–T152 và không thay đổi mã nguồn ứng dụng.

## 213. Câu hỏi cần xác minh và giả thuyết

V12 cho thấy một số ứng viên chia cột cân đối tốt hơn bản gốc tại một kích thước chữ. V13 khảo sát **độ bền của nhận định đó** khi điều kiện đầu vào thay đổi: (1) có còn ít trang hơn/ít chiều cao hơn không; (2) hàng tiêu đề, mã bản ghi và nội dung có còn đọc được không; (3) có giữ được hợp đồng bảo toàn DOCX; (4) khi lề thay đổi hợp lệ nhưng cột giữ nguyên thì có vi phạm vùng in không. 

Giả thuyết nghiên cứu không phải "ứng viên sẽ luôn tốt hơn" mà là **các quyết định chỉ có hiệu lực theo envelope hình học và typography đã được kiểm tra**, mọi thay đổi làm vượt envelope phải kích hoạt phép tính lại hoặc yêu cầu xem xét. Không lấy một bảng giả lập để hiệu chỉnh ngưỡng chung cho tất cả văn bản.

## 214. Corpus nguồn, tái sử dụng và kiểm soát biến

- Nguồn: nguyên bản F03 và F07 cùng các ứng viên V12 `F03_balanced_shortrows_keep` (cột 16–102–47 mm, khóa ngắt hàng có điều kiện) và `F07_balanced` (cột 15–25–45–71–20–20–20–36 mm). Không sửa nội dung hay tạo corpus mới độc lập.
- Mỗi nguồn tạo ba bản: `original` (không thay đổi); `plus1pt` (chỉ tăng `w:sz` trong định nghĩa Normal ở `word/styles.xml` thêm 2 half-points); `plus2pt` (tăng thêm 4 half-points). Font, văn bản, section, bảng, độ rộng cột và hàng không thay đổi.
- Cỡ chữ: F03 14→15→16 pt và F07 13→14→15 pt. Mức F03 16 pt **chỉ là stress test ngoài cỡ chữ nội dung chung 14–15 pt được nêu ở Hướng dẫn 05**, tuyệt đối không mặc nhiên là preset hợp pháp cho văn bản Đảng.
- Mỗi phép đổi cỡ chữ tạo DOCX mới từ nguồn ban đầu, không cộng dồn thay đổi; các thay đổi của bản `plus1pt/plus2pt` giới hạn trong `word/styles.xml` (ngoại lệ metadata lưu ZIP không tính là thay đổi nội dung part).
- Phép thử lề F07 dùng **hai file tách biệt**: từ baseline và balanced, tăng lề trái +5 mm, phải +5 mm trong `word/document.xml`, không đổi độ rộng bảng và dữ liệu. Đây là kiểm tra tính thích ứng với cấu hình lề, không phải yêu cầu phải thay đổi lề của tài liệu thật.

Cần ghi rõ rằng LibreOffice có thể thay thế Times New Roman bằng phông phù hợp trong môi trường thử; cùng các bản DOCX có thể hiển thị khác khi mở bằng Word, trên hệ thống font/printer khác.

## 215. Kết quả thực đo: F03 — bảng dài 47 hàng

| Cấu hình Normal | Bản gốc | Balanced + giữ hàng ngắn | Cải thiện số trang | Kết quả bổ sung |
|---|---:|---:|---:|---|
| 14 pt (gốc) | 6 trang | 4 trang | Giảm 2 trang (33,33%) | 46/46 tiền tố bản ghi có mặt trong PDF ứng viên |
| 15 pt (+1 pt) | 7 trang | 4 trang | Giảm 3 trang (42,86%) | 46/46 tiền tố; 4/4 trang tìm thấy tiêu đề |
| 16 pt (+2 pt, stress-only) | 7 trang | 5 trang | Giảm 2 trang (28,57%) | 46/46 tiền tố ở ứng viên; 5/5 trang tìm thấy tiêu đề |

Phép đo PDF phát hiện số trang trên cùng một renderer không thay đổi giữa F03 ứng viên 14 và 15 pt, nhưng tăng từ 4 lên 5 trang tại 16 pt. Do vậy **không được coi số trang cố định là một bất biến**; phải tính lại khi đổi cỡ chữ. So với baseline từng cấu hình, ứng viên vẫn có lợi ích, nhưng không đủ để suy ra sẽ luôn có lợi ích tương tự trên văn bản Đảng thật.

## 216. Phát hiện quan trọng: chuỗi dữ liệu bị ngắt tại ranh giới trang

Ở F03 baseline 16 pt, chuỗi `Nội dung giả lập số 21:` bị ngắt: cuối trang 3 hiển thị `Nội dung giả lập số`, đầu trang 4 bắt đầu bằng `21:`. Phép kiểm chuỗi nối liền từng trang chỉ nhận được 45/46 tiền tố và báo thiếu **giả**. Trong `word/document.xml`, tất cả dữ liệu vẫn còn; kiểm tra hàng và dấu trang mới thấy nguyên nhân là phân trang.

Quy tắc V13:

1. O1 (integrity): so sánh nội dung/ô/quan hệ OOXML trước-sau là điều kiện bắt buộc, độc lập với text extraction từ PDF.
2. O3 (render): phát hiện hàng bị chia, tiêu đề bị đứt hoặc số liệu khó liên hệ phải dựa trên tọa độ, trang và phân đoạn đọc, **không dùng `substring not found` đơn độc để tuyên bố mất nội dung**.
3. Khi hàng đủ thấp và không phải biểu mẫu bị khóa, có thể **đề xuất** `cantSplit` có điều kiện; hàng dài hơn một trang cần cho phép ngắt. `cantSplit` không được bật đại trà chỉ vì có split ở một test.
4. Nếu PDF extraction không chứng minh được tính đầy đủ, kết quả phải là `REVIEW_RENDER` hoặc `UNVERIFIED_TEXT_EXTRACTION`, không tự gắn `DATA_LOST`.

## 217. Kết quả thực đo: F07 — bảng ngang tám cột

| Cỡ chữ Normal | Baseline, tổng chiều cao bảng | Balanced, tổng chiều cao bảng | Giảm chiều cao | Số trang (cả hai) |
|---|---:|---:|---:|---:|
| 13 pt | 98,14 mm | 45,40 mm | 53,74% | 1 |
| 14 pt | 104,63 mm | 47,84 mm | 54,28% | 1 |
| 15 pt (stress) | 111,12 mm | 50,27 mm | 54,76% | 1 |

Chiều cao được tính từ các đường kẻ ngang đại diện bảng trong PDF của fixture kẻ lưới, **không phải thước đo tổng quát cho bảng không có viền**. Có thể nói phương án V12 bền vững trong ba phép thử cỡ chữ này đối với F07 tổng hợp, nhưng không thể mở rộng kết luận sang các font khác, bảng nhiều trang, bảng nổi hoặc Word khi chưa có kiểm chứng tương ứng.

## 218. Cổng hình học: width gần chạm lề và không có dư địa

Các bảng đang được dùng trong thí nghiệm có tổng độ rộng lưới sát với bề ngang vùng soạn thảo:

| Bảng | Trang | Rộng vùng nội dung theo section | Tổng grid width | Dư địa |
|---|---|---:|---:|---:|
| F03 Balanced | A4 dọc | ≈165,01 mm | ≈164,99 mm | ≈0,02 mm |
| F07 Balanced | A4 ngang | ≈252,01 mm | ≈252,01 mm | ≈0,00 mm |

Sai khác vài phần trăm mm có thể do lượng tử hóa sang twips, không được tự coi là lỗi tràn nghiêm trọng. Nhưng khoảng dư địa về bản chất gần bằng 0, nghĩa là mọi thay đổi `section`, lề, indentation hoặc container cần tính lại tính khả thi. Theo Microsoft Learn, `tblW`/`tcW` là **preferred widths**, không bảo đảm kích thước kết xuất luôn khớp khai báo; không được nhầm yêu cầu hình học với kết quả Word đã xác nhận ([S62], [S95]).

## 219. Phép thử lề F07: một cấu hình đầu vào hợp lệ có thể làm phương án không còn khả thi

Đối chứng độc lập: giữ tổng lưới khoảng 252 mm; tăng lề trái từ 30 lên 35 mm, phải từ 15 lên 20 mm trên trang A4 ngang. Bề rộng còn lại từ khoảng 252 xuống 242 mm; **bảng yêu cầu nhiều hơn vùng nội dung khoảng 10 mm**. Trên PDF thử nghiệm của LibreOffice, đường biên bảng nằm ngoài giới hạn lề phải mới khoảng **8,2 mm** ở trang đầu.

Đây là minh họa rằng cấu hình lề và hướng trang là **đầu vào của quyết định width**, không phải hậu xử lý. Lề 35/20 mm có thể nằm trong dải lề được cho phép của Nghị định 30 với văn bản hành chính phù hợp, nhưng không được tự chuyển lề khi văn bản có cấu hình mẫu khác, và không suy ra toàn bộ điều kiện pháp lý chỉ từ một cặp thông số lề.

Phân xử chuẩn: nếu `ΣminWidths > availableWidth` thì không có phương án chỉ đổi độ rộng là hợp lệ, cần `REVIEW_REQUIRED`; nếu `ΣpreferredWidths > availableWidth` nhưng `ΣminWidths ≤ availableWidth` thì sinh lại các ứng viên **trong giới hạn mới**, không dùng lại bảng width đã tối ưu cho section cũ; tuyệt đối không âm thầm đổi lề hoặc xoay trang.

## 220. Đo lường và ảnh hưởng của font: nêu đúng mức chắc chắn

Các phép tăng cỡ chữ thông qua style mặc định có ích như một **stress test đơn biến**, không phải mô phỏng đầy đủ việc người dùng chuyển theme, thay font, thay máy in hoặc phần mềm Word. Thước đo PDF gồm số trang, đoạn chữ có mặt, chiều cao đường viền, sự xuất hiện của header trên mỗi trang và tính liên tục mã bản ghi. Thước đo OOXML gồm số hàng/cột/bảng, thứ tự `w:t`, ô gộp, tên các ZIP parts thay đổi và SHA-256.

Trong 12 phép font stress, `word/document.xml` và fingerprint bảng giữ nguyên tuyệt đối; với `plus1pt/plus2pt` chỉ `word/styles.xml` thay đổi. Toàn bộ 12 file có PDF xuất thành công và được đo; cần đọc các trường `pdf_coverage_run_count` là **heuristic có thể thiếu giả** khi chuỗi đi qua ranh giới dòng/trang, không phải bằng chứng về dữ liệu đã bị xóa.

## 221. Chính sách quyết định tối ưu cần bổ sung: kiểm tra tính bền có giới hạn

Đề xuất chính sách P13 không buộc mọi bảng chạy mọi kịch bản stress. Trong chế độ bình thường, kiểm một renderer ở cấu hình gốc và thực thi các hard gate. Chỉ đối với bảng có nguy cơ cao (width sát lề, cỡ chữ có thể thay đổi, tài liệu dùng nhiều style, header dài, bảng kéo dài nhiều trang), chạy **một số perturbation có chọn lọc** trên bản sao không làm thay đổi tài liệu gốc.

Một phương án đủ điều kiện `APPLY_CANDIDATE` khi:

- Có quyền chỉnh và không bị khóa bởi biểu mẫu/chữ ký/Track Changes/nguồn quy tắc.
- Có kích thước hợp lệ theo trang, story, section và lề hiện hành, kể cả twips và sai số được quy định minh bạch.
- Toàn bộ dữ liệu/cấu trúc trong phạm vi sửa được bảo toàn, kèm package diff.
- Không phát hiện cắt chữ/tràn/in không đọc được trong môi trường kết xuất đích; tiêu đề và bản ghi có thể đối chiếu.
- Có lợi ích so với baseline ở **cấu hình thực tế của người dùng**, vượt ngưỡng được định nghĩa theo benchmark (không rút từ chỉ F03/F07).
- Người dùng đã duyệt đúng loại tác động, bao gồm thay đổi width, phân trang hoặc `cantSplit` nếu có.

Nếu thiếu renderer mục tiêu, phân loại `LAYOUT_ESTIMATE_ONLY`, không tuyên bố `WORD_PRINT_PASS`. Nếu chỉ khi tăng cỡ chữ cực đoan mới hỏng, ghi rõ `ROBUSTNESS_LIMIT`, không tự bác bỏ tài liệu ở profile đã khóa nhưng phải cảnh báo khi người dùng thay đổi profile.

## 222. Mô hình tối ưu theo phương án, không theo một con số tổng hợp

Dùng sàng lọc từng lớp: `LEGAL/MODEL LOCK → GEOMETRY → INTEGRITY → READABILITY/PAGINATION → MINIMAL DELTA → BENEFIT`. Chỉ sau khi qua tất cả cổng mới cân nhắc xếp hạng thẩm mỹ. Chỉ số chính không chỉ có trang/chiều cao: còn phải đo `unbroken_key_fields`, `header_readability`, `split_short_rows`, `table_overflow`, `page_transition_cost` và sai biệt so với mẫu chính thức.

Nếu baseline tốt, `NO_OP_VALID` có thể là lựa chọn tốt nhất. Nếu bảng tràn do lề nhưng được khóa theo mẫu, `PRESERVE/REVIEW`, không tự phá biểu mẫu. Nếu thay đổi phông chữ vượt profile pháp lý, đó là **ca chịu tải** để hiểu nguy cơ, không được đưa vào đầu ra chuẩn hóa mặc định.

## 223. Cấu trúc bằng chứng tối thiểu cho một quyết định width

```yaml
case_id: F07_balanced__plus1pt
source_profile: synthetic_v12
scenario: font_normal_plus_1pt
renderer: LibreOffice_25.2.3.2
legal_authority: not_certified_fixture
geometry:
  source_section_width_mm: 297
  source_content_width_mm: 252.01
  table_grid_width_mm: 252.01
  minimum_clearance_mm: approximately_zero
integrity:
  source_text_topology_equal: true
  altered_part_against_v12_candidate: word/styles.xml
render:
  pages_baseline: 1
  pages_candidate: 1
  table_height_baseline_mm: 104.63
  table_height_candidate_mm: 47.84
  microsoft_word_verified: false
decision: RESEARCH_CANDIDATE_ONLY
```

Bất cứ ứng viên nào thiếu dữ liệu `renderer` hoặc `source_profile` phải mang nhãn `UNVERIFIED` thay vì ghi mặc định `PASS`. Hash/manifest đi kèm gói thực nghiệm V13 là đầu mối tái lập, không thay cho chứng cứ Word.

## 224. Bộ nghiệm thu tiếp theo: chỉ mở phạm vi khi có bằng chứng

- **Tại Word đích:** render Print Layout chính cùng Office build/OS/font/printer, đối chiếu số trang, vị trí trang, độ cao, ngắt hàng và vùng in; tạo ảnh từng trang trước/sau và kiểm vị trí chữ ký/phụ lục gần bảng.
- **Tại parser/processor đang có:** audit mã nguồn và phần nhận diện bảng hiện tại, dùng các fixture V10–V13 làm regression có giới hạn; chỉ patch đúng thuộc tính được phép, không viết parser hoặc engine dàn bảng mới.
- **Đối với tài liệu thực tế:** sử dụng mẫu ẩn danh, có quyền kiểm tra; lưu hash và bản gốc ở kênh riêng theo chính sách hệ thống, không đưa tài liệu cơ quan hoặc văn bản đã ký số vào corpus công khai.
- **Quy tắc nghiệm thu:** bắt buộc O1/O2 bảo toàn; O3 Word Print Layout khi sản phẩm tuyên bố khớp bản in Word; O4 người duyệt nếu thay đổi trình bày có tính chủ quan. Kiểm tra phạm vi ảnh hưởng, không tự chạy lại toàn hệ thống.

## 225. Kết luận và các khoảng trống còn lại của V13

Đã quan sát rằng F03/F07 **giữ lợi ích trên renderer LibreOffice khi thay đổi cỡ chữ trong các cấu hình đã thử**, đồng thời nhận diện được trường hợp đánh giá PDF thiếu giả vì dữ liệu bị tách qua trang và trường hợp đổi lề khiến cả phương án width cũ vượt vùng nội dung. Đây là bằng chứng đủ để thêm **cổng kiểm tra lại hình học và giới hạn typography**, nhưng chưa đủ để chọn một thuật toán tối ưu duy nhất hoặc chứng nhận `Microsoft Word PASS`.

**Phần tiếp theo cần bằng chứng mới chứ không chỉ thêm mục:** thử ít nhất một bộ DOCX người dùng đã cho phép trên Microsoft Word cùng build mục tiêu, hoặc tích hợp thử nghiệm có kiểm toán vào một bộ xử lý hiện có; khi chưa có, giữ V13 làm baseline nghiên cứu, không tiếp tục đổi threshold chỉ theo cảm nhận.

---

# PHẦN XXX. V14 — TÁI PHÂN BỔ ĐỘ RỘNG CỘT KHI THAY ĐỔI HÌNH HỌC TRANG: KIỂM CHỨNG CÓ ĐỐI CHỨNG

> **Phạm vi V14:** Nghiên cứu thực nghiệm trên đúng một bảng DOCX tổng hợp F07 đã được dùng trong V12–V13. Gồm 5 cách xử lý (1 đối chứng không sửa, 4 phương án thu hẹp) × 2 cấu hình cỡ chữ (gốc và +1 pt), tổng **10 lần kết xuất DOCX→PDF bằng LibreOffice**. Đây là 10 lượt quan sát nghiên cứu mới, **không** phải kết quả chạy bộ 152 kịch bản T01–T152 và **không phải kiểm định Microsoft Word**. Những số đo chỉ được sử dụng trong phạm vi môi trường/fixture nêu rõ bên dưới.

## 226. Câu hỏi còn bỏ ngỏ từ V13

V13 tái hiện một trường hợp rõ ràng: trên A4 ngang, lề trái/phải tăng từ xấp xỉ 30/15 mm lên 35/20 mm; lưới bảng khoảng 252 mm nhưng chiều rộng hữu dụng chỉ còn khoảng 242 mm. V13 dừng ở bước **phát hiện không phù hợp**; chưa thực nghiệm lựa chọn cách phân bổ lại chiều rộng cho vùng chứa đã thay đổi. V14 trả lời ba câu hỏi nhỏ, có thể đo: (a) có thể đưa lưới về giới hạn mới mà giữ nội dung không; (b) cách thu hẹp có gây tăng chiều cao bảng/ngắt tiêu đề không; (c) nếu nhiều ứng viên bằng nhau về hiển thị, có thể phân xử bằng mức xáo trộn và bảo vệ trường trọng tâm không.

Không giả định cột dài nhất là cột quan trọng nhất. Ở F07, `STT`, `Mã`, `Đơn vị`, ba cột năm `2023–2025`, `Nội dung` và `Ghi chú` có nhu cầu bảo toàn khác nhau. Tầm quan trọng nghiệp vụ của các trường này **chỉ là cấu hình giả định của fixture**, không phải quyết định AI có thể suy ra chắc chắn trên một văn bản thật.

## 227. Hình học đầu vào và khóa pháp lý

| Chỉ số kiểm | Giá trị thăm dò | Cách tính / phạm vi |
|---|---:|---|
| Rộng trang | 297 mm | A4 ngang trong section của fixture |
| Lề trái sau stress | xấp xỉ 35 mm | Section margin trên **bản sao** |
| Lề phải sau stress | xấp xỉ 20 mm | Section margin trên **bản sao** |
| Chiều rộng phần thân | **242,023 mm** | Đọc `w:pgSz` − `w:pgMar.left` − `w:pgMar.right`, theo integer twips |
| Tổng lưới ban đầu | **252,007 mm** | Tổng 8 `w:gridCol/@w:w` |
| Mức không phù hợp | **9,984 mm** | 252,007 − 242,023 mm |
| Số bảng/hàng/ô | 1 / 6 / 48 | Một hàng tiêu đề và năm hàng dữ liệu |

Các phép tính được lượng tử hóa theo đơn vị twip (`1 twip = 25,4/1440 mm`). Các con số mm chỉ là **chứng cứ hình học từ DOCX nguồn**, không đồng nghĩa mép viền in và mép chữ luôn trùng với lề section. Nếu bảng có `tblInd`, `tblpPr`, cell margin, căn giữa, ô gộp hoặc bảng lồng, phải đánh giá thêm đúng phạm vi chứa; **không dùng công thức trên như một bộ dựng trang Word hoàn chỉnh**.

Không tự điều chỉnh lề chỉ để bảng vừa: lề do authority văn bản/mẫu và người dùng xác lập. V14 chỉ thử phương án đổi width trong phạm vi bảng trên tài liệu **giả lập**.

## 228. Năm ứng viên, một baseline và chính sách thay đổi tối thiểu

Mỗi phương án tạo **một DOCX độc lập từ cùng source** `F07_balanced__margin_plus5mm.docx`. Không nối tiếp các phép thu hẹp, không sửa bản gốc. Các giá trị bên dưới là tham số đầu vào dự định tính bằng mm; phần mềm lưu số nguyên twips nên tổng thực đo sau lượng tử hóa có sai số nhỏ.

| Ứng viên | STT | Mã | Đơn vị | Nội dung | 2023 | 2024 | 2025 | Ghi chú | Tổng đề xuất |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| N0 — giữ nguyên, đối chứng **không đạt hình học** | 15 | 25 | 45 | 71 | 20 | 20 | 20 | 36 | 252 |
| N1 — thu tỷ lệ các cột | 14,4 | 24 | 43,2 | 68,2 | 19,2 | 19,2 | 19,2 | 34,6 | 242 |
| N2 — bảo vệ STT/Mã/số liệu năm | 15 | 25 | 43 | 66 | 20 | 20 | 20 | 33 | 242 |
| N3 — bảo vệ rộng cột Nội dung | 15 | 25 | 42 | 70 | 18 | 18 | 18 | 36 | 242 |
| N4 — phân bổ có dư địa 2 mm | 15 | 25 | 42 | 65 | 20 | 20 | 20 | 33 | 240 |

N2 và N4 chỉ đổi **3 trong 8 cột**; N1 đổi tất cả 8 cột; N3 thay đổi 5 cột. N2 thay đổi tổng độ rộng tuyệt đối ít hơn N4 do N4 dự phòng thêm 2 mm. Đây là **tiêu chí tie-break**, không phải chứng cứ N2 đẹp nhất. N4 có dư địa hình học lớn hơn nhưng độ rộng thấp hơn; chưa có chứng cứ rằng dự phòng 2 mm là ngưỡng tối ưu pháp lý hay thẩm mỹ.

## 229. Phương pháp kiểm tra và cách tránh kết luận giả

1. Mở từng DOCX như gói ZIP, đọc cấu trúc `word/document.xml`, sao chụp chuỗi `w:t`, đếm `w:tr`, `w:tc` và chữ ký ô gộp.
2. Chỉ cập nhật `w:tblGrid/w:gridCol`, mọi `w:tcPr/w:tcW` tương ứng và `w:tblPr/w:tblW`; **không** tái tạo bảng bằng các lệnh thêm/xóa ô. Đối chứng N0 giữ nguyên từng ZIP part. Khi chỉ thay width, chỉ `word/document.xml` được phép khác nội dung nguồn.
3. Mở lại bằng `python-docx` để đối chiếu số cột và giá trị twips mới, không dùng thao tác đọc lại như bằng chứng tương đương việc render.
4. Kết xuất PDF bằng LibreOffice 25.2.3.2 ở cùng máy. Đọc hình học đường kẻ ngang từ PyMuPDF trên **bảng kẻ lưới này**, đếm trang và chiều cao theo bao phủ đường viền; lấy vị trí mép phải viền từ PDF.
5. Đối chiếu chuỗi từng ô trên bản trích xuất PDF. Việc kiểm đủ 48/48 ô là **phép đối chiếu heuristic**; một số bảng khác có thể bị chia run/trang hoặc sắp xếp lại trật tự và gây thiếu giả. Không thay thế phép bảo toàn DOCX.
6. Chọn đúng một stress biến: tăng Normal style thêm 1 pt qua `word/styles.xml` trên mỗi bản sao ứng viên; source `word/document.xml` phải giữ nguyên byte giữa bản thường và bản tăng cỡ chữ.
7. Quan sát ảnh kết xuất từng ứng viên. Đánh giá đọc rõ của tiêu đề, các mã và dữ liệu số trước khi xếp hạng bằng metric.

Không dùng OCR; không dùng số trang/chiều cao của một bảng có viền để suy ra phương án tương đương cho bảng không viền; không tự động xếp hạng theo phép đo PDF nếu không có renderer đích.

## 230. Kết quả đo thực tế tại cỡ chữ gốc

| Ứng viên | Tổng grid sau lượng tử hóa (mm) | Dư địa nội dung (mm) | Mép phải đường viền so với lề phải (mm) | Cao bảng trên PDF (mm) | Văn bản đối chiếu |
|---|---:|---:|---:|---:|---:|
| N0 — không sửa | 252,007 | −9,984 | **+8,19** (vượt) | 45,40 | 48/48 ô |
| N1 — tỷ lệ | 242,023 | 0,000 | −1,80 (trong) | 45,40 | 48/48 ô |
| N2 — ưu tiên trường khóa | 242,006 | +0,018 | −1,83 (trong) | 45,40 | 48/48 ô |
| N3 — ưu tiên mô tả | 241,970 | +0,053 | −1,87 (trong) | 45,40 | 48/48 ô |
| N4 — dự phòng 2 mm | 239,995 | +2,028 | −3,84 (trong) | 45,40 | 48/48 ô |

Dấu dương ở cột vị trí viền = đường viền ngoài vùng nội dung phía phải; dấu âm = còn ở bên trong. **Đây là số đo của viền**, không đồng nghĩa chữ bị mất hoặc chữ vượt lề; với N0, chuỗi chữ trong các ô vẫn được tìm thấy trong PDF, mặc dù đường viền vượt vùng trình bày. Như vậy cần có ít nhất hai cảnh báo riêng `TABLE_BORDER_OUT_OF_CONTENT_AREA` và `TEXT_CLIPPED/CONTENT_MISSING`, không tự suy ra cái sau từ cái trước.

Đặc biệt ở bản F07, đường viền trái nằm lệch so với tọa độ văn bản đầu ô do đệm ô và cách Word/LibreOffice bố trí lưới. Do đó, không lấy duy nhất `grid_width` trừ lề để mô tả độ lệch **cả hai mép viền** khi kết xuất. Phải có bước đo hoặc cho phép sai lệch hiển thị rõ ràng theo renderer.

## 231. Kết quả phép tăng cỡ chữ +1 pt

| Phương án | Chiều cao gốc (mm) | Chiều cao +1 pt (mm) | Số trang sau tăng | Số ô có văn bản tìm thấy trên PDF |
|---|---:|---:|---:|---:|
| N0 | 45,40 | 47,84 | 1 | 48/48 |
| N1 | 45,40 | 47,84 | 1 | 48/48 |
| N2 | 45,40 | 47,84 | 1 | 48/48 |
| N3 | 45,40 | 47,84 | 1 | 48/48 |
| N4 | 45,40 | 47,84 | 1 | 48/48 |

**Kết luận được chứng minh trong fixture:** tăng 1 pt làm bảng cao hơn ở tất cả ứng viên, nhưng không làm ứng viên N1–N4 khác nhau về tổng chiều cao trên renderer đã thử. Không được kết luận từ đây rằng các phân bổ N1–N4 có cùng mức tối ưu trên bảng khác hoặc khi dùng Microsoft Word. Cũng không được dùng kết quả thử stress để thay profile phông chữ theo yêu cầu pháp lý hiện hành.

## 232. Bảo toàn cấu trúc và nội dung: bằng chứng theo phạm vi

- Toàn bộ 5 phương án đã được tạo và mở lại thành công ở dạng DOCX; số hàng **6**, số ô **48**, số cột **8** và chuỗi `w:t` giữ nguyên so với nguồn; không có gộp ô mới.
- Bốn phương án N1–N4 chỉ có khác biệt nội dung trong ZIP part `word/document.xml`; N0 không thay đổi nội dung part.
- Năm bản tăng font riêng biệt chỉ đổi `word/styles.xml` so với bản tương ứng; toàn bộ byte của `word/document.xml` được giữ nguyên.
- Có **10/10 kết xuất DOCX→PDF LibreOffice**; 10/10 trường hợp đều tìm thấy nội dung của **48/48 ô** bằng phép đối chiếu đã nêu.
- Có `metrics_v14.json`, file DOCX/PDF nguồn–ứng viên, ảnh bản in, mã thử có assertion và danh mục SHA-256 trong ZIP nghiên cứu đi kèm.

Chữ `PASS` ở đây không mở rộng đến đối tượng nhúng, Track Changes, chữ ký số, quyền chỉnh sửa, AlternateContent hay hàng dài nhiều trang, vì fixture F07 không có các cấu trúc đó. **Không tuyên bố đã chạy hoặc PASS 152 tình huống đặc tả T01–T152**.

## 233. Kết quả âm tính có giá trị: chưa thể xếp hạng thẩm mỹ bốn phương án

Trên F07, N1–N4 khác nhau về cấu trúc rộng cột nhưng đều cho 45,40 mm ở cỡ chữ gốc và 47,84 mm khi tăng 1 pt. Các tiêu đề STT, Mã, ba năm và nội dung đọc được; phép đo tổng chiều cao **không đủ độ nhạy để phân biệt chất lượng**. Vì vậy, phải báo `EQUIVALENT_BY_MEASURED_METRICS`, **không được tự nhận một thuật toán semantic là tốt nhất**.

Nếu yêu cầu bắt buộc phải chọn một phương án khi N0 đã lỗi hình học, áp dụng thứ tự tie-break minh bạch: (1) đủ chiều rộng tối thiểu đã được kiểm chứng cho các trường khóa; (2) giữ dạng số/ngày/ID trên một dòng khi có thể; (3) ít cột bị thay đổi và ít phần tử OOXML phải ghi lại; (4) chênh lệch tổng độ rộng ít nhất; (5) độ dư hình học phù hợp mức rủi ro của môi trường, không cố dùng hết trang. Trong corpus F07, N2 là **ứng viên ưu tiên xét tiếp** do giữ nguyên STT/Mã/ba cột năm và chỉ đổi 3 cột; N4 là **phương án dự phòng** khi thực sự cần khoảng an toàn lớn hơn. Đây là **khuyến nghị vận hành có điều kiện**, chưa là kết luận Word PASS.

## 234. Ma trận quyết định V14, áp dụng sau V13 geometry gate

| Tình huống | Quyết định mặc định | Chứng cứ tối thiểu |
|---|---|---|
| Bảng không vượt vùng chứa, đọc tốt | `NO_OP_VALID` | Geometry + kiểm tra render phù hợp phạm vi |
| Bảng rộng hơn vùng chứa, không bị khóa | `GENERATE_LOCAL_WIDTH_CANDIDATES` | Đúng section/container, biết loại bảng, đủ quyền sửa |
| Tổng chiều rộng tối thiểu của các cột vượt giới hạn | `REVIEW_REQUIRED` | Báo không có nghiệm chỉ đổi width; không thay font/lề im lặng |
| Nhiều phương án có metric giống nhau | `TIE_BREAK_WITH_EXPLANATION` | Bảng so sánh thay đổi và các trường được bảo vệ |
| Bảng biểu mẫu được ban hành hoặc vùng ký bị khóa | `PRESERVE_AND_REVIEW` | Authority/mẫu, không dùng template thẩm mỹ ghi đè |
| Đổi lề/section/font sau khi tính width | `INVALIDATE_LAYOUT_CANDIDATES` | So fingerprint mới rồi tính lại, không reuse stale width |
| Chỉ có LibreOffice, yêu cầu khớp bản in Word | `UNVERIFIED_WORD_PRINT` | Không quảng bá Word Print PASS |
| Thấy viền tràn nhưng nội dung chữ còn đủ | `BORDER_GEOMETRY_WARNING` | Tách kiểm viền khỏi phát hiện cắt/mất chữ |

## 235. Chính sách tái sử dụng kỹ thuật, tránh xây thêm hệ dàn trang

Microsoft mô tả `tblPr`, `tblGrid`, `gridCol`, `tr`, `tc` làm cấu trúc bảng; `tblW` và `tcW` có thể bị giải lại khi xung đột do đặc trưng preferred width. Word có `AutoFit Contents`, `AutoFit Window` và `Fixed Column Width`, nhưng người dùng vẫn cần xem kết quả in khi thay đổi layout. Không cần xây bộ dàn trang mới cho DOCX. Để tích hợp vào dự án đang hoạt động, **kiểm toán bộ xử lý hiện có trước** rồi bổ sung tối thiểu bước:

```text
READ EXISTING TABLE STRUCTURE
  → RESOLVE SECTION / CONTAINER / AUTHORITY / LOCKS
  → CHECK PAGE GEOMETRY (twips, indent, floating, merged span)
  → KEEP if valid and readable
  → GENERATE bounded candidate widths without changing content
  → REOPEN + COMPARE ZIP PARTS / TEXT / TOPOLOGY
  → RENDER candidate pairs with SAME renderer
  → KEEP / PROPOSE (approval) / REVIEW / ROLLBACK
```

V14 viết **mã nghiên cứu standalone**, không sửa mã repo nào, không tạo subsystem triển khai song song. Trong ứng dụng, nên reuse parser/validator/snapshot/approval đang có nếu kiểm toán chứng minh đáp ứng; chỉ bổ sung adapter để truyền tập `gridWidth` và kiểm tra geometry nếu cần.

## 236. Gói nghiệm thu tối thiểu có thể giao cho Executor

| Cổng | Điều kiện PASS đề xuất | Thất bại bắt buộc báo |
|---|---|---|
| G0 nguồn | Snapshot / DOCX source không đổi trong suốt quyết định | `SOURCE_CHANGED`, dừng và tính lại |
| G1 authority | Nhận diện hệ NĐ30/HD05 hoặc mẫu, khóa các phần cố định | `UNKNOWN_AUTHORITY`, review |
| G2 geometry | Width theo **đúng** section/story/container; kiểm overflow đã render | `NO_FEASIBLE_WIDTH` hoặc `GEOMETRY_FAIL` |
| G3 integrity | Text/ô/quan hệ/part ngoài phạm vi không mất; track/embedded nếu có phải được xử lý | `INTEGRITY_FAIL`, rollback |
| G4 usability | Mã/số liệu/tiêu đề không bị vỡ hoặc mất; không có hồi quy rõ rệt | `READABILITY_REGRESSION`, review |
| G5 target renderer | Có Word build/OS/font/print driver cho kết luận về bản in Word | `WORD_RENDER_UNVERIFIED` |
| G6 authorization | Người dùng chấp thuận các sửa đổi được đề xuất | `NEEDS_APPROVAL` |

Đối tượng nghiệm thu kế tiếp nên là fixture V14 cộng một file thực tế **đã được phép sử dụng và loại bỏ dữ liệu nhạy cảm**. Không chấp nhận nghiệm thu chỉ dựa trên file XML hợp lệ hoặc việc xuất PDF thành công. Không commit/push/deploy/migrate production khi chưa có phê duyệt độc lập.

## 237. Kết luận V14 và giới hạn kiểm chứng

**Phát hiện có chứng cứ:** Sau khi thay đổi lề F07, bốn phương án cập nhật tổng chiều rộng đã khắc phục tình trạng đường viền bảng vượt lề phải trong PDF LibreOffice mà không làm tăng chiều cao bảng; cả bốn giữ nguyên cấu trúc và chuỗi ký tự trong DOCX mẫu. Trong stress +1 pt, bốn phương án vẫn cùng chiều cao và cùng số trang. Kết quả đủ cơ sở để bổ sung quy trình **re-fit chiều rộng có điều kiện** và các reason code, **chưa đủ để chứng minh một phép chia cột là tối ưu thẩm mỹ**.

**Bằng chứng còn thiếu:** render bằng Microsoft Word trên môi trường đích; corpus bảng nhiều tầng/ô gộp đối với trường hợp lề thay đổi; font fallback khác hệ điều hành; đánh giá người đọc; kiểm thử trong ứng dụng Word/ONLYOFFICE đang sử dụng. Các phần này là bước kiểm chứng tiếp theo — không mặc định xây mới một hệ dàn trang.

**Tài liệu kỹ thuật bổ sung:** Microsoft Learn, *Working with WordprocessingML Tables*; Microsoft Learn, *TableWidth Class — Preferred Table Width*; Microsoft Support, *Resize a table, column, or row*; Microsoft Support, *Repeat table header on subsequent pages* (xem [S97], [S99]–[S101]).

---

# PHẦN XXXI. V15 — KIỂM CHỨNG RANH GIỚI HÌNH HỌC SAU KHI TÁI SỬ DỤNG ĐỘ RỘNG CỘT

> **Đóng góp mới, có phép thử:** kiểm tra độ nhạy của bốn phương án N1–N4 thuộc V14 khi **chỉ tăng lề phải**, không phân bổ lại chiều rộng. 4 phương án × 6 biến thể = **24 DOCX và 24 PDF kết xuất LibreOffice**, với dữ liệu tổng hợp. Đo riêng `grid_width - usable_width` trong OOXML và `right_border - margin_boundary` trên PDF. Đây **không** phải kiểm chứng trong Microsoft Word, cũng **không** là 24 ca mới thuộc tập T01–T152.

## 238. Khoảng trống sau V14: phương án từng đạt có còn hợp lệ khi hình học thay đổi?

V14 đã chứng minh N1–N4 giải quyết được trường hợp lưới F07 quá rộng sau một lần thay lề. Nhưng hệ thống thực tế có thể đổi tiếp section margin do thay profile, mẫu cơ quan, in hai mặt, orientation hoặc bố trí phụ lục. Khi đó phương án width từng được chọn không được **âm thầm tái sử dụng**. Một layout được kiểm chứng ở thời điểm `t0` không có nghĩa vẫn hợp lệ ở `t1`.

Nhu cầu mới cần kiểm định bằng phép thử âm/dương, không viết thêm engine mới: *các phương án đã fit ở V14 có thể bị mất điều kiện hình học trước khi PDF bộc lộ viền vượt lề hay không?* Nếu có, dùng riêng chỉ số đường viền PDF là không đủ.

## 239. Nguồn thí nghiệm, biến độc lập và bất biến

- **Nguồn:** đúng bốn DOCX tổng hợp `N1_proportional_fit`, `N2_semantic_protect`, `N3_content_priority`, `N4_reserve_2mm` của V14, không sinh bảng mới.
- **Biến độc lập:** tăng riêng `w:pgMar/@w:right` lần lượt **0, 1, 2, 3, 4, 5 mm** trên bản sao đã tối ưu. Các giá trị được lượng tử hóa bằng twip, nên sai khác vài phần nghìn mm.
- **Bất biến:** số bảng 1; 6 hàng; 48 ô; 8 cột; chuỗi các `w:t`; `w:gridCol`; `w:tcW`; cấu trúc ô gộp; và mọi part OPC ngoài `word/document.xml` không đổi. Với delta=0, toàn bộ bytes DOCX gốc được sao chép nguyên.
- **Môi trường đo:** LibreOffice 25.2.3.2 trên Linux, PyMuPDF đọc các nét ngang PDF. Mỗi biến thể mở lại bằng `python-docx`; PDF có một trang, đối chiếu heuristic chuỗi 48/48 ô.
- **Lưu ý:** đây là phép stress **sau khi đã cấp width**; không phải quá trình tối ưu lại, không có văn bản hành chính/Đảng thật và không kiểm chứng chữ ký số.

## 240. Hai phép đo độc lập và tình huống sai lệch

Đối với bảng dữ liệu thông thường, không phải bảng nổi/lồng/đặt indent phức tạp:

```text
usable_width_twip := page_width - left_margin - right_margin
width_excess_mm  := sum(tblGrid.gridCol.w) - usable_width_twip
border_excess_mm := PDF rightmost table border - PDF right margin boundary
```

- `width_excess_mm > 0`: **không đáp ứng giới hạn lưới dựa trên section** của fixture; không chấp nhận ứng viên dựa vào cảm giác hình ảnh dù PDF còn khoảng trắng.
- `border_excess_mm > 0`: nét viền được đo nằm ngoài đường biên lề trên PDF trong renderer thử nghiệm; đây là bằng chứng hiển thị cần rà soát.
- `width_excess_mm ≤ 0` chỉ xác nhận **đạt danh nghĩa theo phép tính này**, không xác nhận render Word, không xử lý được `tblInd`, `tblpPr`, `mirrorMargins`, section phức tạp, bảng lồng/ô gộp và không phải sự bảo đảm in hoàn hảo.
- Trị số gần 0 (ví dụ 0,035 mm dự phòng) phải coi là **cận biên chưa hiệu chỉnh ngưỡng an toàn**, không tự gắn trạng thái `ROBUST_PASS`.

**Nguồn kỹ thuật:** Microsoft giải thích `w:tblW` và `w:tcW` là *preferred width* có thể bị thuật toán dàn trang ghi đè; `w:tblGrid` tham gia bố trí lưới; `Fixed Column Width` là khả năng Word có sẵn. Tham khảo [S102]–[S103].

## 241. Bảng kết quả tổng hợp 24 biến thể

| Ứng viên | Rộng lưới (mm) | Dự phòng gốc (mm) | Delta lề còn **đạt hình học danh nghĩa** (mm) | Delta lề còn **chưa thấy viền vượt trên PDF** (mm) |
|---|---:|---:|---|---|
| `N1_proportional_fit` | 242.023 | 0.000 | 0 | 0, 1 |
| `N2_semantic_protect` | 242.006 | 0.017 | 0 | 0, 1 |
| `N3_content_priority` | 241.970 | 0.053 | 0 | 0, 1 |
| `N4_reserve_2mm` | 239.995 | 2.028 | 0, 1, 2 | 0, 1, 2, 3 |

`N4` duy trì điều kiện hình học danh nghĩa khi tăng lề phải 2 mm, nhưng dự phòng tại thời điểm đó chỉ **0,035 mm**, chưa đủ cơ sở để coi là an toàn phổ quát. N1–N3 chỉ có dự phòng không đáng kể tại delta=0 và mất điều kiện hình học từ delta=1.

Bảng sau ghi cặp giá trị **(lưới vượt vùng / viền PDF vượt lề), đơn vị mm**. Dấu dương biểu thị vượt; dấu âm là còn khoảng trống:

| Tăng lề phải | N1 | N2 | N3 | N4 |
|---|---:|---:|---:|---:|
| +0 | +0.000 / -1.796 | -0.017 / -1.831 | -0.053 / -1.866 | -2.028 / -3.842 |
| +1 | +1.005 / -0.790 | +0.988 / -0.825 | +0.952 / -0.861 | -1.023 / -2.836 |
| +2 | +1.993 / +0.198 | +1.976 / +0.162 | +1.940 / +0.127 | -0.035 / -1.848 |
| +3 | +2.998 / +1.203 | +2.981 / +1.168 | +2.945 / +1.133 | +0.970 / -0.843 |
| +4 | +4.004 / +2.208 | +3.987 / +2.173 | +3.951 / +2.138 | +1.976 / +0.162 |
| +5 | +4.992 / +3.196 | +4.975 / +3.161 | +4.939 / +3.126 | +2.964 / +1.150 |

**Tổng hợp tự động:** 24/24 DOCX mở lại được; 24/24 PDF kết xuất được; 24/24 phép đối chiếu heuristic tìm đủ 48/48 nội dung ô; **6/24** biến thể đạt phép tính hình học danh nghĩa; **10/24** có viền phải PDF chưa vượt; **4/24** trường hợp *PDF không vượt nhưng lưới OOXML đã vượt*. Không xem các số này như tỷ lệ lỗi của Word hay của tài liệu thực tế.

## 242. Phát hiện thực nghiệm: “PDF trông vừa” chưa đồng nghĩa “DOCX đạt hình học”

Bốn trường hợp sai lệch đáng chú ý đều có lưới vượt vùng nội dung nhưng viền phải của bản kết xuất LibreOffice chưa vượt lề:

| Tình huống | Lưới vượt (mm) | Viền PDF so với lề (mm) | Kết luận |
|---|---:|---:|---|
| N1, tăng lề 1 mm | +1,005 | −0,790 | Không đạt gate hình học |
| N2, tăng lề 1 mm | +0,988 | −0,825 | Không đạt gate hình học |
| N3, tăng lề 1 mm | +0,952 | −0,861 | Không đạt gate hình học |
| N4, tăng lề 3 mm | +0,970 | −0,843 | Không đạt gate hình học |

Cần kết luận đúng phạm vi: điều này có thể do điểm neo/độ lệch viền so với lưới trong bộ kết xuất thử, không phải khẳng định Word luôn xử lý giống vậy. Do đó, rule không được sửa bằng thủ thuật lấy đường viền PDF làm authority thay cho lưới/section. Ngược lại, nếu lưới đạt nhưng PDF bị cắt/đè chữ, **vẫn phải từ chối**.

![So sánh đường viền PDF và ranh giới lề trong một số biến thể V15](v15_experiment/V15_MARGIN_BOUNDARY_COMPARISON.png)

*Đường đỏ: ranh giới lề phải đo trên PDF; đường xanh: nét viền phải bảng. Hình chỉ minh họa khác biệt giữa hai oracle, không khẳng định tính phù hợp pháp lý.*

## 243. Chính sách khoảng dự phòng thay thế “mặc định 2 mm là tối ưu”

V14 thử một phương án dự phòng khoảng 2 mm. V15 xác nhận dự phòng đó có ích trong đúng tình huống lề phải tăng; **không đủ căn cứ** khuyến nghị 2 mm là một hằng số bắt buộc, tối ưu hoặc đủ an toàn trên mọi DOCX.

Đề xuất `required_reserve_mm` là cấu hình thí nghiệm gắn với profile/renderer/khổ giấy/độ phức tạp; muốn đặt ngưỡng mặc định phải hiệu chỉnh trên corpus và chấp thuận của người dùng. Cho tới khi có kết quả, ghi các trạng thái riêng:

- `GEOMETRY_FAIL`: lưới vượt vùng khả dụng theo mô hình áp dụng; không tự APPLY.
- `GEOMETRY_NOMINAL`: phép tính lưới không vượt, nhưng dự phòng bằng không hoặc quá nhỏ so với ngưỡng chưa được hiệu chỉnh; cần render và người dùng duyệt nếu thay đổi có rủi ro.
- `GEOMETRY_CLEARANCE_OBSERVED`: có dự phòng đo được nhưng vẫn cần qua gate kết xuất.
- `RENDER_FAIL`: cắt chữ, tràn khung, thay đổi trang hoặc che nội dung.
- `NO_OP_VALID`, `REVIEW`, `APPLY_VERIFIED`: chỉ được kết luận trong phạm vi oracle đã thực thi.

**Không đặt một ngưỡng nhỏ tùy tiện rồi báo đã “đạt Word”.** Trường hợp N4 +2 mm là phép thử cận biên rất tốt cho chương trình hiệu chỉnh trong tương lai.

## 244. Hợp đồng vô hiệu hóa ứng viên cũ khi thay đổi bối cảnh

Chỉ được tái dùng đề xuất width nếu khóa bối cảnh còn phù hợp. `layout_context_fingerprint` nên tham chiếu ít nhất:

```yaml
section: page_size, orientation, left/right_margin, mirror_gutter
container: story, nested_parent_width, table_indent, floating_position
format: table_layout_mode, table_style_effective, paragraph_format, font_signature
content: cell_text_hash, grid_structure, merged_structure
renderer: name, version, locale, font_inventory
```

Khi thay lề/section/font, đặt đề xuất cũ là `STALE_RECOMPUTE_REQUIRED`; chạy lại kiểm hình học và chỉ render các ứng viên có khả năng đạt. Không biến fingerprint thành kho lưu nội dung DOCX hoặc lưu dữ liệu nhạy cảm không cần thiết. Nếu hệ thống hiện tại đã có source snapshot/context metadata, **mở rộng tối thiểu**, không lập registry song song.

## 245. Quy trình quyết định có thể triển khai trong formatter hiện có

```text
INPUT: original table snapshot + current section/container + existing candidate widths
1  Resolve effective authority and table classification; official form/locked -> PRESERVE.
2  Read current section/container geometry, not historical mm values.
3  Invalidate old proposal if relevant fingerprint changed.
4  Test no-change baseline, then compute current width-excess for each candidate.
5  Reject geometrically invalid candidates; mark borderline cases REVIEW.
6  Reuse renderer if present; compare table border/text + pagination at same environment.
7  Validate structural / semantic diff and all affected stories.
8  If candidates tie on validated benefits, prefer minimal change and preserved intent.
9  Apply only with user's approval and actual verification; otherwise NO_OP/REVIEW.
10 Emit candidate trace, measured bounds, uncertainty, reason code and rollback data.
```

Trong tài liệu có bảng nổi/lồng, in hai mặt hoặc section phức tạp, `usable_width = page - left - right` không phải mô hình cuối cùng. Nếu không suy ra container đáng tin cậy, **không tự resize**. Các thao tác đọc/ghi margin, lưới và PDF đã có trong thư viện hiện hữu (Word/OOXML, python-docx, lxml và công cụ render); không cần thêm mô hình AI hoặc xây hệ thống dàn trang mới.

## 246. Giới hạn phép đo và nguy cơ đánh giá sai

1. Đường viền được nhận diện bằng các đoạn line ngang đủ dài trong vùng trang của fixture. Với tài liệu có biểu đồ, nhiều bảng, shape hoặc đường kẻ trang trí, cần gắn tọa độ về đúng bảng và định nghĩa ROI riêng trước khi diễn giải.
2. Tìm đủ chuỗi của 48 ô trong PDF bằng heuristic `strip whitespace` chỉ là kiểm tra phụ trợ, có thể có dương/âm tính giả nếu nội dung trùng lặp, mất thứ tự hoặc ngắt trang. **Không thay thế** so sánh XML nguồn/đích và kiểm tra trực quan.
3. Không có Microsoft Word desktop/Word Object Model trong phép thử; Open XML hợp lệ không chứng minh được độ chính xác kết xuất Word. PDF của LibreOffice là oracle thử nghiệm M2, không phải M3 target Word.
4. Mẫu F07 ngắn, có tám cột không gộp, một section; không suy rộng kết quả cho tiếng Việt dài, bảng có ô gộp, nhiều section, track changes hoặc mẫu văn bản ký số.
5. Việc thay một lề trên bản thử có thể ảnh hưởng các thành phần khác của văn bản thực tế; phép thử cố tình cô lập một bảng nên blast radius được giới hạn tại fixture.

## 247. Bộ chứng cứ tối thiểu và tiêu chí kiểm tra V15

| Tiêu chí | Kết quả thực thi / giới hạn |
|---|---|
| Số biến thể | 4 × 6 = 24 DOCX |
| DOCX mở lại | 24/24 PASS |
| OOXML giữ nguyên mọi thuộc tính ngoài lề phải | 24/24 PASS theo canonical tree compare trong phạm vi part được sửa |
| OPC parts ngoài `word/document.xml` | 24/24 không thay đổi bytes |
| Số bảng/hàng/ô/lưới, nội dung `w:t` | 24/24 PASS |
| PDF LibreOffice | 24/24 tạo được; 1 trang/biến thể |
| PDF text heuristic | 24/24 tìm đủ 48/48 ô, không suy ra Word PASS |
| Phép phân định hình học / viền PDF | Có 4 ca khác kết luận: kiểm kép là cần thiết trong phạm vi mẫu |
| Word Print Layout, kiểm in thực tế | **UNVERIFIED** |
| Tích hợp vào repo hoặc plugin | **NOT EXECUTED** |

Bộ QA đính kèm có `metrics_v15.json`, mã `run_v15.py` và `make_evidence.py`, bốn nguồn V14, DOCX/PDF/ảnh, SHA-256. Mã thử nghiệm chỉ là benchmark, **không** là code ứng dụng, không chỉnh phần mềm hiện hành.

## 248. Điều kiện chuyển sang áp dụng thực tế

Không tiếp tục nới rộng lý thuyết hoặc tăng số kịch bản T01–T152 nếu chưa có lỗi/nhu cầu mới. Bước thiết thực là thử trong Microsoft Word với đúng 4 biến thể đại diện (N1+1, N1+2, N4+2, N4+3), kiểm *Print Layout*, in/PDF do Word xuất, vị trí border, cắt chữ và khả năng bảo toàn tài liệu. Sau đó mở rộng theo blast radius khi thay đổi section, nhiều bảng và phụ lục.

**Quyết định hiện tại:** phương án cũ phải vô hiệu hóa khi lề đã đổi. N4 có dự phòng tốt hơn ba phương án còn lại trong thí nghiệm nhưng không phải phương án “tối ưu nhất” chung. Quy tắc `RECOMPUTE_ON_GEOMETRY_CHANGE` được đề xuất làm điều kiện bắt buộc trong bộ định dạng tương lai; **chưa chứng minh đã hoạt động trong phần mềm thực tế**.


# PHỤ LỤC A. BẢNG THUỘC TÍNH CHƯA CÓ ĐỊNH MỨC CHUNG BẮT BUỘC

| Thuộc tính | Có định mức chung cố định cho mọi bảng trong NĐ30 và HD05? | Hướng áp dụng |
|---|---|---|
| Viền ngoài, viền trong | Không xác định một độ dày bắt buộc chung | Theo mẫu hoặc preset |
| Màu đường kẻ | Không xác định một màu viền chung | Đen/xám đậm [KN] |
| Màu nền hàng tiêu đề | Không có màu bắt buộc chung | Trắng mặc định [KN] |
| Độ rộng từng cột | Không có mm cố định chung | Theo nội dung/vùng chữ |
| Chiều cao từng hàng | Không có mm cố định chung | Auto/At least nếu phù hợp |
| Cell padding | Không có trị số riêng chung | 1,5–2 mm ngang, 0,8–1,2 mm dọc [KN] |
| Cell spacing | Không có trị số riêng chung | 0 mm [KN] |
| Mọi ô đều căn giữa | Không | Theo kiểu dữ liệu |
| Dòng xen kẽ tô màu | Không | Mặc định không cần |
| Lặp hàng tiêu đề qua trang | Không có yêu cầu chung cố định theo hai văn bản | Khuyến nghị Word/Accessibility |
| Hạn chế gộp ô | Không phải lệnh cấm chung | Soạn bảng mới đơn giản; bản mẫu có gộp phải giữ |
| Số thứ tự/tên bảng | Không có một khuôn mẫu phổ quát cho mọi bảng | Theo loại báo cáo, mẫu hoặc quy ước |
| Ghi nguồn số liệu | Không có một định dạng bắt buộc chung cho mọi bảng | Ghi khi cần, không tự sáng tác |

# PHỤ LỤC B. BỘ MINH HỌA NỘI DUNG BẢNG (GIẢ LẬP)

## Ví dụ B1 – Bảng phân công công việc

| STT | Nội dung công việc | Đơn vị thực hiện | Thời hạn |
|:---:|---|---|:---:|
| 1 | Kiểm tra hồ sơ | Phòng A | 20/10 |
| 2 | Tổng hợp báo cáo | Phòng B | 25/10 |
| 3 | Hoàn thiện kết quả | Phòng C | 30/10 |

**Thiết kế gợi ý:** kẻ ô Formal Grid; STT/hạn căn giữa; nội dung căn trái; cột nội dung rộng nhất.

## Ví dụ B2 – Bảng thống kê số liệu

**Bảng 01. Tổng hợp kết quả thực hiện nhiệm vụ (số liệu giả lập)**  
*Đơn vị tính: nhiệm vụ*

| Nội dung | Kế hoạch | Hoàn thành |
|---|---:|---:|
| Nhiệm vụ thường xuyên | 25 | 24 |
| Nhiệm vụ đột xuất | 12 | 12 |
| **Tổng cộng** | **37** | **36** |

*Nguồn: Ví dụ giả lập để minh họa định dạng, không phải dữ liệu nghiệp vụ thực tế.*

**Thiết kế gợi ý:** Statistical Minimal; căn phải số; tiêu đề ngắn, rõ; viền tổng cộng nổi bật vừa đủ.

---

# PHỤ LỤC C. NGUỒN THAM KHẢO, LIÊN KẾT VÀ CĂN CỨ

> Phân loại: **[Quy định]** = nguồn quy định; **[Official tech]** = Microsoft/Office; **[Best practice]** = hướng dẫn quốc tế. Những tài liệu best practice không tạo nghĩa vụ pháp lý Việt Nam.

**Nhóm quy định Việt Nam**

- **[S01] [Quy định]** Chính phủ. *Nghị định 30/2020/NĐ-CP về công tác văn thư* (05/03/2020). CSDL quốc gia VBPL, trạng thái còn hiệu lực: https://vbpl.vn/thanhtrachinhphu/Pages/vbpq-thuoctinh.aspx?ItemID=141142
- **[S02] [Quy định]** *Phụ lục I Nghị định 30/2020/NĐ-CP – thể thức, kỹ thuật trình bày văn bản hành chính*. Bản toàn văn phụ lục công khai: https://riam.edu.vn/nghi-dinh-ve-cong-tac-van-thu-phu-luc/ ; đối chiếu văn bản gốc tại mục tệp Phuluc1 ở [S01].
- **[S03] [Quy định]** Cổng thông tin Chính phủ. *Nghị định 30/2020/NĐ-CP cùng các phụ lục* (bản bài chính phủ công bố phụ lục): https://xaydungchinhsach.chinhphu.vn/quy-dinh-ve-cong-tac-van-thu-quan-ly-van-ban-the-thuc-ky-thuat-trinh-bay-van-ban-ban-sao-van-ban-viet-hoa-mau-trinh-bay-van-ban-hanh-chinh-119251023153016706.htm
- **[S04] [Quy định]** Ban Bí thư. *Quy định 399-QĐ/TW ngày 09/01/2026*. Tư liệu – Văn kiện Đảng, trạng thái hiệu lực 09/01/2026: https://tulieuvankien.dangcongsan.vn/he-thong-van-ban/van-ban-cua-dang/quy-dinh-so-399-qd-tw-ngay-09-01-2026-cua-ban-bi-thu-ve-the-loai-tham-quyen-ban-hanh-va-the-thuc-van-ban-cua-dang.html
- **[S05] [Quy định]** Văn phòng Trung ương Đảng. *Hướng dẫn 05-HD/VPTW ngày 27/05/2026*. Tư liệu – Văn kiện Đảng: https://tulieuvankien.dangcongsan.vn/van-ban-cua-dang/huong-dan-so-05-hd-vptw-ngay-27-5-2026-cua-van-phong-trung-uong-dang-ve-the-thuc-va-ky-thuat-trinh-bay-van-ban-cua-dang.html
- **[S06] [Quy định]** *Toàn văn Hướng dẫn 05-HD/VPTW*, bản HTML tra cứu theo mục và Phụ lục 2, LuatVietnam: https://luatvietnam.vn/hanh-chinh/huong-dan-05-hd-vptw-2026-ve-the-thuc-va-ky-thuat-trinh-bay-van-ban-cua-dang-436254-d6.html ; đối chiếu nguồn chính tại [S05].
- **[S15] [Quy định]** Bộ Nội vụ. *Thông tư 01/2020/TT-BNV bãi bỏ Thông tư 01/2011/TT-BNV* (hiệu lực 15/06/2020): https://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=141878&Keyword=
- **[S16] [Quy định]** Chính phủ. *Nghị định 78/2025/NĐ-CP – thể thức văn bản quy phạm pháp luật*, nội dung phụ lục được giới thiệu tại https://xaydungchinhsach.chinhphu.vn/nghi-dinh-so-78-2025-nd-cp-quy-dinh-the-thuc-ky-thuat-trinh-bay-van-ban-quy-pham-phap-luat-119250409084740906.htm ; chú ý các phụ lục đã được thay thế.
- **[S17] [Quy định]** Chính phủ. *Nghị định 187/2025/NĐ-CP* (điều chỉnh các phụ lục của Nghị định 78/2025), toàn văn chính thức: https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/187-ndcp.signed.pdf

**Nhóm Microsoft / Office Open XML**

- **[S07] [Official tech]** Microsoft Support. *Repeat table header on subsequent pages*: https://support.microsoft.com/en-us/word/repeat-table-header-on-subsequent-pages
- **[S08] [Official tech]** Microsoft Support. *Resize a table, column, or row; AutoFit, cell margins and spacing*: https://support.microsoft.com/en-us/word/resize-a-table-column-or-row
- **[S14] [Official tech]** Microsoft Learn. *Working with WordprocessingML tables*: https://learn.microsoft.com/en-us/office/open-xml/word/working-with-wordprocessingml-tables
- **[S18] [Official Microsoft accessibility]** Microsoft Support. *Make your Word documents accessible to people with disabilities*: https://support.microsoft.com/en-us/accessibility/word/make-your-word-documents-accessible-to-people-with-disabilities . Hướng dẫn bảng đơn giản, header có nghĩa và kiểm tra trên thiết bị; đối chiếu khi đánh giá khả năng đọc, không dùng để tự thay đổi mẫu hành chính.
- **[S19] [Official Microsoft OOXML]** Microsoft Learn. *About the Open XML SDK for Office*: https://learn.microsoft.com/en-us/office/open-xml/about-the-open-xml-sdk . Giải thích package parts/relationships và nhiều phần của Word (document, header/footer, chú thích...), phục vụ đối chiếu phạm vi bảo toàn.

**Nhóm best practice thiết kế/khả năng tiếp cận**

- **[S09] [Best practice]** U.S. Section508.gov. *Data tables in Microsoft Word, PowerPoint, Excel, and PDFs* (cập nhật 08/2025): https://www.section508.gov/blog/accessibility-bytes/data-tables-in-documents/
- **[S10] [Best practice]** W3C Web Accessibility Initiative. *Tables Tutorial*: https://www.w3.org/WAI/tutorials/tables/
- **[S11] [Best practice]** UK Government Analysis Function. *Data visualisation: tables* (19/05/2022): https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-tables/
- **[S12] [Best practice]** W3C WAI. *Tips and Tricks for Tables*: https://www.w3.org/WAI/tutorials/tables/tips/
- **[S13] [Best practice]** U.S. Section508.gov. *Module 5: Use Built-in Features to Create Layout and Data Tables*: https://www.section508.gov/training/documents/aed-cop-docx05/

**Cách sử dụng nguồn:** Khi đưa một rule vào hệ thống, lưu `(source_id, tên văn bản, mục/điều, ngày hiệu lực, phạm vi áp dụng)` và dẫn trực tiếp đoạn nguồn. Với đề xuất 0,5 pt, 0,75 pt, cell padding, tỷ lệ cột hoặc điểm thẩm mỹ, ghi `[KN] – preset nội bộ`, **không** trích NĐ30/HD05 như thể đó là con số luật định.

---


### Nguồn bổ sung cho bản 2.0 (đối chiếu đến 20/10/2026)

- **[S20] [Official OOXML]** Microsoft Learn. *TableWidth Class — `w:tblW` (Preferred Table Width)*. Tài liệu giải thích "preferred" width, việc Word có thể vượt độ rộng ưu tiên và cách xác định `pct` theo vùng chữ trang: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablewidth?view=openxml-3.0.1 ; các loại đơn vị (`dxa`, `pct`, `auto`) tại https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablewidthunitvalues.
- **[S21] [Official OOXML]** Microsoft Learn. *Style Conditional Table Formatting Properties (`tblStylePr`)*: https://learn.microsoft.com/en-us/openspecs/office_standards/ms-oe376/f7f85a73-5f60-4f7e-a725-4f1f06198388 ; *TableCellMarginDefault (`tblCellMar`)*: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablecellmargindefault?view=openxml-3.0.1 ; *TableLook*: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablelook?view=openxml-3.0.1 .
- **[S22] [Mature OSS technical documentation]** `python-openxml/python-docx` — *Working with Tables*, giải thích layout grid, merged cells, omitted cells, nested tables: https://github.com/python-openxml/python-docx/blob/master/docs/user/tables.rst ; tài liệu gốc repository: https://github.com/python-openxml/python-docx . Những hạn chế nêu trong tài liệu không chứng minh dự án nào cũng gặp lỗi; chỉ là căn cứ thiết kế bài kiểm tra.
- **[S23] [Official OOXML]** Microsoft Learn. *Introduction to markup compatibility*; chú ý `mc:AlternateContent`, `mc:Ignorable`, khả năng tiền xử lý và lựa chọn nhánh tương thích: https://learn.microsoft.com/en-us/office/open-xml/general/introduction-to-markup-compatibility .
- **[S24] [Official Word]** Microsoft Support. *Resize a table, column, or row*: https://support.microsoft.com/en-us/word/resize-a-table-column-or-row . *Repeat table header on subsequent pages*: https://support.microsoft.com/en-gb/word/repeat-table-header-on-subsequent-pages .
- **[S25] [Accessibility]** Section508.gov. *Accessibility Bytes No. 12: Data Tables in Microsoft Word, PowerPoint, Excel, and PDFs*: https://www.section508.gov/blog/accessibility-bytes/data-tables-in-documents/ . Đặc biệt lưu ý các hướng dẫn riêng về hàng tiêu đề, ô gộp và PDF có gắn thẻ.
- **[S26] [Best practice]** W3C WAI. *Tables Tutorial*: https://www.w3.org/WAI/tutorials/tables/ ; *Tips and Tricks*: https://www.w3.org/WAI/tutorials/tables/tips/ . Đây là nguồn dành cho bảng web, dùng làm tham khảo khả năng tiếp cận; **không chuyển nguyên cơ chế HTML (`<th>`, `scope`, `headers`) thành thuộc tính Word DOCX tương ứng**.
- **[S27] [Best practice]** UK Government Analysis Function. *Data visualisation: tables*: https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-tables/ ; gợi ý bố cục, phân cấp tiêu đề, số liệu, khoảng trắng và đường kẻ, **không phải luật áp dụng cho văn bản Việt Nam**.

- **[S28] [Nguồn nhà nước]** Cổng văn bản Chính phủ. *Nghị định số 30/2020/NĐ-CP về công tác văn thư*: https://vanban.chinhphu.vn/default.aspx?docid=199378&pageid=27160 . Kiểm tra phiên bản văn bản và phụ lục tại nguồn nhà nước khi thực thi quy tắc.

### Nguồn bổ sung cho chuyên đề V3 — trọng tâm nội dung và độ rộng cột (20/10/2026)

- **[S29] [Official OOXML]** Microsoft Learn. *TableCellWidth Class (`w:tcW`) – Preferred Table Cell Width*: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablecellwidth?view=openxml-2.20.0 . Quy cách độ rộng ô là ưu tiên; `tblGrid`, ô gộp và thuật toán layout có thể buộc thay đổi giá trị cuối cùng.
- **[S30] [Technical reference to OOXML]** OOXML Info. *ST_TblLayoutType*, fixed và AutoFit, minimum/maximum content widths: https://ooxml.info/docs/17/17.18/17.18.87/ ; *AutoFit Tables*: https://ooxml.info/docs/l/l.1/l.1.5/l.1.5.7/ . Trang giải thích tiêu chuẩn, **không phải văn bản quy định Việt Nam**; dùng để đối chiếu kỹ thuật, không tuyên bố đây là source code thuật toán Word.
- **[S31] [Official Word]** Microsoft Support. *Resize a table, column, or row*, AutoFit Contents/Window và Fixed Column Width: https://support.microsoft.com/en-us/word/resize-a-table-column-or-row .
- **[S32] [W3C Web/CSS]** W3C. *CSS Table Module Level 3*, khái niệm min-content/max-content và phân phối available width: https://www.w3.org/TR/css-tables-3/ . **Cảnh báo:** áp dụng cho CSS/Web, chỉ tham khảo nguyên lý; không phải thuật toán DOCX.
- **[S33] [UX research]** Nielsen Norman Group. *Data Tables: Four Major User Tasks*: https://www.nngroup.com/articles/data-tables/ . Tầm quan trọng cột đầu giúp định danh, thứ tự cột theo tác vụ, nhóm cột liên quan.
- **[S34] [US government UX]** U.S. Department of Veterans Affairs. *Table – VA.gov Design System*: https://design.va.gov/components/table . Xác định các cột quan trọng với người dùng và ưu tiên thông tin, nhất là màn hình hẹp; không tự suy thành quy định Word Việt Nam.
- **[S35] [Mature OSS pattern]** Textualize. *Rich table source* (`min_width`, `max_width`, `ratio`, wrap and column measurement): https://github.com/Textualize/rich/blob/main/rich/table.py ; giấy phép **MIT** trong https://github.com/Textualize/rich/blob/main/pyproject.toml . Áp dụng cho terminal, không phải engine Word.
- **[S36] [Mature OSS pattern]** PrettyTable. *Repository/README* và các tham số `max_width`, `min_width`, `align`: https://github.com/prettytable/prettytable ; giấy phép **BSD-3-Clause**: https://github.com/prettytable/prettytable/blob/main/pyproject.toml . Không cần tích hợp vào ứng dụng DOCX.
- **[S37] [Government content guidance]** UK Government Analysis Function. *Writing about data*: https://analysisfunction.civilservice.gov.uk/policy-store/writing-about-data/ . Trình bày thông tin quan trọng trước, gắn bảng với thông điệp, cấu trúc dễ quét.
- **[S38] [Mature OSS table model]** python-docx. *Working with Tables – layout grid, merged cells, omitted cells*: https://github.com/python-openxml/python-docx/blob/master/docs/user/tables.rst . Cần giữ ô vật lý thực khi tối ưu, không suy ra số ô từ ma trận phẳng.
- **[S39] [Official Microsoft accessibility]** Microsoft Support. *Make your Word documents accessible to people with disabilities*: https://support.microsoft.com/en-us/accessibility/word/make-your-word-documents-accessible-to-people-with-disabilities . Nhắc cần thận trọng với bảng fixed-width về accessibility, đặc biệt khi đọc màn hình nhỏ/phóng to.
- **[S40] [US government design]** U.S. Web Design System. *Table component*: https://designsystem.digital.gov/components/table/ . Nguyên tắc đơn giản, tiêu đề rõ, giá trị số được căn phải, định dạng nhất quán; chỉ tham khảo trình bày.


### Nguồn đối chiếu bổ sung cho V4 — quyết định theo hàng/trang và chứng cứ render (20/10/2026)

- **[S41] [Official OOXML]** Microsoft Learn. *TableCellWidth (`w:tcW`)* — chiều rộng ưu tiên, có thể bị thay đổi bởi grid/layout: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablecellwidth?view=openxml-2.20.0 ; *TableWidth (`w:tblW`)*: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablewidth?view=openxml-3.0.1 . Đây là nguồn kỹ thuật WordprocessingML, không phải tiêu chuẩn pháp lý Việt Nam.
- **[S42] [Official Word]** Microsoft Support. *Resize a table, column, or row* — AutoFit Contents, AutoFit Window, Fixed Column Width, Cell Margins: https://support.microsoft.com/en-us/word/resize-a-table-column-or-row .
- **[S43] [Official OOXML]** Microsoft Learn. *Working with WordprocessingML tables* — `tblPr`, `tblGrid`, `tr`, `tc`: https://learn.microsoft.com/en-us/office/open-xml/word/working-with-wordprocessingml-tables ; *TableGrid*: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablegrid?view=openxml-3.0.1 ; *VerticalMerge*: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.verticalmerge?view=openxml-3.0.1 .
- **[S44] [Official Word]** Microsoft Support. *Repeat table header on subsequent pages* — chỉ lặp trên ngắt trang tự động, phải chọn hàng đầu và xem ở Print Layout: https://support.microsoft.com/en-gb/word/repeat-table-header-on-subsequent-pages ; Microsoft Learn. *TableHeader (`tblHeader`)* — các hàng tiêu đề phải liền kề đầu bảng: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tableheader?view=openxml-3.0.1 .
- **[S45] [UX research]** Nielsen Norman Group. *Data Tables: Four Major User Tasks* — tác vụ đọc, vai trò định danh hàng và ưu tiên vị trí cột: https://www.nngroup.com/articles/data-tables/ . Dùng tham khảo về UX, **không phải lý do hợp lệ để tự sắp xếp lại cột bảng hành chính**.
- **[S46] [Official OOXML]** Microsoft Learn. *Introduction to markup compatibility* — `mc:AlternateContent`, xử lý nhánh tương thích có thể thay đổi dữ liệu khi ghi lại: https://learn.microsoft.com/en-us/office/open-xml/general/introduction-to-markup-compatibility . Khi thao tác format-only cần chú ý các cấu trúc tương thích chưa hiểu, không tự tiền xử lý rồi loại bỏ nhánh gốc.
- **[S47] [Government best practice]** UK Government Analysis Function. *Data visualisation: tables* — căn phải số liệu, trình bày tên bảng, mức chính xác và cân đối độ rộng các cột: https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-tables/ . Đây là hướng dẫn nghiệp vụ, không phải quy chuẩn bắt buộc của Việt Nam.
- **[S48] [W3C kỹ thuật web — tham khảo nguyên lý, không phải layout DOCX]** W3C. *CSS Table Module Level 3* — min-content, max-content, nhiều cột và phân phối width: https://www.w3.org/TR/css-tables-3/ . Không sao chép công thức CSS trực tiếp thành thuật toán Word; tiêu chuẩn có ghi chú biên tập ở các phần kỹ thuật.
- **[S49] [Nguồn pháp lý đang áp dụng]** Cổng Văn bản Chính phủ, *Nghị định 30/2020/NĐ-CP*: https://vanban.chinhphu.vn/default.aspx?docid=199378&pageid=27160 ; Cổng Tư liệu–Văn kiện Đảng, *Quy định 399-QĐ/TW*: https://tulieuvankien.dangcongsan.vn/he-thong-van-ban/van-ban-cua-dang/quy-dinh-so-399-qd-tw-ngay-09-01-2026-cua-ban-bi-thu-ve-the-loai-tham-quyen-ban-hanh-va-the-thuc-van-ban-cua-dang.html ; *Hướng dẫn 05-HD/VPTW*: https://tulieuvankien.dangcongsan.vn/van-ban-cua-dang/huong-dan-so-05-hd-vptw-ngay-27-5-2026-cua-van-phong-trung-uong-dang-ve-the-thuc-va-ky-thuat-trinh-bay-van-ban-cua-dang.html .


### Nguồn đối chiếu bổ sung V5 — hợp đồng quyết định và kiểm định kết xuất (20/10/2026)

- **[S50] [Văn bản Đảng chính thức]** Văn phòng Trung ương Đảng, *Hướng dẫn số 05-HD/VPTW ngày 27/05/2026*, Phần II.IV.4.1–4.3 về lề trang một/hai mặt, xoay ngang bảng; Phụ lục 2 về cỡ chữ theo thành phần. Bản PDF trên Cổng Tư liệu–Văn kiện Đảng: https://tulieuvankien.dangcongsan.vn/upload/2006988/20260529/HD_05_VPTW_e1550.pdf . Nguồn pháp lý, không suy ra định mức riêng cho viền/width mọi ô bảng.
- **[S51] [Official Microsoft OOXML]** Microsoft Learn, *Working with WordprocessingML tables*: https://learn.microsoft.com/en-us/office/open-xml/word/working-with-wordprocessingml-tables . Cấu trúc `tbl/tblPr/tblGrid/tr/tc` và các thuộc tính bảng, dùng xây/kiểm topology.
- **[S52] [Official Microsoft OOXML]** Microsoft Learn, *TableLayoutValues Enum* (`fixed`, `autofit`): https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablelayoutvalues?view=openxml-3.0.1 . Đặc điểm cấu hình dàn bảng; không phải xác nhận Word sẽ render đúng mọi đề xuất width.
- **[S53] [Official Microsoft OOXML]** Microsoft Learn, *Introduction to markup compatibility*: https://learn.microsoft.com/en-us/office/open-xml/general/introduction-to-markup-compatibility . Cảnh báo preprocessing và lưu lại chỉ giữ markup còn lại sau khi xử lý; cần giữ `AlternateContent` khi can thiệp format-only.
- **[S54] [Official Microsoft OOXML]** Microsoft Learn, *Accept all revisions in a word processing document*: https://learn.microsoft.com/en-us/office/open-xml/word/how-to-accept-all-revisions-in-a-word-processing-document . Ví dụ về các phần tử sửa đổi, di chuyển và xóa; dùng để xác định rủi ro khi thao tác tài liệu có Track Changes, **không đề nghị tự chấp nhận sửa đổi**.
- **[S55] [Official Microsoft Word]** Microsoft Support, *Repeat table header on subsequent pages*: https://support.microsoft.com/en-gb/word/repeat-table-header-on-subsequent-pages . Yêu cầu chọn từ hàng đầu, chỉ hiện Print Layout/in, giới hạn ở ngắt trang tự động.
- **[S56] [U.S. government accessibility guidance]** Section508.gov, *Data Tables in Microsoft Word, PowerPoint, Excel, and PDFs*: https://www.section508.gov/blog/accessibility-bytes/data-tables-in-documents/ . Word và tagged PDF cần quy trình đánh giá riêng, không coi thiết lập header Word tương đương thẻ bảng PDF; đây là best practice tham khảo, không phải quy phạm Việt Nam.
- **[S57] [Official Microsoft Accessibility]** Microsoft Support, *Make your Word documents accessible to people with disabilities*: https://support.microsoft.com/en-us/accessibility/word/make-your-word-documents-accessible-to-people-with-disabilities . Khuyến nghị bảng đơn giản, tiêu đề rõ, xem trên nhiều thiết bị; ưu tiên accessibility không đồng nghĩa được phép phá biểu mẫu được ban hành.

### Nguồn đối chiếu bổ sung V6 — hiệu chỉnh, benchmark, chữ ký số, và giới hạn nghiệm thu (20/10/2026)

- **[S58] [Official Microsoft OOXML]** Microsoft Learn, *How to: Validate a word processing document*. Open XML SDK xác nhận validation tài liệu theo schema, không đồng nghĩa kiểm được layout/rasterization thực tế: https://learn.microsoft.com/en-us/office/open-xml/word/how-to-validate-a-word-processing-document
- **[S59] [Official Microsoft]** Microsoft Support, *Add or remove a digital signature for Microsoft 365 files*. Word đánh dấu file đã ký số ở trạng thái chỉ đọc nhằm tránh thay đổi; không xử lý làm mất chữ ký với tác vụ format-only: https://support.microsoft.com/en-us/office/security-privacy/add-or-remove-a-digital-signature-for-microsoft-365-files
- **[S60] [W3C informative note]** W3C, *Guidance on Applying WCAG 2 to Non-Web ICT (WCAG2ICT)*, Group Note 11/12/2025. Phân biệt nguyên tắc accessibility ngoài web và chuẩn bắt buộc; ví dụ reflow với dữ liệu dạng bảng: https://www.w3.org/TR/wcag2ict/ và bản giải thích https://www.w3.org/WAI/standards-guidelines/wcag/non-web-ict/
- **[S61] [Official Microsoft Word]** Microsoft Support, *Repeat table header on subsequent pages*. Header chỉ lặp khi Word tự ngắt trang phù hợp, không tự lặp với manual page break trong bảng: https://support.microsoft.com/en-gb/word/repeat-table-header-on-subsequent-pages
- **[S62] [Official Microsoft OOXML]** Microsoft Learn, *TableWidth Class*, `w:tblW` là preferred width, chịu tác động `tblGrid`, cell width và layout algorithm: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablewidth?view=openxml-3.0.1
- **[S63] [Mature OSS technical documentation]** `python-docx` 1.2.0, *Working with Tables*. Các tình huống merged cells, omitted cells và nested tables dẫn đến sự khác biệt giữa grid và ô vật lý: https://python-docx.readthedocs.io/en/latest/user/tables.html
- **[S64] [Mature OSS API documentation]** `python-docx` 1.2.0, *Table objects*: gán `cell.text` thay nội dung hiện hữu bằng paragraph/run mới, cần tránh trong tác vụ format-only: https://python-docx.readthedocs.io/en/stable/api/table.html
- **[S65] [Official Microsoft Accessibility]** Microsoft Support, *Make your Word documents accessible to people with disabilities*, khuyến nghị bảng đơn giản, header rõ, hạn chế gộp/lồng bảng khi thiết kế mới. Không được dùng khuyến nghị này để tự tháo biểu mẫu chính thức: https://support.microsoft.com/en-gb/accessibility/word/make-your-word-documents-accessible-to-people-with-disabilities

**Ghi chú về phạm vi nguồn:** [S58]–[S65] là cơ sở kỹ thuật, best practice và tài liệu khả năng tiếp cận; **không** đặt thêm yêu cầu thể thức pháp lý Việt Nam. Những ngưỡng lợi ích, tỷ lệ fixture, thứ tự xếp ứng viên và rubric trong V6 là **đề xuất cần hiệu chỉnh**.

### Nguồn đối chiếu bổ sung V7 — hành vi Word, ưu tiên width, style, đường viền và phân trang (20/10/2026)

- **[S66] [Microsoft Support – official]** *Set or change table properties*: preferred width, table alignment/indent, wrapping, row, cell margins/spacing và border/shading. https://support.microsoft.com/en-us/office/security-privacy/set-or-change-table-properties . Dùng đối chiếu phương án reuse Word UI/capabilities; không là quy chuẩn thể thức Việt Nam.
- **[S67] [Microsoft Support – official]** *Resize a table, column, or row*: AutoFit Contents, AutoFit Window, Fixed Column Width, Cell Margins. https://support.microsoft.com/en-us/word/resize-a-table-column-or-row . Nêu hành vi Word native; không bảo đảm width được suy đoán bằng mm sẽ được render đúng với mọi file.
- **[S68] [Microsoft Support – official]** *Set table cells to expand with contents in Word*: row height Exact có thể ngăn ô tự mở rộng; dùng At least khi phù hợp. https://support.microsoft.com/en-gb/word/set-table-cells-to-expand-with-contents-in-word . Mẫu chính thức khóa chiều cao vẫn phải ưu tiên bảo toàn.
- **[S69] [Microsoft Learn – official OOXML]** `TableLook`: table-style conditional formatting cho first/last row/column và banding. https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablelook?view=openxml-3.0.1 .
- **[S70] [Microsoft Learn – official OOXML]** `TableCellProperties`: `tblStylePr` có thể đưa conditional cell properties vào các vùng của bảng. https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablecellproperties?view=openxml-3.0.1 .
- **[S71] [Microsoft Learn – official interoperability]** [MS-OI29500], *Table Cell Borders* (Part 1 §17.4.66): thứ tự tìm viền, xung đột adjacent borders, khác biệt none/nil. https://learn.microsoft.com/en-us/openspecs/office_standards/ms-oi29500/7c791c5d-44c3-4fe8-abdd-8f136761bb93 . Tham khảo thêm ghi chú bản ECMA khác nhau: https://learn.microsoft.com/en-us/openspecs/office_standards/ms-oe376/23213ddc-942c-4535-bda0-7f9b12d8596a .
- **[S72] [Microsoft Learn – official OOXML]** `TableWidth`: `tblW` chỉ là preferred width; width phần trăm theo text extents của page. https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablewidth?view=openxml-3.0.1 .
- **[S73] [Microsoft Learn – official OOXML]** `TableCellWidth`: `tcW` chỉ là preferred width; width phần trăm tương đối với overall table width. https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablecellwidth?view=openxml-2.20.0 .
- **[S74] [Microsoft Learn – official OOXML]** `CantSplit`: không cắt hàng nếu có thể, nhưng hàng dài hơn một trang vẫn có thể chảy qua nhiều trang. https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.cantsplit?view=openxml-3.0.1 .
- **[S75] [Microsoft Learn – official OOXML]** `TableHeader`: các hàng header phải liên tiếp từ đầu bảng để lặp, không phải bất kỳ hàng giữa bảng. https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tableheader?view=openxml-3.0.1 .
- **[S76] [Microsoft Support – official]** *Keep text together in Word*: nonbreaking space và nonbreaking hyphen ảnh hưởng hành vi ngắt dòng. https://support.microsoft.com/en-us/word/keep-text-together-in-word . Không tự thay ký tự trong tác vụ format-only.
- **[S77] [Microsoft Learn – official OOXML]** `BiDiVisual`: bảng có thể hiển thị theo hướng phải-sang-trái ảnh hưởng vị trí thị giác của cells và borders. https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.bidivisual?view=openxml-3.0.1 . V7 khuyến nghị khóa/review những trường hợp khó xác minh, không diễn giải lại thứ tự nội dung.

**Bổ sung nguồn chính thức V8 — quyết định bố cục, đầu vào Word và nghiệm thu**

- **[S78] [Microsoft Learn – official]** *How to: Validate a word processing document*. Open XML SDK có thể kiểm tra lỗi cấu trúc/schema, không phải xác nhận layout đẹp khi in: https://learn.microsoft.com/en-us/office/open-xml/word/how-to-validate-a-word-processing-document
- **[S79] [Microsoft Learn – official]** *About the Open XML SDK for Office*. DOCX là package gồm nhiều part/relationship và Word có nhiều story: https://learn.microsoft.com/en-us/office/open-xml/about-the-open-xml-sdk
- **[S80] [Microsoft Support – official]** *Repeat table header on subsequent pages*. Hàng tiêu đề phải bắt đầu từ hàng đầu; header không lặp với ngắt trang thủ công trong bảng; kiểm ở Print Layout/in: https://support.microsoft.com/en-us/word/repeat-table-header-on-subsequent-pages
- **[S81] [Microsoft Learn – official OOXML]** `TableLayoutValues`: `fixed`/`autofit` của table layout: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablelayoutvalues?view=openxml-3.0.1
- **[S82] [Microsoft Learn – official OOXML]** `CompatSettingNameValues`: thuộc tính `compatibilityMode` và một số chế độ liên quan đến định dạng bảng: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.compatsettingnamevalues?view=openxml-3.0.1
- **[S83] [Microsoft Support – official]** *Benefits of embedding custom fonts*. Thiếu font có thể thay layout; font embedding có điều kiện/giới hạn và không phải bước mặc định của chuẩn hóa bảng: https://support.microsoft.com/en-us/Office/fonts/benefits-of-embedding-custom-fonts
- **[S84] [Microsoft Learn – official OOXML]** `TablePositionProperties`: bảng nổi có thể có `w:tblpPr`: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tableproperties.tablepositionproperties?view=openxml-3.0.1
- **[S85] [Microsoft Learn – official OOXML]** `GridBefore`: một hàng có thể bỏ trống các grid columns trước ô đầu: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.gridbefore?view=openxml-3.0.1
- **[S86] [Microsoft Learn – official OOXML]** `TableCellMargin.StartMargin`: ô có margin hướng bắt đầu, cần xem cascade và Office version: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablecellmargin.startmargin?view=openxml-3.0.1
- **[S87] [Microsoft Learn – official OOXML]** `TableCellProperties.TextDirection`: `w:textDirection` có thể ảnh hưởng cách đo chữ trong ô: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablecellproperties.textdirection?view=openxml-3.0.1
- **[S88] [Microsoft Support – official]** *Make your Word documents accessible to people with disabilities*. Đơn giản hóa bảng khi phù hợp, tránh bảng lồng/phức tạp không cần thiết; không được thay thế mẫu pháp lý: https://support.microsoft.com/en-us/accessibility/word/make-your-word-documents-accessible-to-people-with-disabilities
- **[S89] [Microsoft Learn – official OOXML]** `Table` element (`w:tbl`) — chú giải về trường hợp hai bảng có cùng style đứng liền nhau có thể được xem như một bảng: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.table?view=openxml-2.20.0
- **[S90] [Unicode Consortium – UAX #14, bản cập nhật 01/09/2026]** *Unicode Line Breaking Algorithm*. Quy định các cơ hội ngắt dòng mặc định, phân biệt cơ hội ngắt với quyết định dàn dòng thực tế: https://www.unicode.org/reports/tr14/
- **[S91] [Unicode Consortium – UAX #29, bản cập nhật 01/09/2026]** *Unicode Text Segmentation*. Định nghĩa extended grapheme cluster, không đồng nhất số code point với ký tự người đọc cảm nhận: https://www.unicode.org/reports/tr29/
- **[S92] [Microsoft Support – official Word]** *Show or hide gridlines for all tables in a document*. View Gridlines là đường lưới hỗ trợ chỉnh sửa, khác đường viền bảng và không in ra: https://support.microsoft.com/en-us/word/show-or-hide-gridlines-for-all-tables-in-a-document
- **[S93] [Microsoft Learn – official Open XML SDK]** *Open XML SDK for Office design considerations*. SDK không cung cấp chức năng dàn trang như Word, không thay Office Object Model và bản thân việc dùng SDK không bảo đảm tính hợp lệ của tài liệu: https://learn.microsoft.com/en-us/office/open-xml/open-xml-sdk-design-considerations

**Giới hạn của nguồn [S78]–[S89]:** đây là tài liệu kỹ thuật/hướng dẫn sản phẩm của Microsoft. Chúng không tạo thêm nghĩa vụ về thể thức văn bản theo pháp luật Việt Nam; không nguồn nào tự xác nhận thuật toán quyết định width, preset thẩm mỹ hoặc 20 ca thử V8 đã được chạy/đạt. Căn cứ pháp lý vẫn theo [S01]–[S06].

**Phạm vi bằng chứng V7:** [S66]–[S77] là hướng dẫn sản phẩm và mô tả định dạng kỹ thuật chính thức. Các mô hình `grid_interval`, `reader_task`, `materiality`, reason code, thuật toán tìm ứng viên và bộ 16 ca thử là **đề xuất thiết kế**, chưa được Microsoft chứng nhận, chưa được thực thi và không phải quy phạm pháp lý của Việt Nam. Không dùng bất kỳ nguồn này để tự thay đổi mẫu biểu chính thức hoặc bỏ qua yêu cầu người dùng duyệt.


**Bổ sung nguồn V11 — quyền áp dụng và giới hạn kỹ thuật/UX của width**

- **[S94] [Microsoft Support — official]** *Resize a table, column, or row*: Word hỗ trợ AutoFit Contents/Window, Fixed Column Width, cell margins và cell spacing. https://support.microsoft.com/en-us/word/resize-a-table-column-or-row
- **[S95] [Microsoft Learn — official]** *TableCellWidth Class*: `w:tcW` là chiều rộng ưu tiên (preferred) trong thuật toán dàn bảng, không phải ràng buộc tuyệt đối. https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablecellwidth?view=openxml-2.20.0
- **[S96] [UK Government Analysis Function — guidance]** *Data visualisation: tables*: phân tách nhãn, đơn vị, số liệu; hướng dẫn căn phải số và không dùng khoảng trắng/hàng trống thay cho cấu trúc. https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-tables/
- **[S97] [Microsoft Learn — official]** *Working with WordprocessingML tables*: `tblGrid`, `gridCol`, `tblPr`, `tcPr` là cấu trúc WordprocessingML cho bảng Word. https://learn.microsoft.com/en-us/office/open-xml/word/working-with-wordprocessingml-tables

Các nguồn [S94]–[S97] **không xác nhận các con số mm của fixture V11** và **không áp đặt kiểu bảng bắt buộc theo pháp luật Việt Nam**. Các số 14–76–38–37 mm và mức giảm 36,37% chỉ là quan sát trong corpus tổng hợp.

- **[S98] [Microsoft Learn — official OOXML]** `CantSplit (w:cantSplit)` — hàng bảng không được chia qua trang nếu vừa một trang; hàng dài hơn một trang vẫn có thể trải trang: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.cantsplit?view=openxml-3.0.1 . Chỉ sử dụng làm căn cứ kỹ thuật, không phải quy định pháp lý về bảng Việt Nam.

- **[S99] [Microsoft Learn — official]** *TableWidth Class — Preferred Table Width*: `tblW` là độ rộng ưu tiên chịu thuật toán dàn bảng, không cam kết đúng số mm trên bản in. https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablewidth?view=openxml-3.0.1
- **[S100] [Microsoft Support — official]** *Resize a table, column, or row*: AutoFit Contents, AutoFit Window, Fixed Column Width và Cell Margins. https://support.microsoft.com/en-us/word/resize-a-table-column-or-row
- **[S101] [Microsoft Support — official]** *Repeat table header on subsequent pages*: giới hạn khi ngắt trang thủ công và yêu cầu tiêu đề bắt đầu từ hàng đầu bảng. https://support.microsoft.com/en-us/word/repeat-table-header-on-subsequent-pages

Các nguồn [S99]–[S101] chỉ cung cấp căn cứ về hành vi Word/OOXML, **không** hợp thức hóa ngưỡng thẩm mỹ 2 mm hoặc chứng minh tính pháp lý của fixture.

**Nguồn chính thức bổ sung V15 — thuật toán bố trí và công cụ Word hiện có**

- **[S102] [Microsoft Learn – official]** *TableWidth (Preferred Table Width)*: độ rộng bảng và ô là giá trị ưu tiên, có thể xung đột với lưới và cách dàn trang; phần trăm bảng căn theo vùng text trang. https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.tablewidth?view=openxml-3.0.1
- **[S103] [Microsoft Support – official]** *Resize a table, column, or row*: cách Word điều chỉnh độ rộng cột, AutoFit Contents/Window và Fixed Column Width, cũng như Cell Margins và Cell Spacing. https://support.microsoft.com/en-us/word/resize-a-table-column-or-row

Hai nguồn chỉ xác nhận khả năng/giới hạn kỹ thuật Microsoft Word/OOXML, không ban hành mức dự phòng 2 mm hoặc yêu cầu pháp lý mới về bảng ở Việt Nam. V15 không có chứng cứ kết xuất Microsoft Word.

### Ghi chú điều chỉnh diễn giải V2

- Đặt hướng dẫn W3C HTML trong vai trò **nguyên lý thiết kế**; không tuyên bố mọi thuộc tính accessibility của bảng HTML đều có tương đương đầy đủ trong Word.
- Phân biệt `Repeat Header Rows` trong Word với kiểm chứng tagged PDF: hai mục tiêu đầu ra có khả năng khác nhau; không tuyên bố một cài đặt đủ cho mọi quy trình.
- Thuộc tính `w:tblW`, `w:tcW` là độ rộng **ưu tiên**, không phải cam kết kích thước luôn cố định.
- Cỡ chữ/giãn dòng của *nội dung chung* không được biến thành định mức cứng của mọi ô bảng nếu quy định hoặc biểu mẫu chưa nêu rõ; phải ghi mức chắc chắn và phạm vi áp dụng.
- Bảng đẹp phải đạt điều kiện bảo toàn, tuân thủ và kiểm chứng kết xuất; tuyệt đối không chỉ dựa trên chấm điểm chủ quan.

# KẾT LUẬN CUỐI CÙNG

**Bổ sung V15 — kiểm tra tái sử dụng ứng viên theo hình học mới:** Khi chỉ tăng tiếp lề phải từ 0 đến 5 mm trên các phương án N1–N4 của V14, có 24/24 DOCX/PDF thử nghiệm. Trong đó chỉ 6/24 đạt hình học danh nghĩa theo lưới và 10/24 còn viền PDF trong lề; **4 trường hợp PDF trông vừa nhưng lưới OOXML vượt vùng nội dung**. Phương án N4 có dự phòng 2,028 mm ở đầu vào và đạt danh nghĩa đến +2 mm nhưng chỉ còn 0,035 mm tại biên; không thể coi đó là chuẩn thẩm mỹ hoặc ngưỡng an toàn chung. **Bắt buộc tính lại khi đổi lề/section; phải kiểm gate hình học trước và gate render sau; Word Print Layout vẫn chưa nghiệm thu.** Xem Phần XXXI, mục 238–248.


**Bổ sung V14 — thực nghiệm refit theo geometry thay đổi:** F07 sau tăng lề có 242,023 mm vùng nội dung nhưng giữ lưới 252,007 mm. Tạo 4 cách chia lại cột để vừa vùng mới; quan sát viền phải ở trong vùng hiển thị (PDF LibreOffice) và không tăng tổng chiều cao bảng so với đối chứng. N1–N4 có cùng chiều cao 45,40 mm tại cỡ chữ gốc và 47,84 mm khi tăng 1 pt; 48/48 nội dung ô được tìm thấy theo heuristic, cấu trúc DOCX không đổi. **Chưa chứng minh cách nào tối ưu thẩm mỹ, chưa kiểm Microsoft Word**. Kết quả tách biệt với 152 ca T01–T152 còn ở mức đặc tả. Xem Phần XXX, mục 226–237.


**Bổ sung V13 — độ bền & cổng hình học:** F03 ứng viên balanced + giữ hàng ngắn cho 4/4/5 trang khi cỡ chữ 14/15/16 pt, so với baseline 6/7/7 trang; F07 ứng viên giữ mức giảm chiều cao khoảng 53,74–54,76% trên các phép thử 13/14/15 pt. Khi tăng lề F07 mỗi bên 5 mm, grid width ~252 mm vượt vùng nội dung ~242 mm nên phải kiểm tra hình học lại trước khi áp dụng. PDF có thể thiếu giả chuỗi cắt qua trang; OOXML chưa mất dữ liệu. 14 PDF thử LibreOffice, chưa chứng nhận Word hay tích hợp formatter.

**Bổ sung V12 — thử nghiệm chéo và phân trang:** F03 từ 6 xuống 4 trang trong LO; phép kết hợp `cantSplit` trên 46 hàng ngắn vẫn 4 trang, có 46 mã bản ghi, 4/4 hàng tiêu đề lặp và 142/142 chuỗi `w:t` được tìm thấy. F07 Balanced giảm từ 98.14 xuống 45.40 mm (53.74%). Các phương án ép cột STT quá nhỏ bị từ chối dù ít trang; F04/F05 không chứng minh lợi ích, F06 giữ mẫu. Có 18 kết xuất PDF thử nghiệm tổng hợp; chưa nghiệm thu Word, chưa tích hợp phần mềm.


**Bổ sung V11 — có thử nghiệm chiều rộng được đo:** F01 cho thấy một ứng viên cân đối giúp bảng thấp hơn 36,37% trong LibreOffice mà vẫn giữ tiêu đề STT nguyên dòng; các phương án quá ưu tiên mô tả bị từ chối do header bị ngắt. F02 là đối chứng NO_OP: đổi width không cải thiện, hoặc làm bảng cao hơn 17,48%. Các ứng viên kiểm tra giữ nguyên chuỗi text và topology WordprocessingML; vẫn chưa có bằng chứng nghiệm thu trên Microsoft Word hay tích hợp processor thực tế.

**Bổ sung V10 — có dữ liệu thử tái lập:** Đã tạo 8 DOCX giả lập, quan sát thử bản in LibreOffice và kiểm tra một cặp F08 `exact → atLeast` sửa lỗi che chữ không đổi nội dung `w:t` trong phạm vi kiểm. Đây chỉ là bằng chứng tổng hợp trên LibreOffice; chưa nghiệm thu Microsoft Word hoặc module ứng dụng. V10 giữ nguyên 152 kịch bản đặc tả, đặt điều kiện đóng khoảng trống bằng corpus/Word renderer/cấp quyền thực tế trước khi bổ sung lý thuyết tiếp.

**Bổ sung V9 — định dạng bảng có chứng cứ in thực tế:** Phân biệt Unicode/grapheme/ngắt dòng và kết quả Word; không nhầm đường lưới soạn thảo với đường viền có thể in; không ép dùng hết chiều ngang trang; chọn độ rộng theo tác vụ đọc, toàn hàng và vùng bị ảnh hưởng, không dựa vào score thẩm mỹ. Tám ca bổ sung T145–T152 nâng tổng số lên 152 ca được **đặc tả, chưa chạy**. Trạng thái nghiệm thu phải ghi đúng oracle đã xác minh.

**Bổ sung V8 — tối ưu đo được và có ngữ cảnh Word:** Cột trọng tâm phải được nhận diện theo tác vụ và kiểm tra khả năng đọc thực tế; không gian bảng phải đúng story, section, container, floating/layout mode và font. Mọi ứng viên tuân theo hard gates G0, xét toàn hàng/bảng và so trên renderer đích, có điều kiện NO_OP_VALID, REVIEW và rollback; thêm 20 ca T125–T144, tổng 144 ca thử được đặc tả. Chưa có bằng chứng engine đã chạy.

**Bổ sung V7 — hợp đồng tối ưu độ rộng có thể kiểm tra:** Ngữ nghĩa cột chỉ được khẳng định theo bằng chứng; ô gộp và ô thiếu được tính trên grid vật lý; định dạng hiệu dụng chịu Table Style và xung đột viền; `tblW/tcW` là width ưu tiên chứ không phải width đã đo. Thuật toán chỉ tìm hữu hạn, giữ baseline, dựa trên render khi kết luận về layout, tạo manifest/rollback và 16 tình huống T109–T124. Chưa thực thi engine.

**Bổ sung V6 — benchmark, hiệu chỉnh và nghiệm thu tái lập:** ứng viên chỉ được xếp hạng sau các hard gates; baseline giữ nguyên luôn là phương án hợp lệ; mức lợi ích phải vượt ngưỡng đã hiệu chỉnh; phân biệt O1 cấu trúc, O2 ngữ nghĩa, O3 render và O4 đánh giá người dùng; không sửa file ký số hoặc biểu mẫu khóa; không chuyển trạng thái đề xuất thành PASS khi chưa có chứng cứ.

**Bổ sung V5 — tối ưu có hợp đồng quyết định và bằng chứng:** xác định người đọc cần gì, giới hạn đổi width từ mẫu/section, mức tin cậy M0–M3, kiểm chứng Word/PDF đúng kênh và giữ nguyên khi không có lợi ích đã được kiểm chứng.

**Bổ sung V4 — tối ưu có kiểm chứng và theo nút thắt hàng/trang:** chỉ chỉnh width khi ứng viên đạt hard gates, có lợi ích đo được so với bản gốc, không tạo hồi quy phân trang/ngoài phạm vi, và phép đo thực tế từ renderer phù hợp. Không đổi width khi chưa cần; ưu tiên thuật toán xác định, tái sử dụng engine hiện có.

**Bổ sung V3 — quyết định độ rộng có ý thức về nội dung trọng tâm:** phải tách `semantic_priority` (mức quan trọng để hiểu/ra quyết định) khỏi `expansion_need` (mức lợi ích thị giác khi cấp thêm mm). Phân bổ có ràng buộc và kiểm chứng renderer; cột ngắn nhưng quan trọng được bảo vệ, cột dài phụ trợ được xuống dòng hợp lý; không phá biểu mẫu.

**Chuẩn hóa bảng đạt chất lượng cao không đồng nghĩa “kẻ viền đồng loạt” hoặc “chỉnh bảng cho đẹp bằng mọi giá”.** Thành phẩm tốt là một bảng **đúng hệ quy định, đúng dữ liệu, dễ đọc, cân đối, có tính thẩm mỹ phù hợp văn bản chính thức, in ổn định và giữ nguyên tính pháp lý/nghiệp vụ của mẫu**.

Đề xuất chọn **Formal Grid – Monochrome** làm phong cách chung khi không có mẫu riêng; bổ sung `Statistical Minimal` cho bảng thống kê và `Preserve Official Form` cho biểu mẫu có cấu trúc cố định. Bộ công cụ xử lý DOCX nên có một engine giữ cấu trúc và provenance, hai cấu hình quy định pháp lý riêng biệt, và một lớp preset thẩm mỹ có xác nhận người dùng. **Bảo toàn nội dung và đúng quy định luôn có ưu tiên cao hơn việc tăng điểm thẩm mỹ.**

*Hết báo cáo — phiên bản 15.0. Cập nhật 21/10/2026. Bảo toàn nghiên cứu V1–V14; Phần XXXI bổ sung 24 biến thể DOCX/PDF F07 về điều kiện hình học và viền PDF. Tổng cộng 31 phần, 248 mục, 152 kịch bản T01–T152 vẫn chỉ được đặc tả, 103 nguồn tham khảo. Chưa nghiệm thu bằng Microsoft Word hoặc tích hợp phần mềm thực tế.*
