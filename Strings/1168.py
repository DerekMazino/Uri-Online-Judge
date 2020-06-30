LED = {
    '0': 6,
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6
}

nCasos=int(input())
respuesta=[]
for i in range(nCasos):
    caso=input()
    temp=0
    for i in caso:
        temp+=LED[i]
    respuesta.append(temp)

for i in range(nCasos):
    print('%d leds' %respuesta[i])
