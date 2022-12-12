# Write a python program to find the longest words.
str = input("Enter the line:")
max = 0
for i in str.split():
    if (len(i)> max and i.isalpha()):
        max = len(i)
        a = i
        print(a)