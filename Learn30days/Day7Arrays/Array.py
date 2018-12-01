#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    Input_array = []
    for i in range(n):
        Input_array.append(arr[n-i-1])
    Output_array = ''
    for j in range(len(Input_array)):
        Output_array+=str(Input_array[j])+' '

print(Output_array)
