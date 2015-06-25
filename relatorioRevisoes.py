class RelatorioRevisoes:
    def __init__(self,revista):
        self.revista = revista

    #Metodo pra ordenação de conjunto de artigos?

    def escreveRelatorio(self):
        file = open("relat-revisoes.csv",'w')

        file.write("Artigo;Autor de contato;Média das avaliacões;Revisor 1; Revisor2; Revisor 3")

        for artigo in revista.getEdicao().getArtigos():
            file.write("\n")
            file.write(artigo.getTitulo() + ";" + artigo.getContato() + ";" + str(artigo.getMedia()) + ";")
            for avaliacao in artigo.getRevisao():
                file.write(avaliacao.getRevisor().getNome() + ";")

        file.close()
