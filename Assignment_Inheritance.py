"""
Assignment:
- Hierarchical Inheritance
- Hybrid Inheritance

------------------------------------------------
1. Hierarchical Inheritance
Hierarchical inheritance occurs when one class serves as a
parent or base class for multiple child classes.

# Parent class

class Animal:
    def __init__(self, species):
        self.species = species

    def show_species(self):
        print("Animal belongs to the species: ",self.species)

# Child classes inheriting from Animal
class Dog(Animal):
    def sound(self):
        print("Woof !")

class Cat(Animal):
    def sound(self):
        print("Meow !")

# Creating instances of the child classes
dog = Dog('Canine')
cat = Cat('Feline')

# Accessing methods from the parent and child classes
dog.show_species() # Output: Animal belongs to the species:  Canine
dog.sound()        # Output : Woof !

cat.show_species() # Output: Animal belongs to the species:  Feline
cat.sound()        # Output: Meow !
#-------------------------------------------------------------------------------------------
"""
#2. Hybrid Inheritance

"""
Hybrid inheritance refers to a combination of multiple types of inheritance, 
such as a mix of single, multiple, hierarchical, or multilevel inheritance
"""

# Parent class 1
class Animal:
    def __init__(self, species):
        self.species = species

    def show_species(self):
        print("Animal belongs to the", self.species, "species.")

# Parent class 2
class SoundMaker:
    def make_sound(self):
        print("Making some sound...")

# Child class inheriting from Animal and SoundMaker
class Dog(Animal, SoundMaker):
    def sound(self):
        print("Woof!")

# Child class inheriting from Animal
class Cat(Animal):
    def sound(self):
        print("Meow!")

# Creating instances of the child classes
dog = Dog('Canine')
cat = Cat('Feline')

# Accessing methods from different inherited classes
dog.show_species()  # Output: Animal belongs to the Canine species.
dog.sound()         # Output: Woof!
dog.make_sound()    # Output: Making some sound...

cat.show_species()  # Output: Animal belongs to the Feline species.
cat.sound()         # Output: Meow!






