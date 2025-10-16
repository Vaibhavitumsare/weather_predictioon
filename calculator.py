def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y
 
def modulo(x,y):
    return x % y

def calculator():
    print("Select operation: +, -, *, /,% ")
    op = input("Operation: ")
    x = float(input("First number: "))
    y = float(input("Second number: "))

    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '%': modulo
    }

    if op in operations:
        try:
            result = operations[op](x, y)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid operation.")

if __name__ == "__main__":
    calculator()