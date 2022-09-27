li = int(input(' '))
co = int(input(' '))
Matrix = [[0 for i in range(co)]for j in range(li)]
Tra = [[0 for i1 in range(li)]for j1 in range(co)]
j2 = 0
for i in range(li):
    i2 = 0
    for j in range(co):
        n = int(input(' '))
        Matrix[i][j] = n
        Tra[i2][j2] = n
        i2 += 1
    j2 += 1
if Matrix == Tra:
    print('Simetrico')
else:
    print('Nao simetrico')
