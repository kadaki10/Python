from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('>>>>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma de {} com {} vai dar {}'.format(n1, n2, soma))
    if opção == 2:
        multiplicação = n1 * n2
        print('A multiplicação de {} x {} ficaria {}'.format(n1, n2, multiplicação))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} O maior numero é {}'.format(n1, n2, maior))
    elif opção == 4:
            print('Informe os numeros novamente: ')
            n1 = int(input('Digite o primeiro numero: '))
            n2 = int(input('Digite o segundo numero: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente!')
    print('=-=' * 10)
    sleep(1)
print('Fim do programa! Volte sempre! ')








