class Artigo:

    __init__(self,codigo,titulo):
        self.codigo = codigo
        self.titulo = titulo
        self.autores = []
        self.revisoes = []

    def vinculaAutor(self,autor):
        self.autores.append(autor)

    def adicionaAvaliacao(self,avaliacao):
        revisoes.append(avalicao)

    def contemAutor(self,autor):
        return autor in autores

    def quantidadeRevisoes(self):
        return len(revisoes) == 3

    def getCodigo(self):
        return self.codigo

    def getTitulo(self):
        return titulo

    def getContato(self):
        if(contato is None):
            return ""
        else:
            return contato.getNome()

    def getRevisao(self):
        return revisoes

    def getMedia(self):
        media = 0
        for(a in revisoes):
            media += a.getSomaNotas()
        return media/3

    def getQuantidadeRevisoes(self):
        return len(revisoes)

    def setContato(self,autor):
        contato = autor

    #Metodo para ordenacao aqui
