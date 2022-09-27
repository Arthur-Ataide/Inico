M = [[0 for i in range(12)]for j in range(12)]
L = int(input())
T = input()
soma = 0
for i in range(12):
    for j in range(12):
        M[i][j] = float(input())
for j in range(12):
    soma += M[L][j]
if T == 'S':
    print(soma)
elif T == 'M':
    print(soma / 12)

