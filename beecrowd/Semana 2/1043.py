import math
A, B, C = map(float, input().split())
Condicao1 = ((A + B) > C) and (math.fabs(A - B) < C)
Condicao2 = ((C + B) > A) and (math.fabs(C - B) < A)
Condicao3 = ((A + C) > B) and (math.fabs(A - C) < B)
if Condicao1 and Condicao2 and Condicao3:
    p = A + B + C
    print(f'Perimetro = {p:.1f}')
else:
    area = ((A + B) * C) / 2
    print(f'Area = {area:.1f}')
