arr = []
s = []

while True:
    s = input().split()
    if "end" in s:
        break
    arr.append(s)

el = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        el=0
        if i+1 == len(arr): el += int(arr[0][j])
        else:               el += int(arr[i+1][j])

        if i == 0:  el += int(arr[len(arr)-1][j])
        else:       el += int(arr[i-1][j])

        if j+1 == len(arr[i]):  el += int(arr[i][0])
        else:                   el += int(arr[i][j+1])

        if j == 0:  el += int(arr[i][len(arr[i])-1])
        else:       el += int(arr[i][j-1])
        print(el, end=" ")
    print()