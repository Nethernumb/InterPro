import math


def cal_cir():
    try:
        radius = int(input("What is the radius? "))

        if radius <= 0:
            raise ValueError
        

        else:
            circle = math.pi * (radius **2)
            print(circle)

    except ValueError:
        print("Radius must be greather than 0. \nTry again.")

    except:
        print("Please enter a number")

cal_cir()