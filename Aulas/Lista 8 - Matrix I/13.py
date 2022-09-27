A = [[0 for i in range(3)]for j in range(5)]
soma =0
for i in range(5):
    soma = 0
    for j in range(5):
        A[i][j] = int(input())
        soma += A[i][j]
        A[i][j] = soma
print(A[i][j])
