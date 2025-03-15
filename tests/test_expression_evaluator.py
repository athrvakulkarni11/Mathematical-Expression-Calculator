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
    ("((2 + 3) * 4) / (1 + 1)", 10),
    ("2 * (-3 + 4)", 2),
    ("(-2) * (-3)", 6),
    ("1 + 2 + 3 + 4 + 5", 15),
    ("1 * 2 * 3 * 4 * 5", 120),
    ("10 - 5 - 3", 2),
    ("10 / 2 / 2", 2.5),
    ("0.1 + 0.2", 0.3),
    ("(1 + 2) * (3 + 4) * (5 + 6)", 231),
    ("-(-3)", 3),
    ("2.5 * (3.0 + 4.5)", 18.75),
    ("0.1 * (0.2 + 0.3)", 0.05),
    ("(1 + 2 + 3) * (4 + 5 + 6)", 90),
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
    "((2 + 3)",
    "2 + + 2",
    "3 ** 2",
    ".5 + 2",
    "2 * ()",
    "2 * ((3 + 4)",
    "2 * (3 + 4))",
    "2 / (3 - 3)",
    "2..5",
    "2 + 3 + ",
])
def test_invalid_expressions(evaluator, expression):
    with pytest.raises((ValueError, ZeroDivisionError)):
        evaluator.parse_expression(expression) 