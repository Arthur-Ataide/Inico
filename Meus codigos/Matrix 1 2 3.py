n = int(input())
matrix = [[3 for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        if j == i:
            matrix[i][j] = 1
        if j + i == n-1:
            matrix[i][j] = 2
        if j != n-1:
            print(matrix[i][j], end = ' ')
        else:
            print(matrix[i][j], end='')
    print()
