from math import sqrt
print("Введите коэффициенты ")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print("Уравнение", a,"x^2 + ", b, "x + ",c," =     0:")
d = b ** 2 - 4 * a * c
print("Дискриминант =", d)
 
if d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print("x1 =", x1, "x2 = ", x2)
elif d == 0:
    x = -b / (2 * a)
    print("x =", x)
else:
    print("Корней нет")
