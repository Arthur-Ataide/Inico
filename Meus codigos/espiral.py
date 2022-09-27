n = int(input())
matrix = [[0 for i in range(n)] for j in range(n)]
cont = 0
num = 1
aux = n
while True:
    for i in range(cont, aux):
        for j in range(cont, aux):
            matrix[i][j] = num
    cont += 1
    aux -= 1
    num += 1
    if cont > aux:
        break
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
