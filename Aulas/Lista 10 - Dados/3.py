from math import fabs
vetor = []
cont = 0
vamo = 'S'
while vamo == 'S':
    vetor.append(float(input('Digite um numero pra lista: ')))
    cont += 1
    vamo = input('Continuara? ')
menor = vetor[0]
media = sum(vetor)/cont
for i in range(cont):
    if fabs(media - vetor[i]) < fabs(media - menor):
        menor = vetor[i]
print(media)
print(menor)
