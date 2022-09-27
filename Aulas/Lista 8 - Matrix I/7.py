M = [[0 for i in range(10)]for j in range(10)]
A = []
for i in range(10):
    for j in range(10):
        M[i][j] = int(input())
for i in range(10):
    for j in range(10):
        if i + j != 10:
            A.append(M[i][j])
print(A)
