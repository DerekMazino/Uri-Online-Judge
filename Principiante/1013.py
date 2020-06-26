cadena=input().split(' ')
a=int(cadena[0])
b=int(cadena[1])
c=int(cadena[2])
mayor1=(a+b+abs(a-b))/2
mayor2=(mayor1+c+abs(mayor1-c))/2
print('%d eh o maior' %mayor2)