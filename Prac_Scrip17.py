# Write a program to find the sum of the following series:
# s = 1 + 4 - 9 + 16 - 25 + 36 - ..............n terms

num = int(input('Enter the number of terms: '))
num1 = num - 1
num2 = num - 2
i = 2
s = 0
if num1%2 == 0:
    i = 2
    s = 0
    c = 0
    while i <= num1:
        s = s + (i*i)
        i += 2
    b = s
else:
    while i <= num:
        s = s + (i*i)
        i += 2
    b = s
    c = 0

j = 3
t = 0
if num2%2 == 0:
    t = 0
    while j <= num1:
        t = t + (j*j)
        j += 2
    c = t
else:
    while j <= num:
        t = t + (j*j)
        j += 2
    c = t

if num <0:
    print('Enter a positive number')
elif num == 0:
    print('Enter a number greater than 0')
elif num == 1:
    print('the sum of the series is 1')
elif num == 2:
    print('The sum of the series is 5')    
else:
    print('The sum of the series is: ',1+b-c)