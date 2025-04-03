



# class Character:
#     def __init__(self, health, damage, speed):
#         self.health = health
#         self.damage = damage
#         self.speed = speed
#     def double_speed(self):
#         self.speed *= 2

# warrior = Character(100, 50, 10)
# ninja = Character(80, 40, 40)

# print(f"Warrior Speed: {warrior.speed}")
# print(f"Ninja speed: {ninja.speed}")
# warrior.double_speed()
# ninja.double_speed()  
# print(f"Warrior Speed: {warrior.speed}")
# print(f"Ninja Speed: {ninja.speed}")

class Pet: 
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def bark(self):     #This is a method
        if self.species == "dog":
            return f"{self.name} barks"
        return f"{self.name} is not a dog."
    def meow(self):
        if self.species == "cat":
            return f"{self.name} meows"
        return f"{self.name} is not a car"
    
    def info(self):
        return f"{self.name} is a {self.species}"
    
dog = Pet(input("What is your dogs name? "), "dog")
cat = Pet("Mittens", "cat")

print(dog.bark())
print(dog.info())