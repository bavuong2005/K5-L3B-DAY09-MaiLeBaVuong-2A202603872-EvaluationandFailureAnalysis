# Trace case: từ trace tới quyết định sai đầu tiên

Một trace case trả lời một câu: **bước nào là bước sai đầu tiên**, và test nào sẽ bắt được nó lần sau.

```bash
cd src
python -m lab9.trace_case --shape seeded_regression --claim C-002 --seed 11
python -m lab9.trace_case --shape fixed --claim C-002 --seed 11   # đối chứng
```

Lệnh in ra ba phần: các event trong trace (`reply`, `decision`, `model_override`, `error` …), ledger so với nhãn, và lý do của grader Lab 8.

## Mẫu điền (mỗi nhóm 1 case, lấy từ trial đang fail trong report)

| Trường | Nội dung |
|---|---|
| Trial | `seeded_regression C-002@11`; report `E-seeded_regression-20261118-91ab` trong `reports/eval_seeded_regression.json` |
| Triệu chứng | Grader Lab 8: `FAIL (status resolved != denied)`. Reply báo đã hoàn 20.000đ; ledger ghi 20.000đ và 1 refund, trong khi nhãn yêu cầu `denied`, 0đ, 0 refund. Reply khớp ledger nhưng cả hai sai nhãn. |
| Bước sai đầu tiên | Event 3: `model_override {"delay_days": 5}`. |
| Vì sao là bước *đầu tiên* | Event 1 `handoff` chỉ cấp tool đọc; event 2 `investigator` tra order O-202, DB ghi `delay_days=2`. Event 3 thay dữ kiện này bằng số ngày do ticket nói; event 4 mới tạo quote 20.000đ. |
| Failure mode | FM-03 `ticket_trust`; hậu quả là refund sai. |
| Đối chứng | `fixed C-002@11` không có `model_override`; event 3 là quote 0đ `no_entitlement`, event 4 reply từ chối. Ledger 0đ/0 refund và grader Lab 8 PASS. |
| Regression test | `tests/test_lab9_trace_case_regression.py`: cùng claim/seed, xác nhận variant lỗi có override đầu tiên ở event 3 và fail nhãn; `fixed` không override, đúng ledger/nhãn và pass. |
| Chưa chắc chắn | Trace chỉ chứng minh đường chạy MockLLM cho claim/seed này; không chứng minh tỷ lệ lỗi trên người dùng hay model thật. |

## Quy tắc

- Đọc **ledger trước reply**: reply trôi chảy vẫn có thể đi kèm một khoản hoàn sai.
- "Bước sai đầu tiên" phải dẫn số event cụ thể, không phải "agent bị nhầm".
- Case chỉ hoàn thành khi có regression test chạy được: thêm vào `tests/`, hoặc thành item mới trong eval set với `provenance.from_trace`.
