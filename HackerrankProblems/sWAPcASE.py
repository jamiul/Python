'''
Sample Input:
HackerRank.com presents "Pythonist 2".
Sample Output:
hACKERrANK.COM PRESENTS "pYTHONIST 2".
'''
'''
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
'''

'''
Str1=input("Enter the string to be converted lowercase: ")

for i in range (0,len(Str1)):

   x=ord(Str1[i]) # The ord() method returns an integer representing the Unicode code point of the given Unicode character.Ex 65 = A
   if x>=65 and x<=90: # if x>=97 and x <=122
       x=x+32 # x=x-32
   y=chr(x) # The chr() method is the inverse of ord()
   print(y,end="")
   '''
