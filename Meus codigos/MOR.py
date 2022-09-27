def Mor(Simpolo1, Simpolo2, Simpolo_Sim_N, Sim_N, Sim_M, n):
    S0 = []
    if Simpolo1 != Simpolo2:
        for i in range(n):
            if Sim_N[i] == Sim_M[i]:
                S0.append('1')
            else:
                if Simpolo1 == Simpolo_Sim_N:
                    if Sim_N == '1':
                        S0.append('0')
                    else:
                        S0.append('1')
                else:
                    if Sim_M == '1':
                        S0.append('0')
                    else:
                        S0.append('1')

    else:
        for i in range(n):
            S0.append('1')

    return (S0)
    