Matrix = [[0 for i in range(10)]for j in range(10)]
D = []
for i in range(10):
    for j in range(10):
        Matrix[i][j] = int(input())
        if i == j:
            D = Matrix[i][j]
print(Matrix)
print(D)
