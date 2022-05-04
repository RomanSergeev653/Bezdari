number = int(input())

print(number, end=" ")
if(number % 10 == 1) and (number // 10 != 1):
    print("программист")
elif(number % 10 > 1) and (number % 10 < 5) and (number // 10 != 1):
    print("программиста")
else:
    print("программистов")