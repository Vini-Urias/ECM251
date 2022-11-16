# Fernando Henriques Neto
# RA:18.00931-0
# from src.models.util import Util

class Contato():
    def __init__(self, nome, sexo, telefone, data_nascimento, id_=None): #str(uuid.uuid4())
        self._id = id_
        self._nome = nome
        self._sexo = sexo
        self._telefone = telefone
        self._data_nascimento = data_nascimento

    def __str__(self) -> str:
        return f' Id: {self._id} Nome :{self._nome} Sexo :{self._sexo} Telefone:{self._telefone} Data Nascimento:{self._data_nascimento}'

    def validar_contato(self):
        return (self._nome != '' and self._sexo != ''  and self._telefone != '' and self._data_nascimento != '')
    
    def get_id(self):
        return self._id
    
    def get_nome(self):
        return self._nome
    
    def get_sexo(self):
        return self._sexo

    def get_telefone(self):
        return self._telefone
        
    def get_data_nascimento(self):
        return self._data_nascimento

    def get_id(self):
        return self._id
     
    def set_id(self, id):
        self._id = id

    def pegar_primeiro_nome(self):
        return self._nome.split()[0]
    



