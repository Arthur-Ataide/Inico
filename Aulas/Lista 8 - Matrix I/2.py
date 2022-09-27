Matrix = [[0 for i in range(7)]for j in range(7)]
cont = 0
n = int(input(' '))
for i in range(7):
    for j in range(7):
        Matrix[i][j] = int(input(' '))
for i in range(7):
    for j in range(7):
        if Matrix[i][j] == n:
            print(i, j)
            cont += 1
if cont == 0:
    print('ERRO')
