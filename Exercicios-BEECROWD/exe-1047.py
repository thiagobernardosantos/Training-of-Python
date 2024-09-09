HI = int(input(''))
MI = int(input(''))
HF = int(input(''))
MF = int(input(''))

if HI > HF:
    if MI > MF:
        H = (24-HI)+HF
        M = (60-MI)+MF
        print('O jogo Durou %.0i Hora(S) e %.0i Minuto(S)' % (H,M))
    elif MI < MF:
        H = (24-HI)+HF
        M = MF - MI
        print('O jogo Durou %.0i Hora(S) e %.0i Minuto(S)' % (H,M))
    else:
        H = (24-HI)+HF + 1
        print('O jogo Durou %.0i Hora(S) e 0 Minuto(S)' % H)
elif HI < HF:
    if MI > MF:
        H = HF - HI - 1
        M = (60-MI)+MF
        print('O jogo Durou %.0i Hora(S) e %.0i Minuto(S)' % (H,M))
    elif MI < MF:
        H = HF - HI
        M = MF - MI
        print('O jogo Durou %.0i Hora(S) e %.0i Minuto(S)' % (H,M))
    else:
        H = HF - HI + 1
        print('O jogo Durou %.0i Hora(S) e 0 Minuto(S)' % H)
else:
    print('O jogo Durou 24 Hora(S) e 0 Minuto(S)')