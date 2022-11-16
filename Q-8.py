"""   Write a Python program to convert a list of characters into a string. """

def convert(s):
    new = ""
    for i in s:
        new +=i
        return new
        s = ['p','y','t','h','o','n']
        print(convert(s))

"""s = ['a', 'b', 'c', 'd']
str1 = ''.join(s)
print(str1)"""