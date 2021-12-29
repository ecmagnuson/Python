import sys

def animal_info(species, age, weight):
    print(species)
    print(age)
    print(weight)
    

animal_info(sys.argv[1], sys.argv[2], sys.argv[3])
