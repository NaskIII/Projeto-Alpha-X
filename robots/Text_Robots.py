import Algorithmia


class TextRobots(object):
    def __init__(self, content=[]):
        self.content = content

    def wiki(self):
        print("\n"*3)

        input = {
            "articleName": self.content[1] + "\n" + self.content[0],
            "lang": "PT"
        }

        client = Algorithmia.client('simyw+zYbXC1hUyLm4AVdUorUMD1')
        algo = client.algo('web/WikipediaParser/0.1.2')
        algo.set_options(timeout=300)
        print(algo.pipe(input).result)

    def slice(self, text):
        for i in text:
            print(i)
            if i == '\\':
                print("\n")