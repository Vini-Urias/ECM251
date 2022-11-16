# Fernando Henriques Neto
# RA:18.00931-0
# import streamlit as st
# from src.models.contato.contato import Contato 
# from src.models.usuario.usuario import Usuario

from src.dao.usuario_dao import Usuario_DAO
from src.dao.contato_dao import Contato_DAO

class Usuario_Controller:
    def __init__(self) -> None:
        pass

    def buscar_user_email(self, email_usuario):
        user = Usuario_DAO.get_instance().buscar_user_email_db(email_usuario)
        return user
    
    def buscar_todos_users(self):
        usuarios_cadastrados = Usuario_DAO.get_instance().buscar_todos_users_db()
        return usuarios_cadastrados
    
    def adicionar_user(self, usuario):
        id_ctt = Contato_DAO().adicionar_contato(usuario)
        Usuario_DAO.get_instance().adicionar_user_db(usuario, id_ctt)
    
    def atualizar_user(self, email_antigo, novo_user):
        Contato_DAO().atualizar_contato(novo_user)
        return Usuario_DAO.get_instance().atualizar_user_db(email_antigo, novo_user)
    
    def deletar_todos_users(self):
        Contato_DAO().apagar_todos_contatos()
        Usuario_DAO.get_instance().deletar_todos_users_db()

    
    # def adicionar_usuario(self, novo_usuario):
    #     self._lista_usuarios_cadastrados.append(novo_usuario)

    # def reinserir_usuario(self, posicao, novo_usuario):
    #     self._lista_usuarios_cadastrados.insert(posicao, novo_usuario)
    
    # def remover_usuario(self, usuario):
    #     posicao_user = self._lista_usuarios_cadastrados.index(usuario)
    #     self._lista_usuarios_cadastrados.remove(usuario)
    #     return posicao_user
    
    # def update_usuario_compra(self, produto):
    #     lista_info_usuario = self.buscar_usuario_email(st.session_state["Logado"])
    #     self._lista_usuarios_cadastrados.remove(lista_info_usuario[0])
    #     lista_info_usuario[0].adicionar_compra_carrinho(produto)
    #     self._lista_usuarios_cadastrados.insert(lista_info_usuario[1], lista_info_usuario[0])
    
    # def update_usuario_venda(self, produto):
    #     lista_info_usuario = self.buscar_usuario_email(st.session_state["Logado"])
    #     self._lista_usuarios_cadastrados.remove(lista_info_usuario[0])
    #     lista_info_usuario[0].remover_compra_carrinho(produto)
    #     self._lista_usuarios_cadastrados.insert(lista_info_usuario[1], lista_info_usuario[0])
    
                
