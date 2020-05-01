cadena1=input()
cadena2=input()
#Manejo para la primera cadena
cadena1=cadena1.split()
u1=int(cadena1[1])
p1=float(cadena1[2])
#Madenejo para segunda cadena
cadena2=cadena2.split()
u2=int(cadena2[1])
p2=float(cadena2[2])
#Calculo del total a pagar
tp=(p1*u1)+(p2*u2)
print('VALOR A PAGAR: R$ {:.2F}'.format(tp))
