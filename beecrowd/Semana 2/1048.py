s = float(input())

if s <= 400:
    p = 15/100
    print(f'Novo salario: {s * (1 + p):.2f}\nReajuste ganho: {s * p:.2f}\nEm percentual: 15 %')

elif s > 400 and s <= 800:
    p = 12 / 100
    print(f'Novo salario: {s * (1 + p):.2f}\nReajuste ganho: {s * p:.2f}\nEm percentual: 12 %')

elif s > 800 and s <= 1200:
    p = 10 / 100
    print(f'Novo salario: {s * (1 + p):.2f}\nReajuste ganho: {s * p:.2f}\nEm percentual: 10 %')

elif s > 1200 and s <= 2000:
    p = 7 / 100
    print(f'Novo salario: {s * (1 + p):.2f}\nReajuste ganho: {s * p:.2f}\nEm percentual: 7 %')

else:
    p = 4 / 100
    print(f'Novo salario: {s * (1 + p):.2f}\nReajuste ganho: {s * p:.2f}\nEm percentual: 4 %')
