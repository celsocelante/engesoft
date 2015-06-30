# -*- coding: utf-8 -*-
class Edicao:
  def __init__(self,volume,numero,data,tema,editorChefe):
    self.volume = volume
    self.numero = numero
    self.data = data
    self.tema = tema
    self.editorChefe = editorChefe
    self.submetidos = []

  def submeterArtigo(self,artigo):
    self.submetidos.append(artigo)

  def buscaArtigo(self,codigo):
    for a in self.submetidos:
      if a.getCodigo() == codigo:
        return a
    return None

  def getTema(self):
    return self.tema

  def getNumero(self):
    return self.numero

  def getVolume(self):
    return self.volume

  def getData(self):
    meses = ["Janeiro","Fevereiro",u"Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
    v = self.data.split("/")
    mes = meses[int(v[1]) - 1]
    ano = v[2]

    return mes + " de " + ano
  
  def getEditorChefe(self):
    return self.editorChefe

  def getArtigos(self):
    return self.submetidos
