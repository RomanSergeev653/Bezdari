a = int(input())
b = int(input())
c = int(input())
d = 0

if(a < b):
    d = a
    a = b
    b = d
if(b < c):
    d = b
    b = c
    c = d
if(a < b):
    d = a
    a = b
    b = d

print(c)
print(a)
print(b)