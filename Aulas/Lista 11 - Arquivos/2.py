import random
num = int(input())
nomes = ['Arthur', 'Guto', 'Cecilia', 'Junior', 'Xaxa', 'Toddy']
sobrenome = ['Ataide', 'Melo', 'Saraiva', 'Alencar', 'Augustos', 'Dias', 'Anjos']
Ark = input()
arquivo = open(Ark, 'w')
for i in range(num):
    N = nomes[random.randint(0, 5)]
    S = sobrenome[random.randint(0, 6)]
    I = str(random.randint(1, 100))
    arquivo.write(f'{N} {S} tem {I} anos\n')
arquivo.close()
