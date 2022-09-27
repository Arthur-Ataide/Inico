Matrix = [[0 for i in range(10)]for j in range(10)]
for i in range(10):
    for j in range(10):
        Matrix[i][j] = int(input())
for i in range(10):
    for j in range(10):
        if j != i:
            print(Matrix[i][j])


