#Modules 
# it is a file with some python code
# we use modules to organize our code into files (eg:sections in supermarket)
# Insted of writing all functions and classes in .py file, we want to break up our code into multiple files.
# We refer to each file as a module
# with this module, we can reuse our code easily

#Let's say we can put these 2 functions into a module called converters.py, then we can import that module into any program that needs these converter functions

#create a new file with the name converters.py
import converters
print(converters.lbs_to_kg(65))

#we can also import specific functions in the program
import converters
from converters import lbs_to_kg

lbs_to_kg(65)