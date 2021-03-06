import sys
input = sys.stdin.readline
tests = int(input())
while tests:
    nor = int(input())
    candidate = list(map(int,input().split()))
    candidate.sort()
    pre_sum = candidate[0] + candidate[1]
    pos_sum = candidate[-1]
    
    left = 1
    right = len(candidate) - 1
    flag = True
    while left < right:
        if pre_sum < pos_sum:
            flag = False
            print("YES")
            break
        left += 1
        right -= 1
        pre_sum += candidate[left]
        pos_sum += candidate[right]
        
    if flag:
        print("NO")
        
    tests -= 1
    # time and space complexity
    # tiem = O(nlog(n))
    # space = O(1)