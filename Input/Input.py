def start():
    def inputTermo():
        print()
        termo = input('Digite um termo para o Wikipedia: ')
        print()
        return termo

    def inputPrefixo():
        prefixos = ['Quem e', 'O que e', 'A historia', 'Sair']
        print ('Escolha um:')
        for index, item in enumerate(prefixos):
            print(index + 1, item)

        print()
        escolha = int(input('>>'))
        return prefixos[escolha-1]

    content = []
    content.append(inputTermo())
    content.append(inputPrefixo())
    print(content)

start()
