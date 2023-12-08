from math import cos, sin, sqrt
a = float(input("Введите угол альфа: "))
z1 = 1 - (0.25*(sin(2*a)**2)) + cos(2*a)
z2 = cos(a)**2 + cos(a)**4
print (f"z1=", z1, " z2=", z2)
