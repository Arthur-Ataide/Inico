matrix = [[0 for j in range(3)]for i in range(3)]
par = 0
colun = 0
lin = 0
for j in range(3):
    for i in range(3):
        matrix[i][j] = int(input('Digite um numero: '))
for j in range(3):
    for i in range(3):
        if matrix[i][j] % 2 == 0:
            par += matrix[i][j]
        print(matrix[i][j], end=' ')
    print()
for i in range(3):
    colun += matrix[i][2]
for j in range(3):
    lin += matrix[1][j]
print(par)
print(colun)
print(lin)
