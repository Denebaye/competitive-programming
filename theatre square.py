# m = int(input())
# n = int(input())
# a = int(input())

line = input()
line = line.split()
m = int(line[0])
n = int(line[1])
a = int(line[2])
x = m//a
y = n//a
if m%a!= 0:
    x += 1 
if n%a!= 0:
    y += 1
print(x*y)    
    