from math import sqrt
entrada=input().split()
a=float(entrada[0])
b=float(entrada[1])
c=float(entrada[2])
if a==0 or (b**2-4*a*c)<0:
    print('Impossivel calcular')
else:
    R1=(-b+(sqrt(b**2-4*a*c)))/(2*a)
    R2=(-b-(sqrt(b**2-4*a*c)))/(2*a)
    print('R1 = {:.5F}'.format(R1))
    print('R2 = {:.5F}'.format(R2))