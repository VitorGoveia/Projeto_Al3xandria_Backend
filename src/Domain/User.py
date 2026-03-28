class UserDomain:
    def __init__(self, nome, email, senha, celular):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.celular = celular
        self.status = "Inativo"
    
    def to_dict(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "celular": self.celular,
            "status": self.status,
        }