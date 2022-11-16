import sqlite3
from src.models.pedido.pedido import Pedido
from src.models.item.item import Item

class Pedido_DAO:
    _instance = None

    def __init__ (self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = Pedido_DAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db', check_same_thread=False)
    
    def buscar_todos_pedidos_db(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Pedidos;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(self.formar_pedido(resultado))
        self.cursor.close()
        return resultados

    def buscar_pedidos_numero_db(self, numero_pedido):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Pedidos WHERE numero_pedido = '{numero_pedido}';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append
        self.cursor.close()
        return resultados
    
    def buscar_pedidos_itens_finalizados_user_db(self, email_usuario):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Pedidos INNER JOIN Itens ON Pedidos.id_item = Itens.id WHERE email_usuario = '{email_usuario}' AND status = 'Finalizado' ORDER BY data_hora ASC, id ASC;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(self.formar_pedido_item(resultado))
        self.cursor.close()
        return resultados
    
    def buscar_pedidos_carrinho_db(self, email_usuario):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
             SELECT * FROM Pedidos INNER JOIN Itens ON Pedidos.id_item = Itens.id WHERE email_usuario = '{email_usuario}' AND status = 'Carrinho' ORDER BY id ASC;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(self.formar_pedido_item(resultado))
        self.cursor.close()
        return resultados
    
    def deletar_pedido_por_item_db(self, id_item):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
                DELETE FROM Pedidos WHERE id_item = {id_item} AND status = 'Carrinho' ;
        """)
        self.conn.commit()
        self.cursor.close()
    
    def adicionar_pedido_db(self, pedido):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
        INSERT INTO Pedidos(id_item, email_usuario, quantidade, numero_pedido, status, data_hora)
        VALUES(
                {pedido.get_id_item()},
                "{pedido.get_email_usuario()}",
                {pedido.get_quantidade()},
                "{pedido.get_numero_pedido()}",
                "{pedido.get_status()}",
                "{pedido.get_data_hora()}"
                );
        """)
        self.conn.commit()
        self.cursor.close()

    def atualizar_pedido_db(self, pedido):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Pedidos SET
                id_item = {pedido.get_id_item()},
                email_usuario = '{pedido.get_email_usuario()}',
                quantidade = {pedido.get_quantidade()},
                numero_pedido = '{pedido.get_numero_pedido()}',
                status = '{pedido.get_status()}',
                data_hora = '{pedido.get_data_hora()}'
                WHERE id_item = {pedido.get_id_item()}
                AND numero_pedido = '{pedido.get_numero_pedido()}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True          
    
    def formar_pedido(self, pedido_data):
        pdd = Pedido(id_=pedido_data[0], id_item=pedido_data[1], email_usuario=pedido_data[2], quantidade=pedido_data[3], numero_pedido=pedido_data[4], status=pedido_data[5], data_hora=pedido_data[6])
        return pdd
    
    def formar_pedido_item(self, pedido_item_data):
        pdd = Pedido(id_=pedido_item_data[0], id_item=pedido_item_data[1], email_usuario=pedido_item_data[2], quantidade=pedido_item_data[3], numero_pedido=pedido_item_data[4], status=pedido_item_data[5], data_hora=pedido_item_data[6])
        item = Item(id_=pedido_item_data[7], nome=pedido_item_data[8], descricao=pedido_item_data[9], valor=pedido_item_data[10], plataforma=pedido_item_data[11], imagem=pedido_item_data[12])
        return [pdd, item]



