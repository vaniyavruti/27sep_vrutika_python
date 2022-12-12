# Write a Python program to read a file line by line store it into a variable.
fl = open("test.txt","r")
str = ""
for i in  range(0,100):
    str = str + fl.read(i)
print(str)

"""variable = fl.readlines()
print(variable)"""


