import platform
import sys
import os
dir = os.path.dirname(os.path.realpath(__file__ ))
sys.path.append(dir)
from robots import Wikipedia
from robots import Diretorios
from robots import New_Text_Robots
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
    Versão: 1.3
    Autor: Raphael Nascimento
    ID: Nask!
    Notas: Para sair digite 'exit' ou selecione a opção 4.
    ''')

    termo = input('Digite um termo para o Wikipedia: ')
    if termo == 'exit' or termo == 'sair':
        print('Finalizando')
        sys.exit()
    print()

    dire = Diretorios.start(termo)

    wiki = Wikipedia.Wikipedia(termo)
    content = wiki.content()

    robot = New_Text_Robots.TextRobots()
    robot.write(content, dire + wiki.title())
    texto = robot.formatarTexto(dire + wiki.title(), wiki.references())
    robot.resumir(texto, dire + wiki.title())
    lista = robot.read(dire + wiki.title())

    doc = Docx.Docx()
    doc.docx(lista, dire, wiki.title())

    robot.apagar(dire + wiki.title())

    print('\nFINISH')