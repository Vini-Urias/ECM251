import streamlit as st
from models.enum import Paginas
from models.util import Util

class Login_View:
    def __init__(self, controller) -> None:
        self.controller = controller

        st.title("Bem vindo ao W🌎rld Games! 🚀")
        st.header("Login")

        self.login_email = st.text_input(label="E-mail", placeholder ="Digite seu E-mail", value="")
        self.login_senha = st.text_input(label="Senha", placeholder ="Digite sua Senha", type='password', value="")

        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 3.35, 1.1])
        with col1:
            self.btt_fazer_login = st.button(
                label="Entrar", 
                on_click=self.autenticar_login
                )
        with col4:
            self.msg_cadastro = st.write("Novo por aqui? Faça agora seu Cadastro👉")
        with col5:
            self.btt_fazer_cadastro = st.button(
                label="Cadastro",
                on_click=Util.setar_ambiente_pagina_cadastro
                )

        Util.escrever_mensagem()
    
    def autenticar_login(self):
        if not(Util.validar_string(self.login_email) and Util.validar_string(self.login_senha)):
            st.session_state["Caption"] = "Preencher todos os campos!"
        else:
            usuario = self.controller.buscar_user_email(self.login_email)
            if (usuario != None and usuario.get_senha() == self.login_senha):
                st.session_state["Logado"] = usuario.get_email()
                st.session_state["Pagina"] = Paginas.HOME.name
                st.session_state["Alterar Dados"] = True
            else:
                st.session_state["Caption"] = "Dados de Login Incorretos!"
   