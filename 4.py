room_type = input("Введите тип комнаты (треугольник, прямоугольник, круг) - ")

if(room_type == "треугольник"):
    a = float(input("A = "))
    b = float(input("B = "))
    c = float(input("C = "))
    
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)

elif (room_type == "круг"):
    R = float(input("R = "))

    print(3.14*(R*R))

elif (room_type == "прямоугольник"):
    a = float(input("A = "))
    b = float(input("B = "))

    print(a*b)