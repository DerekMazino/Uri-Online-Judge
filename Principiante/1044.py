cadena=input().split(' ')
n1=int(cadena[0])
n2=int(cadena[1])
if n1>n2:
    a=n1%n2
elif n2>n1:
    a=n2%n1
else:
    a=0

if a==0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
