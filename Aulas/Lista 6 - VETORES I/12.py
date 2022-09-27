alturas = 0
media = 0
atletas = []
maiores = []
for c in range(10):
    n = int(input(' '))
    alturas += n
    atletas.append(n)
media = alturas/10
for c in range(10):
    if media < atletas[c]:
        maiores.append(atletas[c])
print(maiores)
