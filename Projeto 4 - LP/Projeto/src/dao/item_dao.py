import sqlite3
from src.models.item.item import Item

class Item_DAO:
    _instance = None

    def __init__ (self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = Item_DAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db', check_same_thread=False)

    def coletar_todos_itens_db(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f""" SELECT * FROM Itens ORDER BY nome ASC; """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(self.formar_item(resultado))
        self.cursor.close()
        return resultados
    
    def coletar_item_nome_db(self, nome):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Itens 
            WHERE nome LIKE '{nome}%';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(self.formar_item(resultado))
        self.cursor.close()
        return resultados
    
    def coletar_item_id_db(self, id_):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Itens 
            WHERE id = {id_};
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(self.formar_item(resultado))
        self.cursor.close()
        return resultados
    
    def coletar_todos_itens_nomes_db(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f""" SELECT nome FROM Itens ORDER BY nome ASC; """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(resultado[0])
        self.cursor.close()
        return resultados
    
    def coletar_item_plataforma_db(self, plataforma):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Itens 
            WHERE plataforma = '{plataforma}';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(self.formar_item(resultado))
        self.cursor.close()
        return resultados

    def adicionar_item_db(self, item):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""      
        INSERT INTO Itens(nome, descricao, valor, plataforma, imagem)
        VALUES(
            '{item.get_nome()}',
            '{item.get_descricao()}',
            '{item.get_valor()}',
            '{item.get_plataforma()}',
            '{item.get_imagem()}'
        );
        """)
        self.conn.commit()
        self.cursor.close()

    def atualizar_item_db(self, item):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Itens SET
                id          =  {item.get_id()},
                nome        = '{item.get_nome()}',
                descricao   = '{item.get_descricao()}',
                valor       = {item.get_valor()},
                plataforma  = '{item.get_plataforma()}',
                imagem      = '{item.get_imagem()}'
                WHERE id    = {item.get_id()}
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def apagar_item_db(self, id_):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            DELETE FROM Itens
            WHERE id = '{id_}'
            """)
        self.conn.commit()
        self.cursor.close()
    
    def apagar_todos_itens_db(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""DELETE FROM Itens;""")
        self.conn.commit()
        self.cursor.close()
    
    def retornar_id_ultimo_item_tabela(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f""" SELECT id FROM Itens ORDER BY id DESC LIMIT 1;""")
        id_ = self.cursor.fetchone()[0]
        self.conn.commit()
        return id_

    def formar_item(self, item_data):
        return Item(id_=item_data[0], nome=item_data[1], descricao=item_data[2], valor=item_data[3], plataforma=item_data[4], imagem=item_data[5])






