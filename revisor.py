from colaborador import Colaborador

class Revisor(Colaborador):
    def __init__(self,nome,email,endereco,senha,codigo):
        Colaborador.__init__(self,nome,email,endereco,senha,codigo)
        self.instituicoes = []
        self.revisoes = []

    def vinculaInstituicao(self,inst):
        self.instituicoes.append(inst)

    def vinculaRevisao(self,artigo):
        self.revisoes.append(artigo)

    def participouDaEdicao(self):
        return len(revisoes) != 0

    def getRevisoes(self):
        return self.revisoes

    def getQuantidadeArtigos(self):
        return len(self.revisoes)

    
