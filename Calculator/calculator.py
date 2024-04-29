# app.py
# This is a test commits
class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def test_add(self):
        assert self.add(1, 2) == 3
        assert self.add(1, -1) == 0

    def test_sub(self):
        assert self.sub(3, 2) == 1
        assert self.sub(2, 1) == 1

# Instantiate the Calculator class
calc = Calculator()

# Test the methods
calc.test_add()
calc.test_sub()

