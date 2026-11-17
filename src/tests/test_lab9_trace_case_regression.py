"""Regression evidence for the first wrong step in C-002@11."""

from lab9.trace_case import investigate


def test_ticket_fact_override_precedes_wrong_refund() -> None:
    bad = investigate("seeded_regression", "C-002", 11)
    good = investigate("fixed", "C-002", 11)

    bad_trial = bad["trial"]
    good_trial = good["trial"]
    assert bad_trial["events"][2]["kind"] == "model_override"
    assert bad_trial["events"][2]["payload"]["delay_days"] == 5
    assert not bad_trial["lab8_pass"]
    assert bad_trial["snapshot"]["refund_vnd"] == 20_000
    assert bad_trial["snapshot"]["refund_count"] == 1

    assert all(event["kind"] != "model_override" for event in good_trial["events"])
    assert good_trial["lab8_pass"]
    assert good_trial["snapshot"]["refund_vnd"] == 0
    assert good_trial["snapshot"]["refund_count"] == 0
