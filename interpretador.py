class Interpretador:
	def __init__(self, args):
	      self.args = args
	      self.entradas = []

	def retornaEntradas(self):	      
	      for i in range(0,5):
		      self.entradas.append("")
		      
	      for i in range(0,len(self.args)):
		      if self.args[i] == "-e":
			      self.entradas[0] = self.args[i+1]
		      if self.args[i] == "-t":
			     self. entradas[1] = self.args[i+1]
		      if self.args[i] == "-p":
			      self.entradas[2] = self.args[i+1]
		      if self.args[i] == "-a":
			      self.entradas[3] = self.args[i+1]
		      if self.args[i] == "-r":
			      self.entradas[4] = self.args[i+1]

	      return self.entradas
