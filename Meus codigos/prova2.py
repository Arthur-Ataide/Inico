a = 0
vai = 0
linha, coluna =map(int,input().split())
matrix = [[0 for j in range(coluna)] for i in range(linha)]
for i in range(linha):
    num = input().split()
    for j in range(coluna):
        matrix[i][j] = int(num[j])
saida = 'S'
indices = []
for i in range(linha):
    for j in range(coluna):
        if matrix[i][j] != 0:
            if vai == 0:
                indices.append(i)
                indices.append(j)
                vai = 1
            else:
                if i != indices[a]:
                    indices.append(i)
                    indices.append(j)
                    a += 2
cont = 0
for i in indices:
    cont+= 1

for c in range(0, cont, 2):
    for j in range(coluna):
        for i in range(linha):
            if indices[c] == i and indices[c+1] == j:
                for I in range(i+1, linha):
                    if matrix[I][j] != 0:
                        saida = 'N'

total = -1
for i in range(linha):
    linha_toda = 1
    for j in range(coluna):
        if matrix[i][j] != 0:
            linha_toda = 0
        if linha_toda == 1:
            total = i
            break

if total > -1:
    if total != linha:
        for i in range(total +1, linha):
            for j in range(coluna):
                if matrix[i][j] != 0:
                    saida = 'N'

print(saida)

