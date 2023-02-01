def Int():
    return(int(input()))
def Lstring():
    return(list(map(input().split())))
def List():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def two():
    return(map(int,input().split()))

    
for _ in range(Int()):
    row,col = two()
    print("Tonya") if (row + col) % 2 == 0 else print("Burenka")