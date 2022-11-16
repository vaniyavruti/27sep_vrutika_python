""" Write a Python program to map two lists into a dictionary  """

keys = ['red', 'green', 'blue']
values = ['#FF0000',' #008000','#0000FF']
colour_dict = dict(zip(keys,values))
print(colour_dict)