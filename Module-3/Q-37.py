"""  Write a Python program to combine values in python list of dictionaries. """

from collections import Counter
list = [{'item': 'item1', 'amount': 500}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 650}]
result = Counter()
for d in list:
    result[d['item']] += d['amount']
print(result) 
