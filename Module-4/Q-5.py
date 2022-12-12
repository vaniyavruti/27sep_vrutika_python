# Write a Python program to read a file line by line and store it into a list.
fl = open("test.txt","r")
list = fl.readlines()
print(list)