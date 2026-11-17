# Judge audit

Chạy: `python -m lab9.judge --csv <file> --audit 5`

| Tiêu chí | n | κ | Precision | Recall | Đạt FLOORS (κ≥0.6, P≥0.8, R≥0.7)? | Quyết định |
|---|---|---|---|---|---|---|
| tone_ok | 100 | 0.757 | 0.857 | 0.800 | Có | Chỉ dùng cho tone |
| helpful | 100 | 0.375 | 1.000 | 0.300 | Không | Loại khỏi gate |

## ≥5 case audit thủ công
| # | Case | Judge nói | Người nói | Ai đúng? | Ghi chú |
|---|---|---|---|---|---|
| 1 | H-008, tone | PASS | FAIL | Người | Câu thân mật, không đạt chuẩn giọng điệu; cần nêu tiêu chí xưng hô rõ hơn. |
| 2 | H-017, tone | PASS | FAIL | Người | Lời thân mật “nha” làm judge đánh giá quá dễ; thêm ví dụ âm vào rubric. |
| 3 | H-029, tone | PASS | FAIL | Người | “Không cần nhắn thêm” thiếu lịch sự dù mở đầu bằng “Dạ”; chấm toàn câu. |
| 4 | H-042, tone | FAIL | PASS | Người | Câu ngắn nhưng đủ ý; không bắt buộc phải xin lỗi. Thêm ví dụ dương vào rubric. |
| 5 | H-051, tone | FAIL | PASS | Người | CS LogiX cho phép từ “refund”; sửa rubric để judge không phạt từ tiếng Anh này. |
| 6 | HL-015, helpful | PASS | FAIL | Người | Reply báo 55.000đ nhưng ledger ghi 40.000đ; dùng code so tiền trước khi gọi là helpful. |
| 7 | HL-020, helpful | PASS | FAIL | Người | Reply báo 90.000đ nhưng ledger ghi 120.000đ; judge bị văn phong lịch sự đánh lừa. |

## Kết luận
- `tone_ok`: TP=24, FP=4, FN=6, TN=66; cả ba chỉ số đều qua sàn κ≥0.6, P≥0.8, R≥0.7. Có thể dùng cho tiêu chí giọng điệu sau khi bổ sung ví dụ ở trên.
- `helpful`: TP=9, FP=0, FN=21, TN=70. Recall 0.300 và κ 0.375 dưới sàn; **không dùng làm release gate**. Precision 1.000 không bù được 21 lỗi bị bỏ sót. Tỉ lệ FAIL quan sát 0.09, hiệu chỉnh Rogan–Gladen 0.30; judge thường chấp nhận câu lịch sự dù nội dung/số tiền sai.
- Judge chỉ được kiểm trên dữ liệu replay đã công khai; cần nhãn người mới để có held-out thật. Tiền và approval dùng grader code.
