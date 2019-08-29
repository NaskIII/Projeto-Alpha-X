from robots import New_Text_Robots


def start():
    def inputTermo():
        print()
        termo = input('Digite um termo para o Wikipedia: ')
        print()
        return termo

    def inputPrefixo():
        prefixos = ['Quem e', 'O que e', 'A historia', 'Exit', '']
        print ('Escolha um:')
        for index, item in enumerate(prefixos):
            print(index + 1, item)

        print()
        escolha = int(input('>> '))
        return prefixos[escolha-1]

    artigo = {
        'termo': inputTermo(),
        'prefixo': inputPrefixo()
    }

    def call():
        robotText = New_Text_Robots.TextRobots(artigo, '/home/nask/Documentos/Arquivos/').resumir()

    call()
start()