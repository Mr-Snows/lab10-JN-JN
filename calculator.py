# https://github.com/Mr-Snows/lab10-JN-JN
# Partner 1: Jayci Nieves
# Partner 2: Jayci Nieves

def calculator:
    def square_root(a):
        if a <  0:
            raise ZeroDivisionError("Must be positive")
        return math.sqrt(a)

    def hypotenuse(a, b):
        return math.hypot(a, b)

    def add(a, b): 
        return a + b

    def subtract(a, b):
        return a- b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if a == 0:
            raise ZeroDivisionError("Can't divide by zero")
        return b / a

    def logarithm(a, b):
        if a <= 0 or a == 1:
            raise ValueError("Base can't be 1 and must be positive")
        if b <= 0:
            raise ValueError("Must be positive")
        return math.log(b, a)

    def exponent(a, b):
        return a ** b

    def mul(a, b):
        return a * b

    def div(a, b):
        if a == 0:
            raise ZeroDivisionError("Can't divide by zero")
        return b / a

    def exp(a, b):
        return a ** b
