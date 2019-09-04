from Old_robots import Text_Robots, Resumir, Write


def start():
    def inputTermo():
        print()
        termo = input('Digite um termo para o Wikipedia: ')
        print()
        return termo

    def inputPrefixo():
        prefixos = ['Quem e', 'O que e', 'A historia', 'Exit', '']
        print('Escolha um:')
        for index, item in enumerate(prefixos):
            print(index + 1, item)

        print()
        escolha = int(input('>> '))
        return prefixos[escolha - 1]

    robots = Text_Robots
    content = []
    content.append(inputTermo())
    content.append(inputPrefixo())

    def call():  # Chamada dos Robos
        rob = robots.TextRobots(content)
        robo = Write.Write("/home/nask/Documentos/Arquivos/", rob.pularLinhas())
        text = robo.atributos(rob.atributos())
        res = Resumir.Resumir(text)
        res.arquivoResumo()

    call()


start()
