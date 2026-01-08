is_hot = True
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

'''
TASK:
Price of a house is 1M. If buyer has good credit, they need to put down 10 %
otherwise they need to put down 20% and finally print the down payment
'''
price = 100000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f'Down Payment: {down_payment}')

'''Logical operators
use when we have multiple conditions (to combine two conditions)
eg: if applicant has high income AND good credit, then eligible for loan
AND: BOTH
OR: AT LEAST ONE
NOT
'''
has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print('Eligible for Loan')
elif has_good_credit and not has_criminal_record:
    print('Not Eligible for Loan')

'''Comparison operator'''
'''TASK: If name is less than 3 characters long, name must be at least 3 characters; 
otherwise if its more than 50 characters long, name can be a max of 50 characters;
otherwise name looks good'''
name = input('Enter your name: ')
if len(name) < 3:
    print("Name must be at least 3 characters long")
elif len(name) > 50:
    print("Name must be maximum of 50 characters long")
else:
    print("Name looks Good!")


'''While Loop
while condition:
    ...(when the wile condition is true, the block inside the loop gets executed)
'''

i = 1
while i<=5:
    print(i)
    i=i+1
print("Done")

i=1
while i<=5:
    print('*' * i)
    i=i+1
print("Done")

'''Guess number'''
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count <= guess_limit:
    guess = int(input('Guess the number: '))
    guess_count+=1
    if guess == secret_number:
        print('You win!')
        break
else:
    print('You lose!')

'''For loops'''
for item in 'Python':
    print(item)

for item in [1,2,3,4,5]:
    print(item)

'''when we deal with large number; we use range function'''
for item in range(5):
    print(item)
for item in range(5,10):
    print(item)
for item in range(1,10,2):
    print(item)

'''TASK: To calculate total cost in shopping Cart'''
prices = [10,20,30,40,50]
sum = 0
for i in prices:
    sum = sum + i
print(f"Total: {sum}")
    
'''Nested Loops - loop inside another loop; after completion of inner loop then takes to outer loop'''
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

'''TASK & HINT
XXXXX
XX
XXXXX
XX
XX
NUMBERS = [5,2,5,2,2]
'''
'''one method - this method is only available in python'''
numbers = [5,2,5,2,2]
for x_count in numbers:
    print('x' * x_count)

'''another method'''
numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

'''Lists -> mutable'''
names = ['Sakthee', 'Aathi', 'Jai']
print(names)
'''To access element in list'''
print(names[0])
print(names[1:])
names[0] = 'Sakthee P'
print(names)

'''Write a program to print largest number in list'''
'''create a variable max and compare each number with max'''
numbers = [3,6,2,10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

'''2D Lists -> 2 Dimensional Lists is a list where each item in list is another list and that list represents items in each row
123
456
789
'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)

numbers = [5,7,10,1,7,5]
numbers.append(20)
numbers.insert(1,50)
numbers.remove(1)
numbers.clear()
numbers.pop()
print(numbers.index(5))
numbers.count(5)
numbers.sort()
numbers.reverse()
numbers2 = numbers.copy()

'''program to remove duplicate in list'''
numbers = [2,2,4,6,3,6,1]
uniques = []
for number in numbers:
    if numbers not in uniques:
        uniques.append(number)
print(uniques)

'''Tuples -> are immutable'''
numbers = (1,2,3)
print(numbers[0])


'''Unpacking'''
coordinates = (1,2,3)
x = coordinates[0] 
y = coordinates[1] 
z = coordinates[2]

'''short way to achieve the above way'''
x,y,z = coordinates
print(x)
print(y)
print(z)

'''Dictionaries -> to store values as key value pair - not also duplicates'''
customer = {
    "name" : "Sakthee",
    "age" : 23,
    "is_verified" : True
}

'''to access elements in dic using GET method'''
print(customer.get("name"))
'''returns none if value is not listed in dict'''
print(customer.get("birthdate"))

'''to assign value to dcit'''
customer["birthdate"] = "Oct 30 2002"

