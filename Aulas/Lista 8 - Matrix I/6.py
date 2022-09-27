M = [[0 for i in range(12)]for j in range(12)]
soma = 0
for i in range(12):
    for j in range(12):
        M[i][j] = float(input())
for i in range(12):
    for j in range(12):
        if j > i:
            soma += M[i][j]
print(f'{soma:.1f}')

