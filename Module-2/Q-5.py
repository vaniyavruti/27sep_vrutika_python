#Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.
num = int(input("Enter your number:-"))
remainder = num % 2
if remainder > 0: #or if (remainder == 0):
    print("odd nummber:")
else:
    print("even number:")