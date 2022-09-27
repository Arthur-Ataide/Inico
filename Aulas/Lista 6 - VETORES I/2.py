menor = []
m = int(input('Digite o numero de comparaçao: '))
for c in range(10):
    n = int(input('Digite um numero: '))
    if n < m:
        menor.append(n)
print('menor:', menor)
