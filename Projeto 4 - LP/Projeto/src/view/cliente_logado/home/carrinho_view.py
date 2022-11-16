import streamlit as st
from models.util import Util

class Carrinho_View:
    # def __init__(self, usuario_controller, carrinho_de_compras) -> None:
    def __init__(self, app_controller) -> None:
        self.app_controller = app_controller
        self.numero_pdd_carrinho = self.app_controller.get_car_pdd()
        self.carrinho_cliente = app_controller.carrinho_cliente

        st.header("Confira tudo pra ver se não faltou nada! 😉")
        col1, col2, col3 = st.columns([1.8,1.5,0.8])
        with col1:
            st.header("Produto")
        with col2:
            st.header("Quantidade")
        with col3:
            st.header("Total")
        col1, col2, col3, col4, col5, col6 = st.columns([1.85,0.05,0.5,0.5,0.9,1])

        for i, pedido in enumerate(self.carrinho_cliente[self.numero_pdd_carrinho]):
            with col1:
                st.subheader(pedido["Item"].get_nome())

            with col3:
                st.write("")
                self.add_espaco(i)
                btt_adicionar = st.button(
                    label="-", 
                    key=("btt"+str(pedido)),
                    on_click= self.app_controller.remover_compra,
                    kwargs={"item": pedido["Item"]}
                    )
            
            with col4:
                if(i != 0):
                    st.write("")
                self.add_espaco(i)
                st.write("")
                qtde_carrinho = self.app_controller.pegar_qtd_item(pedido["Item"])
                st.text(qtde_carrinho)

            with col5:
                st.write("")
                self.add_espaco(i)
                btt_add_remover = st.button(
                    label="+", 
                    key=("btt"+str(pedido)+"2"),
                    on_click= self.app_controller.adicionar_compra,
                    kwargs={"item": pedido["Item"]}
                    )

            with col6:
                self.add_espaco(i)
                valor_total_produto = Util.converter_float_str_decimal_BR((pedido["Item"].get_valor())*pedido["Qtde"])
                st.subheader("R$ " + valor_total_produto)

        col1, col2 = st.columns([1,0.4])

        with col2:
            st.write("")
            str_valor_total = Util.converter_float_str_decimal_BR(self.app_controller.calcular_valor_total())
            st.header("Valor Total: R$ " + str_valor_total)
        
    def add_espaco(self, i):
        if(len(self.carrinho_cliente[self.numero_pdd_carrinho][i]["Item"].get_nome()) > 18):
            st.write("")
        elif (i != 0 and len(self.carrinho_cliente[self.numero_pdd_carrinho][i-1]["Item"].get_nome()) > 18):
            st.write("")
            st.write("")



