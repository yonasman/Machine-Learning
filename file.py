# working with files
import os
import urllib.parse
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
# working with regular expressions
# reading a file and compute the sum of numbers in the text
import re
def read_and_compute_sum(filename):
    sum = 0
    with open(filename) as file:
        for line in file:
            nums = re.findall('[0-9]+',line)
            if len(nums) > 0:
                for num in nums:
                    sum += int(num)
    return sum
# print(read_and_compute_sum('regex_sum_2117125.txt'))
# parsing xml
import xml.etree.ElementTree as ET
def xmlParser():
    data = '''
    <parent>
        <name>Yonas</name>
        <age>23</age>
        <email hide="yes">yonpython@gmail.com</email>
    </parent>
    '''
    tree = ET.fromstring(data)
    print("Name:", tree.find('name').text)
    print("attr:", tree.find('email').get('hide'))
# xmlParser()
def xmlParser_2():
    data= '''
    <staff>
        <users>
            <user>
                <id>001</id>
                <name>yonas</name>
            </user>
            <user>
                <id>002</id>
                <name>john</name>
            </user>
        </users>
    </staff>
    '''
    staff = ET.fromstring(data)
    users = staff.findall('users/user')
    print("Number of users:", len(users))
    for user in users:
        print("id:", user.find('id').text)
        print("name:",user.find('name').text)
# xmlParser_2()
# read from url and parse xml
import urllib.request
def read_and_parse():
    url = input("Enter your url: ")
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    # parse the xml
    tree = ET.fromstring(data)
    counts = tree.findall(".//count")
    total_sum = 0
    for count in counts:
        total_sum += int(count.text)
    return total_sum
print(read_and_parse())