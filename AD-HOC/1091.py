respuesta=[]
while True:
    nCasos=int(input())
    if nCasos==0:
        break
    x, y=input().split(' ')
    x=int(x)
    y=int(y)
    for i in range(nCasos):
        x1, y1=input().split(' ')
        x1=int(x1)
        y1=int(y1)
        if x1==x or y1==y:
            respuesta.append('divisa')
        elif x1>x and y1>y:
            respuesta.append('NE')
        elif x1<x and y1>y:
            respuesta.append('NO')
        elif x1<x and y1<y:
            respuesta.append('SO')
        elif x1>x and y1<y:
            respuesta.append('SE')
for i in respuesta:
    print(i)