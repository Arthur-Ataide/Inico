n = int(input())
entra = input().split()
menor = int(int(entra[0]))
pos = 0
for i in range(n):
    if menor > int(entra[i]):
        menor = int(entra[i])
        pos = i
print(f'Menor valor: {menor}\nPosicao: {pos}')
