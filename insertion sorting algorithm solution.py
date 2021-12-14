#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def printarr(arr):
    for num in arr:
        print(num, end = " ")
    print()
        
def insertionSort1(n, arr):
    last_ele = arr[n-1]
    
    for i in range(n-2 , -1, -1):
        if last_ele < arr[i]:
            arr[i+1] = arr[i]
            printarr(arr)           
        else:    
            arr[i+1] = last_ele
            printarr(arr)
            break 
            
    if(arr[0] > last_ele):
            arr[0] = last_ele
            printarr(arr)
            
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
