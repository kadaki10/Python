casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de {:.2f} em {} anos'.format(casa, anos))
print('A prestação será de {:.2f}'.format(prestação))
if prestação <= minimo:
    print('VOCE FOI APROVADO! PODEMOS SEGUIR ADIANTE!')
else:
    print('VOCE FOI NEGADO! INFELIZMENTE NAO PODEMOS SEGUIR ADIANTE')
