# Write a Python program to count the number of lines  text file. 
fl = open("test.txt")
count = 0
content = fl.read()
conlist = content.split('\n')
#print(conlist)
for i in  conlist:
    if i:
        count+=1
        print("Number of line in file",count)
