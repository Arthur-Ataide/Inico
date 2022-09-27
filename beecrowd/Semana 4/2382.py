import math
L, A, P, R = map(int, input().split())
Esfera = L*L + A*A + P*P
caixa = 4 * R * R
if Esfera > caixa:
    print('N')
else:
    print('S')
