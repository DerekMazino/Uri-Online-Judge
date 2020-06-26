cadena=input().split(' ')
a=float(cadena[0])
b=float(cadena[1])
c=float(cadena[2])
pi=3.14159
tri=(a*c)/2
cir=pi*c**2
tra=((a+b)/2)*c
cua=b*b
rec=a*b
print('TRIANGULO: {:.3f}'.format(tri))
print('CIRCULO: {:.3f}'.format(cir))
print('TRAPEZIO: {:.3f}'.format(tra))
print('QUADRADO: {:.3f}'.format(cua))
print('RETANGULO: {:.3f}'.format(a*b))