num = int(input())
if(num >=2 and num <=20):
    for i in range(1,11):
        result = num * i
        print(num,"x",i,"=",result)
else:
    print("Please Enter 2 to 20")        