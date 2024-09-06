num = int(input(""))
Valor = 1


if num > 1 and num < 1000:
    
    for i in range(0, num):
        print(Valor, Valor**2, Valor**3)
        Valor += 1