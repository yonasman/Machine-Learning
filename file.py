# working with files
import os
# creating file
def create_file(filename):
    try:
        with open(filename,'w') as file:
            file.write("Hello, I am yonas")
    except IOError:
        print("Error while creating the file", filename)
def writing_to_file(filename):
    try:
        with open(filename, 'w') as file:
            file.write("Hello yonas, how you doing?")
    except IOError:
        print("Error while write to the file", filename)
def reading_file(filename):
    try:
        with open(filename,'r') as file:
            file.read()
    except IOError:
        print("Error while opening file", filename)
def appending_file(filename):
    try:
        with open(filename,'a') as file:
            file.write("I am an appended text")
    except IOError:
        print("Error while appending to file", filename)
def rename_file(filename, newname):
    try:
        os.rename(filename, newname )
    except IOError:
        print("Error while renaming file", filename)
# filename = input("Enter the filename: ")
# newname = input("Enter the new name: ")
# rename_file(filename,newname)
# create_file(filename)
# writing_to_file(filename)
# reading_file(filename)
# appending_file(filename)
# function that removes punctuations
import string
def remove_punctuation(s):
    newStr = s.translate(s.maketrans('Hello','hello',string.punctuation))
    return newStr
# print(remove_punctuation("Hello, how you doing?"))
