from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class ExpressionEvaluator:
    def __init__(self):
        self.pos = 0
        self.expression = ""
    
    def parse_expression(self, expression):
        """Parse and evaluate a mathematical expression string."""
        self.expression = expression.replace(" ", "")  # Remove spaces
        self.pos = 0
        return self.parse_addition_subtraction()
    
    def get_current_char(self):
        """Get the current character in the expression."""
        if self.pos < len(self.expression):
            return self.expression[self.pos]
        return None
    
    def parse_addition_subtraction(self):
        """Parse and evaluate addition and subtraction operations."""
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
        """Parse and evaluate multiplication and division operations."""
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
        """Parse a number or an expression inside parentheses."""
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
        """Parse a number from the expression."""
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

app = FastAPI()

class ExpressionRequest(BaseModel):
    expression: str

@app.post("/evaluate")
async def evaluate_expression_endpoint(request: ExpressionRequest):
    try:
        evaluator = ExpressionEvaluator()
        result = evaluator.parse_expression(request.expression)
        
        # Convert to int if it's a whole number
        if result == int(result):
            result = int(result)
            
        return {"expression": request.expression, "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

 