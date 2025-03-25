# If statement to check wheather a number is positive or negative

num = int(input("Enter a number: "))
if num < 0:
    print("Negative number")
else:
    print("Positive number")

# If statement to check wheather a number is even or odd

num = int(input("Enter a number: "))
if num%2 == 0:
    print("Even number")
else:
    print("Odd number")

# If elif else statement to grade a student based on marks

marks = int(input("Enter the marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")