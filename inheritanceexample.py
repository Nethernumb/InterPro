#Mason


class Pet: 
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):     #This is a method
        print(f"{self.name} made a stupid noise")
    
    def info(self):
        print(f"{self.name} is a {self.species}")

class Dog(Pet):
    def __init__(self, name, species, tail_length, breed):
        super().__init__(name, species)
        self.tail_length = tail_length
        self.breed = breed
        
    def speak(self):
        super().speak()
        print(f"{self.name} barks")

    def info(self):
        super().info()
        print(f"{self.name} is a {self.breed} with a tail that is {self.tail_length} inches long.")

my_dog = Dog("Fido", "dog", 40, "Chiwawa")

my_dog.speak()