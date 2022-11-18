""" Write a Python program to find the second smallest number in a list.   """


def second_smallest(numbers):
  if (len(numbers)<2):
    return
  if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
    return
  dup_items = set()
  uniq_items = []
  for i in numbers:
    if i  not in dup_items:
      uniq_items.append(i)
      dup_items.add(i)
  uniq_items.sort()    
  return  uniq_items[1]   

print(second_smallest([3,4,1,5,2,6]))








