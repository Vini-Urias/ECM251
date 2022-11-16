# Fernando Henriques Neto
# RA:18.00931-0
from src.models.item.item import Item
from src.dao.item_dao import Item_DAO

class Item_Controller():
    def __init__(self) -> None:
        pass

    def coletar_todos_itens(self):
        return Item_DAO.get_instance().coletar_todos_itens_db()

    def coletar_todos_itens_nomes(self):
        return Item_DAO.get_instance().coletar_todos_itens_nomes_db()

    def coletar_item_nome(self, nome):
        return Item_DAO.get_instance().coletar_item_nome_db(nome)
    
    def coletar_item_plataforma(self, plataforma):
        return Item_DAO.get_instance().coletar_item_plataforma_db(plataforma)    
    
    def adicionar_item(self, item):
        Item_DAO.get_instance().adicionar_item_db(item)
        id_ = Item_DAO.get_instance().retornar_id_ultimo_item_tabela()
        item.set_id_imagem(id_)
        return self.atualizar_item(item)
    
    def atualizar_item(self, item):
        return Item_DAO.get_instance().atualizar_item_db(item)

    def apagar_item(self, id_):
        Item_DAO.get_instance().apagar_item_db(id_)

    def apagar_todos_itens(self):
        Item_DAO.get_instance().apagar_todos_itens_db()

