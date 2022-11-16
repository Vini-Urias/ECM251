# from src.models.carrinho.carrinho import Carrinho

class Usuario():
    def __init__(self, email, senha, contato, carrinho_de_compras=[], pedidos=[]):
        self._email = email
        self._senha = senha
        self._contato = contato
    
    def get_contato(self):
        return self._contato
    
    def get_email(self):
        return self._email
        
    def get_senha(self):
        return self._senha
    
    def set_email(self, email):
        self._email = email

    def set_senha(self, senha):
        self._senha = senha

    def set_contato(self, contato):
        self._contato = contato
    
    def __str__(self) -> str:
        return f'Email:{self._email} Senha:{self._senha} Contato: {self._contato}'



    
    
    
