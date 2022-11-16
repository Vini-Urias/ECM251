from src.controllers.contato_controller import Contato_Controller

controller = Contato_Controller()

lista_contatos = controller.buscar_todos_contacts()
for i, contato in enumerate(lista_contatos):
    print(f'Contato {i}: {contato}')