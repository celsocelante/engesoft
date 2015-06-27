from avaliacao import Avaliacao
class CadastroRevisoes:

    def __init__(self,entrada,revista):
		self.entrada = entrada
		self.revista = revista

		f = open(self.entrada,'r')
		cabecalho = f.readline().strip()


		for linha in f:
			token = linha.strip().split(';')

			codigo = int(token[0])
			revisor = int(token[1])

			originalidade = float(token[2].replace(',','.'))
			conteudo = float(token[3].replace(',','.'))
			apresentacao = float(token[4].replace(',','.'))
			
			c = revista.buscaColaboradorCodigo(revisor)
			r = c

			avaliacao = Avaliacao(r)
			avaliacao.atribuirNota(originalidade,conteudo,apresentacao)

			artigo = (revista.getEdicao()).buscaArtigo(codigo)

			if artigo is not None:
				artigo.adicionaAvaliacao(avaliacao)
				r.vinculaRevisao(artigo)
