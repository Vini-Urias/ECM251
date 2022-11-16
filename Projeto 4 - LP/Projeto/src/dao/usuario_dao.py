import sqlite3
from src.models.usuario.usuario import Usuario
from src.models.contato.contato import Contato

class Usuario_DAO:
    _instance = None

    def __init__ (self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = Usuario_DAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db', check_same_thread=False)

    def buscar_todos_users_db(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Usuarios INNER JOIN Contatos ON Usuarios.contato_id = Contatos.id;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(self.formar_usuario_info_basico(resultado))
        self.cursor.close()
        return resultados
    
    def buscar_user_email_db(self, email):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Usuarios INNER JOIN Contatos ON Usuarios.contato_id = Contatos.id WHERE email='{email}';
        """)
        resultado = self.cursor.fetchone()
        user = (self.formar_usuario_info_basico(resultado)) if resultado != None else None 
        self.cursor.close()
        return user

    def adicionar_user_db(self, user, id_ctt):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
        INSERT INTO Usuarios(email, senha, contato_id)
        VALUES(
            '{user.get_email()}',
            '{user.get_senha()}',
            {id_ctt}
            );
        """)
        self.conn.commit()
        self.cursor.close()

    def atualizar_user_db(self, email_antigo, novo_user):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Usuarios SET
                email = '{novo_user.get_email()}',
                senha = '{novo_user.get_senha()}',
                contato_id = {novo_user.get_contato().get_id()}
                WHERE email ='{email_antigo}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def deletar_todos_users_db(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""DELETE FROM Usuarios;""")
        self.conn.commit()
        self.cursor.close()

        
    def formar_usuario_info_basico(self, user_data):
        ctt = Contato(id_=user_data[3], nome=user_data[4], sexo=user_data[5], telefone=user_data[6], data_nascimento=user_data[7])
        user = Usuario(email=user_data[0], senha=user_data[1], contato=ctt)
        return user





