import sqlite3
from src.models.usuario.usuario import Usuario
from src.models.contato.contato import Contato

class Contato_DAO:
    _instance = None

    def __init__ (self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = Contato_DAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db', check_same_thread=False)

    def coletar_todos_contatos(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Contatos;
        """)
        resultados=[]
        for resultado in self.cursor.fetchall():
            resultados.append(Contato(id_=resultado[0], nome=resultado[1], sexo=resultado[2], telefone=resultado[3], data_nascimento=resultado[4]))
        self.cursor.close()
        return resultados

    def adicionar_contato(self, user):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            INSERT INTO Contatos(nome, sexo, telefone, data_nascimento)
            VALUES(
            '{user.get_contato().get_nome()}',
            '{user.get_contato().get_sexo()}',
            '{user.get_contato().get_telefone()}',
            '{user.get_contato().get_data_nascimento()}'
            );
        """)
        self.cursor.execute(f""" SELECT * FROM Contatos ORDER BY id DESC LIMIT 1;""")
        id_ = self.cursor.fetchone()[0]
        self.conn.commit()
        self.cursor.close()
        return id_

    def atualizar_contato(self, user):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            UPDATE Contatos SET
            id = {user.get_contato().get_id()},
            nome = '{user.get_contato().get_nome()}',
            sexo = '{user.get_contato().get_sexo()}',
            telefone = '{user.get_contato().get_telefone()}',
            data_nascimento = '{user.get_contato().get_data_nascimento()}'
            WHERE id = '{user.get_contato().get_id()}'
        """)
        self.conn.commit()
        self.cursor.close()
    
    def apagar_todos_contatos(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""DELETE FROM Contatos;""")
        self.conn.commit()
        self.cursor.close()






