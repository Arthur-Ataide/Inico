antiga = input(' ')
antigas = antiga.split()
cont = 0
frase = ''
for i in antigas:
    cont += 1
nova = input(' ')
for i in range(cont-1):
    frase += ' ' + antigas[i]
frase += ' ' + nova
print(frase)
