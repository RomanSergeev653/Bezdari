def sum_tuple(a, b):
    return a[0] + b[0], a[1] + b[1]
 
 
coms = {
    "R": (-1, 0),
    "L": (1, 0),
    "U": (0, 1),
    "D": (0, -1)
}
 
input()
input()
start, cords = (0, 0), set()
for com in input():
    nxt = sum_tuple(start, coms[com])
    cords.add(tuple(sorted((start, nxt))))
    start = nxt
print(len(cords))