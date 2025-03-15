#ONLY WORKS IF YOU HAVE API RUNNING 
import requests

def evaluate_expression(expression):
    try:
        response = requests.post(
            "http://localhost:8000/evaluate",
            json={"expression": expression}
        )
        
        if response.status_code == 200:
            return response.json()["result"]
        else:
            return f"Error: {response.json()['detail']}"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    while True:
        expression = input("Enter an expression (or 'quit' to exit): ")
        if expression.lower() == 'quit':
            break
            
        result = evaluate_expression(expression)
        print(f"Result: {result}")

if __name__ == "__main__":
    main() 