# FInd the sum of all numbers between a and b and print table of a and b
# where a and b are user input

a = int(input('Enter a =',))
b = int(input('Enter b =',))

sum = 0
for i in range(a,b+1):
    sum = sum + i
print('Sum of all numbers between',a,'and',b,'is',sum)

for i in range(a,a*11,a):
    print(i,end=' ')

for j in range(b,b*11,b):
    print(j,end=' ')    