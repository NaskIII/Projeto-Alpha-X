import platform
import sys
import os
dir = os.path.dirname(os.path.realpath(__file__ ))
sys.path.append(dir)
import robots.New_Text_Robots # Importo o robo responsavel pelo texto


def start():
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
    
    print ('''
========================WikiText========================
Versão: 1.3
Autor: Raphael Nascimento
ID: Nask!
Notas: Para sair digite 'exit' ou selecione a opção 4.
''')
            
    def inputTermo():  # Aqui eu pego um termo para ser pesquisado
        print()
        termo = input('Digite um termo para o Wikipedia: ')
        if termo == 'exit' or termo == 'sair':
            print('Finalizando')
            sys.exit()
        print()
        return termo

    def inputPrefixo():  # Aqui recebo um prefixo, pois a maquina so sabe o termo, nao o objetivo dele
        prefixos = ['Quem é', 'O que é', 'A história', 'Exit', '']
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
