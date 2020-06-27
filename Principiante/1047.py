cadena=input().split()
ti=int(cadena[0])
mi=int(cadena[1])
tf=int(cadena[2])
mf=int(cadena[3])
#Calculando horas
if ti>tf:
    cal=24-ti+tf
elif tf>ti:
    cal=tf-ti
elif ti==tf:
    cal=24
#Calculando minutos
if mi<mf:
    cal2=mf-mi
    if ti==tf:
        cal=0
elif mi>mf:
    cal2=60-mi+mf
    cal=cal-1
elif mi==mf:
    cal2=0
print('O JOGO DUROU '+str(cal)+' HORA(S) E '+str(cal2)+' MINUTO(S)')
