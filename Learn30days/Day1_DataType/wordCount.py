strn = str(input())
b = strn.lower().split(" ")
lcnt = 0
Mcnt = 0
Lcnt = 0
rcnt = 0
for i in b:
    if (i == 'lol') :
        lcnt = lcnt + 1
    elif(i == 'lmao'):
        Mcnt = Mcnt + 1

    elif (i == 'lel'):
        Lcnt = Lcnt + 1
    elif (i == 'rofl') :
        rcnt = rcnt + 1    

sumlol = (lcnt*1 + rcnt*2 + Mcnt*3 + Lcnt*4)
if (1<= sumlol and sumlol <= 5):
    print("Patient has bright red face")
elif (6 <= sumlol and sumlol <= 12):
    print("Patient is unable to speak")
elif (13 <= sumlol and sumlol<=20):
    print("Patient's sides are mildly bruised") 
elif (21 <= sumlol and sumlol<=30):
    print("Patient has broken jaw, fractured ribs")
elif (31 <= sumlol and sumlol<=49):
    print("Patient is in a coma")
else:
    print("Patient is dead")                 

      
