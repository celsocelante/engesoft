class Resumo:
    __init__(self,revista):
        self.revista = revista

    def escreveResumo(self):
        edicao = self.revista.getEdicao()

        file = open("relat-resumo.txt",'w')

        file.write("EngeSoft, num. " + str(edicao.getNumero()) + str(edicao.getVolume()) + " - " + edicao.getData() + "\n")

        if edicao.getTema() != None:
            file.write("Tema " + edicao.getTema().getTitulo() + "\n")

        file.write("Editor-chefe: ")
        if edicao.getEditorChefe() != None:
            file.write(edicao.getEditorChefe().getNome() + "\n\n")

        file.write("Consistência dos dados:")
        file.write("- Nenhum problema encontrado.\n\n")

        file.write("Artigos submetidos: " + str(len(revista.getEdicao().getArtigos())))
        file.write("Revisores capacitados: " + str(revista.getEdicao().getTema().getQuantidadeRevisores()))
        file.write("Revisores envolvidos: " + str(revista.getRevisoresEnvolvidos()))

        #Ver como converter para padrão brasileiro
        media = revista.getArtigosRevisados()/revista.getRevisoresEnvolvidos()

        file.write("Média artigos/revisor: " + str(media).)
        file.close()
