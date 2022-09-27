N = int(input('Quantas posiçoes deve ter? '))
X = []
menor = 0
A = input(' ').split()
for i in range(N):
    X.append(int(A[i]))
menor = X[0]
for i in range(N):
    if menor > X[i]:
        menor = X[i]
print(f'Menor valor: {menor}')
for i in range(N):
    if menor == X[i]:
        print(f'Posicao: {i}')
        break
