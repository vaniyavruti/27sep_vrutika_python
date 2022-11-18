""" Write a Python program to combine two dictionary adding values for 
common keys.  """

from collections import Counter
n1 = {'a': 100, 'b': 200, 'c':300}
n2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(n1) + Counter(n2)
print(d)
