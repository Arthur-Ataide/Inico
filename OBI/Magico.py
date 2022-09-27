N = int(input())  # dimensao do magico
matrix = [[0 for i in range(N)] for j in range(N)]
cont = -1
L_soma = 0  # soma linha
C_soma = 0  # soma coluna
D_soma = 0  # soma diagonal
for i in range(N):
    for j in range(N):
        matrix[i][j] = int(input(' '))
        L_soma += matrix[i][j]
if L_soma % N != 0:

    for j in range(N):
        for i in range(N):
            C_soma += matrix[i][j]
    if C_soma % N != 0:
        for i in range(N):
            D_soma += matrix[i][i]

