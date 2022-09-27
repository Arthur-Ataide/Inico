matrix = [[0.0 for i in range(12)] for j in range(12)]
soma = 0
ope = input()
cont = 0
for i in range(12):
    for j in range(12):
        matrix[i][j] = float(input())

for i in range(12):
    for j in range(12):
        if j < i and i > 11 - j:
            cont += 1
            soma += matrix[i][j]
if ope == 'M':
    soma = soma/cont

print(f'{soma:.1f}')
