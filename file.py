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
    # if line.startswith('From:'):
    #     continue
    # elif line.startswith("From"):
    #     splittedLine = line.split()
    #     hours.append(splittedLine[5][:2])
     
# print(remove_punctuation("Hello, how you doing?"))
# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)
# hours = []

# for line in handle:
    #print(line)

# hours count hashmap
# hoursCount = {}

# for h in hours:
#     hoursCount[h] = hoursCount.get(h,0) + 1
    
# print hours with their count
# hourTuples = hoursCount.items()
# sortedHours = sorted(hourTuples)

# for k,v in sortedHours:
    # print(k,v)
# function to compare by len of string
def compareByLen(s):
    wordLenPair = []
    for word in s.split():
        wordLenPair.append((len(word),word))
    wordLenPair = sorted(wordLenPair)

    # build the final sorted list
    sortedList = []
    for length, word in wordLenPair:
        sortedList.append(word)
    return sortedList
# print(compareByLen('but soft what light in yonder window breaks'))