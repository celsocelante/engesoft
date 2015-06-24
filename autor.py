from colaborador import Colaborador

class Autor(Colaborador):
    __init__(self,nome,email,endereco,senha,codigo):
        Colaborador.__init__(self,nome,email,endereco,senha,codigo)
        self.instituicoes = []

    def vinculaInstituicao(self,inst):
        instituicoes.append(inst)
