# Mathematical Expression Evaluator

A robust mathematical expression evaluator that supports basic arithmetic operations, parentheses, and decimal numbers. The project includes both a FastAPI backend service and a Streamlit web interface.

## Wanna Try Using Application Without Doing The Setup Here are the Live Demo's 


- **Streamlit Interface**: [https://mathematical-expression-calculator.streamlit.app/](https://mathematical-expression-calculator.streamlit.app/)
- **FASTAPI DEMO**: [https://mathematical-expression-calculator.onrender.com/docs](https://mathematical-expression-calculator.onrender.com/docs)
## Video Demonstration
- **Video Demo**: [https://drive.google.com/file/d/1N6spOJXYPlDGmpWpvclJbaJvzBJ06YeL/view?usp=sharing](https://drive.google.com/file/d/1N6spOJXYPlDGmpWpvclJbaJvzBJ06YeL/view?usp=sharing)

### GITHUB REPO FOR VISUALIZATION OF README AND CODE :
- **Git hub Repo**: [https://github.com/athrvakulkarni11/Mathematical-Expression-Calculator.git](https://github.com/athrvakulkarni11/Mathematical-Expression-Calculator.git)

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

## Installation (make sure you have python installed in your system)


2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
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

### Directly With Streamlit 

1. Directly With Streamlit:
```bash
streamlit run src/streamlit_expression.py
```
2. Access the web interface at: `http://localhost:8501`

### Basic Functionality

1. Run The Basic Logic of The Code
```bash
python src/test.py
```

## Testing

### Running Tests

1. Running Tests with Tox

Tox allows you to test your application across different python versions. 
To run tests across all supported python versions (3.8, 3.9, 3.10, 3.11):
```bash
tox
```
2. Run all tests with pytest:
```bash
pytest
```


## Project Structure

```
mathematical-expression-evaluator/
├── src/
│   ├── expression_api.py      # FastAPI backend
│   ├── streamlit_app.py       # Streamlit frontend
│   └── streamlit_expression.py # Expression evaluator
|   └── test.py # test logic
├── tests/
│   ├── test_api.py
│   ├── test_expression_evaluator.py
├── setup.py
├── requirements.txt
├── tox.ini
└── README.md
```



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

