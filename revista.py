from revisor import Revisor
class Revista:
    def __init__(self,nome):
        self.nome = nome
        self.temas = []
        self.colaboradores = []
        self.edicao = None

    def adicionaTema(self,tema):
        self.temas.append(tema)

    def adicionaColaborador(self,colaborador):
        self.colaboradores.append(colaborador)

    def buscaColaboradorCodigo(self,codigo):
        for c in self.colaboradores:
            if c.getCodigo() == int(codigo):
                return c
        return None

    def buscaColaboradorNome(self,nome):
        for c in self.colaboradores:
            if c.getNome() == nome:
                return c
        return None

    def buscaTema(self,titulo):
        for t in self.temas:
            if titulo == t.getTitulo():
                return t
        return None

    def setEdicao(self,edicao):
        self.edicao = edicao

    def getEdicao(self):
        return self.edicao

    def getColaboradores(self):
        return self.colaboradores

    def getRevisoresEnvolvidos(self):
        qnt = 0
        for c in self.colaboradores:
            if isinstance(c,Revisor):
                if len(c.getRevisoes()) != 0:
                    qnt+=1
        return qnt

    def getArtigosRevisados(self):
        totalArtigosRevisados=0
        for c in self.colaboradores:
            if isinstance(c,Revisor):
                if len(c.getRevisoes()) != 0:
                    totalArtigosRevisados+=c.getQuantidadeArtigos()

        return totalArtigosRevisados
