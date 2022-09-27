def fatorial(num):
    if num == 1:
        return 1
    else:
        fat = num * fatorial(num-1)
        return fat

palavra = input()
letras = []
quant = 0

for i in palavra:
    letras.append(i)
    quant += 1
print(letras)






