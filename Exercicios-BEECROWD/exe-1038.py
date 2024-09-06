entrada = input("Digite o código e a quantidade (exemplo: '1 2'): ")
TC, TQ = entrada.split()
cod = int(TC)
qtd = int(TQ)

if cod == 1:
    cachorro = qtd * 4
    print("Total: R$ ", cachorro)
elif cod == 2:
    Salada = qtd * 4.5 
    print("Total: R$ ", Salada) 
elif cod == 3:
    Bacon = qtd * 5
    print("Total: R$ ", Bacon)  
elif cod == 4:
    Torrada = qtd * 2
    print("Total: R$ ", Torrada) 
elif cod == 5:
    Refrigerante = qtd * 1.5
    print("Total: R$ ", Refrigerante)  
    