oper = input()
soma = 0
cont = 0
n = 0
for i in range(12):
    for j in range(12):
        n = float(input())
        if j > i and i + j < 11:
            soma += n
            cont += 1
if oper == 'M':
    soma = soma/cont
print(f'{soma:.1f}')
