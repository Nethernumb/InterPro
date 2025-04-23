#Mason Shaw
#Project 4 - GUI Project


import random
from tkinter import *
#from PIL import ImageTk, Image        #did pip install Pillow to try it for images too, but i could get it to work either. 

# I also had bigger windows like 400x400, and I tried to make it to where everytime the button was clicked it would move to a different spot on the window,
# but i couldnt get it to run more than one function, I even tried Lambda and it would run the random tank, but not move the button to a different area.

def maketankwin():      # Function to make the tank window, 
    def tank_rand():        #this function will do a randint between the number of tanks, and will correlate their number to their in game order left to right, and return the name of what it chose.
        tanknum = random.randint(1,13)
        
        # first off, I used an if statement to go though the random number output since its easy, it works, and I know it well since i've used this process
        # multiple times. I know it isnt pretty but it gets the job done, being pretty is the GUI's job anyways honestly. 
        # Second, it's also because i don't know another sure fire way to run through a process like that, I though about doing a dictionary so I could
        # collapse it but I didnt, and I knew that the If statement would work for sure. 

        if tanknum == 1:
            # image_label.image = image
            # image_label.config(image=image)       #leftover image stuff
            hero_text.config(text=f"Your selected hero is D.VA")
        elif tanknum == 2:
            hero_text.config(text=f"Your selected hero is DoomFist")
        elif tanknum == 3:
            hero_text.config(text=f"Your selected hero is Hazard")
        elif tanknum == 4:
            hero_text.config(text=f"Your selected hero is Junker Queen")
        elif tanknum == 5:
            hero_text.config(text=f"Your selected hero is Mauga")
        elif tanknum == 6:
            hero_text.config(text=f"Your selected hero is Orisa")
        elif tanknum == 7:
            hero_text.config(text=f"Your selected hero is Ramattra")
        elif tanknum == 8:
            hero_text.config(text=f"Your selected hero is Reinhardt")
        elif tanknum == 9:
            hero_text.config(text=f"Your selected hero is Roadhog")
        elif tanknum == 10:
            hero_text.config(text=f"Your selected hero is Sigma")
        elif tanknum == 11:
            hero_text.config(text=f"Your selected hero is Winston")
        elif tanknum == 12:
            hero_text.config(text=f"Your selected hero is Wrecking Ball")
        elif tanknum == 13:
            hero_text.config(text=f"Your selected hero is Zarya")
        else:
            hero_text.config(text="Something went wrong")

    tank = Tk()     #this is the tank window
    tank.title("Tank Selector")
    tank.geometry("400x100") #used to be 400x400 when (and if) I get to figuring out how to properly put my images in I will put it back to that size. 

    # image = PhotoImage(file="ana.png")
    # image_label = Label(tank, image=image)        I Couldnt get anything relating to images to work, so I just decied to scratch it for now.
    # image_label.place(x=100, y=100)

    hero_text = Label(tank, text="Click Submit to get a random Tank", font=("Arial", 11)) 
    hero_text.pack(anchor=CENTER, pady=10)

    butt2 = Button(tank, text="Submmit", font=("Arial", 12), command=tank_rand)
    butt2.pack(padx=20, pady=5)     #Submit button, it calls the function that will randomly pick a number then run it through the if statement.

        #It is almost identical for the other 3 role windows. I'm pretty sure just the names and characters change. 

