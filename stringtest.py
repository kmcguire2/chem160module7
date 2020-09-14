#converting string to list breaks it up into individual characters
string = "abcdefghi"
alist = list(string)
print(string)
print(alist)

alist.reverse() #reverse the order of characters in the list

newstring = "".join(alist) #joins the list back into a string
print(newstring)

newstring2 = "-".join(alist) #linking character
print(newstring2)
