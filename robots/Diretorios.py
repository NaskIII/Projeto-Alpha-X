'''
Autor: Raphael Nascimento
ID: Nask
Objetivo: Criar pastas para os arquivos serem criadaos
'''


import platform  # Modulo usado para identificar o SO
import os.path  # Modulo usado para manipular os caminhos


def start(artigo):  # Metodo que recebe uma dict, usado para nomar as pastas

    def diretorios():  # Metodo qye criara os diretorios
        so = platform.system()
        if so == 'Linux':
            dir = os.path.expanduser('~/Documentos/')  # Pego o caminho ate a pasta Documentos
            os.makedirs(dir + 'Arquivos/' + artigo['termo'] + '/', exist_ok=True)  # Crio a pasta Arquivos e outra com o titulo da busca, se existir nao me retorna nenhum exeçao
            dir = os.path.expanduser('~/Documentos/Arquivos/' + artigo['termo'] + '/')  # Pego o caminho completo para ser retornado ao robo de texto
            return dir
        elif so == 'Windows':
            print("...")
    dir = diretorios()

    return dir
