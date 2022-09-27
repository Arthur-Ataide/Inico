n = int(input())
gasto = []
matrix = [[' ', 0]for i in range(n)]
menor = 0
for i in range(n):
    matrix[i][0] = (input(' '))
    n = int(input(' '))
    gasto.append((1000/n)*3.5)
    matrix[i][1] = n
    if matrix[i][1] < matrix[menor][1]:
        menor = i
print(matrix[menor][0])
