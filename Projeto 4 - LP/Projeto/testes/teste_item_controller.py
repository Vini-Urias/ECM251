from src.controllers.produto_controller import Produto_Controller
from src.models.produtos.item import Item

controller = Produto_Controller()

item = Item(nome="Doom", descricao="MUITO LEGAL", valor=99.90, plataforma="PS4")
print(controller.adicionar_item(item))


print('##########################')
lista_itens = controller.coletar_todos_itens()
for i, item in enumerate(lista_itens):
    print(f'item {i}: {item}')