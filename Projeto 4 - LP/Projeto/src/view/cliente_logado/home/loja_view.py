import streamlit as st
from models.util import Util

class Loja_View:
    def __init__(self, app_controller) -> None:
        self.app_controller     = app_controller
        self.usuario_controller = self.app_controller.usuario_controller
        self.item_controller    = self.app_controller.item_controller
        self.pedido_controller  = self.app_controller.pedido_controller

        st.title("A sua Loja favorita de Ga🎮es!")
        self.lista_itens = self.item_controller.coletar_todos_itens()
        self.lista_nomes_itens = self.item_controller.coletar_todos_itens_nomes()

        self.lista_nomes_itens.insert(0, "Visualizar Todos")
        self.opcao_busca = st.selectbox(
                    label="Pesquise aqui seu jogo!", 
                    options=self.lista_nomes_itens, 
                    index=0
                    )

        self.exibir_itens_colunas()

    def exibir_itens_colunas(self):
        if self.opcao_busca != "Visualizar Todos":
            lista_itens_busca = self.item_controller.coletar_item_nome(self.opcao_busca)
            if len(lista_itens_busca)==1:
                self.item_1_coluna(lista_itens_busca, 250, 300)
            elif len(lista_itens_busca)==2:
                self.item_2_coluna(lista_itens_busca, 250, 300)
            else:
                self.item_3_colunas(lista_itens_busca, 200, 250)
        else:
            self.item_3_colunas(self.lista_itens, 220, 270)

    def item_1_coluna(self, lista_itens, largura_imagem, altura_imagem):
        col1, col2, col3 = st.columns(3)
        with col2:
            self.exibir_item(lista_itens[0], largura_imagem, altura_imagem)
    
    def item_2_coluna(self, lista_itens, largura_imagem, altura_imagem):
        col1, col2, col3 = st.columns([1,0.6,1])
        with col1:
            self.exibir_item(lista_itens[0], largura_imagem, altura_imagem)
        
        with col3:
            self.exibir_item(lista_itens[1], largura_imagem, altura_imagem)

    def item_3_colunas(self, lista_itens, largura_imagem, altura_imagem):
        col1, col2, col3 = st.columns(3)
        list_coluna1=range(1,len(lista_itens)-1,3)
        list_coluna2=range(2,len(lista_itens),3)

        for i, item in enumerate(lista_itens):
            if(i in list_coluna1):
                with col1:
                    self.exibir_item(item, largura_imagem, altura_imagem)
            elif(i in list_coluna2):
                with col2:
                    self.exibir_item(item, largura_imagem, altura_imagem)
            else:
                with col3:
                    self.exibir_item(item, largura_imagem, altura_imagem)
        
    def exibir_item(self, item, x, y):
        nome_item = st.subheader(item.get_nome())
        st.image(Util.ajustar_imagem(item.get_imagem(), x, y))
        st.info("R$ " + Util.converter_float_str_decimal_BR(item.get_valor()),icon="💵")

        btt_add_car = st.button(
                label="Adicionar ao carrinho", 
                key=("btt"+str(nome_item)),
                on_click= self.app_controller.adicionar_compra,
                kwargs={"item": item}
                )

        if(btt_add_car):
            # st.balloons()
            st.caption("Adicionado com Sucesso!")

