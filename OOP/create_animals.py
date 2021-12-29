import animal #animal.py 
import sys

#importing a different file.
#creating an instance of Animal
#using command line arguments as parameters

#sys.argv[0] is the name of the file
animal_instance = animal.Animal(sys.argv[1], sys.argv[2], sys.argv[3])


animal_instance.print_info()

