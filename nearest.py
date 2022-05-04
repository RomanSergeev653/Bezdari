import random 

a,b,n = (int(i) for i in input().split()) #Получаем строку с нужными данными

arr = [0] * n #Массив для генерируемых чисел
check = False #проверка на дубли

for i in range(n):#генерация чисел
    arr[i] = random.randint(a,b)
    print(arr[i], end=' ')
print(' ')
 
pos1 = 0
pos2 = 1

for i in reversed( range(0, n-1) ):#Перебор на дубли с конца
    for j in range(i+1,n):
        if (arr[i] == arr[j]):
            pos1 = i
            pos2 = j
            check = True#Если есть хоть один и мы считаем с конца то это то что нам нужно
            break
    if (check):#Если есть дубли можем заканчивать
        print(pos1+1, pos2+1)
        break
if (not check):#Если нет то скорее всего самих элементов перебора не так много
    minr = abs( arr[ pos1 ] - arr[ pos2 ] )#Запоминаем и в дальнейшем сравниваем минимальную разницу элементов
    for i in range( n - 1 ):
        for j in range( i+1, n ):
            if ( abs( arr[i] - arr[j] ) <= minr ):
                pos1 = i
                pos2 = j
                minr = abs( arr[ pos1 ] - arr[ pos2 ] )
    print( pos1 + 1, pos2 + 1)

    