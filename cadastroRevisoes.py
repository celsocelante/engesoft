class CadastroRevisoes:

    _init__(self,entrada,revista):
        self.entrada = entrada
        self.revista = revista

    f = open(entrada,'r')
    cabecalho = f.readline().rstrip()
    linha = "."

    while linha != '':
        linha = f.readline().rstrip()
        token = linha.split(';')
        
        codigo = int(token[0])
        revisor = int(token[1])

        originalidade = float(token[2].replace(',','.')
        conteudo = float(token[3].replace(',','.')
        apresentacao = float(token[4].replace(',','.')

        c = revista.buscaColaborador(revisor)
        r = c

        avaliacao = Avaliacao(r)
        avaliacao.atribuirNota(originalidade,conteudo,apresentacao)

        artigo = (revista.getEdicao()).buscaArtigo(codigo)

        if artigo != None:
            artigo.adicionaAvaliacao(avaliacao)
            r.vinculaRevisao(artigo)
