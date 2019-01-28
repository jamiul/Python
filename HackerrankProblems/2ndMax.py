'''n = int(input())
a = [int(x) for x in input().split()]
largest = secondlargest = -100
for x in a:
    if x > largest:
        secondlargest = largest
        largest = x
    elif x > secondlargest and x != largest:
        secondlargest = x
print(secondlargest)'''

ara = [2,3,4,5,6]
for x in ara:
    print(x)
