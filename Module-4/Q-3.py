# Write a Python program to read first n lines of a file.
fl = open('test.txt','r')
n =int(input("How many lines to  display")) 
if n < 0:
    print("Kindly enter the intger values")
else:
    for i in range(n+1):
        line = fl.readline()
        print(line)
 
"""def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_head('test.txt',2)"""
