# Print First 10 Numbers using while loop

i = 1
while i <= 10:
    print(i)
    i += 1

# For loop to print first 100 numbers

for i in range(1,101):
    print(i,end=" ")

#Print table of 2 till 100 using for loop

for i in range(2,101,2):
    print(i, end = " ")

# Print sum of first 5 numbers using for loop

sum = 0
for i in range(1,6):
    sum += i
print("Sum of First 5 Numbers is ",sum)    