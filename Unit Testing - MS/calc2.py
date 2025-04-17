import math 

def get_user_input():
    while True:
        try:
            u_input = int(input("Enter a number : "))
            return u_input
        except ValueError:
            print("Please enter a number. ") 



class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
            
        if self.x == 0:
            raise ZeroDivisionError

        return self.x / self.y

    def to_the_power_of(self):
        return self.x ** self.y


if __name__ == "__main__":
    add()
    subtract()
    multiply()
    divide()
    to_the_power_of()
    square_root()