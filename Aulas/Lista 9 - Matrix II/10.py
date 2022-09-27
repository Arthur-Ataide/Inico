Matrix = [[0 for i in range(3)]for j in range(3)]
mama = [[0 for i2 in range(3)]for j2 in range(3)]
i_2 = 2
for i in range(3):
    j_2 = 2
    for j in range(3):
        n = int(input(' '))
        Matrix[i][j] = n
        mama[i_2][j_2] = n
        j_2 -= 1
    i_2 -= 1
print(Matrix)
print(mama)
