a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(S)