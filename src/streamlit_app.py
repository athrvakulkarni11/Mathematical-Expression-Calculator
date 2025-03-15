import streamlit as st
import requests

st.title("Mathematical Expression Evaluator")

# Input field for the expression
expression = st.text_input("Enter a mathematical expression:", "2 * (3 + 4)")

# Add some example expressions


if expression:  # Only evaluate if there's input
    try:
        # Make API call to the FastAPI endpoint
        response = requests.post(
            "http://localhost:8000/evaluate",
            json={"expression": expression},
            timeout=5  # Add timeout to prevent hanging
        )
        
        if response.status_code == 200:
            result = response.json()
            st.success(f"Result: {result['result']}")
        else:
            st.warning("Please check your expression and try again.")
    except requests.exceptions.ConnectionError:
        st.warning("Cannot connect to the server. Please make sure the API is running.")
    except requests.exceptions.Timeout:
        st.warning("Server request timed out. Please try again.")
    except Exception:
        st.warning("Please enter a valid mathematical expression.")

