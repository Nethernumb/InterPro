#Mason Shaw
#Project 4 - GUI Project


import random
from tkinter import *
#in order to use png, jpeg, and jpg you need pillow (PIL)
from PIL import ImageTk, Image

#----------------------------------------------------------------------------#
#                       DICTIONARIES FOR EACH HERO                           #
#----------------------------------------------------------------------------#
tank_heroes = {
    1: ("D.VA", "images/dva.png"),
    2: ("DoomFist", "images/doomfist.png"),
    3: ("Hazard", "images/hazard.png"),
    4: ("Junker Queen", "images/junkerqueen.png"),
    5: ("Mauga", "images/mauga.png"),
    6: ("Orisa", "images/orisa.png"),
    7: ("Ramattra", "images/ramattra.png"),
    8: ("Reinhardt", "images/reinhardt.png"),
    9: ("Roadhog", "images/roadhog.png"),
    10: ("Sigma", "images/sigma.png"),
    11: ("Winston", "images/winston.png"),
    12: ("Wrecking Ball", "images/wreckingball.png"),
    13: ("Zarya", "images/zarya.png")
}
dps_heroes = {
    1: ("Ashe", "images/ashe.png"),
    2: ("Bastion", "images/bastion.png"),
    3: ("McCree", "images/mccree.png"),
    4: ("Echo", "images/echo.png"),
    5: ("Freyja", "images/freyja.png"),
    6: ("Genji", "images/genji.png"),
    7: ("Hanzo", "images/hanzo.png"),
    8: ("Junkrat", "images/junkrat.png"),
    9: ("Mei", "images/mei.png"),
    10: ("Pharah", "images/pharah.png"),
    11: ("Reaper", "images/reaper.png"),
    12: ("Sojourn", "images/sojourn.png"),
    13: ("Soldier: 76", "images/soldier76.png"),
    14: ("Sombra", "images/sombra.png"),
    15: ("Symmetra", "images/symmetra.png"),
    16: ("Torbin Time", "images/torbjorn.png"),
    17: ("Tracer", "images/tracer.png"),
    18: ("Venture", "images/venture.png"),
    19: ("Widowmaker", "images/widowmaker.png")
}
supp_heroes = {
    1: ("Ana", "images/ana.png"),
    2: ("Baptiste", "images/baptiste.png"),
    3: ("Brigitte", "images/brigitte.png"),
    4: ("Illari", "images/illari.png"),
    5: ("Juno", "images/juno.png"),
    6: ("Kiriko", "images/kiriko.png"),
    7: ("Lifeweaver", "images/lifeweaver.png"),
    8: ("Lucio", "images/lucio.png"),
    9: ("Mercy", "images/mercy.png"),
    10: ("Moira", "images/moira.png"),
    11: ("Zenyatta", "images/zenyatta.png")
}

def tank_rand():
    index = random.randint(1, len(tank_heroes))
    name, image_path = tank_heroes[1]
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
    name, image_path = supp_heroes[11]
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
