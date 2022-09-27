Matrix = [[0 for i in range(5)]for j in range(5)]
for i in range(5):
    for j in range(5):
        Matrix[i][j] = int(input(' '))
        if j == 4:
            print(Matrix[i][j])
print(Matrix)
