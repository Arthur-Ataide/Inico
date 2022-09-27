Numero_conta = []
saldo = []
sinal = []
total_clientes = 0
negativos = 0
Saldo_Empresa = 0
while True:
    conta = int(input('Qual o numero da conta? '))
    if conta < 0:
        break
    else:
        valor = int(input('Qual o valor da conta? '))
        Numero_conta.append(conta)
        saldo.append(valor)
        total_clientes += 1
        Saldo_Empresa += valor
        if valor >= 0:
            sinal.append('POSITIVO')
        else:
            sinal.append('NEGATIVO')
            negativos += 1
porcentagem = negativos/total_clientes
for c in range(total_clientes):
    print(f'A conta do cliente {Numero_conta[c]} deu um valor de {saldo[c]} com saldo {sinal[c]}')
print(f'O total de clientes com saldo negativo é {negativos}\nO total de clientes foi {total_clientes}')
print(f'o saldo da agencia é {sum(saldo)}\nO percentual de pessoas com negativo foi {porcentagem}')
print(Saldo_Empresa)
