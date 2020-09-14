import sys
import os
from os import path

filename = input("Enter the name of the file: ")
if not os.path.exists(filename):
    sys.exit("Cannot find file given")
file = open(filename, "r")

#read file line by line and print
while 1:
    line = file.readline()
    print(line, end = "")
    if line == "":
        break