def makedpswin():
    def dps_rand():
        dpsnum = random.randint(1,19)
        if dpsnum == 1:
            hero_text.config(text=f"Your selected hero is Ashe")
        elif dpsnum == 2:
            hero_text.config(text=f"Your selected hero is Bastion")
        elif dpsnum == 3:
            hero_text.config(text=f"Your selected hero is McCree")
        elif dpsnum == 4:
            hero_text.config(text=f"Your selected hero is Echo")
        elif dpsnum == 5:
            hero_text.config(text=f"Your selected hero is Freyja")
        elif dpsnum == 6:
            hero_text.config(text=f"Your selected hero is Genji")
        elif dpsnum == 7:
            hero_text.config(text=f"Your selected hero is Hanzo")
        elif dpsnum == 8:
            hero_text.config(text=f"Your selected hero is Junkrat")
        elif dpsnum == 9:
            hero_text.config(text=f"Your selected hero is Mei")
        elif dpsnum == 10:
            hero_text.config(text=f"Your selected hero is Pharah")
        elif dpsnum == 11:
            hero_text.config(text=f"Your selected hero is Reaper")
        elif dpsnum == 12:
            hero_text.config(text=f"Your selected hero is Sojourn")
        elif dpsnum == 13:
            hero_text.config(text=f"Your selected hero is Soldier: 76")
        elif dpsnum == 14:
            hero_text.config(text=f"Your selected hero is Sombra")
        elif dpsnum == 15:
            hero_text.config(text=f"Your selected hero is Symmetra")
        elif dpsnum == 16:
            hero_text.config(text=f"Your selected hero is Torbin Time")
        elif dpsnum == 17:
            hero_text.config(text=f"Your selected hero is Tracer")
        elif dpsnum == 18:
            hero_text.config(text=f"Your selected hero is Venture")
        elif dpsnum == 19:
            hero_text.config(text=f"Your selected hero is Widowmaker")
        else:
            hero_text.config(text="Something went wrong")

    dps = Tk()
    dps.title("DPS Selector")
    dps.geometry("400x100")

    hero_text = Label(dps, text="Click Submit to get a random DPS", font=("Arial", 11))
    hero_text.pack(anchor=CENTER, pady=10)

    butt2 = Button(dps, text="Submit", font=("Arial", 12), command=dps_rand)
    butt2.pack(padx=20, pady=5)

def makesuppwin():
    def supp_rand():
        suppnum = random.randint(1,11)
        if suppnum == 1:
            hero_text.config(text=f"Your selected hero is Ana")
        elif suppnum == 2:
            hero_text.config(text=f"Your selected hero is Baptiste")
        elif suppnum == 3:
            hero_text.config(text=f"Your selected hero is Brigitte")
        elif suppnum == 4:
            hero_text.config(text=f"Your selected hero is Illari")
        elif suppnum == 5:
            hero_text.config(text=f"Your selected hero is Juno")
        elif suppnum == 6:
            hero_text.config(text=f"Your selected hero is Kiriko")
        elif suppnum == 7:
            hero_text.config(text=f"Your selected hero is Lifeweaver")
        elif suppnum == 8:
            hero_text.config(text=f"Your selected hero is Lucio")
        elif suppnum == 9:
            hero_text.config(text=f"Your selected hero is Mercy")
        elif suppnum == 10:
            hero_text.config(text=f"Your selected hero is Moira")
        elif suppnum == 11:
            hero_text.config(text=f"Your selected hero is Zenyatta")
        else:
            hero_text.config(text="Something went wrong")

    supp = Tk()
    supp.title("Support Selector")
    supp.geometry("400x100")

    hero_text = Label(supp, text="Click Submit to get a random Support", font=("Arial", 11))
    hero_text.pack(anchor=CENTER, pady=10)

    butt2 = Button(supp, text="Submit", font=("Arial", 12), command=supp_rand)
    butt2.pack(padx=20, pady=5)

#this is the main window
root = Tk()
root.title("RNG Overwatch Hero Picker")         
root.geometry("400x100")

# the top label, mad eit look fancy
label = Label(root, text="Randomized Heros", font=("Arial", 18))
label.pack(padx=10, pady=10)

#this is the button frame stuff, I really like this I think it looks nice if everything I've used it with
buttonframe = Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

# These are for the 3 role buttons that open up their respective windows
tankbutton = Button(buttonframe, text="Tank", font=("Arial", 14), command=maketankwin)
tankbutton.grid(row=0, column=0, sticky=W+E)

dpsbutton = Button(buttonframe, text="Damage", font=("Arial", 14), command= makedpswin)
dpsbutton.grid(row=0, column=1, sticky=W+E)

suppbutton = Button(buttonframe, text="Support", font=("Arial", 14), command= makesuppwin)
suppbutton.grid(row=0, column=2, sticky=W+E)

# this does the thing that makes the button grid frame whatever look pretty
buttonframe.pack(fill="x", pady=2)


root.mainloop()