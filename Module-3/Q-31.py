""" Write a Python script to merge two Python dictionaries  """

n1 = {'a': 100, 'b': 200}
n2 = {'c': 300, 'd': 200}
d = n1.copy()
d.update(n2)
print(d)
