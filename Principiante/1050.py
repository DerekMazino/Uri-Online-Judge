DDD = {
    61:'Brasilia',
    71:'Salvador',
    11:'Sao Paulo',
    21:'Rio de Janeiro',
    32:'Juiz de Fora',
    19:'Campinas',
    27:'Victoria',
    31:'Belo Horizonte'
}
try:
    print(DDD[int(input())])
except KeyError:
    print("DDD nao cadastrado")
