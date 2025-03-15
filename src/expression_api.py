from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class ExpressionEvaluator:
    """
    A mathematical expression parser and evaluator that handles basic arithmetic operations.

    This class implements a recursive descent parser to evaluate mathematical expressions
    supporting the following features:
    - Basic arithmetic operations (+, -, *, /)
    - Parentheses for grouping
    - Negative numbers
    - Decimal numbers

    Attributes:
        pos (int): Current position in the expression string
        expression (str): The mathematical expression being evaluated
    """

    def __init__(self):
        self.pos = 0
        self.expression = ""
    
    def parse_expression(self, expression):
        """
        Parse and evaluate a mathematical expression string.

        Args:
            expression (str): The mathematical expression to evaluate

        Returns:
            float: The result of evaluating the expression

        Raises:
            ValueError: If the expression is malformed or contains invalid characters
        """
        self.expression = expression.replace(" ", "")  # Remove spaces
        self.pos = 0
        return self.parse_addition_subtraction()
    
    def get_current_char(self):
        """
        Get the current character in the expression.

        Returns:
            str or None: The current character at the current position, or None if at end
        """
        if self.pos < len(self.expression):
            return self.expression[self.pos]
        return None
    
    def parse_addition_subtraction(self):
        """
        Parse and evaluate addition and subtraction operations.

        This method handles the lowest precedence operations (+ and -).
        It first evaluates higher precedence operations by calling parse_multiplication_division().

        Returns:
            float: The result of evaluating the addition/subtraction expression

        Raises:
            ValueError: If the expression is malformed
        """
        left = self.parse_multiplication_division()
        
        while self.get_current_char() in ['+', '-']:
            operator = self.get_current_char()
            self.pos += 1
            right = self.parse_multiplication_division()
            
            if operator == '+':
                left += right
            else:  # operator == '-'
                left -= right
                
        return left
    
    def parse_multiplication_division(self):
        """
        Parse and evaluate multiplication and division operations.

        This method handles the higher precedence operations (* and /).
        It first evaluates parentheses and numbers by calling parse_number_or_parentheses().

        Returns:
            float: The result of evaluating the multiplication/division expression

        Raises:
            ValueError: If the expression is malformed
            ZeroDivisionError: If division by zero is attempted
        """
        left = self.parse_number_or_parentheses()
        
        while self.get_current_char() in ['*', '/']:
            operator = self.get_current_char()
            self.pos += 1
            right = self.parse_number_or_parentheses()
            
            if operator == '*':
                left *= right
            else:  # operator == '/'
                left /= right
                
        return left
    
    def parse_number_or_parentheses(self):
        """
        Parse a number or an expression inside parentheses.

        This method handles:
        - Parenthesized expressions: (expression)
        - Numbers: both integers and floating-point

        Returns:
            float: The parsed number or result of the parenthesized expression

        Raises:
            ValueError: If there's a missing closing parenthesis or invalid number format
        """
        char = self.get_current_char()
        
        # Handle parentheses
        if char == '(':
            self.pos += 1
            result = self.parse_addition_subtraction()
            
            # Ensure closing parenthesis
            if self.get_current_char() == ')':
                self.pos += 1
                return result
            else:
                raise ValueError("Missing closing parenthesis")
        
        # Handle numbers (integers and floats)
        else:
            return self.parse_number()
    
    def parse_number(self):
        """
        Parse a number from the expression.

        Handles:
        - Integer numbers
        - Floating-point numbers
        - Negative numbers
        - Leading minus sign

        Returns:
            float: The parsed number value

        Raises:
            ValueError: If the number format is invalid or no number is found
        """
        start_pos = self.pos
        
        # Handle negative numbers
        if self.get_current_char() == '-':
            self.pos += 1
        
        # Parse digits before decimal point
        while self.get_current_char() and self.get_current_char().isdigit():
            self.pos += 1
        
        # Parse decimal point and digits after it
        if self.get_current_char() == '.':
            self.pos += 1
            if not self.get_current_char() or not self.get_current_char().isdigit():
                raise ValueError("Invalid number format")
            
            while self.get_current_char() and self.get_current_char().isdigit():
                self.pos += 1
        
        if self.pos == start_pos:
            raise ValueError("Expected number")
        
        # Convert the substring to a number
        return float(self.expression[start_pos:self.pos])

    def _check_parentheses_balance(self, expression):
        """
        Check if parentheses in the expression are properly balanced.

        Args:
            expression (str): The mathematical expression to check

        Returns:
            bool: True if parentheses are balanced, False otherwise

        Example:
            >>> _check_parentheses_balance("(2 + 3) * (4 - 1)")
            True
            >>> _check_parentheses_balance("(2 + 3)) * (4 - 1)")
            False
        """

app = FastAPI()

class ExpressionRequest(BaseModel):
    expression: str

@app.post("/evaluate")
async def evaluate_expression_endpoint(request: ExpressionRequest):
    """
    Evaluate a mathematical expression via HTTP POST request.

    Args:
        request (ExpressionRequest): Request body containing the expression to evaluate

    Returns:
        dict: JSON response containing:
            - expression: The original expression
            - result: The evaluated result (int or float)

    Raises:
        HTTPException: 400 status code if expression is invalid or evaluation fails
    """
    try:
        evaluator = ExpressionEvaluator()
        result = evaluator.parse_expression(request.expression)
        
        # Convert to int if it's a whole number
        if result == int(result):
            result = int(result)
            
        return {"expression": request.expression, "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

 