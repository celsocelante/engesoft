class Colaborador:
    def __init__(self,nome,email,endereco,senha,codigo):
        self.nome = nome
        self.email = email
        self.edereco = endereco
        self.senha = senha
        self.codigo = codigo

    def getCodigo(self):
        return self.codigo

    def getNome(self):
        return self.nome
