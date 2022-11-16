from src.dao.contato_dao import Contato_DAO

class Contato_Controller:
    def __init__(self) -> None:
        pass

    def buscar_todos_contacts(self):
        contatos_cadastrados = Contato_DAO.get_instance().coletar_todos_contatos()
        return contatos_cadastrados
