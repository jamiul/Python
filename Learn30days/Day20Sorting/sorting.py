import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numberOfSwaps = 0
for i in range(0,len(a)-1):
    for j in range(0,len(a)-1-i):
        if a[j] > a[j+1]:
            numberOfSwaps+=1
            a[j],a[j+1] = a[j+1],a[j]



print("Array is sorted in",numberOfSwaps,"swaps.")
print("First Element:",a[0])
print("Last Element:",a[-1])
