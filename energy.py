str1 = "Energy= 10.452 Momentum= 22.313"
str2 = "Energy= 11.134 Momentum= 31.357"
str1list = str1.split()
str2list = str2.split()

#print sum of second fields by parsing
print(str1list[1] + str2list[1])

#use float command to force values into numeerical values
print(float(str1list[1]) + float(str2list[1]))
