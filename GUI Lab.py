# CISW 126 Intermediate Programming
# GUI Lab - Tkinter 
# 
# Today we'll be messing with the built in graphic app for Python.
# If you haven't realized by now, it's name is Tkinter.
# Quick fact: Tkinter stands for Toolkit Interface if you were wondering.
# 
# Now, there's a lot of little things that you can do with tkinter.
# You'll be experimenting with a few of the more common and standard
# ways of using tkinter, but also looking into just messing around with
# it and applying it to the programs you've made in the past.
# ---------------------------------------------------------------------------

# This lab is less about solving a problem or using the things you've read about
# and more about just playing around and experimenting with a GUI environment.
# 
# The simplest way to do this, would be to think about how you could break down
# your original shape calculator (shapes.py) and then instead of having main.py
# run the program within the terminal, you could create something that runs and
# loads tkinter instead.
# 
# That's what I would recommend doing today. If you have another project or goal
# in mind then feel free to do that as well, but at the end of the day you want
# to have something with tkinter that opens, receives some input, and displays output.
# 
# I won't require that you use exceptions for this lab, but it will be required for
# the GUI project. So keep that in mind.
# 
# As always, feel free to ask questions.
from shape_calculator.shapecalc.shapes import *
from tkinter import *
from tkinter import messagebox



def maketriwindow():
    def get_area():
        x = float(entry.get())
        y = float(entry1.get())

        triangle = Triangle("Triangle", x, y)
        area_text.config(text=f"The area of the triangle is {triangle.triarea()}")
    
    
    roo = Tk()
    roo.title("Triangle Area")
    roo.geometry("300x300")

    entry = Entry(roo)
    entry.place(x=100, y=30)

    entry1 = Entry(roo)
    entry1.place(x=100, y=50)

    submit = Button(roo, text="Submit", command=get_area)
    submit.place(x=120, y=80)

    area_text = Label(roo, text="")
    area_text.place(x=20, y=100)


def makecirwindow():
    root = Tk()
    root.title("Circle Area")
    root.geometry("300x300")

def maketrapwindow():
    root = Tk()
    root.title("Trapezoid Area")
    root.geometry("300x300")

def makesqrwindow():
    root = Tk()
    root.title("Square Area")
    root.geometry("300x300")


def register():
    pass



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

