def area(larg, comp):
    a = larg * comp
    print(f'A aréa de um terreno {larg} x {comp} é de {a}m².')


#programa principal
print('Controle de terrenos')
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)