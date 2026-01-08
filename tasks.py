'''Loops'''
'''sum of numbers'''
numbers = [10,20,30,40,66,74,84,34]
total = 0
for i in numbers:
    total = total + i
print(total)

'''unique elements in a list'''
numbers = [10,4,4,5,60,78,20,20]
unique =[]
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)

'''pattern printing'''
for row in range(1,6):
    '''1,(1+1) -> (1,2)'''
    for col in range(1,row+1):
        print("*", end="")
    print()

for row in range(5,0,-1):
    for col in range(1, row+1):
        print("*", end="")
    print()

for row in range(1,6):
    for col in range(1, row+1):
        print(col, end="")
    print()

for row in range(5,0,-1):
    for col in range(1, row+1):
        print(col, end="")
    print()

'''
1
22
333
4444
55555
'''
for row in range(1,6):
    for col in range(1,row+1):
        print(row, end="")
    print()

'''Dictionary'''
'''TASK
get a number input and print one, two, three, four
'''
numbers=input("Enter the number: ")
dict_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}
for number in numbers:
    output = dict_mapping.get(number)
print(output)

'''Emoji converter'''
message = input(">")
words = message.split(' ')
emojis = {
    ":)" : "🙂",
    ":(" : "😔"
}
out = ""
for word in words:
    out += emojis.get(word, word) + " "
print(out)

