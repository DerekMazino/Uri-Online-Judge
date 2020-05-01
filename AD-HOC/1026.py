
def sumaBinaria(numero):
    resp=int(numero[0])^int(numero[1])
    print(resp) 

if __name__ == '__main__':
    while True:
        try:
            numero=input().split()
        except EOFError:
            break
        sumaBinaria(numero)
