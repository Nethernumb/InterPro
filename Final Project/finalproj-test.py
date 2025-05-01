import random
from tkinter import *
#in order to use png, jpeg, and jpg you need pillow (PIL)
from PIL import ImageTk, Image

def updatetextroom():
    # message_label.pack_forget()
    # message_label.config
    button1.pack_forget()
    button1.config(text="test30")
    button1.pack()

def updatetextforest():
    # message_label.pack_forget()
    # message_label.config
    button2.pack_forget()



window = Tk()
window.title("Overwatch Hero Picker")
window.config(bg="red")

topframe = Frame(window, width=300, height=70)
topframe.pack(padx=10, pady=10)
topframe.pack_propagate(False)

roombutton = Button(topframe, text = "Dark Room", command=updatetextroom)
roombutton.pack(side=LEFT, padx=10, pady=10)

forestbutton = Button(topframe, text = "Desolate Forest", command=updatetextforest)
forestbutton.pack(side=LEFT, padx=10, pady=10)

#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

frame1 = Frame(window, width = 300, height = 200)
frame1.pack(side=LEFT, padx=10, pady=10)
frame1.pack_propagate(False)

message_label = Label(frame1, text="")
message_label.pack(padx=10, pady=10)

button1 = Button(frame1, text="test1")
button1.pack(side= LEFT, padx=10,pady=10)

button2 = Button(frame1, text="test2")
button2.pack(side= LEFT, padx=10,pady=10)

# Button(window, text="Tank", width=15).pack(pady=5)
# Button(window, text="DPS", width=15).pack(pady=5)
# Button(window, text="Support", width=15).pack(pady=5)

# Button(window, text="Tank 5", width=15).pack(pady=5)
# Button(window, text="DPS 5 ", width=15).pack(pady=5)
# Button(window, text="Support 5", width=15).pack(pady=5)
window.mainloop()
