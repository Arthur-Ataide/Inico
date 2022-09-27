w1 = 1
w2 = 1
r = 1
while w1 != 0 and w2 != 0 and r != 0:
    w1, w2, r = map(float, input().split())
    m = w1 * (1+r/30)
    m += w2 * (1+r/30)
    m = m/2
    if 1 <= m < 13:
        print('Nao vai da nao')
    elif 13 <= m < 14:
        print('E 13')
    elif 14 <= m < 40:
        print('Bora, hora do show! BIIR!')
    elif 40 <= m <= 60:
        print('Ta saindo da jaula o monstro!')
    elif m > 60:
        print('AQUI E BODYBUILDER!!')

print('\nAqui nois constroi fibra rapaz! Nao e agua com musculo!')
