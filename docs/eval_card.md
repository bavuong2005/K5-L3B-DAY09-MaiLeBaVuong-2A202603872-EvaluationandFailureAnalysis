# Eval card — LogiX-VN refund agent

Card này đi kèm report và được dùng lại ở Day 10. Các số dưới đây lấy từ `lab9.eval` và `lab9.gate`, chạy trên eval set v1 ngày 18/11/2026. Không thay số trong report bằng tay.

- **Run ID / eval set SHA:** baseline `E-swarm-20261118-91ab`; `fixed` `E-fixed-20261118-91ab`; regression `E-seeded_regression-20261118-91ab`; SHA `91abb4caf475`.
- **Phiên bản:** eval set v1; metric spec `1.1`; seeds `11,22,33,44,55`. Commit code/grader: xem commit chứa card này.
- **Eval set:** 14 item × 5 seed = 70 trial/shape, nguồn `lab8_public`; nhãn riêng ở `data/eval/labels_v1.json`.
- **Metric blocking v1:** `approval_bypass=0`, `secret_leak=0`, `refund_amount_correct≥0.95`, `proposal_amount_correct≥0.95`, `reply_amount_correct≥0.95`, `pass_rate≥0.85`; các metric capability này không được giảm có ý nghĩa theo paired bootstrap. `db_fact_kept`, `pass_5`, `cost_per_success` chỉ theo dõi hoặc cảnh báo theo spec.

| Metric | Baseline swarm | Fixed | Seeded regression |
|---|---:|---:|---:|
| approval_bypass | 0 | 0 | 0 |
| secret_leak | 0 | 0 | 0 |
| db_fact_kept | 0.9857 | 1.0000 | 0.9286 |
| refund_amount_correct | 0.9857 | 1.0000 | 0.8571 |
| proposal_amount_correct | 0.9857 | 1.0000 | 0.7857 |
| reply_amount_correct | 1.0000 | 1.0000 | 0.7857 |
| pass_rate | 0.9857 | 1.0000 | 0.7143 |
| pass_5 | 0.9286 | 1.0000 | 0.7143 |
| cost_per_success (VND mô phỏng) | 49.5670 | 48.7157 | 81.2020 |

**Paired gate:** `fixed` exit 0. Với `seeded_regression`, `pass_rate` Δ = −0.271, CI 95% [−0.500, −0.057], nên gate exit 1; `refund_amount_correct`, `proposal_amount_correct` và `reply_amount_correct` cũng dưới ngưỡng. `lab9.mutation --detect`: 100% phát hiện trace lỗi, 0% báo nhầm trên `fixed`. Baseline và hai variant dùng cùng eval-set SHA và seed set.

- **Judge:** `tone_ok` κ=0.757, P=0.857, R=0.800, qua floors; `helpful` κ=0.375, P=1.000, R=0.300, bị loại khỏi gate. Xem `docs/judge_audit.md`.
- **Trace case:** `docs/trace_case.md`, C-002@11; event 3 ghi đè số ngày DB bằng số từ ticket. Regression test: `tests/test_lab9_trace_case_regression.py`.
- **Gate owner:** chủ repo Day 9 / người mở PR xử lý khi exit 1; cần sửa nguyên nhân, chạy lại eval và lưu output trong PR.
- **Phạm vi pilot:** claim hoàn phí vận chuyển LogiX-VN trong bộ synthetic công khai; đánh giá offline bằng MockLLM trên 14 item.
- **Giới hạn:** chưa có người dùng thật hay model thật; CI trên 14 item rộng nên chỉ có sức bắt regression đủ lớn. Judge replay dùng CSV công khai, chưa có nhãn held-out mới; cost chỉ là giá mô phỏng.
- **Tăng eval-set version:** khi thêm item từ trace hoặc adversarial pack, tạo v2 và sinh baseline mới; khi đổi metric/ngưỡng, tăng metric-spec version và ghi lý do trong PRD.

## Eval set v2 — Advanced / Expert

- **Baseline:** `E-swarm-20261118-0f49`, eval-set SHA `0f49c028e9be`, 28 item × 5 seed, metric spec 2.1. V2 là v1 cộng adversarial pack; `evalset --v2 --build` báo 0 problem.
- **Baseline metrics:** `pass_rate=0.9786`, `pass_hat_5=0.8929`, `refund_amount_correct=0.9786`, `proposal_amount_correct=0.9786`, `reply_amount_correct=1.0000`, `approval_bypass=0`, `secret_leak=0`.
- **A/A:** so seeds `11,22,33,44,55` với `66,77,88,99,110` trên cùng swarm MockLLM, Δ=0 ở mọi metric, kể cả `pass_hat_5`. Sàn blocking `pass_hat_5≥0.80` nằm dưới baseline 0.8929 và ngoài dải nhiễu A/A quan sát được. Với LLM thật, dải này có thể khác 0 và cần đo lại trước khi đặt sàn.
- **Slices:** `money_movement` chặn `slice_regression`: pass rate của slice là 0.8500 so với baseline 1.0000, CI của Δ [−0.300, 0.000] chạm 0 nên riêng phép thử ý nghĩa không chặn; sàn slice 0.90 chặn. Sàn 0.85 trong chỉ dẫn ban đầu bằng đúng giá trị lỗi và sẽ cho lỗi lọt. `adversarial` có sàn 0.85 để theo dõi các ca tấn công; `denial` có sàn 0.90.
- **Scorecard:** `seeded_regression`, `slice_regression`, `flaky_regression` đều bị chặn (3/3); `fixed` và `honest_refactor` được merge (0 báo nhầm). `flaky_regression` bị chặn bởi `pass_hat_5` cùng các metric khác.
- **Integrity:** bốn trap công khai `evaluator_errors_as_nan`, `dropped_failing_rows`, `cherry_picked_seeds`, `loosened_spec` đều bị chặn; `lab9.traps` exit 0.
- **Giới hạn:** 5 seed không đảm bảo bắt ổn định bug chỉ xuất hiện ở khoảng 1/3 seed. Variant/trap ẩn và dữ liệu người dùng thật chưa được kiểm trong card này.
