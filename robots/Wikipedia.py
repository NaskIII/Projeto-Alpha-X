import wikipedia


class Wikipedia(object):
    def __init__(self, artigo):
        self.termo = artigo['termo']
        self.prefixo = artigo['prefixo']
        wikipedia.set_lang('PT')
        self.pesquisa = wikipedia.page(self.prefixo + ' ' + self.termo)

    def url(self):
        return self.pesquisa.url

    def title(self):
        return self.pesquisa.title

    def content(self):
        return self.pesquisa.content

    def references(self):
        return self.pesquisa.references