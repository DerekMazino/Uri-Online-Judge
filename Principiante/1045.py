cadena=input().split(' ')
cadena= [float(x) for x in cadena]#Convierto todos los elementos float
cadena.sort(reverse=True)
a=cadena[0]
b=cadena[1]
c=cadena[2]
if a>=(b+c):
    print('NAO FORMA TRIANGULO')
else:
    if a**2==b**2+c**2:
        print('TRIANGULO RETANGULO')
    if a**2>b**2+c**2:
        print('TRIANGULO OBTUSANGULO')
    if a**2<b**2+c**2:
        print('TRIANGULO ACUTANGULO')
    if a==b and a==c:
        print('TRIANGULO EQUILATERO')
    if (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
        print('TRIANGULO ISOSCELES')
