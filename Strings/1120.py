resp=[]
while True:
    failed, original = input().split()#Se almacena las dos partes en cada variable
    if failed=='0' and original=='0':#Se harán n casos, hasta que el juez digite 0 y 0
        break
    original='0'+original#Se agrega un cero en caso de que toda la cadena sea eliminada
    resp.append(int(original.replace(failed,'')))#Se agrega a la lista el retorno de la cadena a la cual
                                                #se le eliminaron los 'failed'
for i in resp:#Impresion final
    print(i)
    

