# Taxi Fare Calculator
# For the first 5 kms fare is 30/km
# For the next km onwards fare is 20/km

km = float(input('Enter Distance Travelled =',))

a = 20
b = 150

if km <=5:
    bb = km*30
    print('fare is',bb)
else:
    d = km - 5
    c = d*20
    print('fare is',a+b+c) 