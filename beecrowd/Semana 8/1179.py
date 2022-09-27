par = []
impar = []
C_par = 0
C_imp = 0
for j in range(15):
    n = int(input('Digite um numero: '))

    if n % 2 == 0:
        par.append(n)
        C_par += 1
        if C_par == 5:
            for i in range(5):
                print(f'par[{i}] = {par[i]}')
            par.clear()

    else:
        impar.append(n)
        C_imp += 1
        if C_imp == 5:
            for i in range(5):
                print(f'impar[{i}] = {impar[i]}')
            impar.clear()

for i in range(len(impar)):
    print(f'impar[{i}] = {impar[i]}')

for i in range(len(par)):
    print(f'par[{i}] = {par[i]}')
