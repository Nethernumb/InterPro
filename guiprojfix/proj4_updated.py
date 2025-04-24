#Mason Shaw
#Project 4 - GUI Project

# images won't load natively(?) you need to right click the folder that has the program, so in this case guiprojfix and click 
# open in integrated terminal. in the terminal it opens you then type python then tab and it should autofill. if not put the file location. 

# in my current directory i need to add guiprojfix to the beginning of all the image links. Without it it cant find anything. 

import random
from tkinter import *
#in order to use png, jpeg, and jpg you need pillow (PIL)
from PIL import ImageTk, Image

#----------------------------------------------------------------------------#
#                       DICTIONARIES FOR EACH HERO                           #
#----------------------------------------------------------------------------#
tank_heroes = {
    1: ("D.VA", "guiprojfix/images/dva.png"),
    2: ("DoomFist", "guiprojfix/images/doomfist.png"),
    3: ("Hazard", "guiprojfix/images/hazard.png"),
    4: ("Junker Queen", "guiprojfix/images/junkerqueen.png"),
    5: ("Mauga", "guiprojfix/images/mauga.png"),
    6: ("Orisa", "guiprojfix/images/orisa.png"),
    7: ("Ramattra", "guiprojfix/images/ramattra.png"),
    8: ("Reinhardt", "guiprojfix/images/reinhardt.png"),
    9: ("Roadhog", "guiprojfix/images/roadhog.png"),
    10: ("Sigma", "guiprojfix/images/sigma.png"),
    11: ("Winston", "guiprojfix/images/winston.png"),
    12: ("Wrecking Ball", "guiprojfix/images/wreckingball.png"),
    13: ("Zarya", "guiprojfix/images/zarya.png")
}
dps_heroes = {
    1: ("Ashe", "guiprojfix/images/ashe.png"),
    2: ("Bastion", "guiprojfix/images/bastion.png"),
    3: ("McCree", "guiprojfix/images/mccree.png"),
    4: ("Echo", "guiprojfix/images/echo.png"),
    5: ("Freyja", "guiprojfix/images/freyja.png"),
    6: ("Genji", "guiprojfix/images/genji.png"),
    7: ("Hanzo", "guiprojfix/images/hanzo.png"),
    8: ("Junkrat", "guiprojfix/images/junkrat.png"),
    9: ("Mei", "guiprojfix/images/mei.png"),
    10: ("Pharah", "guiprojfix/images/pharah.png"),
    11: ("Reaper", "guiprojfix/images/reaper.png"),
    12: ("Sojourn", "guiprojfix/images/sojourn.png"),
    13: ("Soldier: 76", "guiprojfix/images/soldier76.png"),
    14: ("Sombra", "guiprojfix/images/sombra.png"),
    15: ("Symmetra", "guiprojfix/images/symmetra.png"),
    16: ("Torbin Time", "guiprojfix/images/torbjorn.png"),
    17: ("Tracer", "guiprojfix/images/tracer.png"),
    18: ("Venture", "guiprojfix/images/venture.png"),
    19: ("Widowmaker", "guiprojfix/images/widowmaker.png")
}
supp_heroes = {
    1: ("Ana", "guiprojfix/images/ana.png"),
    2: ("Baptiste", "guiprojfix/images/baptiste.png"),
    3: ("Brigitte", "guiprojfix/images/brigitte.png"),
    4: ("Illari", "guiprojfix/images/illari.png"),
    5: ("Juno", "guiprojfix/images/juno.png"),
    6: ("Kiriko", "guiprojfix/images/kiriko.png"),
    7: ("Lifeweaver", "guiprojfix/images/lifeweaver.png"),
    8: ("Lucio", "guiprojfix/images/lucio.png"),
    9: ("Mercy", "guiprojfix/images/mercy.png"),
    10: ("Moira", "guiprojfix/images/moira.png"),
    11: ("Zenyatta", "guiprojfix/images/zenyatta.png")
}

def tank_rand():
    index = random.randint(1, len(tank_heroes))
    name, image_path = tank_heroes[index]
    hero_text.config(text=f"Your selected hero is {name}")
    img = ImageTk.PhotoImage(Image.open(image_path)) 
    #this is the old code that didn't work with png and jpg
    #img = PhotoImage(file=img_p)
    hero_image_label.config(image=img)
    hero_image_label.image = img

def dps_rand():
    index = random.randint(1, len(dps_heroes))
    name, image_path = dps_heroes[index]
    hero_text.config(text=f"Your selected hero is {name}")
    img = ImageTk.PhotoImage(Image.open(image_path)) 
    hero_image_label.config(image=img)
    hero_image_label.image = img

def supp_rand():
    index = random.randint(1, len(supp_heroes))
    name, image_path = supp_heroes[index]
    hero_text.config(text=f"Your selected hero is {name}")
    img = ImageTk.PhotoImage(Image.open(image_path)) 
    hero_image_label.config(image=img)
    hero_image_label.image = img

window = Tk()
window.title("Overwatch Hero Picker")

hero_text = Label(window, text="Pick a role to get a hero!", font=("Arial", 16))
hero_text.pack(pady=10)

hero_image_label = Label(window)
hero_image_label.pack()

Button(window, text="Tank", command=tank_rand, width=15).pack(pady=5)
Button(window, text="DPS", command=dps_rand, width=15).pack(pady=5)
Button(window, text="Support", command=supp_rand, width=15).pack(pady=5)

window.mainloop()
