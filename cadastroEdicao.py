class CadastroEdicao:
    _init__(self,entrada,revista):
        self.entrada = entrada
        self.revista = revista

    f = open(entrada,'r')

    tema = f.readline().rstrip()
    editor = f.readline().rstrip()
    volume = int(f.readline().rstrip())
    numero = int(f.readline().rstrip())

    data = f.readline().rstrip()

    t = revista.buscaTema(tema)
    c = revista.buscaColaborador(editor)

    revista.setEdicao(Edicao(volume,numero,data,t,c)
