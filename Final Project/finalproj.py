#Mason Shaw
#Intermediate Programming
# Final Project

#This is my final project. This one has been fixed and revised overtime with more to come within a day or so. The test file is a back up,
# and more of a raw copy of this before some things commented out were removed, and before documentation on the project.
# It is very slow, and pretty routine throughout. I would recommend tweaking the wait settings a bit if you are wanting to test it. I will mark them with a !!!

import random
import time
from tkinter import *

#---------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------VARIABLES-------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

counter = 0
buttontime = 0

wood = 10
traps = 0                   #These are my variables, everywhere they are references are globals, but that works out since I kind of need them all to be accessed by different functions
fur = 0
meat = 0
teeth = 0
huts = 0 

#---------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------FUNCTIONS-------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

def woodclicker():
    global counter              #Woodclicker function is the main function that keeps track of clicks for one, and secondly removes wood per click on the stoke button press
    global buttontime
    global wood

    currenttime = time.time()
    if currenttime -buttontime >= 4:        #!!!
        print (time.time())
        buttontime = currenttime
        counter += 1

        print("it counted")
        wood -= 1
        print(wood)

    if counter >= 3:
        message_label.place_forget()

                                                        #These are different thresholds that will make other buttons or messages appear.
    if counter >= 6:
        forestbutton.pack(side=LEFT, padx=10, pady=10)

    else:
        pass

def getwoodclicker():               #the getwood clicker funciton is for the first button in the forest area, it gets wood.
    global counter
    global buttontime
    global wood

    currenttime = time.time()
    if currenttime -buttontime >= 9:        #!!!
        print (time.time())
        buttontime = currenttime
        counter += 1

        print("it counted")
        wood += 15
        print(wood)

        if huts == 1:
            wood += 25          #The amount of wood it will get per click is determined on huts, since I didn't know how to directly recreate them

        if huts == 2:
            wood +=40

        if huts >=3:
            wood += 60
    else:
        pass

def maketrap():
    global wood
    global traps            #This function will make a trap, which is how to currently get fur, teeth, and meat. 
    if wood >=30:               #Bones would also be a good addition
        wood -= 30
        traps += 1

def checktrap():
    global fur
    global teeth
    global meat         #Check trap checks the trap. I tried to implement a timer like I did with the get wood and stoke functions, but I couldnt get it.
                        #Everything has a random change to drop an amount within the range, and the amounts increase the more traps you have

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
    if wood >=100:      #This function makes a hut
        wood -=100
        huts +=1




def updatetextroom():

    button1.place_forget()
    button1.config(text="stoke", command=lambda: [woodclicker(), updatetextroom()])
    button1.place(x=10, y=30)

    button2.place_forget()
    if counter >= 9:                            #This funtion will essentially refresh the page each time it is called. It makes it forget what is what (as in values and content) and replaces it.
        button2.config(text="make trap (-30 wood)") #Individually doing every single thing in the frames was pretty much the most effective way to do this, so as a result it is very long.
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
        rightframe_fur.config(text=f"fur: {fur}")   #These if statements will make the materials appear on the right side frame when they actually aquire them, this purpose is to keep the user in the dark about what can be gotten.
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

    button1.place_forget()
    button1.config(text="get wood", command=lambda: [getwoodclicker(), updatetextforest()]) #almost identical to the main one, except it refreshes the second area with different buttons
    button1.place(x=10, y=30)

    button2.place_forget()
    if counter >= 15:
        button2.config(text="check trap", command= lambda: [checktrap(), updatetextforest()])
        button2.place(x= 10, y= 60)

    button3.place_forget()          #The second area doesnt have a third button 

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


#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------MAIN WINDOW AND FRAME---------------------------------------------
#---------------------------------------------------------------------------------------------------------------

window = Tk()
window.title("Final Project")           #This is the main application window
window.config(bg="gray")

topframe = Frame(window, width=300, height=70)  #This is the top frame that has the buttons for the two areas, as seen below
topframe.pack(padx=10, pady=10)
topframe.pack_propagate(False)

roombutton = Button(topframe, text = "Dark Room", command=updatetextroom)
roombutton.pack(side=LEFT, padx=10, pady=10)

forestbutton = Button(topframe, text = "Desolate Forest", command=updatetextforest)

#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------FRAMES AND LABELS-------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

frame1 = Frame(window, width = 300, height = 200)
frame1.pack(side=LEFT, padx=10, pady=10)
frame1.pack_propagate(False)

frame2 = Frame(window, width = 300, height = 200)   #This is the left, middle, and right frames in order.
frame2.pack(side=LEFT, padx=10, pady=10)
frame2.pack_propagate(False)

frame3 = Frame(window, width = 300, height = 200)
frame3.pack(side=LEFT, padx=10, pady=10)
frame3.pack_propagate(False)


leftframe_label = Label(frame1, text="")

rightframe_wood = Label(frame3, text="")
rightframe_fur = Label(frame3, text="")         #These are the labels for the loot on the right side frame, that is achieved currently from traps only.
rightframe_traps = Label(frame3, text="")
rightframe_huts = Label(frame3, text="")
rightframe_meat = Label(frame3, text="")
rightframe_teeth = Label(frame3, text="")

#---------------------------------------------------------------------------------------------------------------
#------------------------------------------------BUTTONS-------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

message_label = Label(window, text="NOTE: Some buttons (like stoke, and get wood) have timers so the clicks don't count, but you can still click.", bg="gray", fg="white" )
message_label.place(x= 200, y= 78)
        # The above message label is a litte note between the top frame and mid frames. It is a disclaimer that an action performed for getting wood has a wait time, even thought the button is being pressed.

button1 = Button(frame2, text="stoke", command=lambda: [woodclicker(),updatetextroom() ])
button1.place(x=10, y=30)

button2 = Button(frame2, text="make trap", command=lambda: [maketrap(), updatetextroom()])      #These are the main buttons. Only three at the moment. They are tied to their repsective funtions on the first area, 
                                                                                                # WHen the second area refreshes it configs these buttons instead of making completely new ones.

button3 = Button(frame2, text="make hut", command=lambda: [makehut(),updatetextroom() ])

#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------



window.mainloop()
