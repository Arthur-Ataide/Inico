Matrix = [[0 for i in range(7)]for j in range(5)]
for i in range(7):
    for j in range(5):
        n = int(input(' '))
        if n % 2 != 0:
            Matrix[i][j] = 2 * n
        else:
            Matrix[i][j] = n
print(Matrix)
