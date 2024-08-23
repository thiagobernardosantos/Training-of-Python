valor = 0
Alc = 0
Gas = 0
Die = 0

print("1. Alcool")
print("2. Gasolina")
print("3. Diesel")
print("4. Fim")

while True:
    
    valor = int(input(""))
    
    if valor == 1:
        Alc = Alc + 1
    elif valor == 2:
        Gas = Gas + 1
    elif valor == 3:
        Die = Die + 1
        
    

    if valor == 4:
        break

print("Muito obrigado!")
print("Alcool: ", Alc)
print("Gasolina: ", Gas)
print("Diesel: ", Die)