n = int(input())
digit = 1
count = 0
while(True):
    for i in range(digit):
        print(digit, end=" ")
        count += 1
        if count >= n:
            break
    if count >= n:
        break
    digit += 1
