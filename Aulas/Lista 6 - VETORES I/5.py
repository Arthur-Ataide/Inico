nota = []
cont = 0
for c in range(5):
    aluno = int(input(' '))
    nota.append(aluno)
    cont += 1
media = sum(nota) / cont
print(media)
