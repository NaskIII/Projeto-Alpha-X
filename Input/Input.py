from robots import Text_Robots

def start():
    def inputTermo():
        print()
        termo = input('Digite um termo para o Wikipedia: ')
        print()
        return termo

    def inputPrefixo():
        prefixos = ['Quem e', 'O que e', 'historia', 'Sair']
        print ('Escolha um:')
        for index, item in enumerate(prefixos):
            print(index + 1, item)

        print()
        escolha = int(input('>>'))
        return prefixos[escolha-1]

    robots = Text_Robots
    content = []
    content.append(inputTermo())
    content.append(inputPrefixo())
    rob = robots.TextRobots(content)
    rob.wiki()


start()
