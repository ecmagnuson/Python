import sys

class Animal:
    
    def __init__(self, species, age, weight):
        self.species = species
        self.age = age
        self.weight = weight
    
    def print_info(self):
        print(self.species)
        print(self.age)
        print(self.weight)

animal_instance = Animal(sys.argv[1], sys.argv[2], sys.argv[3])


animal_instance.print_info()
