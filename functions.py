#functions
def greet_user():
    print('Hi there!')
    print('Welcome onboard')


#call the function
greet_user()

#function with parameters
def greet(name):
    print(f'Hi {name}!')

greet("Sakthee")

#Write a function that takes two numbers and returns their sum.
def add_numbers(a, b):
    return a + b

# Example usage:
result = add_numbers(5, 10)
print("Sum:", result)

#Create a function that checks if a given number is even or odd.
def check_odd_even(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "odd"

ans = check_odd_even(3)
print(ans)

#Define a function that takes a list and returns the maximum element.
def max_ele():
    list = [1,20,3,40,30]
    max = list[0]
    for number in list:
        if number > max:
            max = number 
    return max

result = max_ele()
print(result)

#Create a function that accepts a list and returns a new list with only unique elements.
def unique_element():
    numbers = [10,10,3,3,5]
    new_list = []
    for number in numbers:
        if number not in new_list:
            new_list.append(number)
    return new_list

answer = unique_element()
print(answer)

#function that counts how many tmes each word appears in a sentence
def count_of_word(sentence):
    words = sentence.lower().split()
    # Create a dictionary to store word counts
    word_count = {}

    #count each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

result = count_of_word("Python is easy and python is powerful")
print(result)

#Function that takes a sentence and returns a dic of word count
def word_count(input):
    word = input.lower().split()

    count_of_word = {}

    for x in word:
        if x in count_of_word:
            count_of_word[x] += 1
        else:
            count_of_word[x] = 1

    return count_of_word

output = word_count("Python is very powerful language")
print(output)

#function to remove duplicates from a list and returns a new list
def remove_duplicates():
    list = [10,10,3,5,4,3]
    unique = []

    for x in list:
        if x not in unique:
            unique.append(x)
    return unique

result = remove_duplicates()
print(result)


    
