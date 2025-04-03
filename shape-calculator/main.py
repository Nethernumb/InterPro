

from shapecalc.shapes import *



def greeting():
    while True:
        print(f"\nDo you need to find the area of a Circle, Triangle, Rectangle, or Trapezoid?")
        print("1 (Circle)")
        print("2 (Triangle)")
        print("3 (Rectangle)")
        print("4 (Trapezoid)")
        print("Exit\n")
        choice = input("Choose an option: (1-4) > ")

        if choice == "1":
            try:
                x = int(input("What is the Radius of your Circle?"))            #this makes it to where it will try my inputs before putting them into the class stuff, Thanks Tom.
                if x <= 0:
                    raise ValueError
                else:
                    circle = Circle("Circle", x)
                    circle.circarea()
            except ValueError:
                print("Please input a valid number! (No negatives, No words)")

        if choice == "2":
            try:
                x = int(input("What is the base of your Triangle? "))
                y = int(input("What is the height of your Triangle? "))
                if x <= 0:
                    raise ValueError
                elif y <= 0:
                    raise ValueError
                
                else:
                    triangle = Triangle("Triangle", x, y)
                    triangle.triarea()

            except ValueError:
                print("Please input a valid number! (No negatives, No words)")


        if choice == "3":
            try:
                x = int(input("What is the Width of your Rectangle? "))
                y = int(input("What is the height of your Rectangle? "))
                if x <= 0:
                    raise ValueError
                elif y <= 0:
                    raise ValueError
                
                else:
                    rectangle = Rectangle("Rectangle", x, y)
                    rectangle.recarea()

            except ValueError:
                print("Please input a valid number! (No negatives, No words)")


        if choice == "4":
            try:
                x = int(input("What is the base of your Trapezoid? "))
                y = int(input("What is the width of your Trapezoid? "))
                z = int(input("What is the height of your Trapezoid? "))
                if x <= 0:
                    raise ValueError
                elif y <= 0:
                    raise ValueError
                elif z <= 0:
                    raise ValueError
                
                else:
                    trapezoid = Trapezoid("Trapezoid", x, y, z)
                    trapezoid.traparea()

            except ValueError:
                print("Please input a valid number! (No negatives, No words, No zeros)")


        if choice.lower() == "exit":
            exit()


if __name__ == '__main__':
    # Create one object per shape child class.
    # Set the properties appropriately.
    # Then display something like:
    
    # _shapename_ with _property 1_ and _property 2_ has area _area_
    # Example:
    #  Triangle with base 6 and height 4 has area 12.
    # circle = Circle("Circle", 4)
    # triangle = Triangle("Triangle", 3, 4)
    # rectangle = Rectangle("Rectangle", 4, 5)
    # trapezoid = Trapezoid("Trapezoid", 5, 4, 3)

    # circle.circarea()
    # triangle.triarea()
    # rectangle.recarea()
    # trapezoid.traparea()          #old non user input area stuff

    greeting()