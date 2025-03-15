import pytest
from src.streamlit_expression import ExpressionEvaluator
from streamlit.testing.v1 import AppTest

def test_streamlit_input():
    at = AppTest.from_file("src/streamlit_expression.py")
    at.run()
    
    # Test input widget exists
    assert at.text_input[0].value == "2 * (3 + 4)"
    
    # Test example expressions are displayed
    assert len(at.code) >= 6  # Should have at least 6 example expressions

def test_streamlit_evaluation():
    at = AppTest.from_file("src/streamlit_expression.py")
    
    # Run the app first
    at.run()
    
    # Set input and click evaluate
    at.text_input[0].input("2 + 2").run()
    at.button[0].click().run()
    
    # Check success message
    assert "Result: 4" in at.success[0].value 