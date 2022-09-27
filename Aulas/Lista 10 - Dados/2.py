lista1 = []
lista2 = []
listas = []
cont1 = 0
cont2 = 0
for i in range(4):
    lista1.append(int(input(' Digite um numero pra lista 1: ')))
for i in range(6):
    lista2.append(int(input(' Digite um numero pra lista 2: ')))
for i in range(10):
    if i < 7:
        if i % 2 == 0:
            listas.append(lista1[cont1])
            cont1 += 1
        else:
            listas.append(lista2[cont2])
            cont2 += 1
    else:
        listas.append(lista2[cont2])
        cont2 += 1
print(lista1)
print(lista2)
print(listas)
