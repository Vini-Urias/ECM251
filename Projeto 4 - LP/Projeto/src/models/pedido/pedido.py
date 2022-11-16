# Fernando Henriques Neto
# RA:18.00931-0
class Pedido:
    def __init__(self, id_item, quantidade, numero_pedido, email_usuario, status, data_hora=None, id_=None) -> None:
        self._id            = id_
        self._id_item       = id_item
        self._email_usuario = email_usuario
        self._quantidade    = quantidade
        self._numero_pedido = numero_pedido
        self._status        = status
        self._data_hora     = data_hora

    def __str__(self) -> str:
        return f'Pedido: id: {self._id} - Item: {self._id_item} - Quantidade: {self._quantidade} - Numero do Pedido: {self._numero_pedido} - Cliente: {self._email_usuario} - Status: {self._status} - Data e Hora: {self._data_hora}'

    def get_id(self):
        return self._id

    def get_id_item(self):
        return self._id_item

    def get_email_usuario(self):
        return self._email_usuario

    def get_quantidade(self):
        return self._quantidade

    def get_numero_pedido(self):
        return self._numero_pedido
    
    def get_status(self):
        return self._status

    def get_data_hora(self):
        return self._data_hora