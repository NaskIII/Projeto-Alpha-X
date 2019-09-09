print ('''
========================WikiText========================
Versão: 1.1
Autor: Raphael Nascimento
ID: Nask!
Notas: Para sair digite 'exit' ou selecione a opção 4.
''')

import sys
import os
dir = os.path.dirname(os.path.realpath(__file__ ))
sys.path.append(dir)
import robots.New_Text_Robots # Importo o robo responsavel pelo texto


def start():
    def inputTermo():  # Aqui eu pego um termo para ser pesquisado
        print()
        termo = input('Digite um termo para o Wikipedia: ')
        if termo == 'exit' or termo == 'sair':
            print('Finalizando')
            sys.exit()
        print()
        return termo

    def inputPrefixo():  # Aqui recebo um prefixo, pois a maquina so sabe o termo, nao o objetivo dele
        prefixos = ['Quem e', 'O que e', 'A historia', 'Exit', '']
        print('Escolha um:')
        for index, item in enumerate(prefixos):  # Itero minha lista para enumerar
            print(index + 1, item)  # Escrevo o conteudo com uma soma para nao aparecer o valor 0

        print()
        escolha = int(input('>>> '))
        if escolha == 4:
            print('Finalizando')
            sys.exit()
        return prefixos[escolha - 1]  # Retorno como subtraçao pois somei logo acima

    artigo = {  # Dict que e passada como parametro para o robo de texto
        'termo': inputTermo(),
        'prefixo': inputPrefixo()
    }

    def call():  # Metodo responsavel por chamar todos os robos
        robots.New_Text_Robots.TextRobots(artigo).chamadas()  # Construtor com chamada do metodo

    call()
    print('\nFinalizando...')

start()
