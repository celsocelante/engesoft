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
	    codigo = token[0]
	    nome = token[1]
	    email = token[2]
	    senha = token[3]
	    instituicao = token[4]
	    endereco = token[5]
	    tipo = token[6]

	    cdg = int(codigo)
	    if tipo == "A":
		autor = Autor(nome,email,endereco,senha,cdg)
		autor.vinculaInstituicao(instituicao)
		revista.adicionaColaborador(autor)

	    if tipo == "R":
		revisor = Revisor(nome,email,endereco,senha,cdg)
		revisor.vinculaInstituicao(instituicao)
		revista.adicionaColaborador(revisor)