def ConvertBinary(num):
    if num > 1:
        ConvertBinary(num // 2)
    print(num % 2,end='')

num = 13
ConvertBinary(num)
