def div(x,y):
    try:
        result = x // y
    except Exception as e:
        raise("Can not divided by Zero\n",e)
    finally:
        print("Executed !!")
    return result

print(div(4,2))
