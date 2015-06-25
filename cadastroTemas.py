from tema import Tema

class CadastroTemas:

    def __init__(self,entrada,revista):
        self.entrada = entrada
        self.revista = revista

        f = open(self.entrada,'r')
        cabecalho = f.readline().strip()
        
        for linha in f:           
            token = linha.strip().split(';')
            self.codigo = int(token[0])

            self.nome = token[1]
            self.revisores = token[2]

            self.tema = Tema(self.nome,self.codigo)
            revisor = self.revisores.split(',')

            for r in revisor:
                cdg = int(r)
                c = revista.buscaColaborador(cdg)
                self.tema.vinculaRevisor(r)
