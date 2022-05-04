n = int(input())
arr = []

for i in range(n):
    s = []
    for j in range(n):
        s.append(0)
    arr.append(s)

move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
side = 0
i = 0
j = 0

for count in range(1,(n*n)+1):
    arr[i][j] = count
    if (i+move[side][0] == n) or (i+move[side][0] == -1) or (j+move[side][1] == n) or (j+move[side][1] == -1):
        side = (side + 1) % 4
        i += move[side][0]
        j += move[side][1]
        continue
    if (arr[i+move[side][0]][j+move[side][1]] != 0):
        side = (side + 1) % 4
    i += move[side][0]
    j += move[side][1]
i = 0
j = 0
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print(" ")