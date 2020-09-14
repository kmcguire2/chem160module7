import math

funcs = {"sqrt":math.sqrt, "log":math.log, "log10":math.log10} #values are functions

f = "start"
while f != "stop":
    n = int(input("Enter number: ")) #read in number, convert to int
    f = input("Function to perform or stop: ") #read in function name
    if not f in funcs: #is f in the dictionary?
          print("No such function")
    else:
        #if the function exists in the dictionary, apply it to the value
        print("Applyin function %s to %d gives %f"%(f,n,funcs[f](n)))
