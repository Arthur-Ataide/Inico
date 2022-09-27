Matrix = [[0 for i in range(10)]for j in range(10)]
linha = []
coluna = []
seg = []
prin = []
for i in range(10):
    for j in range(10):
        n = int(input())
        Matrix[i][j] = n
        if i == j:
            prin.append(n)
        if i + j == 9:
            seg.append(n)
        if j == 4:
            coluna.append(n)
linha = Matrix[1][:]
Matrix[1] = Matrix[8][:]
Matrix[8] = linha[:]
for i in range(10):
    Matrix[i][3] = Matrix[i][9]
    Matrix[i][9] = coluna[i]
for i in range(10):
    Matrix[i][i] = seg[i]
    for j in range(10):
        if j + i == 9:
            Matrix[i][j] = prin[i]
print(Matrix)
