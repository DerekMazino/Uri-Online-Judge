#Hallando el MDC entre en numerador y el denominador
def hallarMCD(n, d):
	resto = 0
	while(d > 0):
		resto = d
		d = n % d
		n = resto
	return n

#Optiene la simplificacion completa entre n y d
def simplificarT(n, d):
    mcd=hallarMCD(n,d)
    n=int(n/mcd)
    d=int(d/mcd)
    return n, d
def simplificar(n,d):
    nf, df=simplificarT(n,d)
    cadena=str(nf)+'/'+str(df)
    return cadena
resp=[]
nCasos=int(input())
for i in range(nCasos):
    n1, d1, n2, op, n3, d2, n4 = input().split(' ')
    if op == '+':
        ni=int(n1)*int(n4)+int(n2)*int(n3)
        n = str(ni)
        di = int(n2)*int(n4)
        d = str(di)
        final=simplificar(ni,di)
    elif op == '-':
        ni=int(n1)*int(n4)-int(n2)*int(n3)
        n = str(ni)
        di = int(n2)*int(n4)
        d = str(di)
        final=simplificar(ni,di)
    elif op == '*':
        ni=int(n1)*int(n3)
        n = str(ni)
        di = int(n2)*int(n4)
        d = str(di)
        final=simplificar(ni,di)
    elif op == '/':
        ni=int(n1)*int(n4)
        n = str(ni)
        di = int(n2)*int(n3)
        d = str(di)
        final=simplificar(ni,di)
    resp.append(n+'/'+d+' = '+final)
for i in resp:
    print(i)