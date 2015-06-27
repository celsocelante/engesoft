import sys
from revista import Revista
from interpretador import Interpretador
from cadastroEdicao import CadastroEdicao
from cadastroArtigos import CadastroArtigos
from cadastroPessoas import CadastroPessoas
from cadastroRevisoes import CadastroRevisoes
from cadastroTemas import CadastroTemas
from resumo import Resumo
from relatorioRevisoes import RelatorioRevisoes
from relatorioRevisores import RelatorioRevisores

args = sys.argv

revista = Revista("EngSoft")

interpretador = Interpretador(args)

entradas = []

entradas = interpretador.retornaEntradas()

#Instanciando objetos que fazem a leitura

pessoas = CadastroPessoas(entradas[2],revista)
temas = CadastroTemas(entradas[1],revista)
edicao = CadastroEdicao(entradas[0],revista)
artigos = CadastroArtigos(entradas[3],revista)
revisoes = CadastroRevisoes(entradas[4],revista)


resumo = Resumo(revista)
resumo.escreveResumo()

relatRevisoes = RelatorioRevisoes(revista)
RelatorioRevisoes.escreveRelatorio()


relatRevisores = RelatorioRevisores(revista)
relatRevisores.escreveRelatorio()