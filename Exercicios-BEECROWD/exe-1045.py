TV1,TV2,TV3 = input("").split()
V1 = float(TV1)
V2 = float(TV2)
V3 = float(TV3)

if V1 > V2 and V1 > V3:
    A = V1
    if V2 > V3:
        B = V2
        C = V3
    else:
        B = V3
        C = V2
elif V2 > V1 and V2 > V3:
    A = V2
    if V1 > V3:
        B = V1
        C = V3
    else:
        B = V3
        C = V1
else:
    A = V3
    if V1 > V2:
        B = V1
        C = V2
    else:
        B = V2
        C = V1
# agora temos a resolução de verade
if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A*2 == B*2 + C*2:
        print("TRIANGULO RETANGULO")
    elif A*2 > B*2 + C*2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")
        
    if A == B and B == C and A == C:
        print("TRIANGULO EQUILATERO")
    elif (A == B and A != C) or (A == C and A != B) or (B == C and B != A):
        print("TRIANGULO ISOSCELES")