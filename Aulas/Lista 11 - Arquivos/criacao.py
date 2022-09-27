from asyncore import write
import random
num = int(input())
nomes = ['Arthur', 'Guto', 'Cecilia', 'Junior', 'Xaxa', 'Toddy','Ataide', 'Melo', 'Saraiva', 'Alencar', 'Augustos', 'Dias', 'Anjos']
ark1 = input()
ark2 = input()
ark1 = open(ark1, 'w')
ark2 = open(ark2, 'w')
for i in range(num):
    N = nomes[random.randint(0, 13)]
    nota = str(random.randint(0, 10))
    ark1.write(f'{N}\n')
    ark2.write(f'{nota}\n')
ark1.close()
ark2.close()
