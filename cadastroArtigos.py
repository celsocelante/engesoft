from artigo import Artigo

class CadastroArtigos:
    def __init__(self,entrada,revista):
        self.entrada = entrada
        self.revista = revista

	f = open(self.entrada,'r')
	cabecalho = f.readline().strip()	

	for linha in f:	    
	    token = linha.strip().split(';')
	    token.pop()
	    codigo = int(token[0])
	    titulo = token[1]
	    artigo = Artigo(codigo,titulo)

	    (revista.getEdicao()).submeterArtigo(artigo)

	    autorContato = None

	    autores = token[2]
	    token2 = autores.split(',')

	    cdg = int(token2[0])
	    c = revista.buscaColaborador(cdg)
	    autor = c

	    autorContato = c
	    artigo.vinculaAutor(c)
	    artigo.setContato(autorContato)	   
	    if len(token) > 3:
		contato = int(token[3])

		c = revista.buscaColaborador(contato)

		autor = c
		if artigo.contemAutor(autor):
		    artigo.setContato(autor)
                
