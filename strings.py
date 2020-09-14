str1 = "Hello World"
print(str1)

str2 = '1 2 3 4 5 6'
print(str2)

str4 = str1 + str2 #concatenates the strings
print(str4)

greetings = 4*"Hi " #math operations work
print(greetings)

str5 = "When in the course of human events"
print(len(str5)) #how many characters

#substrings, like indexing a list
print(str5[0])
print(str5[24:])
print(str5[5:17])

# compare using if statement
s1 = "alpha"
s2 = "beta"
s3 = s1 + s2
if s3 == "alphabeta":
    print(s3)


# if you iterate over a string, it prints each successive character
string = "abcdefg"
for i in string:
    print(i)
