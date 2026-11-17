# Bonus — đối chiếu grader với Inspect AI

`src/scripts/bonus_eval_compare.py` chuyển ba grader code `ApprovalBypass`, `RefundAmountCorrect`, `SecretLeak` sang custom scorer của Inspect AI (`TaskState`, `Target`, `Score`). Logic hai phía nhận cùng trial và label; không gọi model hay API.

Chạy từ `src/`:

```bash
python -m pip install -r requirements.txt -r requirements-lab9.txt -r requirements-bonus.txt
python -m scripts.bonus_eval_compare
```

Kết quả trên Inspect AI 0.3.290 và pydantic-evals 2.68.0:

| Grader | Kết quả khớp |
|---|---:|
| ApprovalBypass | 8/8 |
| RefundAmountCorrect | 8/8 |
| SecretLeak | 8/8 |
| **Tổng** | **24/24 (100%)** |

Sáu vector tự dựng kiểm ca sạch, refund thiếu approval, ledger có dòng claim khác, số tiền sai, secret lọt và từ chối đúng. Hai vector còn lại lấy từ trace thật `seeded_regression C-002@11` và `fixed C-002@11`. Sự khớp trên tám ca này xác nhận phép chuyển đổi cho các nhánh đã thử; không chứng minh tương đương trên mọi đầu vào. Tài liệu API dùng: [Inspect AI Custom Scorers](https://inspect.aisi.org.uk/custom-scorers.html).
