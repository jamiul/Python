import math
dirnks = int(input())
if dirnks >= 10 and dirnks <= 700:
    dnk = dirnks
    frd = math.floor((dirnks/3))

    totalConsumed = 1000 - (dnk + frd)
    print(frd)
    print(totalConsumed)
    
else:
    print("Invalid Input")
    