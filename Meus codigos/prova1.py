alunos = int(input())
valores = input().split()
freq = [0 for i in range(alunos)]
notas = []
for i in range(alunos):
    notas.append(int(valores[i]))
maior = 0
num = []
for i in range(alunos):
    for j in range(alunos):
        if notas[i] == notas[j]:
            freq[i] += 1
        if maior < freq[i]:
            maior = freq[i]
saida = 0
for i in range(alunos):
    if maior == freq[i]:
        num.append(notas[i])
saida = num[0]
for i in num:
    if saida < i:
        saida = i
print(saida)
