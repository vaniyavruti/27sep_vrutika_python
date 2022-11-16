"""  Write a Python script to sort (ascending and descending) a dictionary by 
value. """

import operator
d = {'python': 90, 'java':80,'cpp':100,'php':60}
print(d)
asc = dict(sorted(d.items(), key = operator.itemgetter(1)))
print("ascending =",asc)

dsc = dict(sorted(d.items(), key = operator.itemgetter(1), reverse = True))
print("descending =",dsc)



 
