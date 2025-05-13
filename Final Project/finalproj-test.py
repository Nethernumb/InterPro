import random
import time
from tkinter import *
#in order to use png, jpeg, and jpg you need pillow (PIL)
from PIL import ImageTk, Image

counter = 0
buttontime = 0

wood = 10
traps = 0
fur = 0
meat = 0
teeth = 0
huts = 0 

def woodclicker():
    global counter  
    global buttontime
    global wood

    currenttime = time.time()
    if currenttime -buttontime >= 1:
        print (time.time())
        buttontime = currenttime
        counter += 1

        print("it counted")
        wood -= 1
        print(wood)

    if counter >= 3:
        message_label.place_forget()

        
    if counter >= 6:
        forestbutton.pack(side=LEFT, padx=10, pady=10)


    else:
        pass

def getwoodclicker():
    global counter
    global buttontime
    global wood

    currenttime = time.time()
    if currenttime -buttontime >= 5:
        print (time.time())
        buttontime = currenttime
        counter += 1

        print("it counted")
        wood += 15
        print(wood)
    else:
        pass

def maketrap():
    global wood
    global traps
    if wood >=30:
        wood -= 30
        traps += 1

traps_loot[]

def makehut():
    global wood
    global huts
    if wood >=100:
        wood -=100
        huts +=1



def updatetextroom():

    button1.place_forget()
    button1.config(text="stoke", command=lambda: [woodclicker(), updatetextroom()])
    button1.place(x=10, y=30)
    button2.place_forget()
    if counter >= 9:
        button2.config(text="make trap (-30 wood)")
        button2.place(x= 10, y= 60)

    leftframe_label.place_forget()

    if wood <= 4:
        leftframe_label.place_forget()
        leftframe_label.config(text="The wood is running low")
        leftframe_label.place(x = 10, y = 10)
    

    rightframe_wood.place_forget()
    rightframe_wood.config(text=f"wood: {wood}")
    rightframe_wood.place(x = 15, y= 15)

    if traps >= 1:
        rightframe_traps.place_forget()
        rightframe_traps.config(text=f"traps: {traps}")
        rightframe_traps.place(x=15, y=30)
   

    

def updatetextforest():
    # message_label.pack_forget()
    # message_label.config
    button1.place_forget()
    button1.config(text="get wood", command=lambda: [getwoodclicker(), updatetextforest()])
    button1.place(x=10, y=30)
    button2.place_forget()
    if counter >= 15:
        button2.config(text="check trap")
        button2.place(x= 10, y= 80)

    leftframe_label.place_forget()

    if wood <= 4:
        leftframe_label.place_forget()
        leftframe_label.config(text="The wood is running low")
        leftframe_label.place(x = 10, y = 10)
    

    rightframe_wood.place_forget()
    rightframe_wood.config(text=f"wood: {wood}")
    rightframe_wood.place(x = 15, y= 15)

# def stokefire():
#     global wood
#     wood -= 1
#     print(wood)

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
#---------------------------------------------FRAMES AND LABELS-------------------------------------------------
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


leftframe_label = Label(frame1, text="")

rightframe_wood = Label(frame3, text="")
rightframe_fur = Label(frame3, text="")
rightframe_traps = Label(frame3, text="")
rightframe_huts = Label(frame3, text="")

#---------------------------------------------------------------------------------------------------------------
#------------------------------------------------BUTTONS-------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

message_label = Label(window, text="NOTE: Some buttons (like stoke, and get wood) have timers so the clicks don't count, but you can still click.", bg="gray", fg="white" )
message_label.place(x= 200, y= 78)


button1 = Button(frame2, text="stoke", command=lambda: [woodclicker(),updatetextroom() ])
button1.place(x=10, y=30)

button2 = Button(frame2, text="make trap", command=lambda: [maketrap(), updatetextroom()])
#button2.place(x= 10, y= 80)

button3 = Button(frame2, text="make hut", command=lambda: [])

button4 = Button(frame2, text="", command=lambda: [])

#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------



window.mainloop()
