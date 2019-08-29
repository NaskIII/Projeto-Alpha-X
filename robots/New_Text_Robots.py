'''
Autor: Raphael Nascimento
ID: Nask
Objetivo: Buscar termos na Wikipedia e retornar os resultados em formato .txt, alem de
gerar um resumo do conteudo original. No final serao gerados 2 arquivos, um contendo o conteudo do Wikipedia
e o outro o resumo.
'''

'''
FLUXO DE CHAMADAS DOS METODOS!!!
    1 - self.resumir()
    2 - self.formatarTexto()
    3 - countLines()
    4 - self.write()
    5 - self.wiki()
    6 - self.cleanSentences()
    7 - formatarReferencias()
    
    FLUXO DE FUNCIONAMENTO DO CODIGO!!!
    1 - self.wiki()
    2 - self.write()
    3 - self.cleanSentences()
    4 - contLines()
    5 - self.formatarTexto()
    6 - self.formatarReferencias()
    7 - self.resumir
'''

import Algorithmia  # API usada para buscar e resumir o conteudo da wikipedia


class TextRobots(object):  # Classe responsavel por gerar todo o conteudo de texto
    def __init__(self, artigo, caminho):
        self.artigo = artigo
        self.caminho = caminho
        self.content = None

    def wiki(self):  # Metodo usado para pegar o conteudo
        input = {
            "articleName": self.artigo['prefixo'] + " " + self.artigo['termo'],  # Aqui passamos os termos e os prefixos
            "lang": "PT"  # Aqui definimos a linguagem
        }

        client = Algorithmia.client('simyw+zYbXC1hUyLm4AVdUorUMD1')  # Faço minha autenticaçao na API
        algo = client.algo('web/WikipediaParser/0.1.2')  # Utilizo o algoritmo que manipula o conteudo do Wikipedia
        algo.set_options(timeout=300)  # Defino um tempo maximo de resposta, opcional
        content = algo.pipe(input).result  # O Algoritmo me retorna uma Dict contendo o conteudo, link das imagens, titulo, links em geral e referencias
        return content

    def cleanSentences(self, texto):  # Retiro as sentencas de marcaçao utilizado no Wikipedia
        texto = texto.replace('=', '')
        texto = texto.replace('Referências', '')
        return  texto

    def write(self):  # Escrevo o conteudo em um arquivo .txt para poder formatar linha por linha
        content = self.wiki()
        self.content = content
        texto = self.cleanSentences(self.content['content'])
        new_arq = open(self.caminho + self.content['title'] + '.txt', 'w')
        new_arq.writelines(texto)
        new_arq.close()
        return content

    def contLines(self):  # Itero o arquivo para poder saber o numero de linhas
        self.write()
        arq = open(self.caminho + self.content['title'] + '.txt', 'r')
        linhas = len(arq.readlines())
        arq.close()
        return linhas

    def formatarReferencias(self):  # Retiro as marcaçoes que estao nas referencias
        referencias = str(self.content['references'])
        referencias = referencias.replace('[', '')
        referencias = referencias.replace(']', '')
        referencias = referencias.replace("'", '')
        referencias = referencias.replace(',', '\n')
        return referencias

    def formatarTexto(self):  # Formato o texto para ser reescrito no .txt
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

    def resumir(self):  # Metodo utilizado para resumir uma string
        texto = self.formatarTexto()  # Recupero o texto formatado

        input = texto, 50  # Variavel utilizada para dar entrada no algoritmo
        client = Algorithmia.client('simyw+zYbXC1hUyLm4AVdUorUMD1')  # Faço minha autenticaçao na API
        algo = client.algo('nlp/Summarizer/0.1.8')  # Chamo o Algoritmo que faz resumos
        algo.set_options(timeout=300)  # Defino um tempo maximo de resposta, opcional
        resumo = algo.pipe(input).result  # Recupero o texto resumido

        arquivo = open(self.caminho + self.content['title'] + '_Resumido.txt', 'w')  # Gero um novo arquivo para o novo conteudo
        arquivo.writelines(resumo)  # Escrevo o mesmo em um novo arquivo
        arquivo.close()  # FIM