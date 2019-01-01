import sys

def string_integer(S):
    try:
        print(int(S))
    except ValueError:
        print("Bad String")
        return None

S = input().strip()
string_integer(S)
