"""  Write a Python function to get the largest number, smallest num and sum of all from a list.   """

List = []
Num = int(input(" enter Number: "))
for i in range(1, Num + 1):
    value = int(input(" enter the Value of %d Element : " %i))
    List.append(value)

print("The Smallest Element  : ", min(List))
print("The Largest Element  : ", max(List))
