class Tema:
  def __init__(self,titulo,codigo):
    self.titulo = titulo
    self.codigo = codigo
    self.revisores = []

  def getTitulo(self):
    return self.titulo

  def vinculaRevisor(self,revisor):
    self.revisores.append(revisor)

  def getQuantidadeRevisores(self):
    return len(self.revisores)

  def contemRevisor(self,revisor):
    return revisor in self.revisores

    
