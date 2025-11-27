sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, digite um sexo valido: '))
print('Sexo {} registrado com sucesso obrigado!'.format(sexo))


