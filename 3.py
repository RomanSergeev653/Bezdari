a=float(input("Введите первое число: "))
b=float(input("Введите второе число: "))
what = input("Выберите операцию (+,-,*,/, mod, div, pow) ")

if (what == "+"):
    print(a + b)
elif (what == "-"):
    print(a - b)
elif (what == "*"):
    print(a * b)
elif (what == "/"):
    if (b == 0):
        print("Деление на ноль!")
    else:
        print(a/b)
elif (what == "mod"):
    if (b == 0):
        print("Деление на ноль!")
    print(a % b)
elif (what == "div"):
    if (b == 0):
        print("Деление на ноль!")
    print(a // b)
elif (what == "pow"):
    print(a ** B)
else:
    print("Некорректная операция")
