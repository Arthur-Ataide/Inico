dados = []
vezes = [0 for i in range(6)]
for i in range(10):
    dados.append(int(input('Digite um numero: ')))
for i in range(10):
    cont = 1
    while True:
        if dados[i] == cont:
            vezes[cont-1] += 1
            break
        else:
            cont += 1
print(dados)
print(vezes)
