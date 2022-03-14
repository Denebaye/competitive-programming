import sys

def solver(n,uniques):
    for i in range(1,n + 1):
        if i > uniques:
            print( i, end = " ")
        else:
            print(uniques, end = " ")
    print()


input = sys.stdin.readline
tests = int(input())

while tests:
    n = int(input())
    types = set((map(int,input().split())))
    solver(n,len(types))
    tests -= 1

# time and space complexity
# time O(n)
# space O(n)