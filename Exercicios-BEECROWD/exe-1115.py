
x = int(input(""))
y = int(input(""))
while True:
    if x > 0 and y > 0:
        print("primeiro")
    elif x > 0 and y < 0:
        print(" Quarto")
    elif x < 0 and y > 0:
        print("segundo")
    elif x < 0 and y < 0: 
        print("terceiro")
    
    if x == 0 or y == 0:
        break