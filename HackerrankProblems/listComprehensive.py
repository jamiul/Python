# Manually Program
'''x = int(input())
y = int(input())
z = int(input())
n = int(input())

empty_list = []
for a in range(x+1):
    for b in range(y+1):
        for c in range(z+1):
            if a + b + c != n:
                empty_list.append([a,b,c])
print(empty_list)'''
# Using List comprehension
x,y,z,n = (int(input()) for _ in range(4))

print([[i,j,k] for i in range(x+1)
               for j in range(y+1)
               for k in range(z+1)
                  if (i+j+k) != n])

#print(ara)
