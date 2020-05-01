valorInicial=int(input())
horas=int(valorInicial/3600)
minutos=int((valorInicial-horas*3600)/60)#Se obtiene el residuo, y se divide en 60
#Se resta al valor Inicial la cantidad de segundos que hay en las horas y minutos
segundos=int(valorInicial-(horas*3600+minutos*60))
print(str(horas)+':'+str(minutos)+':'+str(segundos))