# -*- coding: utf-8 -*-
from revisor import Revisor

class RelatorioRevisores:
    def __init__(self,revista):
        self.revista = revista

    def getMediaNotasAtribuidas(self,revisor):
        media = 0.0

        for artigo in revisor.getRevisoes():
            for avaliacao in artigo.getRevisao():
                if revisor.getNome() == avaliacao.getRevisor().getNome():
                    media += avaliacao.getSomaNotas()
        return media/revisor.getQuantidadeArtigos()

    def escreveRelatorio(self):
        arq = open("relat-revisores.csv",'w')

        arq.write("Revisor;Qtd. artigos revisados;Média das notas atribuídas")

        for colaborador in self.revista.getColaboradores():
            if isinstance(colaborador,Revisor):
                r = colaborador
                if r.participouDaEdicao():
                    arq.write("\n")
                    arq.write(r.getNome() + ";" + str(r.getQuantidadeArtigos()) + ";" + str(self.getMediaNotasAtribuidas(r)))

        arq.close()
