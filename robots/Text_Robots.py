'''
Autor: Raphael Nascimento
ID: Nask
Objetivo: Buscar termos na Wikipedia e retornar os resultados em formato .txt, alem de
gerar um resumo do conteudo original. No final serao gerados 2 arquivos, um contendo o conteudo do Wikipedia
e o outro o resumo.

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
    7 - self.resumir()
'''

import Algorithmia  # API usada para buscar e resumir o conteudo da wikipedia
import os


class TextRobots(object):  # Classe responsavel por gerar todo o conteudo de texto
    def cleanSentences(self, texto):  # Retiro as sentencas de marcaçao utilizado no Wikipedia
        texto = texto.replace('Referências', '')
        return texto

    def write(self, content, caminho):  # Escrevo o conteudo em um arquivo .txt para poder formatar linha por linha
        self.content = content
        texto = self.cleanSentences(self.content)
        new_arq = open(caminho + '.txt', 'w', encoding='utf-8')
        new_arq.writelines(texto)
        new_arq.close()
        return content

    def contLines(self, path):  # Itero o arquivo para poder saber o numero de linhas
        arq = open(path + '.txt', 'r', encoding='utf-8')
        linhas = len(arq.readlines())
        arq.close()
        return linhas

    def formatarReferencias(self, references):  # Retiro as marcaçoes que estao nas referencias
        referencias = str(references)
        referencias = referencias.replace('[', '')
        referencias = referencias.replace(']', '')
        referencias = referencias.replace("'", '')
        referencias = referencias.replace(',', '\n')
        return referencias

    def formatarTexto(self, caminho, references):  # Formato o texto para ser reescrito no .txt
        linhas = self.contLines(caminho)
        texto_final = ""
        arq = open(caminho + '.txt', 'r', encoding='utf-8')

        for i in range(linhas):
            texto = str(arq.readline())
            if texto != '\n':
                texto = texto.lstrip(" ")
                texto_final += texto

        texto_final.replace('Referências', '')
        arq.close()
        new_arq = open(caminho + '.txt', 'w', encoding='utf-8')
        new_arq.writelines(texto_final)
        new_arq.writelines('\n')
        new_arq.writelines('\n')
        new_arq.writelines('Referências:\n')
        new_arq.writelines(references)
        new_arq.close()
        texto_final = texto_final.replace('\n', '\n\n')
        return texto_final

    def resumir(self, texto, path):  # Metodo utilizado para resumir uma string
        input = texto, 50  # Variavel utilizada para dar entrada no algoritmo
        client = Algorithmia.client('simyw+zYbXC1hUyLm4AVdUorUMD1')  # Faço minha autenticaçao na API
        algo = client.algo('nlp/Summarizer/0.1.8')  # Chamo o Algoritmo que faz resumos
        algo.set_options(timeout=300)  # Defino um tempo maximo de resposta, opcional
        resumo = algo.pipe(input).result  # Recupero o texto resumido

        arquivo = open(path + '_Resumido.txt',
                       'w', encoding='utf-8')  # Gero um novo arquivo para o novo conteudo
        arquivo.writelines(resumo)  # Escrevo o mesmo em um novo arquivo
        arquivo.close()  # Fecha o Arquivo

    def read(self, caminho):  # Irá ler o txt novamente e colocar o conteudo dentro de uma lista
        arquivo = open(caminho + '.txt', 'r', encoding='utf-8')
        linhas = self.contLines(caminho)
        lista = []

        for i in range(linhas):
            lista.append(str(arquivo.readline()))
        arquivo.close()
        return lista

    def apagar(self, path):  # Apago o txt com o mesmo conteúdo do docx
        os.remove(path + '.txt')
