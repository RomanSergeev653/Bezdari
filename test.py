class Square():
    def __init__(self,sideLen):
        self.sideLen = sideLen

    def area(self):
        a = self.sideLen * self.sideLen
        return a

figure = Square(int(input("Введите длину стороны квадрата: ")))
print(figure.area())