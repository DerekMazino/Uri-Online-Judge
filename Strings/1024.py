from math import trunc
def pasandoAscii(caracter):
    return ord(caracter)
def devolviendoAscii(caracter, espacios):
    if (caracter>=65 and caracter<=90) or (caracter>=97 and caracter<=122):
        return chr(caracter + espacios)
    return chr(caracter)
def devolviendoAscii2(caracter, espacios):
    return chr(caracter + espacios)
def invertirCadena(cadena):
    return cadena[::-1]
listaN=['0','1','2','3','4','5','6','7','8','9',' ']
respuestaFinal=[]#Almacenara las palabars codificadas para mostrarlas al final
casos=int(input())#Leyendo casos
cadenas=[]
for i in range(casos):
    cadenas.append(input())
for i in range(casos):
    temporal=""
    #Haciendo paso 1, mover tres posiciones a la derecha en ascii
    for j in cadenas[i]:
        temporal+=devolviendoAscii(pasandoAscii(j),3)    
    #respuestaFinal.append(temporal)
    #Paso 2: Invertir cada linea
    inicio=trunc(len(cadenas[i])/2)#desde donde se recorrera la cadena
    temporal=invertirCadena(temporal)
    temporalF=temporal[:inicio]#Se guarda la primera midad
    temporal2=temporal[inicio:]#Se guarda la segunda mitad
    for j in temporal2:
        temporalF+=devolviendoAscii2(pasandoAscii(j),-1)
    respuestaFinal.append(temporalF)
for i in respuestaFinal:
    print(i)

