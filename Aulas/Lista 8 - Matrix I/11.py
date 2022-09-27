A = [[0 for i in range(5)]for j in range(5)]
B = [[0 for i in range(5)]for j in range(5)]
D = [[0 for i in range(5)]for j in range(5)]
for i in range(5):
    for j in range(5):
        A[i][j] = int(input())
        B[i][j] = int(input())
        D = A[i][j] - B[i][j]
print(D)




