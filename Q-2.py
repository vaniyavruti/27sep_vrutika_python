"""   Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given 
list of strings.     """

s = 0
list1 = ['aba', '121', 'kgf', 'abc']
for i in list1:
    if len(i)>1 and i[0]==i[-1]:
        print("the given words":,i) 
        s=s+1
print("No. of words you want:",i)

