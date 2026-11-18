"""A wrong quote must be visible even when the host prevents a refund."""

import pytest
from pydantic_evals.evaluators import EvaluatorContext

from lab9.graders import ProposalAmountCorrect

pytestmark = pytest.mark.student


def _context(proposal: int) -> EvaluatorContext:
    return EvaluatorContext(
        name="C-013", inputs={}, metadata=None,
        expected_output={"proposal_amount": 35_000, "refund_vnd": 0},
        output={"result": {"proposal_amount": proposal},
                "snapshot": {"refund_vnd": 0, "refund_count": 0}},
        duration=0.0, _span_tree=None, attributes={}, metrics={},
    )


def test_proposal_grader_catches_wrong_quote_with_correct_ledger() -> None:
    grader = ProposalAmountCorrect()
    assert grader.evaluate(_context(0)).value is False
    assert grader.evaluate(_context(35_000)).value is True
