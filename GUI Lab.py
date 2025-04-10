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


def register():
    # Get the user input from the form
    first_name = first_name_entry.get()
    Last_name = Last_name_entry.get()
    email = email_entry.get()
    Mobile = Mobile_entry.get()

    # Create a new row with the user input
    new_row = [first_name, Last_name, email,Mobile]

    # Append the new row to the Excel sheet
    # workbook = openpyxl.load_workbook("registration_data.xlsx")
    # sheet = workbook.active
    # sheet.append(new_row)
    # workbook.save("registration_data.xlsx")
    # messagebox.showinfo("Success", "Registration successful!")


# Create the main tkinter window
root = Tk()
root.title("Shape Calculator")
root.geometry('600x600')

# Create labels and entry fields for each input
button

Sircle_label = Label(root, text="Circle")
Sircle_label.grid()
Sircle_entry = Button(root, text="Circle", command= None)
Sircle_entry.grid(row=0, column=0, sticky=W+E)

square_label = Label(root, text="Square")
square_label.grid()
square_entry = Button(root, text="Sqare", command= None)
square_entry.grid(row=0, column=1, sticky=W+E)

triangle_label = Label(root, text="Trangle")
triangle_label.grid()
triangle_entry = Button(root, text="Trangle", command= None)
triangle_entry.grid(row=1, column=0, sticky=W+E)

trapezoid_label = Label(root, text="Trapezoid")
trapezoid_label.grid()
trapezoid_entry = Button(root, text="Zoid", command= None)
trapezoid_entry.grid(row=1, column=1, sticky=W+E)





register_button = Button(root, text="Register", command= None)
register_button.grid()

root.mainloop()

