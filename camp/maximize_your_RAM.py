import sys
input = sys.stdin.readline
tests = int(input())
while tests:
    nor,curr_RAM = map(int,input().split())
    usage = list(map(int,input().split()))
    adition = list(map(int,input().split()))

    options = []
    
    for i in range(nor):
        options.append((usage[i],adition[i]))
        
    options.sort()
    
    tot_RAM = curr_RAM
    for option in options:
        if option[0] <= tot_RAM:
            tot_RAM += option[1]
        else:
            break
        
    print(tot_RAM)
    tests -= 1
    



