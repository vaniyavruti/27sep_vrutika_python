# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
def num(x, y):
   if x == y or abs(x-y) == 5 or (x+y) == 5:
       return True
   else:
       return False
print(num(6, 1))
print(num(3, 2))
print(num(4, 1))
print(num(5, 5))
print(num(27, 45))