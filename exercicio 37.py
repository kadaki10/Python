numero = int(input('Digite um numero qualquer: '))
print(''' Escolha uma das bases para conversão: 
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINARIO é igual a {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção invalida. tente novamente')
