import math

print('\n',"Areade las Plantillas", '\n')

L = eval(input("Lado del Cuadrado: "))

L2 = pow(L, 2)

pi = math.pi

r1 = 4 - pi

x = L2*((r1)/4)

z = round(x, 2)

print('\n',"El area de la platilla es = ", x, '\n')
print('\n',"o aprox. =", z, '\n')