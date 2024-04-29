# calculator.py
# This is a test commits

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def test_operations():
    # Addition
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    
    # Subtraction
    assert subtract(5, 2) == 3
    assert subtract(10, 5) == 5
    
    # Multiplication
    assert multiply(2, 3) == 6
    assert multiply(4, -2) == -8
    
    # Division
    assert divide(6, 2) == 3
    assert divide(10, 5) == 2
    
    # Test division by zero
    try:
        divide(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero!"

# Run the tests
test_operations()
