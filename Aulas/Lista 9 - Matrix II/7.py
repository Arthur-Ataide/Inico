Matrix = [[0 for j in range(50)] for i in range(4)]
curso = []
maior = 0
p = 0
for i in range(10):
    for j in range(3):
        if j == 0:
            n = input(' ')
            Matrix[i][j] = n
            for c in list(n):
                curso.append(list(c))
            A = curso[3]+curso[4]+curso[5]
            Matrix[i][3] = ''.join(A)
        elif j == 3:
            n = int(input(' '))
            Matrix[i][4] = n
            if i == 0:
                maior = n
                p = i
            elif maior < n:
                maior = n
                p = i
        else:
            Matrix[i][j] = int(input(' '))
print(Matrix[p][0], Matrix[p][3], Matrix[p][2])
