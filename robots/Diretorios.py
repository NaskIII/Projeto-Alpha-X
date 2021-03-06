'''
Autor: Raphael Nascimento
ID: Nask
Objetivo: Criar pastas para os arquivos serem criadaos
'''

import os.path  # Modulo usado para manipular os caminhos
import platform  # Modulo usado para identificar o SO
import sys


def start(artigo):  # Metodo que recebe uma dict, usado para nomear as pastas

    def diretorios():  # Metodo qye criara os diretorios
        so = platform.system()
        if so == 'Linux':
            dir = os.path.expanduser('~/Documentos/')  # Pego o caminho ate a pasta Documentos
            os.makedirs(dir + 'Arquivos/' + artigo+ '/', exist_ok=True)  # Crio a pasta Arquivos e outra com o titulo da busca, se existir nao me retorna nenhum exeçao
            dir = os.path.expanduser('~/Documentos/Arquivos/' + artigo + '/')  # Pego o caminho completo para ser retornado ao robo de texto
            return dir
        elif so == 'Windows':
            dir = os.path.expanduser('~\\OneDrive\\Documentos\\')
            os.makedirs(dir + 'Arquivos\\' + artigo + '\\', exist_ok=True)
            dir = os.path.expanduser('~\\OneDrive\\Documentos\Arquivos\\' + artigo + '\\')
            return dir
        else:
            print('Sistema operacional não identificado')
            sys.exit()

    dir = diretorios()

    return dir
