notas = []
nomes = []
maior = 0
menor = 0
for c in range(10):
    nota = int(input('Digite uma nota: '))
    notas.append(nota)
    nome = input('Digite o nome: ')
    nomes.append(nome)
    menor = nota
    maior = nota
for c in range(10):
    if maior < notas[c]:
        maior = notas[c]
    elif menor > notas[c]:
        menor = notas[c]
print(f'a maior nota foi {maior} e a menor foi {menor}')
for c in range(10):
    if maior == notas[c]:
        print(nomes[c], 'teve a maior nota')
    if menor == notas[c]:
        print(nomes[c], 'teve a menor nota')
