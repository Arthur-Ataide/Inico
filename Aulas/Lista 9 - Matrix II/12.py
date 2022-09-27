Matrix = [[0 for i in range(2)]for j in range(2)]
pri = 1
sec = 1
for i in range(2):
    for j in range(2):
        n = int(input())
        Matrix[i][j] = n
        if i == j:
            pri *= n
        if i + j == 1:
            sec *= n
print(pri-sec)
