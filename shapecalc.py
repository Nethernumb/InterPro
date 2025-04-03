# Set up your classes before the 'main' line below

# class Shape():      #parent class
#     def __init__(self, name, x, y ):
#         self.name = name
#         self.x = x
#         self.y = y

# class Circle(Shape):
#     def __init__(self, name, x):
#         self.name = name
#         self.x = x
    
#     def circarea(self):
#         print(f"A {self.name} with a radius of {self.x} has an area of {3.14 * (self.x ** 2)} ")

# class Rectangle(Shape): 
#     def __init__(self, name,  x, y):
#         super().__init__(name, x, y)
        
#     def recarea(self):
#         print(f"A {self.name} with a width of {self.x} and a height of {self.y} has an area of {self.x * self.y}")

# class Triangle(Shape): 
#     def __init__(self, name,  x, y):
#         super().__init__(name, x, y)

#     def triarea(self):
#         print(f"A {self.name} with a base of {self.x} and a height of {self.y} has an area of {self.x * self.y / 2}")
    

# class Trapezoid(Shape): 
#     def __init__(self, name, x, y, z):
#         super().__init__(name, x, y)
#         self.z = z

#     def traparea(self):
#         print(f"A {self.name} with a base of {self.x}, a width of {self.z} and a height of {self.y}, has an area of {0.5 * (self.z + self.x) * self.y}")

#and the rest goes here
if __name__ == '__main__':
    # Create one object per shape child class.
    # Set the properties appropriately.
    # Then display something like:
    
    # _shapename_ with _property 1_ and _property 2_ has area _area_
    # Example:
    #  Triangle with base 6 and height 4 has area 12.
    circle = Circle("Circle", 4)
    triangle = Triangle("Triangle", 3, 4)
    rectangle = Rectangle("Rectangle", 4, 5)
    trapezoid = Trapezoid("Trapezoid", 5, 4, 3)

    circle.circarea()
    triangle.triarea()
    rectangle.recarea()
    trapezoid.traparea()