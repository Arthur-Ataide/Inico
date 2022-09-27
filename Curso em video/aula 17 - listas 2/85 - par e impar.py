numeros = [[], []]
for i in range(7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print(numeros)
print(numeros[0])
print(numeros[1])
