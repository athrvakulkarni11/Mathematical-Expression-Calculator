import pytest
from src.streamlit_expression import ExpressionEvaluator

@pytest.fixture
def evaluator():
    return ExpressionEvaluator()

@pytest.mark.parametrize("expression,expected", [
    ("2 + 2", 4),
    ("3 * 4", 12),
    ("10 / 2", 5),
    ("2 * (3 + 4)", 14),
    ("(3 + 5) * (2 - 1) / 4", 2),
    ("-5 + 10", 5),
    ("3.5 + 2.7", 6.2),
])
def test_valid_expressions(evaluator, expression, expected):
    result = evaluator.parse_expression(expression)
    assert abs(result - expected) < 1e-10

@pytest.mark.parametrize("expression", [
    "2 + ",
    "* 3",
    "2 * (3 + 4",
    "10 / 0",
    "2 + a",
])
def test_invalid_expressions(evaluator, expression):
    with pytest.raises((ValueError, ZeroDivisionError)):
        evaluator.parse_expression(expression) 