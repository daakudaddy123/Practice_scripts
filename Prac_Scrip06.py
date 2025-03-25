# Find Factorial of a number given by the user

num = int(input("Enter a number: "))

if num < 0:
    print("Enter a positive number")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    print("The factorial of",num,"is",fact)        