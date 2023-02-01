import sys
import heapq
from collections import defaultdict
from functools import lru_cache
import threading

############ ---- Input Functions ---- ############
def Iinput():
    return(int(input()))
def Lsinput():
    return(list(map(input().split())))
def Linput():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def two():
    return(map(int,input().split()))

@lru_cache()
def solve(remaining):
    if remaining < 0:
        return sys.maxsize
    if remaining == 0:
        return 0
    temp = sys.maxsize
    for change in [1,5,10,20,100]:
        temp = min(temp, solve(remaining - change))
    
    return temp + 1
    
def solution():
    
    output = solve(Iinput())
    if output == sys.maxsize + 1:
        print(-1)
    else:
        print(output)

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
thread = threading.Thread(target= solution)
thread.start(); thread.join()
# solution()