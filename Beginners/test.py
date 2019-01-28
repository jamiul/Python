z = 10

def func1():
       global z
       z = 3

def func2(x,y):
      global z
      return x+y+z

func1()
total = func2(4,6)
print(total)
