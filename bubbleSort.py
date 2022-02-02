#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    x = len(a)
    kutir = 0
    for i in range(0,x):
        for j in range(0,x):
            if  j<x-1 and a[j]>a[j+1] :
                a[j + 1],a[j] = a[j],a[j + 1]
                kutir = kutir + 1
    print("Array is sorted in",kutir,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[x-1])            
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
