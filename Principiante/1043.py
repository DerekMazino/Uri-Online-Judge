cadena=input().split()
a=float(cadena[0])
b=float(cadena[1])
c=float(cadena[2])
#Evaluar si puede ser un triangulo
if (a+b>c) and (a+c>b) and (b+c>a):
    perimetro=a+b+c
    print('Perimetro = {:.1f}'.format(perimetro))
else:
    area=(a+b)/2*c
    print('Area = {:.1f}'.format(area))