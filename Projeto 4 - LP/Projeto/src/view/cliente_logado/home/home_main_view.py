import streamlit as st
from models.util import Util
from view.cliente_logado.home.loja_view import Loja_View
from view.cliente_logado.home.carrinho_view import Carrinho_View
from view.cliente_logado.info_cliente.contato_info_view import Contato_Info_View
from view.cliente_logado.info_cliente.contato_info_view import Contato_Info_View

class Home_Main_View:
    def __init__(self, app_controller) -> None:

        side_bar_option = st.sidebar.radio("Navegação",["Home", "Meus Dados", "Histórico de Pedidos", "Manipular Itens Loja"])
        st.sidebar.button(label="Sair", on_click=Util.setar_ambiente_pagina_login)

        if side_bar_option == "Home":
            qtde_total_itens = app_controller.qtde_total_itens()
            loja, carrinho, pagamento = st.tabs(["Loja", f"Carrinho ({qtde_total_itens}) 🛒" ,"Pagamento"])

            with loja:
                self.pagina_loja = Loja_View(app_controller)

            with carrinho:
                if (qtde_total_itens != 0):
                    self.pagina_carrinho = Carrinho_View(app_controller)
                else:
                    self.pagina_carrinho = None
                    self.exibr_carrinho_vazio()

            with pagamento:
                st.write("TESTE PAGAMENTO")

        
        elif side_bar_option == "Meus Dados":
            self.pagina_cadastro = Contato_Info_View(app_controller)

        elif side_bar_option == "Histórico de Pedidos":
            st.write("Em andamanento...")

        elif side_bar_option == "Manipular Itens Loja":
            st.write("Em andamanento...")

    
    def exibr_carrinho_vazio(self):
            st.header("Putz! Parece que seu carrinho está vazio! 😢")

                
