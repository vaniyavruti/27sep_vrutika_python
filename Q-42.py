""" Write a Python function that checks whether a passed string is 
palindrome or not  """
s = input("Enter a string")
revstr = (s[::-1])
if revstr == s:
    print("palindrom")
else:
    print(("not palindrom"))
    