cadena=input().split(' ')
ti=int(cadena[0])
tf=int(cadena[1])
if ti>tf:
    cal=24-ti+tf
    print('O JOGO DUROU %d HORA(S)' %cal)
elif tf>ti:
    cal=tf-ti
    print('O JOGO DUROU %d HORA(S)' %cal)
elif ti==tf:
    print('O JOGO DUROU 24 HORA(S)')