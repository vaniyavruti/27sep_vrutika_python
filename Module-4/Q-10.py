# Write a Python program to write a list to a file.

# list of names
names = ['Dip', 'Python', 'Rajkot']
fl = open('test.txt', 'w') # as fl:
for item in names:
        fl.write("%s \n" %item)
print('Done')