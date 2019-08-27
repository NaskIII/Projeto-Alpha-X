'''
Autor: Raphael Nascimento
ID: Nask
Objetivo: Escrever em um arquvo para que o mesmo seja formatado
'''

class Write(object):
    def __init__(self, caminho, text):
        self._caminho = caminho
        self._text = text

    @property
    def caminho(self):
        return self._caminho

    @caminho.setter
    def caminho(self, caminho):
        self._caminho = caminho

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    def write(self):
        new_arq = open(self.caminho + "Arquivo.txt", "w")
        new_arq.writelines(self.text)
        new_arq.close()

    def formatar(self):
        arq = open(self.caminho + "Arquivo.txt", "r")
        linhas = len(arq.readlines())
        arq.close()
        print(linhas)
        numero = 0
        texto_final = ""
        arq = open(self.caminho + "Arquivo.txt", "r")
        while numero <= linhas:
            numero += 1
            if numero != 1:
                texto = str(arq.readline())
                texto = texto.lstrip(" ")
                if texto != ' Ver também ':
                    texto_final += texto
                else:
                    print('Teste')
                    numero = linhas + 10
            else:
                texto = str(arq.readline())
                texto_final += texto
        new_arq = open(self.caminho + "Arquivo_Formatado.txt", 'w')
        new_arq.writelines(texto_final)
        arq.close()
        new_arq.close()
