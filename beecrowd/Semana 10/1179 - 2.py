par = []
impar = []
cont_p = 0
cont_i = 0
for i in range(15):
    n = int(input())
    if n % 2 == 0:
        par.append(n)
        cont_p += 1
        if cont_p == 5:
            cont_p = 0
            for j in range(5):
                print(f'par[{j}] = {par[j]}')
            par.clear()

    else:
        impar.append(n)
        cont_i += 1
        if cont_i == 5:
            cont_i = 0
            for j in range(5):
                print(f'impar[{j}] = {impar[j]}')
            impar.clear()

for i in range(cont_i):
    print(f'impar[{i}] = {impar[i]}')
for i in range(cont_p):
    print(f'par[{i}] = {par[i]}')
