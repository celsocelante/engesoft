class Edicao:
  def __init__(self,volume,numero,data,tema,editorChefe):
    self.volume = volume
    self.numero = numero
    #Tratar formato da data
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
    #retornar data formatada
    return None
  
  def getEditorChefe(self):
    return self.editorChefe

  def getArtigos(self):
    return self.submetidos
