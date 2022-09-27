dia1, dia2, dia3 = map(int, input().split())
if dia1 > dia2:
    if dia2 <= dia3:
        print(':)')
    elif abs(abs(dia1) - abs(dia2)) > abs(abs(dia2) - abs(dia3)):
        print(':)')
    else:
        print(':(')
elif dia1 < dia2:
    if dia2 >= dia3:
        print(':(')
    elif abs(abs(dia1) - abs(dia2)) > abs(abs(dia2) - abs(dia3)):
        print(':(')
    else:
        print(':)')
else:
    if dia2 < dia3:
        print(':)')
    else:
        print(':(')
