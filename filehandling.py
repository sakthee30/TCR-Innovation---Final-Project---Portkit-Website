#file handling allows python programs to create, read, write and modify files stored on computer
#python provides a built-in-function called open() to work with files

#opening a file
#syntax
file = open("filename", "mode")

#commonmodes
'''
r -> read mode
w -> write mode
a -> append mode
r+ -> read + write
w+ -> write + read
a+ -> append + read

'''
#reading from a file

#read() -> reads entire file
f = open("data.txt","r")
content = f.read()
print(content)
f.close()

#readline() -> reads one line
f = open("data.txt","r")
line = f.readline()
print(line)
f.close()

#readlines() -> reads all lines as list
f = open("data.txt","r")
lines = f.readlines()
print(lines)
f.close()

#writing to a file
#write()
f = open("data.txt","r")
f.write("Hello World")
f.close()

#append mode
f = open("data.txt","a")
f.write("\n new line added")
f.close()

#closing the file
f.close()

#using with open() -> automatically closes the file
with open("data.txt", "r") as f:
    content = f.read()
    print(content)

#loop through each line
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())

#to delete a file
#to delete a file, we must import the OS module and run its os.remove() function
import os
os.remove("file.txt")

#TASK 
#count number of lines in a file
def count_of_line(file_path):
    count = 0
    with open(file_path, "r") as f:
        for line in f:
            count += 1
    return count

file_path = "sample.txt"
line_count = count_of_line(file_path)
print(f"Number of lines: {line_count}")

#counting the number of lines using pandas 
import pandas as pd

def count_of_rows(file_path):
    df = pd.read_excel(file_path)
    return len(df)

file_path = r"C:\Users\sakthep\OneDrive - Capgemini\SAKTHEE\projects\python practice\Adv Python\output.xlsx"
row_count = count_of_rows(file_path)
print(row_count)