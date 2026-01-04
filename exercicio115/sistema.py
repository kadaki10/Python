from exercicio115.lib.interface import *
from exercicio115.lib.arquivo import *
from time import sleep

arq = 'kadaki.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho ('Opção 2')
    elif resposta == 3:
        cabeçalho ('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção valida!\033[m')
    sleep(1)
