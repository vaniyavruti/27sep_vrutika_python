""" Write a Python program to find the highest 3 values in a dictionary """

from heapq import nlargest
my_dict = {'a':500, 'b':4000, 'c': 560,'d':2550, 'e':5874, 'f': 20}  
three_largest = nlargest(3, my_dict, key=my_dict.get)
print(three_largest) 
