A, G, Ra, Rg = map(float, input().split())
if A >= 0.01 and G <= 10 and Ra >= 0.01 and Rg <= 20:
    if Ra / A > Rg / G:
        print('A')
    elif Ra / A < Rg / G:
        print('G')
    else:
        print('G')
