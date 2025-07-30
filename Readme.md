# Author
  
  Vaibhavi Tumsare


# Simple Python Calculator

This is a simple command-line calculator written in Python. It supports basic arithmetic operations: addition, subtraction, multiplication, division, and modulo.

## Features

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`) with division by zero handling
- Modulo (`%`)
- User-friendly command-line interface

## How to Use

1. **Save the code** into a file (for example, `calculator.py`).
2. **Run the script** using Python 3.x:

   ```bash
   python calculator.py
   ```

3. **Follow the prompts:**
   - Select an operation (`+`, `-`, `*`, `/`, `%`)
   - Enter the first number
   - Enter the second number

4. **View the result**.

## Example

```
Select operation: +, -, *, /,%
Operation: %
First number: 10
Second number: 3
Result: 1.0
```

## Code Overview

```python
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

def modulo(x, y):
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
```

## Notes

- Handles division by zero and unsupported operations gracefully.
- All operations work with floating-point numbers.

## License

This project is open source and free to use for any purpose.