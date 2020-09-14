import sys
from collections import Counter
import os
from os import path

filename = input("Enter the name of the file: ")
if not os.path.exists(filename):
    sys.exit("Cannot find file given")
file = open(filename, "r")

words = []

#read file line by line and print
while 1:
    line = file.readline()
    if line == "":
        break
    #take all elements in one list, appends to other list
    words.extend(line.split())

#convert all characters to lowercase
words_lower = []
for i in words:
    words_lower.append(i.lower())
words = words_lower


counts = Counter(words) #counter object

# loop over counts, a dictionary
for i in counts:
    print("%2d: %s" %(counts[i], i))
