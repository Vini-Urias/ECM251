import streamlit as st
from src.controllers.pedido_controller import Pedido_Controller
from src.controllers.usuario_controller import Usuario_Controller
from src.controllers.item_controller import Item_Controller
from src.controllers.pedido_controller import Pedido_Controller
from src.models.pedido.pedido import Pedido
from src.models.util import Util
import uuid

class App_Controller:
    _instance = None

    def __init__(self) -> None:
        self.usuario_controller   = Usuario_Controller()
        self.item_controller      = Item_Controller()
        self.pedido_controller    = Pedido_Controller()
        self.usuario_logado       = self.usuario_controller.buscar_user_email(st.session_state["Logado"])
        self.cliente_hist_pedidos = self.resgatar_hist_pedido_usuario()
        self.carrinho_cliente     = self.resgatar_carrinho_usuario()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = App_Controller()
        return cls._instance
    
    def resgatar_carrinho_usuario(self):
        carrinho_usuario = self.pedido_controller.buscar_pedidos_carrinho(self.usuario_logado.get_email())
        return self.montar_carrinho(carrinho_usuario) if len(carrinho_usuario) != 0 else self.criar_carrinho_vazio()

    def resgatar_hist_pedido_usuario(self):
        listas_pedidos_itens = self.pedido_controller.buscar_hist_pedido_user(self.usuario_logado.get_email())
        return self.montar_hist_pedidos(listas_pedidos_itens) if len(listas_pedidos_itens) != 0 else []

    def montar_hist_pedidos(self, listas_pedidos_itens):  # listas_pedidos_itens= [ [pedido1, item1], [pedido2, item2] ]
        list_hist_pedidos = []
        aux_dict_pedido = {}
        numero_pedido_anterior = None
        for pedido_item in listas_pedidos_itens:
            if(pedido_item[0].get_numero_pedido() != numero_pedido_anterior): # Se pdd_atual != pdd_anterior
                list_hist_pedidos.append(aux_dict_pedido)
                aux_dict_pedido = {pedido_item[0].get_numero_pedido():[self.montar_item_do_pedido(pedido_item)]} # {"001":[{"item1":valorItem, "qtd": valorQtd}]}
                numero_pedido_anterior = pedido_item[0].get_numero_pedido()                                           # Atualizando var de controle
            else:
                aux_dict_pedido[pedido_item[0].get_numero_pedido()].append(self.montar_item_do_pedido(pedido_item)) # Add um item ao mesmo pedido
        
        list_hist_pedidos.append(aux_dict_pedido) # Adiciona Ultimo Pedido
        list_hist_pedidos.remove({})              # Remove Primeira Inserção de Dict vazio (esperado)

        return list_hist_pedidos

    def montar_carrinho(self, listas_pedidos_carrinho_itens):
        carrinho = {listas_pedidos_carrinho_itens[0][0].get_numero_pedido():[]} # {"001":[]}
        for pedido_item in listas_pedidos_carrinho_itens:
            carrinho[pedido_item[0].get_numero_pedido()].append(self.montar_item_do_pedido(pedido_item)) # Add um item ao carrinho
        return carrinho

    def criar_carrinho_vazio(self):
        dict_carrinho = {str(uuid.uuid4()):[]} # {"001" : []}
        return dict_carrinho

    def montar_item_do_pedido(self, pedido_item):
        return {"Item":pedido_item[1], "Qtde": pedido_item[0].get_quantidade(), "DataHora": pedido_item[0].get_data_hora()}
    
    def get_car_pdd(self):
        return list(self.carrinho_cliente.keys())[0]
    
    def qtde_total_itens(self):
        qtd_total =0
        for pedido in self.carrinho_cliente[self.get_car_pdd()]:
            qtd_total += pedido["Qtde"] 
        return qtd_total

    def pegar_qtd_item(self, item):
        for pedido in self.carrinho_cliente[self.get_car_pdd()]:
            if pedido["Item"].get_nome() == item.get_nome():
                return pedido["Qtde"]
        return 0
    
    def calcular_valor_total(self):
        total = 0
        for pedido in self.carrinho_cliente[self.get_car_pdd()]:
            total += pedido["Item"].get_valor() * pedido["Qtde"]
        
        return total

    def adicionar_compra(self, item):
        qtde_atual = self.pegar_qtd_item(item)      
        if qtde_atual != 0:
            self.alterar_qtd_item_carrinho(item, (qtde_atual+1))
        else:
            self.adicionar_novo_item_carrinho(item, 1)
    
    def remover_compra(self, item):
        qtde_atual = self.pegar_qtd_item(item)      
        if qtde_atual != 1:
            self.alterar_qtd_item_carrinho(item, (qtde_atual-1))
        else:
            self.remover_item_carrinho(item)

    def remover_item_carrinho(self, item):
        self.pedido_controller.deletar_pedido_por_item(item.get_id())

    def adicionar_novo_item_carrinho(self, item, qtde):
        pedido = Pedido(id_item=item.get_id(), quantidade=qtde, numero_pedido=self.get_car_pdd(), email_usuario=self.usuario_logado.get_email(), status='Carrinho')
        self.pedido_controller.adicionar_pedido(pedido)
    
    def alterar_qtd_item_carrinho(self, item, qtde):
        pedido = Pedido(id_item=item.get_id(), quantidade=qtde, numero_pedido=self.get_car_pdd(), email_usuario=self.usuario_logado.get_email(), status='Carrinho')
        self.pedido_controller.atualizar_pedido(pedido)









