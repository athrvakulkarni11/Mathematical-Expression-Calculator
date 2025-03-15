# Mathematical Expression Evaluator

A robust mathematical expression evaluator that supports basic arithmetic operations, parentheses, and decimal numbers. The project includes both a FastAPI backend service and a Streamlit web interface.

## Wanna Try Using Application Without Doing The Setup Here are the Live Demo's 


- **Streamlit Interface**: [https://mathematical-expression-calculator.streamlit.app/](https://mathematical-expression-calculator.streamlit.app/)
- **FASTAPI DEMO**: [https://mathematical-expression-calculator.onrender.com/docs](https://mathematical-expression-calculator.onrender.com/docs)


## Features

- Evaluates mathematical expressions with:
  - Basic arithmetic operations (+, -, *, /)
  - Parentheses support
  - Decimal numbers
  - Negative numbers
- RESTful API endpoint
- User-friendly web interface
- Comprehensive error handling
- Extensive test coverage

## Limitations

- Does not support advanced mathematical functions (sin, cos, log, etc.)
- No support for variables or constants (e.g., pi, e)
- Limited to basic arithmetic operations
- No support for exponents or roots

## Installation


2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

## Running the Application

### FastAPI Backend

1. Start the API server:
```bash
uvicorn src.expression_api:app --reload
```
2. Access the API documentation at: `http://localhost:8000/docs`

### Streamlit Frontend

1. Start the Streamlit application:
```bash
streamlit run src/streamlit_app.py
```
2. Access the web interface at: `http://localhost:8501`

## Testing

### Running Tests

1. Run all tests:
```bash
pytest
```

2. Run tests with coverage:
```bash
pytest --cov=src tests/
```

3. Running Tests with Tox

Tox allows you to test your application across different Python versions. Make sure you have tox installed:
```bash
pip install tox
```

To run tests across all supported Python versions (3.8, 3.9, 3.10, 3.11):
```bash
tox
```



### Test Files

- `tests/test_api.py`: API endpoint tests
- `tests/test_expression_evaluator.py`: Core evaluator tests
- `tests/test_streamlit.py`: Streamlit interface tests

## Project Structure

```
mathematical-expression-evaluator/
├── src/
│   ├── expression_api.py      # FastAPI backend
│   ├── streamlit_app.py       # Streamlit frontend
│   └── streamlit_expression.py # Expression evaluator
├── tests/
│   ├── test_api.py
│   ├── test_expression_evaluator.py
│   └── test_streamlit.py
├── setup.py
├── requirements.txt
├── tox.ini
└── README.md
```

## Video Demonstration

[Insert video demonstration link here]

## API Usage Example

```python
import requests

response = requests.post(
    "http://localhost:8000/evaluate",
    json={"expression": "2 * (3 + 4)"}
)
result = response.json()
print(result)  # {"expression": "2 * (3 + 4)", "result": 14}
```

