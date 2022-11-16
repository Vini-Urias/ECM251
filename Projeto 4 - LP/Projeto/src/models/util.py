# Fernando Henriques Neto
# RA:18.00931-0

import streamlit as st
import datetime as dt
from src.models.enum import Paginas
from PIL import Image as img
import os
import time
import uuid

class Util():
    @staticmethod
    def calcular_idade(data_nascimento):
        today = dt.date.today()
        idade = today.year - data_nascimento.year - ((today.month, today.day) < (data_nascimento.month, data_nascimento.day))
        return idade

    @staticmethod
    # Retorna True se campo diferete de vazio
    def validar_string(campo_str):
        return(campo_str != None and campo_str!="")

    @staticmethod
    # Retorna True se dicionario diferente de vazio
    def validar_dicionario(dict):
        return len(dict.keys()) != 0

    @staticmethod
    def validar_lista(lista):
        for valor in lista:
            if not(Util.validar_string(valor)):
                return False
        return True

    @staticmethod
    def limpar_tela():
        os.system('cls')

    @staticmethod
    def ajustar_imagem(path_imagem,x,y):
        imagem = img.open(path_imagem)
        return imagem.resize((x, y))

    @staticmethod
    def converter_float_str_decimal_BR(valor):
        result = str("{:.2f}".format(valor))
        return result.replace(".",",")

    @staticmethod
    def setar_ambiente_pagina_login():
        st.session_state["Logado"]      = None
        st.session_state["Caption"]     = None
        st.session_state["Sucesso"]     = None
        st.session_state["Pagina"]      = Paginas.LOGIN.name
    
    @staticmethod
    def setar_ambiente_pagina_cadastro():
        st.session_state["Logado"]      = None
        st.session_state["Caption"]     = None
        st.session_state["Sucesso"]     =  None
        st.session_state["Pagina"]      = Paginas.CADASTRO.name
    
    @staticmethod
    def escrever_mensagem():
        if(Util.validar_string(st.session_state["Caption"])):
            st.error(st.session_state["Caption"], icon="⚠️")
        elif(Util.validar_string(st.session_state["Sucesso"])):
            st.success(st.session_state["Sucesso"], icon="✅")

    @staticmethod
    def exibir_spinner(tempo, msg, msg_sucesso):
        with st.spinner(msg):
            time.sleep(tempo)
            st.success(msg_sucesso)
    
    @staticmethod
    # Retorna True se campo diferete de vazio
    def gerarUUID():
        return str(uuid.uuid4())


    

