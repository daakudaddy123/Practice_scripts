# Write a program to check wheather a number is prime or not

num = int(input("Enter a number: "))
i = 1
if num <=1:
    print("Not a prime number")
elif num == 2:
    print("Prime number")
else:
    for i in range(2,(num//2)+1):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
        