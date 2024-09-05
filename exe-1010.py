peca1 = int(input(''))
quant1 = int(input(''))
valor1 = float(input(''))

peca2 = int(input(''))
quant2 = int(input(''))
valor2 = float(input(''))

preco1 = quant1 * valor1
preco2 = quant2 * valor2

total = preco1 + preco2
print('Valor a Pagar: %.2f' % total)