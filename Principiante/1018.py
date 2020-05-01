
valorInicial=int(input())
print(valorInicial)
b1=int(valorInicial/100)#->Se castea la divición para que sea entera
r=valorInicial-b1*100#->Se obtiene el resudio de la división
b2=int(r/50)#->Ahora el residuo es el nuevo valor inicial
r=r-b2*50
b3=int(r/20)
r=r-b3*20
b4=int(r/10)
r=r-b4*10
b5=int(r/5)
r=r-b5*5
b6=int(r/2)
r=r-b6*2
b7=int(r/1)
print('%d nota(s) de R$ 100,00' % b1)
print('%d nota(s) de R$ 50,00' % b2)
print('%d nota(s) de R$ 20,00' % b3)
print('%d nota(s) de R$ 10,00' % b4)
print('%d nota(s) de R$ 5,00' % b5)
print('%d nota(s) de R$ 2,00' % b6)
print('%d nota(s) de R$ 1,00' % b7)
