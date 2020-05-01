import math
linea1=input()
linea2=input()
#Punto 1
linea1=linea1.split()
x1=float(linea1[0])
y1=float(linea1[1])
#Punto 2
linea2=linea2.split()
x2=float(linea2[0])
y2=float(linea2[1])
#Calculo de la distancia
d=math.sqrt((x2-x1)**2+(y2-y1)**2)
print('{:.4F}'.format(d))