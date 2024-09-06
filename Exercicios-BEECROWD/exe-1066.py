a = [0] * 5

a[0] = int(input("valor 1 \n"))
a[1] = int(input("valor 2 \n"))
a[2] = int(input("valor 3 \n"))
a[3] = int(input("valor 4 \n"))
a[4] = int(input("valor 5 \n"))

par  = 0
impar = 0
positivo = 0
negativo = 0
i = 0

while True:
    
    if a[i] % 2 == 0:
        par = par + 1
    i = i +1
    if i <=5:
        break
for i in range(5):
    if a[i] % 2 == 0:
        par += 1
    else:
        impar += 1
    
    if a[i] > 0:
        positivo += 1
    elif a[i] < 0:
        negativo += 1
        
print("Par(es): ", par)
print("Impar(es): ", impar)
print("Positivo(s): ", positivo)
print("Negativo(s): ", negativo)
