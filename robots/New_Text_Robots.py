'''
Autor: Raphael Nascimento
ID: Nask
Objetivo: Escrever em um arquvo para que o mesmo seja formatado
'''


import Algorithmia


class TextRobots(object):
    def __init__(self, artigo, caminho):
        self.artigo = artigo
        self.caminho = caminho
        self.content = None

    def wiki(self):
        print(self.artigo)
        input = {
            "articleName": self.artigo['prefixo'] + " " + self.artigo['termo'],
            "lang": "PT"
        }

        client = Algorithmia.client('simyw+zYbXC1hUyLm4AVdUorUMD1')
        algo = client.algo('web/WikipediaParser/0.1.2')
        algo.set_options(timeout=300)
        content = algo.pipe(input).result
        return content

    def cleanSentences(self, texto):
        texto = texto.replace('=', '')
        texto = texto.replace('Referências', '')
        return  texto

    def write(self):
        content = self.wiki()
        self.content = content
        texto = self.cleanSentences(self.content['content'])
        new_arq = open(self.caminho + self.content['title'] + '.txt', 'w')
        new_arq.writelines(texto)
        new_arq.close()
        return content

    def contLines(self):
        self.write()
        arq = open(self.caminho + self.content['title'] + '.txt', 'r')
        linhas = len(arq.readlines())
        arq.close()
        return linhas

    def formatarReferencias(self):
        referencias = str(self.content['references'])
        referencias = referencias.replace('[', '')
        referencias = referencias.replace(']', '')
        referencias = referencias.replace("'", '')
        referencias = referencias.replace(',', '\n')
        return referencias

    def formatarTexto(self):
        linhas = self.contLines()
        texto_final = ""
        arq = open(self.caminho + self.content['title'] + '.txt', 'r')

        for i in range(linhas):
            texto = str(arq.readline())
            texto = texto.lstrip(" ")
            texto_final += texto

        texto_final.replace('Referências', '')
        arq.close()
        new_arq = open(self.caminho + self.content['title'] + '.txt', 'w')
        new_arq.writelines(texto_final)
        new_arq.writelines('\n')
        new_arq.writelines('\n')
        new_arq.writelines('Referências:\n')
        new_arq.writelines(self.formatarReferencias())
        new_arq.close()
        texto_final = texto_final.replace('\n', '\n\n')
        return texto_final

    def resumir(self):
        texto = self.formatarTexto()

        input = texto, 50
        client = Algorithmia.client('simyw+zYbXC1hUyLm4AVdUorUMD1')
        algo = client.algo('nlp/Summarizer/0.1.8')
        algo.set_options(timeout=300)  # optional
        resumo = algo.pipe(input).result

        arquivo = open(self.caminho + self.content['title'] + '_Resumido.txt', 'w')
        arquivo.writelines(resumo)
        arquivo.close()