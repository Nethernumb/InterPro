import random
import time
from tkinter import *
#in order to use png, jpeg, and jpg you need pillow (PIL)
from PIL import ImageTk, Image

counter = 0
buttontime = 0


def clicker():
    global counter  
    global buttontime

    currenttime = time.time()
    if currenttime -buttontime >= 5:
        print (time.time())
        buttontime = currenttime
        counter += 1
        print("it counted")

    if counter >= 3:
        message_label.place_forget()


    if counter >= 5:
        button2.place(x= 10, y= 80)
    else:
        pass
        
    if counter >= 10:
        forestbutton.pack(side=LEFT, padx=10, pady=10)

    else:
        pass



def updatetextroom():
    # message_label.pack_forget()
    # message_label.config
    button1.place_forget()
    button1.config(text="stoke")
    button1.place(x=10, y=30)
    button2.place_forget()
    button2.config(text="build hut")
    button2.place(x= 10, y= 80)

    

def updatetextforest():
    # message_label.pack_forget()
    # message_label.config
    button1.place_forget()
    button1.config(text="get wood")
    button1.place(x=10, y=30)
    button2.place_forget()
    button2.config(text="set trap")
    button2.place(x= 10, y= 80)



window = Tk()
window.title("Final Project")
#window.geometry("500x700")
window.config(bg="gray")

topframe = Frame(window, width=300, height=70)
topframe.pack(padx=10, pady=10)
topframe.pack_propagate(False)

roombutton = Button(topframe, text = "Dark Room", command=updatetextroom)
roombutton.pack(side=LEFT, padx=10, pady=10)

forestbutton = Button(topframe, text = "Desolate Forest", command=updatetextforest)
#forestbutton.pack(side=LEFT, padx=10, pady=10)

#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

frame1 = Frame(window, width = 300, height = 200)
frame1.pack(side=LEFT, padx=10, pady=10)
frame1.pack_propagate(False)

frame2 = Frame(window, width = 300, height = 200)
frame2.pack(side=LEFT, padx=10, pady=10)
frame2.pack_propagate(False)

frame3 = Frame(window, width = 300, height = 200)
frame3.pack(side=LEFT, padx=10, pady=10)
frame3.pack_propagate(False)

message_label = Label(window, text="NOTE: Some buttons (like stoke, and get wood) have timers so the clicks don't count, but you can still click.", bg="gray", fg="white" )
message_label.place(x= 200, y= 78)

button1 = Button(frame2, text="stoke", command=clicker)
button1.place(x=10, y=30)

button2 = Button(frame2, text="build hut")
#button2.place(x= 10, y= 80)



# Button(window, text="Tank", width=15).pack(pady=5)
# Button(window, text="DPS", width=15).pack(pady=5)
# Button(window, text="Support", width=15).pack(pady=5)

# Button(window, text="Tank 5", width=15).pack(pady=5)
# Button(window, text="DPS 5 ", width=15).pack(pady=5)
# Button(window, text="Support 5", width=15).pack(pady=5)
window.mainloop()
