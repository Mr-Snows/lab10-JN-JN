# I did both Jayci
# First example
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


