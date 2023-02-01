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
    total = Int()
    print(max(0,((total - 3)//3) - 1))
