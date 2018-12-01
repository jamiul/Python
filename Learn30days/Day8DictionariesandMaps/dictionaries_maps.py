# Take input in a Dictionary

num = int(input())
pair = dict()
for i in range(0,num):
    word = input().split()
    key = word[0]
    value = word[1]
    pair[key] = value
for n in range(0,num):
    test = str(input())
    if test in pair:
        print(test,pair[test],sep='=')
    else:
        print("Not found")
