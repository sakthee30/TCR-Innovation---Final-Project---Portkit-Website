#ython interpreter executes line by line and it is a case sensitive language

print('Hello World')
print('o----')
print(' ||||')
print('*' * 10)

#Variables
price = 10
rating = 4.9
name = 'Sakthee'
is_published = True
print(price)

patient_name = 'John Smith'
age = 20
is_new_patient = True
print(patient_name,age,is_new_patient)

#etting input from user
'''Expression - piece of code that produces a value'''
user_name = input('Enter your name: ')
print('Hello ' + user_name)

#TASK: Take 2 inputs name and color and print name likes color'''
name = input('Enter your name: ')
color = input('Enter your favorite color: ')
print(name + ' likes ' + color)

#Type conversion
'''Take year of born and print age'''
birth_year = input('Enter your birth year: ')
'''without int() it throws error because taking string as input but trying to return integer value'''
age = 2025 - int(birth_year)
print(age)

'''Take user their weight (in pounds), convert it to kilograms'''
weight_lbs = input('Enter your weight in (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

'''Strings'''
course = 'Python course for "Beginners"'
course = "Python's course for Beginners"
course = ''' 
Hi Sakthee,
Here is my first email.

Thankyou,
Regards.

'''
print(course)

'''To access elements in string'''
'''python index starts with 0'''
course = 'Python for Beginners'
print(course[0])
print(course[-1])
print(course[0:5]) 
print(course[0:])
print(course[:5])
print(course[1:-1])

'''Formatted String - to dynamically generates text in variables'''
first = 'Sakthee'
last = 'P'
message = first + ' [' + last + '] is a coder'
print(message)

'''TASK : To print Sakthee [P] is a coder'''
msg = f'{first} [{last}] is a coder'
print(message)

'''String Methods'''
course = 'Python for Beginners'
print(len(course))
'''To use string methods we use . operator'''
print(course.upper())
print(course.lower())

'''prints the first index of that particular occurrence'''
print(course.find('P'))

'''to replace character/string'''
print(course.replace('Beginners', 'Absolute Beginners'))

'''to check the existence of the charcter/string'''
'''Returns the boolean value'''
print('Python' in course)

'''
upper(), lower(), title(), find(), replace()
'''

'''Arithmetic operator'''
print(10 + 3)
'''
(+, -, *, /, //, %(reminder of division), **(exponent (power of))
'''
x = 10
x = x + 3
'''
[x += 3] augumented assignment operator
'''

'''operator precedence (BODMAS)
parenthesis
exponentiation
multiplication or division
addition or subtraction
'''
x = (10 + 3) * 2 - 1 
print(x)

'''Math Function'''
x = 2.9
print(round(x))
print(abs(-2.9))

'''importing math module'''
import math
n = 2.5
math.ceil(n)
math.floor(n)

'''If statements'''
is_hot = True
if is_hot:
    print("It's a hot day")
print("Enjoy your day")

#Exceptions - to handle errors
try:
    age = int(input('Enter your Age: '))
    print(age)
except ValueError:
    print('Invalid value')

#Generating Random Values (built in modules in python)
# refer chrome for more

#generating random values
import random
for i in range(3):
    #prints new random value between 0 to 1
    print(random.random())
    #print random value between 10 and 20
    print(random.randint(10,20))

members = ['Sakthee', 'Jai', 'Vani', 'Aathi']
#print random string from this list
random.choice(members)