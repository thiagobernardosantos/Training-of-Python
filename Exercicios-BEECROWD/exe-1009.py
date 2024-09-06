nome = input('')
salario = float(input(''))
vendas = float(input(''))

comissao = salario + (vendas * 0.15)
print('Total = %.2f' % comissao)