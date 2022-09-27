M = [[0 for i in range(12)]for j in range(12)]
T = input()
soma = 0
for i in range(12):
    for j in range(12):
        M[i][j] = float(input())
for i in range(12):
    for j in range(12):
        if j > 11 - i:
            soma += M[i][j]
if T == 'S':
    print(f'{soma:.1f}')
elif T == 'M':
    print(f'{soma/66:.1f}')
