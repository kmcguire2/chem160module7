s = input("Enter DNA string: ")
comp = {"G":"C","C":"G","A":"T","T":"A"}
slist = list(s)
rs = ""

#create complementary strand and reverse it
for i in slist:
    rs = comp[i] + rs

if rs == s:
    print("DNA Palindrome")
else:
    print("Not DNA Palindrome")
