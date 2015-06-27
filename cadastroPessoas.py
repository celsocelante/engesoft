from autor import Autor
from revisor import Revisor

class CadastroPessoas:
    def __init__(self,entrada,revista):
		self.entrada = entrada
		self.revista = revista

		f = open(self.entrada,'r')
		cabecalho = f.readline().strip()
		

		for linha in f:	    
			token = linha.split(';')
			codigo = int(token[0])
			nome = token[1].replace("\n","")
			email = token[2].replace("\n","")
			senha = token[3].replace("\n","")
			instituicao = token[4].replace("\n","")
			endereco = token[5].replace("\n","")
			tipo = token[6].replace("\n","")

			if tipo == "A":
				autor = Autor(nome,email,endereco,senha,codigo)
				autor.vinculaInstituicao(instituicao)
				revista.adicionaColaborador(autor)

			if tipo == "R":
				revisor = Revisor(nome,email,endereco,senha,codigo)
				revisor.vinculaInstituicao(instituicao)
				revista.adicionaColaborador(revisor)