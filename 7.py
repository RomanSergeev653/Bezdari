t = input("Номер билета - ")
l = int(t[0])+int(t[1])+int(t[2])
r = int(t[3])+int(t[4])+int(t[5])
if(l == r):
    print("Счастливый")
else:
    print("Обычный")