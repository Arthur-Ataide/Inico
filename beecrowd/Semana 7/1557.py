n = 1
while True:
    n = int(input())
    if n == 0:
        break
    Matrix = [['' for i in range(n)]for j in range(n)]
    M = str(4 ** (n - 1)) #o maior numero
    for i in range(n):
        for j in range(n):
            cont = 0
            A = str((2 ** i) * (2 ** j))
            while len(M) > len(A) + cont:
                Matrix[i][j] += ' '
                cont += 1
            Matrix[i][j] += A
            if j != n - 1:
                print(Matrix[i][j], end=' ')
            else:
                print(Matrix[i][j], end='')
        print('')
    print('')
