tiempo=int(input())
velocidad=int(input())
#x=v*t
x=velocidad*tiempo
#Sabemos que el auto recorre 12km por litro
resp=x/12
print('{:.3F}'.format(resp))