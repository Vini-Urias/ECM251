# Fernando Henriques Neto
# RA:18.00931-0
from src.dao.pedido_dao import Pedido_DAO

class Pedido_Controller:
    def __init__(self) -> None:
        pass
    
    def buscar_todos_pedidos(self):
        return Pedido_DAO.get_instance().buscar_todos_pedidos_db()
    
    def buscar_pedidos_numero(self, numero_pedido):
        return Pedido_DAO.get_instance().buscar_pedidos_numero_db(numero_pedido)

    # def buscar_pedido_por_item(self, item):
    #     return Pedido_DAO.get_instance().buscar_pedidos_numero_db(item)
    
    def buscar_hist_pedido_user(self, email_usuario):
        return  Pedido_DAO.get_instance().buscar_pedidos_itens_finalizados_user_db(email_usuario)

    def buscar_pedidos_carrinho(self, email_usuario):
        return Pedido_DAO.get_instance().buscar_pedidos_carrinho_db(email_usuario)

    def adicionar_pedido(self, pedido):
        Pedido_DAO.get_instance().adicionar_pedido_db(pedido)
    
    def deletar_pedido_por_item(self, item_id):
        Pedido_DAO.get_instance().deletar_pedido_por_item_db(item_id)
    
    def atualizar_pedido(self, pedido):
        return Pedido_DAO.get_instance().atualizar_pedido_db(pedido)
        










