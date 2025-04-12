# CISW 126 Intermediate Programming
# GUI Lab - Tkinter 
# Mason Shaw
from Resources.gui_shapes import *
from tkinter import *


#the floats are to convert it from a string into a number, plus decimals so yay
# I created a dupiclate of my shapes.py so i could use it as a standalone instead of the original because if i changed anything it would break shape calc
# All i did was comment out the prints to get rid of the terminal outputs. 

# The main window code is all the way at the bottom, i was gonna add a menubar up top with some goofy stuff just cuz, but I dont really need to right now
# I'm a little lost on how the gui runs, since i think i referred back to the homework video. Its not in a function but calling mainloop() makes it run?
# Nevernmind, it looks like doing the name like sqr.mainloop(), will make it run since im calling to the sqr = tk stuff for whatever, makes enough sense



# the code below is basically copied and pasted to the rest of the windows, so i think it only needs to be explained once, but ill make comments along the way if nescessary

def maketriwindow():        # Makes a window for triangle, all of the shapes have this exact same thing but with proper naming
    def get_area():
        x = float(entry.get())          #.get gets the input that sits in the text box
        y = float(entry1.get())         # the get_area function is also tied to the submit button, giving it a purpose instead of sitting there useless and not doing anything like the stupid submit button it is.

        triangle = Triangle("Triangle", x, y)
        area_text.config(text=f"The area of the triangle is {triangle.triarea()}")          #I think the .config just allows things to be changed or tweaked.
    
    
    tri = Tk()          #To be very honest, I have no idea how to explain this other than it makes it work. 
    tri.title("Triangle Area")      #This is the title of the page
    tri.geometry("300x300")         #This defines how big the box is

    entry = Entry(tri)
    entry.place(x=100, y=30)        #Entry is the text box, .place is manually putting it somewhere in the box

    entry1 = Entry(tri)         #second text box
    entry1.place(x=100, y=50)

    submit = Button(tri, text="Submit", command=get_area)           # the command = is very useful, makes buttons and stuff have use or do specific things
    submit.place(x=120, y=80)

    area_text = Label(tri, text="")     # this is a variable for the result that will actually place it in the window, leaving the text area blank
    area_text.place(x=20, y=100)        # allows area_text.config to add whatever by also putting text="", its also reusable this way so i dont need
                                        # so many variables

# I had to do circle different because it only takes one input and its radius
def makecirwindow():
    def get_area():
        x = float(entry.get())

        circle = Circle("Circle", x)
        area_text.config(text=f"The area of the circle is {circle.circarea()}")

    cir = Tk()
    cir.title("Circle Area")
    cir.geometry("300x300")

    entry = Entry(cir)
    entry.place(x=100, y=30)

    submit = Button(cir, text="Submit", command=get_area)
    submit.place(x=120, y=80)

    area_text = Label(cir, text="")
    area_text.place(x=20, y=100)

def maketrapwindow():
    def get_area():
        x = float(entry.get())
        y = float(entry1.get())     #trapezoid needs an extra entry box because of the 3rd input
        z = float(entry2.get())

        trapezoid = Trapezoid("Trapezoid", x, y, z)
        area_text.config(text=f"The area of the trapezoid is {trapezoid.traparea()}")

    trap = Tk()
    trap.title("Trapezoid Area")
    trap.geometry("300x300")

    entry = Entry(trap)
    entry.place(x=100, y=30)

    entry1 = Entry(trap)
    entry1.place(x=100, y=50)

    entry2 = Entry(trap)
    entry2.place(x=100, y=70)

    submit = Button(trap, text="Submit", command=get_area)
    submit.place(x=120, y=100)

    area_text = Label(trap, text="")
    area_text.place(x=20, y=150)


# sqr means square, also in my shape calc the class is called Rectangle, they have the same calculation so TECHNICALLY im not wrong
def makesqrwindow():
    def get_area():
        x = float(entry.get())
        y = float(entry1.get())

        square = Rectangle("Square", x, y)
        area_text.config(text=f"The area of the square is {square.recarea()}")

    sqr = Tk()
    sqr.title("square Area")
    sqr.geometry("300x300")

    entry = Entry(sqr)
    entry.place(x=100, y=30)

    entry1 = Entry(sqr)
    entry1.place(x=100, y=50)

    submit = Button(sqr, text="Submit", command=get_area)
    submit.place(x=120, y=80)

    area_text = Label(sqr, text="")
    area_text.place(x=20, y=100)



# Create the main tkinter window
root = Tk()
root.title("Shape Calculator")
root.geometry('600x600')

# Create labels and entry fields for each input
buttonframe = Frame(root)
buttonframe.pack(pady=200)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)

# Sircle_label = Label(root, text="Circle")
# Sircle_label.grid()
Sircle_entry = Button(buttonframe, text="Circle", command= makecirwindow)
Sircle_entry.grid(row=0, column=0, sticky=W+E)

# square_label = Label(root, text="Square")
# square_label.grid()
square_entry = Button(buttonframe, text="Sqare", command= makesqrwindow)
square_entry.grid(row=0, column=1, sticky=W+E)

# triangle_label = Label(root, text="Trangle")
# triangle_label.grid()
triangle_entry = Button(buttonframe, text="Trangle", command= maketriwindow)
triangle_entry.grid(row=1, column=0, sticky=W+E)

# trapezoid_label = Label(root, text="Trapezoid")
# trapezoid_label.grid()
trapezoid_entry = Button(buttonframe, text="Zoid", command= maketrapwindow)
trapezoid_entry.grid(row=1, column=1, sticky=W+E)

buttonframe.pack(fill="x")



# register_button = Button(root, text="Register", command= None)
# register_button.grid()

root.mainloop()

#right up above i have alot of stuff commented out because I wanted to use the grid button layout stuff, and for some reason it was throwing errors
# i didnt understand with that in, so i just commented it all out and it worked fine how i wanted it to, its REALLY ugly though, but hey it does what it needs to.

## Also thank you for all your help Tom i really appreciate all the help and how much you work with me whether its with helping me fix my code or I dont get something in on time,
# The stuff you showed in class (basically what i used) really helped me with actually understanding what things were doing and why, and how to apply them correctly. 
# thank you very much!