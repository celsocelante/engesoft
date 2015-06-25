class Artigo:

    def __init__(self,codigo,titulo):
        self.codigo = codigo
        self.titulo = titulo
        self.autores = []
        self.revisoes = []
	self.contato = None 
	
    def vinculaAutor(self,autor):
        self.autores.append(autor)

    def adicionaAvaliacao(self,avaliacao):
        self.revisoes.append(avaliacao)

    def contemAutor(self,autor):
        return autor in self.autores

    def quantidadeRevisoes(self):
        return len(self.revisoes) == 3

    def getCodigo(self):
        return self.codigo

    def getTitulo(self):
        return self.titulo

    def getContato(self):
        if self.contato is None:
            return ""
        else:
            return self.contato.getNome()

    def getRevisao(self):
        return revisoes

    def getMedia(self):
        media = 0
        for a in revisoes:
            media += a.getSomaNotas()
        return media/3

    def getQuantidadeRevisoes(self):
        return len(revisoes)

    def setContato(self,autor):
        self.contato = autor

    #Metodo para ordenacao aqui
