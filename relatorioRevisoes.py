# -*- coding: utf-8 -*-
class RelatorioRevisoes:
    def __init__(self,revista):
        self.revista = revista

    #Metodo pra ordenação de conjunto de artigos?

    def escreveRelatorio(self):
        arq = open("relat-revisoes.csv",'w')

        arq.write("Artigo;Autor de contato;Média das avaliacões;Revisor 1; Revisor2; Revisor 3")

        for artigo in self.revista.getEdicao().getArtigos():
            arq.write("\n")
            arq.write(artigo.getTitulo() + ";" + artigo.getContato() + ";" + format(artigo.getMedia(),'.2f') + ";")
            for avaliacao in artigo.getRevisao():
                arq.write(avaliacao.getRevisor().getNome() + ";")

        arq.close()
