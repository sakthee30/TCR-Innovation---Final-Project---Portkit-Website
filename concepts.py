#VARIABLES
#Legal Variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names
2myvar = "John"
my-var = "John"
my var = "John"

#NOTE : Remember that variable names are case-sensitive

#Multi Words Variable Names
#Camel Case -> each word except the first, starts with capital letter

myVariableName = "John"

#Pascal Case -> each word starts with a capital letter
MyVariableName = "John"

#Snake Case -> each word is separated by an underscore character
my_variable_name = "John"

#Global Variables
#Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

#If you create a variable with the same name inside a function, this variable will be local and can only be used inside the function
def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#GLOBAL keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)