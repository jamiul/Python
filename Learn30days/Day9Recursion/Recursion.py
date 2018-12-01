def Factorial(num):
    if num <= 1 :
        return 1
    else:
        return num*Factorial(num-1)


num = int(input())
result = Factorial(num)
print(result)            
