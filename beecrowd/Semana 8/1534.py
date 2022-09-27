while True:
    try:
        n = int(input())
        matrix = [[0 for i in range(n)]for j in range(n)]
        for i in range(n):
            for j in range(n):
                if n-1 == i + j:
                    matrix[i][j] = 2
                elif i == j:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = 3
                print(matrix[i][j], end='')
            print()
    except EOFError:
        break
