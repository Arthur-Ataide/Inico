soma = 0
num = 1
den = 1
cont = 0
while cont < 39:
    s = num / den
    soma += s
    num += 2
    den = den * 2
    cont += 1
print(f'{soma:.2f}')
