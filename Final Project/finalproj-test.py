#Mason Shaw
#Intermediate Programming
# Final Project




import random
import time
from tkinter import *
from tkinter import messagebox

#---------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------VARIABLES-------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

counter = 0
buttontime = 0

wood = 10
traps = 0
fur = 0
meat = 0
teeth = 0
huts = 0 

#---------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------FUNCTIONS-------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

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

        if huts == 1:
            wood += 25

        if huts == 2:
            wood +=40

        if huts >=3:
            wood += 60
    else:
        pass

def maketrap():
    global wood
    global traps
    if wood >=30:
        wood -= 30
        traps += 1

def checktrap():
    global fur
    global teeth
    global meat


    if traps == 1:
        fur += random.randint(1,7)
        teeth +=random.randint(0,3)
        meat +=random.randint(4,8)

    if traps == 2:
        fur += random.randint(3,9)
        teeth +=random.randint(1,3)
        meat +=random.randint(7,15)

    if traps == 3:
        fur += random.randint(8,12)
        teeth +=random.randint(2,4)
        meat +=random.randint(8,16)
    
    if traps >= 4:
        fur += random.randint(10,19)
        teeth +=random.randint(3,7)
        meat +=random.randint(9,19)



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

    button3.place_forget()
    if counter >= 15:
        button3.config(text="make hut (-100 wood)")
        button3.place(x=10, y=90)


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

    if fur >= 1:
        rightframe_fur.place_forget()
        rightframe_fur.config(text=f"fur: {fur}")
        rightframe_fur.place(x=15, y=45)

    if meat >= 1:
        rightframe_meat.place_forget()
        rightframe_meat.config(text=f"meat: {meat}")
        rightframe_meat.place(x=15, y=60)

    if teeth >= 1:
        rightframe_teeth.place_forget()
        rightframe_teeth.config(text=f"teeth: {teeth}")
        rightframe_teeth.place(x=15, y=75)

    if huts >= 1:
        rightframe_huts.place_forget()
        rightframe_huts.config(text=f"huts: {huts}")
        rightframe_huts.place(x=15, y=90)
   

    

def updatetextforest():
    # message_label.pack_forget()
    # message_label.config
    button1.place_forget()
    button1.config(text="get wood", command=lambda: [getwoodclicker(), updatetextforest()])
    button1.place(x=10, y=30)

    button2.place_forget()
    if counter >= 15:
        button2.config(text="check trap", command= lambda: [checktrap(), updatetextforest()])
        button2.place(x= 10, y= 60)

    button3.place_forget()
    # if counter >= 15:
        # button3.config(text="make hut (-100 wood)")
        # button3.place(x=10, y=90)

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

    if fur >= 1:
        rightframe_fur.place_forget()
        rightframe_fur.config(text=f"fur: {fur}")
        rightframe_fur.place(x=15, y=45)

    if meat >= 1:
        rightframe_meat.place_forget()
        rightframe_meat.config(text=f"meat: {meat}")
        rightframe_meat.place(x=15, y=60)

    if teeth >= 1:
        rightframe_teeth.place_forget()
        rightframe_teeth.config(text=f"teeth: {teeth}")
        rightframe_teeth.place(x=15, y=75)

    if huts >= 1:
        rightframe_huts.place_forget()
        rightframe_huts.config(text=f"huts: {huts}")
        rightframe_huts.place(x=15, y=90)

# def stokefire():
#     global wood
#     wood -= 1
#     print(wood)

#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------MAIN WINDOW AND FRAME---------------------------------------------
#---------------------------------------------------------------------------------------------------------------

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
rightframe_meat = Label(frame3, text="")
rightframe_teeth = Label(frame3, text="")

#---------------------------------------------------------------------------------------------------------------
#------------------------------------------------BUTTONS-------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

message_label = Label(window, text="NOTE: Some buttons (like stoke, and get wood) have timers so the clicks don't count, but you can still click.", bg="gray", fg="white" )
message_label.place(x= 200, y= 78)


button1 = Button(frame2, text="stoke", command=lambda: [woodclicker(),updatetextroom() ])
button1.place(x=10, y=30)

button2 = Button(frame2, text="make trap", command=lambda: [maketrap(), updatetextroom()])
#button2.place(x= 10, y= 80)

button3 = Button(frame2, text="make hut", command=lambda: [makehut(),updatetextroom() ])

# button4 = Button(frame2, text="", command=lambda: [])

#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------



window.mainloop()