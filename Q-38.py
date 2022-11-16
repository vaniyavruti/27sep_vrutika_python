""" Write a Python program to create a dictionary from a string.  """

str1 = 'python'
dict = {}
for letter in str1:
dict[letter]=dict.get(letter,0)+1
print(dict)
