import streamlit as st

class ExpressionEvaluator:
    def __init__(self):
        self.pos = 0
        self.expression = ""
        
    def get_next_token(self):
        while self.pos < len(self.expression) and self.expression[self.pos].isspace():
            self.pos += 1
            
        if self.pos >= len(self.expression):
            return None
            
        if self.expression[self.pos].isdigit():
            start = self.pos
            while self.pos < len(self.expression) and (self.expression[self.pos].isdigit() or self.expression[self.pos] == '.'):
                self.pos += 1
            return float(self.expression[start:self.pos])
            
        token = self.expression[self.pos]
        self.pos += 1
        return token
        
    def parse_expression(self, expression):
        self.expression = expression
        self.pos = 0
        return self.parse_addition()
        
    def parse_addition(self):
        result = self.parse_multiplication()
        
        while True:
            token = self.get_next_token()
            if token not in ('+', '-'):
                self.pos -= 1
                break
                
            right = self.parse_multiplication()
            if token == '+':
                result += right
            else:
                result -= right
                
        return result
        
    def parse_multiplication(self):
        result = self.parse_parentheses()
        
        while True:
            token = self.get_next_token()
            if token not in ('*', '/'):
                self.pos -= 1
                break
                
            right = self.parse_parentheses()
            if token == '*':
                result *= right
            else:
                if right == 0:
                    raise ValueError("Division by zero")
                result /= right
                
        return result
        
    def parse_parentheses(self):
        token = self.get_next_token()
        
        if token == '(':
            result = self.parse_addition()
            if self.get_next_token() != ')':
                raise ValueError("Missing closing parenthesis")
            return result
        elif token == '-':
            return -self.parse_parentheses()
        elif isinstance(token, (int, float)):
            return token
        else:
            raise ValueError(f"Unexpected token: {token}")

# Streamlit UI
st.title("Mathematical Expression Evaluator")

# Input field for the expression
expression = st.text_input("Enter a mathematical expression:", "2 * (3 + 4)")

# Add some example expressions

if expression:  # Only evaluate if there's input
    try:
        evaluator = ExpressionEvaluator()
        result = evaluator.parse_expression(expression)
        
        # Convert to int if it's a whole number
        if result == int(result):
            result = int(result)
            
        st.success(f"Result: {result}")
    except ZeroDivisionError:
        st.warning("Cannot divide by zero. Please check your expression.")
    except ValueError as e:
        st.warning(f"Invalid expression: {str(e)}")
    except Exception:
        st.warning("Please enter a valid mathematical expression.")
