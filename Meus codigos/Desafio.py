# 8
# 2 3 4 6 9
# 2 e 6
vetor = []
cont = 0
vamo = 1
num = int(input('Qual o valor da soma? '))
n = int(input('Quantos valores voce digitara? '))
for i in range(n):
    vetor.append(int(input(f'Qual o {i+1}° termo da sequência: ')))
while True:
    if vetor[cont] + vetor[vamo] == num:
        print(f'{vetor[cont]} + {vetor[vamo]} = {num}')
        break
    else:
        if vamo == len(vetor) - 1:
            cont += 1
            vamo = cont + 1
            if cont == len(vetor) - 1:
                print('Nao tem')
                break
        else:
            vamo += 1
