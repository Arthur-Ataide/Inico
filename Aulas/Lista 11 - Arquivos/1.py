nome_arq = input()
arq_N = open(nome_arq, 'w')
for i in range(200, 49, -1):
    i = str(i)
    arq_N.write(i)
    arq_N.write('\n')
arq_N.close()
