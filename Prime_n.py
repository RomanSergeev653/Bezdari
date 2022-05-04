import math

N =int(input()) 
count = 3 
check = False 
simps = [2] 

if (N > 0):
    print(2,end=" ")
s = 0
while(N > len(simps)): 
    check = True 
    s = math.sqrt(count)
    if (s == int(s)):
        count += 2
        continue
    for i in range(1,len(simps)): 
        if (count % simps[i] == 0): 
            check = False
            break
        if (simps[i] > s):
            break
    if (check): 
        simps.append(count)
        print(count, end=' ')
    count += 2 