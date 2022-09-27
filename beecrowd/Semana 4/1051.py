salario = float(input())
salario = f'{salario:.2f}'
salario = float(salario)
imposto1 = 0.08
imposto2 = 0.18
imposto3 = 0.28

if salario <= 2000 and salario >= 0:
    print('Isento')

elif salario <= 3000 and salario >= 2000.01:
    salario = salario - 2000
    print(f'R$ {(salario * imposto1):.2f}')

elif salario <= 4500.00 and salario >= 3000.01:
    salario = salario - 3000
    print(f'R$ {(80 + (salario * imposto2)):.2f}')

elif salario > 4500:
    salario = salario - 4500
    print(f'R$ {(80 + (1500 * imposto2) + (salario * imposto3)):.2f}')
