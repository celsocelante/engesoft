# -*- coding: utf-8 -*-
class Resumo:
    def __init__(self,revista):
        self.revista = revista

    def escreveResumo(self):
        edicao = self.revista.getEdicao()

        arq = open("relat-resumo.txt",'w')

        #arq.write("EngeSoft, num. " + str(edicao.getNumero()) + str(edicao.getVolume()) + " - " + edicao.getData() + "\n")

        if edicao.getTema() is not None:
            arq.write("Tema " + edicao.getTema().getTitulo() + "\n")

        arq.write("Editor-chefe: ")
        if edicao.getEditorChefe() is not None:
            arq.write(edicao.getEditorChefe().getNome() + "\n\n")

        arq.write("Consistência dos dados:\n")
        arq.write("- Nenhum problema encontrado.\n\n")

        #arq.write("Artigos submetidos: " + str(len(self.revista.getEdicao().getArtigos())))
        #arq.write("Revisores capacitados: " + str(self.revista.getEdicao().getTema().getQuantidadeRevisores()))
        arq.write("Revisores envolvidos: " + str(self.revista.getRevisoresEnvolvidos()) + "\n")

        #Ver como converter para padrão brasileiro
        media = self.revista.getArtigosRevisados()/self.revista.getRevisoresEnvolvidos()

        arq.write("Média artigos/revisor: " + str(media) + ".")
        arq.close()
