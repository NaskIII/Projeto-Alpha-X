import Algorithmia


class TextRobots(object):
    def __init__(self, content=[]):
        self.content = content
        self.text = None

    def wiki(self):
        print("\n" * 2)

        input = {
            "articleName": self.content[1] + " " + self.content[0],
            "lang": "PT"
        }

        client = Algorithmia.client('simyw+zYbXC1hUyLm4AVdUorUMD1')
        algo = client.algo('web/WikipediaParser/0.1.2')
        algo.set_options(timeout=300)
        content = algo.pipe(input).result
        return content

    def pularLinhas(self):
        self.text = self.wiki()
        saida = str(self.text['content'])
        saida = saida.replace('=', '')

        return saida

    def atributos(self):
        return self.text
