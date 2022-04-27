from lib import interface
from lib import arquivo
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    resposta = interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        arquivo.lerArquivo(arq)
    elif resposta == 2:
        interface.cabeçalho('Opção 2')
    elif resposta == 3:
        interface.cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! digite uma opção válida!\033[m')
    sleep(2)
