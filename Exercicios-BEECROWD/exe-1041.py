eixox = float(input("digite o primeiro eixo"))
eixoy = float(input("digite o segundo eixo"))

if eixox > 0 and eixoy > 0:
    print("Quadrante Q1")

elif eixox > 0 and eixoy < 0:
    print("Quadrante Q4")

elif eixox < 0 and eixoy > 0:
    print("Quadrante Q2")

elif eixox < 0 and eixoy < 0:
    print("Quadrante Q3")

elif eixox == 0 and eixoy == 0:
    print("Origem")

elif eixox == 0:
    print("Eixo X")

elif eixoy == 0:
    print("Eixo y")