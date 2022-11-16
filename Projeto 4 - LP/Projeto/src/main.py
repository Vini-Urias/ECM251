# Fernando Henriques Neto
# RA:18.00931-0

import streamlit as st
from controllers.usuario_controller import Usuario_Controller
from controllers.app_controller import App_Controller
from view.cliente_deslogado.login_view import Login_View
from view.cliente_deslogado.cadastro_view import Cadastro_View
from view.cliente_logado.home.home_main_view import Home_Main_View
from models.util import Util
from models.enum import Paginas

# --------------------- COMEÇO ---------------------
if __name__ == "__main__":

# --------------------- SETANDO/COLETANDO INFORMAÇÕES ---------------------
    if not(Util.validar_dicionario(st.session_state)):
        Util.setar_ambiente_pagina_login()
    # else:
    #     usuario_controller = st.session_state["Usuario_Controller"]
    #     produto_controller = st.session_state["Produto_Controller"]

# --------------------- LOGIN---------------------
    if st.session_state["Pagina"] == Paginas.LOGIN.name:
        pagina_atual = Login_View(Usuario_Controller())

# --------------------- CADASTRO---------------------
    elif st.session_state["Pagina"] == Paginas.CADASTRO.name:
        pagina_atual = Cadastro_View(Usuario_Controller())

# --------------------- HOME--------------------
    elif st.session_state["Pagina"] == Paginas.HOME.name:
        pagina_atual = Home_Main_View(App_Controller())
        
# # --------------------- SALVAR CONTROLLER ---------------------
#     st.session_state["Usuario_Controller"] = usuario_controller
#     st.session_state["Produto_Controller"] = produto_controller

# --------------------- FIM ---------------------


