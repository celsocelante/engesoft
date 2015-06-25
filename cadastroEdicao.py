from edicao import Edicao
class CadastroEdicao:
    def __init__(self,entrada,revista):
        self.entrada = entrada
        self.revista = revista

	f = open(self.entrada,'r')

	tema = f.readline().strip()
	editor = f.readline().strip()
	volume = int(f.readline().strip())
	numero = int(f.readline().strip())

	data = f.readline().rstrip()

	t = revista.buscaTema(tema)
	c = revista.buscaColaborador(editor)

	self.revista.setEdicao(Edicao(volume,numero,data,t,c))
