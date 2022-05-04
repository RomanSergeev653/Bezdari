p = int(input())
s = p
q = p*p
while(s != 0):
    p = int(input())
    s += p
    q += p*p
print(q)