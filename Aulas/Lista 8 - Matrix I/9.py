A = [[0 for i in range(3)]for j in range(4)]
B = [[0 for i in range(3)]for j in range(4)]
for i in range(3):
    for j in range(4):
        n = int(input())
        A[i][j] = n
        B[i][j] = n*3
print(A)
print(B)
