# Write a Python program to read last n lines of a file. 

n = int(input("Enter the lines:-"))
fl = open("test.txt","r")
for line in (fl.readlines() [-n:]):
    print(line,end="")
    fl.close()
