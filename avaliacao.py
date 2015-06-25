class Avaliacao:
      def __init__(self,revisor):
	  self.revisor = revisor
	  self.originalidade = 0
	  self.conteudo = 0
	  self.apresentacao = 0
	  self.somaNotas = 0

      def getRevisor(self):
	  return self.revisor

      def getSomaNotas(self):
	  return self.somaNotas

      def atribuirNota(self,originalidade,conteudo,apresentacao):
	  self.originalidade = originalidade
	  self.conteudo = conteudo
	  self.apresentacao = apresentacao
	  self.somaNotas = self.originalidade + self.conteudo + self.apresentacao

	  #Metodo para ordenacao do set
