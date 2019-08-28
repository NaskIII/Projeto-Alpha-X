'''
Autor: Raphael Nascimento
ID: Nask
Objetivo: Escrever em um arquvo para que o mesmo seja formatado
'''


class Write(object):
    def __init__(self, caminho, text):
        self.caminho = caminho
        self.text = text
        self.titulo = None
        self.referencias = None

    def write(self):
        new_arq = open(self.caminho + self.titulo + ".txt", "w")
        new_arq.writelines(self.text)
        new_arq.close()

    def countLines(self):
        arq = open(self.caminho + self.titulo + ".txt", "r")
        return len(arq.readlines())

    def formatar(self):
        texto_final = ""
        arq = open(self.caminho + self.titulo + ".txt", "r")

        for linhas in range(self.countLines()):
            texto = str(arq.readline())
            texto = texto.lstrip(" ")
            texto_final += texto

        texto_final = texto_final.replace("Referências ", '')
        new_arq = open(self.caminho + self.titulo + ".txt", 'w')
        new_arq.writelines(texto_final)
        new_arq.writelines("\n")
        new_arq.writelines("\n")
        new_arq.writelines("Referências:\n")
        new_arq.writelines(self.referencias)
        arq.close()
        new_arq.close()
        return texto_final

    def atributos(self, lista):
        self.titulo = lista['title']
        self.referencias = str(lista['references'])
        self.organizar()
        self.write()
        self.countLines()
        text = self.formatar()
        return lista

    def organizar(self):
        self.referencias = self.referencias.replace('[', '')
        self.referencias = self.referencias.replace(']', '')
        self.referencias = self.referencias.replace("'", '')
        self.referencias = self.referencias.replace(',', '\n')

    def conteudoSanitizado(self, content, resumo):
        resumo = resumo.replace('=', '')
        resumo = resumo.lstrip(" ")
        arq = open(self.caminho + self.text['title'] + "_Resumido.txt", "w")
        arq.writelines(resumo)
        arq.close()