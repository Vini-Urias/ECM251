# Fernando Henriques Neto
# RA:18.00931-0
class Item():
    def __init__(self, nome, descricao, valor, plataforma, imagem='./assets/semfoto', id_=None):
        self._id = id_
        self._nome = nome
        self._descricao = descricao
        self._valor = valor
        self._plataforma = plataforma
        self._imagem = imagem

    def get_id(self):
        return self._id
    
    def get_valor(self):
        return self._valor

    def get_descricao(self):
        return self._descricao

    def get_nome(self):
        return self._nome
    
    def get_plataforma(self):
        return self._plataforma
    
    def get_imagem(self):
        return self._imagem
    
    def set_nome(self, nome):
        self._nome = nome

    def set_descricao(self, descricao):
        self._descricao = descricao

    def set_valor(self, valor):
        self._valor = valor

    def set_plataforma(self, plataforma):
        self._plataforma = plataforma

    def set_id_imagem(self, id_):
        self._id = id_
        self._imagem = f'./assets/item_{str(id_)}.jpg'

    def __str__(self) -> str:
        return f'Id: {self._id} Produto:{self._nome} Descrição:{self._descricao} Plataforma: {self._plataforma} Valor:{self._valor} Imagem:{self._imagem}'