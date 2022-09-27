a = int(input('Digite a variavel: '))
vetor = []
impar = []
par = []
for c in range(30):
    n = int(input('Digite um numero: '))
    vetor.append(n * a)
    if (n * a) % 2 == 0:
        par.append(n*a)
    else:
        impar.append(n*a)
print(vetor)
print(f'sao par: {par}')
print(f'sao impar: {impar}')
