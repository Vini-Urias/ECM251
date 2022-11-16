import streamlit as st
from models.contato.contato import Contato
from models.usuario.usuario import Usuario
from models.util import Util
import datetime as dt

class Contato_Info_View:
    def __init__(self, controller) -> None:
        self.usuario_logado = controller.usuario_logado
        self.controller = controller
        self.usuario_controller = controller.usuario_controller
        self.habilitar_alteracao = st.session_state["Alterar Dados"]
        
        st.title("Todos seus Dados em um só Lugar ! 👀")
        self.exibir_btt_alterar_dados()

        dt_nascimento_ano, dt_nascimento_mes, dt_nascimento_dia  = str(self.usuario_logado.get_contato().get_data_nascimento()).split("-", 2)
        data_min = dt.date(1900, 1, 1)
        data_max = dt.date.today()
        dt_nascimento = dt.date(int(dt_nascimento_ano), int(dt_nascimento_mes), int(dt_nascimento_dia))

        self.nome_contato = st.text_input(label="Nome", placeholder ="Digite seu Nome Completo",  value=self.usuario_logado.get_contato().get_nome(), disabled=self.habilitar_alteracao)
        
        col1, col2 = st.columns(2)
        with col1:
            self.email_usuario = st.text_input(label="E-mail", placeholder ="Digite seu endereço de E-mail", value=self.usuario_logado.get_email(), disabled=self.habilitar_alteracao)
            self.telefone_contato = st.text_input(label="Telefone", placeholder ="Digite seu Telefone",  value=self.usuario_logado.get_contato().get_telefone(), disabled=self.habilitar_alteracao)
        with col2:
            self.genero = st.selectbox('Gênero', ('Masculino', 'Feminino', 'Nenhum'), ('Masculino', 'Feminino', 'Nenhum').index(self.usuario_logado.get_contato().get_sexo()))
            self.dt_nascimento_contato = st.date_input(label="Data de Nascimento", min_value=data_min, max_value=data_max, disabled=self.habilitar_alteracao, value=dt_nascimento)
        
        self.senha_usuario = st.text_input(label="Senha", placeholder ="Digite uma senha", value=self.usuario_logado.get_senha(),  type='password', disabled=self.habilitar_alteracao)
        self.senha_usuario_check = st.text_input(label="Confirmação de Senha", placeholder ="Digite novamente sua senha", value=self.usuario_logado.get_senha(), type='password', disabled=self.habilitar_alteracao)

        self.lista_campos_alteracao = [self.nome_contato, self.genero, self.email_usuario, self.telefone_contato, self.dt_nascimento_contato, self.senha_usuario,self.senha_usuario_check]

        col1, col2 = st.columns([8, 1])

        with col1:
            self.btt_confirmar_cadastro = st.button(
                label="Confirmar Alterações", 
                    on_click=self.autenticar_alteracao,
                    disabled = self.habilitar_alteracao
            )

            Util.escrever_mensagem()
    
    def autenticar_alteracao(self):
        if not self.checar_lista_cadastro():
                st.session_state["Caption"] = "Preencher todos os campos!"
        elif self.senha_usuario != self.senha_usuario_check:
                st.session_state["Caption"] = "As senhas não conferem!"
        else:
            novo_usuario_email = self.controller.usuario_controller.buscar_user_email(self.email_usuario)
            print("novo_usuario_email:", novo_usuario_email)
            if(novo_usuario_email != None and novo_usuario_email.get_email() != self.usuario_logado.get_email()):
                st.session_state["Caption"] = "Email já utilizado por outro Usuário!"
            else:
                contato_user = Contato(id_=self.usuario_logado.get_contato().get_id(), nome=self.nome_contato, sexo=self.genero, telefone=self.telefone_contato, data_nascimento=self.dt_nascimento_contato)
                usuario_novo = Usuario(email=self.email_usuario, senha=self.senha_usuario, contato=contato_user)
                self.usuario_controller.atualizar_user(self.usuario_logado.get_email(), usuario_novo)
                st.session_state["Caption"] =  None
                st.session_state["Sucesso"] = "Dados Alterados com Sucesso"
                self.alterar_permissao_habilitar()
                st.session_state["Logado"] = usuario_novo.get_email()


        
    def checar_lista_cadastro(self):
        for campo in self.lista_campos_alteracao:
            if not Util.validar_string(campo):
                return False
        return True
    
    def exibir_btt_alterar_dados(self):
        if(st.session_state["Alterar Dados"]): 
            self.btt_habilitar_alteracao = st.button(
                label="Quero Alterar Meus Dados 🟢", 
                on_click=self.alterar_permissao_habilitar
            )
        else:
            self.btt_habilitar_alteracao = st.button(
                label="Não Quero Alterar Meus Dados 🔴", 
                on_click=self.alterar_permissao_habilitar
            )
    
    def alterar_permissao_habilitar(self):
        if(st.session_state["Alterar Dados"]): 
            st.session_state["Alterar Dados"] = False
        else:
            st.session_state["Alterar Dados"] = True

    
    def dados_alteracao_usuario(self):
        data_min = dt.date(1900, 1, 1)
        data_max = dt.date.today() 

        self.nome_contato = st.text_input(label="Nome", placeholder ="Digite seu Nome Completo",  value=self.usuario_logado.get_contato().get_nome(), disabled=self.habilitar_alteracao)
        
        col1, col2 = st.columns(2)
        with col1:
            self.email_usuario = st.text_input(label="E-mail", placeholder ="Digite seu endereço de E-mail", value=self.usuario_logado.get_email(), disabled=self.habilitar_alteracao)
            self.telefone_contato = st.text_input(label="Telefone", placeholder ="Digite seu Telefone",  value=self.usuario_logado.get_contato().get_telefone(), disabled=self.habilitar_alteracao)
        with col2:
            self.genero = st.selectbox('Gênero', ('Masculino', 'Feminino', 'Nenhum'), ('Masculino', 'Feminino', 'Nenhum').index(self.usuario_logado.get_contato().get_sexo()))
            self.dt_nascimento_contato = st.date_input(label="Data de Nascimento", min_value=data_min, max_value=data_max, disabled=self.habilitar_alteracao, value=data_min)
        
        self.senha_usuario = st.text_input(label="Senha", placeholder ="Digite uma senha", value=self.usuario_logado.get_senha(),  type='password', disabled=self.habilitar_alteracao)
        self.senha_usuario_check = st.text_input(label="Confirmação de Senha", placeholder ="Digite novamente sua senha", value=self.usuario_logado.get_senha(), type='password', disabled=self.habilitar_alteracao)

        return [self.nome_contato, self.genero, self.email_usuario, self.telefone_contato, self.dt_nascimento_contato, self.senha_usuario,self.senha_usuario_check]





