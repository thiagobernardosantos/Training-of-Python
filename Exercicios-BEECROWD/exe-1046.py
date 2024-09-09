I = int(input(''))
F = int(input(''))

if I > F:
    T = (24-I)+F
    print('O jogo Durou %.0i Hora(S)' % T)
elif I < F:
    T = F - I 
    print('O jogo Durou %.0i Hora(S)' % T)
else:
    print('O jogo Durou 24 Hora(S)')