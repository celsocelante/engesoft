from tema import Tema

class CadastroTemas:

    __init__(self,entrada,revista):
        self.entrada = entrada
        self.revista = revista

        f = open(entrada,'r')
        cabecalho = f.readline().rstrip()
        linha = "."
        while linha != '':
            linha = f.readline().rstrip()
            token = linha.split(';')

            self.codigo = int(token[0])

            self.nome = token[1]
            self.revisores = token[2]

            self.tema = Tema(nome,codigo)
            revisor = revisores.split(',')

            for r in revisor:
                cdg = int(r)
                c = revista.buscaColaborador(cdg)
                self.tema.vinculaRevisor(r)
