id = []
pagar = []
soma = 0
cont = 0
while True:
    N_id = int(input(' '))
    N_pagar = int(input(' '))
    if N_id < 0:
        break
    else:
        id.append(N_id)
        pagar.append(N_pagar)
        cont += 1
for c in range(cont):
    soma += pagar[c]
print(id)
print(pagar)
print(soma)
