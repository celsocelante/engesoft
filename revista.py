class Revista:
    __init__(self,nome):
        self.nome = nome
        self.temas = []
        self.colaboradores = []
        self.edicao = None

    def adicionaTema(self,tema):
        self.temas.append(tema)

    def adicionaColaborador(self,colaborador):
        self.colaboradores.append(colaborador)

    def buscaColabordor(self,codigo):
        for c in colaboradores:
            if c.getCodigo() == codigo:
                return c
        return None

    def buscaColaborador(self,nome):
        for c in colaboradores:
            if nome == c.getNome():
                return c
        return None

    def buscaTema(self,titulo):
        for t in temas:
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
        qnt=0
        for c in colaboradores:
            if isinstance(c,Revisor):
                if len(c.getRevisoes()) != 0:
                    qnt+=1
        return qnt

    def getArtigosRevisados(self):
        totalArtigosRevisados=0
        for c in colaboradores:
            if isinstance(c,Revisor):
                if len(c.getRevisoes()) != 0:
                    totalArtigosRevisados+=c.getQuantidadeArtigos()

        return totalArtigosRevisados
