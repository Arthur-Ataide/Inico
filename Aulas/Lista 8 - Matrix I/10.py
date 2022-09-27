A = [[0 for i in range(4)]for j in range(4)]
B = [[0 for i in range(4)]for j in range(4)]
soma = [[0 for i in range(4)]for j in range(4)]
for i in range(4):
    for j in range(4):
        A[i][j] = int(input())
        B[i][j] = int(input())
        soma = A[i][j] + B[i][j]
print(soma)
