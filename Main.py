import platform
import sys
import os
dir = os.path.dirname(os.path.realpath(__file__ ))
sys.path.append(dir)
from robots import Wikipedia
from robots import Diretorios
from robots import Text_Robots
from robots import Docx

if __name__ == '__main__':
    def clear():
        so = platform.system()

        if so == 'Windows':
            os.system('cls')
        elif so == 'Linux':
            os.system('clear')
        else:
            print('Sistema operacional não suportado')
            sys.exit()

    clear()

    print('''
    ========================WikiText========================
    Versão: 1.4
    Autor: Raphael Nascimento
    ID: Nask!
    Notas: Para sair digite 'exit' ou selecione a opção 4.
    ''')

    termo = input('Digite um termo para o Wikipedia: ')
    if termo == 'exit' or termo == 'sair':
        print('Finalizando')
        sys.exit()
    print()

    wiki = Wikipedia.Wikipedia(termo)
    if wiki.searchs() is True:
        possibleSearchs = wiki.search()

        print('Escolha um item para ser pesquisado:')
        for index, item in enumerate(possibleSearchs):  # Itero minha lista para enumerar
            print(index + 1, item)  # Escrevo o conteudo com uma soma para nao aparecer o valor 0

        choice = input('>> ')
        if choice == '!EXIT' or choice == '!SAIR':
            print('FINISH')
            sys.exit()
        else:
            termo = possibleSearchs[int(choice) - 1]
            wiki.page(termo)

    dire = Diretorios.start(termo)

    content = wiki.content()

    robot = Text_Robots.TextRobots()
    robot.write(content, dire + wiki.title())
    texto = robot.formatarTexto(dire + wiki.title(), wiki.references())
    robot.resumir(texto, dire + wiki.title())
    lista = robot.read(dire + wiki.title())

    doc = Docx.Docx()
    doc.docx(lista, dire, wiki.title())

    robot.apagar(dire + wiki.title())

    print('\nFINISH')