valorA = float(input("digite valor A \n"))
valorB = float(input("digite valor B \n"))
valorC = float(input("digite valor C \n"))


if valorA >= valorB + valorC:
    calc = ((valorA + valorB)* valorC)/2
    print("Area = %.1f" % calc)
elif valorA < valorB + valorC:
    calc = valorA + valorB + valorC
    print("Perimetro = %.1f" % calc)