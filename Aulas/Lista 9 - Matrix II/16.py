Matrix = [[0 for i in range(2)]for j in range(2)]
mama = [[0.0 for i1 in range(2)]for j1 in range(2)]
Inv = [[1, 0], [0, 1]]
pri = 1
sec = 1
quarda = 0
for i in range(2):
    for j in range(2):
        n = int(input(' '))
        Matrix[i][j] = n
        if i == j:
            pri *= n
        if i + j == 1:
            sec *= n
det = pri-sec
for i in range(2):
    for j in range(2):
        if i + j == 1:
            mama[i][j] = -1 * Matrix[i][j] / det
        else:
            mama[i][j] = Matrix[i][j]/det
quarda = mama[0][0]
mama[0][0] = mama[1][1]
mama[1][1] = quarda
print(mama)
