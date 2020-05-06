
valorInicial=float(input())
b1=int(valorInicial/100)#->Se castea la divición para que sea entera
r=int(valorInicial)-b1*100#->Se obtiene el resudio de la división
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
m1=int(r/1)
monedas=int(valorInicial*100)%100
m2=int(monedas/50)
r=monedas-m2*50
m3=int(r/25)
r=r-m3*25
m4=int(r/10)
r=r-m4*10
m5=int(r/5)
r=r-m5*5
m6=int(r/1)
print('NOTAS:')
print('%d nota(s) de R$ 100.00' % b1)
print('%d nota(s) de R$ 50.00' % b2)
print('%d nota(s) de R$ 20.00' % b3)
print('%d nota(s) de R$ 10.00' % b4)
print('%d nota(s) de R$ 5.00' % b5)
print('%d nota(s) de R$ 2.00' % b6)
print('MOEDAS:')
print('%d moeda(s) de R$ 1.00' % m1)
print('%d moeda(s) de R$ 0.50' % m2)
print('%d moeda(s) de R$ 0.25' % m3)
print('%d moeda(s) de R$ 0.10' % m4)
print('%d moeda(s) de R$ 0.05' % m5)
print('%d moeda(s) de R$ 0.01' % m6)