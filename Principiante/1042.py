lista=input().split(' ')
lista= [int(x) for x in lista]#Convierto todos los elementos int
lista2=lista[:]#Clono la lista pero como un objeto completamente independiente
lista2.sort()#Uso la función sort para ordenar la lista

for i in lista2:
    print(i)
print('')
for i in lista:
    print(i)