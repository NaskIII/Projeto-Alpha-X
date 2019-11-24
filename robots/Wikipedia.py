import sys
import wikipedia


class Wikipedia(object):
    def __init__(self, artigo):
        wikipedia.set_lang('PT')
        self.pesquisa = wikipedia.page(artigo)

    def url(self):
        return self.pesquisa.url

    def title(self):
        return self.pesquisa.title

    def content(self):
        try:
            return self.pesquisa.content
        except wikipedia.exceptions.PageError:
            print('O conteúdo informado não foi encontrado, tente buscar com outras palavras!')
            sys.exit()

    def references(self):
        return self.pesquisa.references