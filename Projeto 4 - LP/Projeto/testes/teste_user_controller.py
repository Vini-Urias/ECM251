from src.controllers.usuario_controller import Usuario_Controller
from src.models.usuario.usuario import Usuario
from src.models.contato.contato import Contato

controller = Usuario_Controller()

lista_usuarios = controller.buscar_todos_users()
for i, usuario in enumerate(lista_usuarios):
    print(f'Usuario {i}: {usuario}')
