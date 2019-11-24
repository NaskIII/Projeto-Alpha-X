import sys
import wikipedia


class Wikipedia(object):
    def __init__(self, artigo):
        self.artigo = artigo
        wikipedia.set_lang('PT')
        self.pesquisa = wikipedia.page(artigo)

    def searchs(self):
        if len(wikipedia.search(self.artigo)) > 0:
            return True
        else:
            return False

    def search(self):
        return wikipedia.search(self.artigo)

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

    def page(self, artigo):
        self.pesquisa = wikipedia.page(artigo)