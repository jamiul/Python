# Enter your code here. Read input from STDIN. Print output to STDOUT

tc = int(input())
even = ''
odd = ''
for i in range(0,tc):
    S = (input())
    for j in range(len(S)):
        if(j==0 or j%2==0):
            even+=S[j]
        else:
             odd+=S[j]
    print(even+" "+odd)
    even = ''
    odd = ''


      
            

