def f_and(simpolo1, simpolo2, simpolo_sim_n, sim_n, sim_m, num):
    s0 = []
    if simpolo1 != simpolo2:
        for c in range(num):
            if sim_n[c] == '1' and sim_m[c] == '1':
                s0.append('1')

            else:
                s0.append('0')

    else:
        if simpolo1 == simpolo_sim_n:
            for c in range(num):
                if sim_n[c] == '1':
                    s0.append('1')

                else:
                    s0.append('0')

        else:
            for c in range(num):
                if sim_m[c] == '1':
                    s0.append('1')
                else:
                    s0.append('0')

    return s0


def f_or(simpolo1, simpolo2, simpolo_sim_n, sim_n, sim_m, num):
    s0 = []
    if simpolo1 != simpolo2:
        for c in range(num):
            if sim_n[c] == '0' and sim_m[c] == '0':
                s0.append('0')

            else:
                s0.append('1')

    else:
        if simpolo1 == simpolo_sim_n:
            for c in range(num):
                if sim_n[c] == '1':
                    s0.append('1')

                else:
                    s0.append('0')

        else:
            for c in range(num):
                if sim_m[c] == '1':
                    s0.append('1')
                else:
                    s0.append('0')
    return s0


def f_xor(simpolo1, simpolo2, sim_n, sim_m, num):
    s0 = []
    if simpolo1 != simpolo2:
        for c in range(num):
            if sim_n[c] == sim_m[c]:
                s0.append('0')

            else:
                s0.append('1')

    else:
        for c in range(num):
            s0.append('0')

    return s0


def f_mor(simpolo1, simpolo2, simpolo_sim_n, sim_n, sim_m, num):
    sim_n_novo = []
    sim_m_novo = []
    if simpolo1 == simpolo_sim_n:
        for c in range(num):
            if sim_n[c] == '1':
                sim_n_novo.append('0')

            else:
                sim_n_novo.append('1')
            sim_m_novo.append(sim_m[c])

    else:
        for c in range(num):
            if sim_m[c] == '1':
                sim_m_novo.append('0')

            else:
                sim_m_novo.append('1')
            sim_n_novo.append(sim_n[c])

    return f_or(simpolo1, simpolo2, simpolo_sim_n, sim_n_novo, sim_m_novo, num)


S1 = []
S2 = []
S3 = []
ERRO = 0
operador = []
sequencia = []

n = int(input().strip())
se1 = input().strip().upper()
se2 = input().strip().upper()
operacao = input().strip().upper().split()

if n > 1000:
    ERRO = 1

cont = 0
for i in se1:
    S1.append(i)
    cont += 1
    if i != '1' and i != '0':
        ERRO = 1

if cont != n:
    ERRO = 1

cont = 0
for i in se2:
    S2.append(i)
    cont += 1
    if i != '1' and i != '0':
        ERRO = 1

if cont != n:
    ERRO = 1

for i in range(len(operacao)):
    if i % 2 != 0:
        operador.append(operacao[i])

    else:
        sequencia.append(operacao[i])
1
if len(operacao) != 3 and len(operacao) != 5:
    ERRO = 1

if len(sequencia) != 2 and len(sequencia) != 3:
    ERRO = 1

for i in range(len(sequencia)):
    if sequencia[i] != 'S1' and sequencia[i] != 'S2':
        ERRO = 1

if len(operador) != 1 and len(operador) != 2:
    ERRO = 1

for i in range(len(operador)):
    if operador[i] != 'AND' and operador[i] != 'OR' and operador[i] != 'XOR' and operador[i] != 'NAND' \
            and operador[i] != 'NOR' and operador[i] != 'MOR':
        ERRO = 1

if ERRO == 1:
    print('ERRO')
    exit()

cont = 0

for i in range(len(sequencia)):
    if i == 2:
        sequencia.insert(2, 'S3')

for i in range(len(operador)):
    if operador[i] == 'AND' or operador[i] == 'NAND':
        if cont == 0:
            S3 = f_and(sequencia[cont], sequencia[cont + 1], 'S1', S1, S2, n)
        else:
            if sequencia[cont + 1] == 'S2':
                S3 = f_and(sequencia[cont], sequencia[cont + 1], 'S3', S3, S2, n)
            else:
                S3 = f_and(sequencia[cont], sequencia[cont + 1], 'S3', S3, S1, n)
        if operador[i] == 'NAND':
            for j in range(n):
                if S3[j] == '1':
                    S3[j] = '0'
                else:
                    S3[j] = '1'

    elif operador[i] == 'OR' or operador[i] == 'NOR':
        if cont == 0:
            S3 = f_or(sequencia[cont], sequencia[cont + 1], 'S1', S1, S2, n)
        else:
            if sequencia[cont + 1] == 'S2':
                S3 = f_or(sequencia[cont], sequencia[cont + 1], 'S3', S3, S2, n)
            else:
                S3 = f_or(sequencia[cont], sequencia[cont + 1], 'S3', S3, S1, n)
        if operador[i] == 'NOR':
            for j in range(n):
                if S3[j] == '1':
                    S3[j] = '0'
                else:
                    S3[j] = '1'

    elif operador[i] == 'XOR':
        if cont == 0:
            S3 = f_xor(sequencia[cont], sequencia[cont + 1], S1, S2, n)
        else:
            if sequencia[cont + 1] == 'S2':
                S3 = f_xor(sequencia[cont], sequencia[cont + 1], S3, S2, n)
            else:
                S3 = f_xor(sequencia[cont], sequencia[cont + 1], S3, S1, n)

    elif operador[i] == 'MOR':
        if cont == 0:
            S3 = f_mor(sequencia[cont], sequencia[cont + 1], 'S1', S1, S2, n)
        else:
            if sequencia[cont + 1] == 'S2':
                S3 = f_mor(sequencia[cont], sequencia[cont + 1], 'S3', S3, S2, n)
            else:
                S3 = f_mor(sequencia[cont], sequencia[cont + 1], 'S3', S3, S1, n)
    cont += 2

for i in S3:
    print(i, end='')
print()
