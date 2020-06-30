casos = int(input())
final=[]
for i in range(casos):
    t1,t2 = input().split(" ")
    t_new = ''
    #Tengo en cuenta dos casos, t>t2 o t2>t1
    if(len(t1) <= len(t2)):
        for i in range(len(t1)):#Se recorre hasta el tamaño de la palabra más pequeña
            t_new += t1[i]
            t_new += t2[i]
        t_new += t2[len(t1):]#Se agregan los caracteres faltantes de la palabra más grande
        final.append(t_new)
    else:
        for i in range(len(t2)):
            t_new += t1[i]
            t_new += t2[i]
        t_new += t1[len(t2):]
        final.append(t_new)
for i in final:
    print(i)
