import streamlit as st
import requests

st.title("Mathematical Expression Evaluator")

# Input field for the expression
expression = st.text_input("Enter a mathematical expression:", "2 * (3 + 4)")

if st.button("Evaluate"):
    try:
        # Make API call to the FastAPI endpoint
        response = requests.post(
            "http://localhost:8000/evaluate",
            json={"expression": expression}
        )
        
        if response.status_code == 200:
            result = response.json()
            st.success(f"Result: {result['result']}")
        else:
            st.error(f"Error: {response.json()['detail']}")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Add some example expressions
st.markdown("### Example expressions:")
examples = [
    "(3 + 5) * (2 - 1) / 4",
    "3 + 5 * 2",
    "10 / 2 + 3",
    "2 * (3 + 4)",
    "8 / (4 - 2)",
    "-5 + 10"
]

for example in examples:
    st.code(example) 