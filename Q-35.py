""" Write a Python program to create and display all combinations of letters, 
selecting each letter from a different key in a dictionary.  """

d = {"a":["a","b","c"], "b":["c","d","e"]}
l = list(d.values())
for com  in l[1:]:
    for i in l[0]:
        for j in com:
            print(i+j )