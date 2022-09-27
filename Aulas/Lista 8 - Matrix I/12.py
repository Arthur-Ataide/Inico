A = [[0 for i in range(4)]for j in range(5)]
soma = 0
for i in range(5):
    for j in range(5):
        A[i][j] = int(input())
        soma += A[i][j]
print(soma)

