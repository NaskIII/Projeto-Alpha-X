import Algorithmia
from Old_robots import Write


class Resumir(object):
    def __init__(self, text):
        self.text = text

    def resumir(self):
        input = self.text['content'], 50
        client = Algorithmia.client('simyw+zYbXC1hUyLm4AVdUorUMD1')
        algo = client.algo('nlp/Summarizer/0.1.8')
        algo.set_options(timeout=300)  # optional
        resumo = algo.pipe(input).result
        return resumo

    def arquivoResumo(self):
        arquivo = Write.Write("/home/nask/Documentos/Arquivos/", self.text)
        arquivo.conteudoSanitizado(self.text, self.resumir())