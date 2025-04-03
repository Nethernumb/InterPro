import math


def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
        
    if x == 0:
        raise ValueError

    return x / y

def to_the_power_of(x,y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

if __name__ == "__main__":
    add()
    subtract()
    multiply()
    divide()
    to_the_power_of()
    square_root()