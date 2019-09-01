from robots import New_Text_Robots  # Importo o robo responsavel pelo texto
import platform
import os
import os.path


def start():
    def inputTermo():  # Aqui eu pego um termo para ser pesquisado
        print()
        termo = input('Digite um termo para o Wikipedia: ')
        print()
        return termo

    def inputPrefixo():  # Aqui recebo um prefixo, pois a maquina so sabe o termo, nao o objetivo dele
        prefixos = ['Quem e', 'O que e', 'A historia', 'Exit', '']
        print('Escolha um:')
        for index, item in enumerate(prefixos):  # Itero minha lista para enumerar
            print(index + 1, item)  # Escrevo o conteudo com uma soma para nao aparecer o valor 0

        print()
        escolha = int(input('>>> '))
        return prefixos[escolha - 1]  # Retorno como subtraçao pois somei logo acima

    artigo = {  # Dict que e passada como parametro para o robo de texto
        'termo': inputTermo(),
        'prefixo': inputPrefixo()
    }

    def call():  # Metodo responsavel por chamar todos os robos
        New_Text_Robots.TextRobots(artigo).chamadas()  # Construtor com chamada do metodo

    call()


start()
