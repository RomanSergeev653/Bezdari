import math
import time

startTime = time.time() # время начала замера

N = 30000 #int(input())
simp = [2,3,5]
count = 7

if (N > 0):
    print(2, end=" ")
    if (N > 1):
        print(3, end=" ")
        if (N > 2):
            print(5, end=" ")

check = False

while len(simp) < N:
    if ()

endTime = time.time() #время конца замера
totalTime = endTime - startTime #вычисляем затраченное время

print("Время, затраченное на выполнение данного кода = ", totalTime)