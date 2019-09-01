import platform
import os
import os.path


def start(artigo):

    def diretorios():
        so = platform.system()
        if so == 'Linux':
            dir = os.path.expanduser('~/Documentos/')
            os.makedirs(dir + 'Arquivos/' + artigo['termo'] + '/', exist_ok=True)
            dir = os.path.expanduser('~/Documentos/Arquivos/' + artigo['termo'] + '/')
            return dir
        elif so == 'Windows':
            print("...")
    dir = diretorios()

    return dir
