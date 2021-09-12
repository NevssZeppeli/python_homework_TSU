import math
a = float(input("Введите сторону A: "))
b = float(input("Введите сторону B: "))
alpha = math.radians(float(input("Введите угол альфа: ")))
print("Сторона C равна: ", math.sqrt((a**2 + b**2) - (2 * a * b * math.cos(alpha))))