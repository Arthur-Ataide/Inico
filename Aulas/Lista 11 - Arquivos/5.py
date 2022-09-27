ark1 = input()
ark2 = input()
novo = input()
ark1 = open(ark1, 'r')
ark2 = open(ark2, 'r')
novo = open(novo, 'w')
notas = []
nomes = []
valor = 0
for i in range(10):
    nomes.append(ark1.readline())
    cont = 0
    total = 0
    valor = ark2.readline().split()
    for j in valor:
        total += int(j)
        cont += 1
    notas.append(total / cont)
for i in range(10):
    novo.write(f'{nomes[i]} teve {notas[i]} de nota\n')
ark1.close()
ark2.close()
novo.close()
