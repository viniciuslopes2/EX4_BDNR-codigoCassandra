import usuario
import vendedor
import produto
import compra
from mycassandra import cluster


def menu_usuario():
    sub = 0
    while sub != 'V':
        print("1-Inserir usuário")
        print("2-Atualizar usuário")
        sub = input("Operacao (V para voltar): ")

        if sub == '1':
            usuario.create_usuario()

        elif sub == '2':
            nome = input("Nome: ")
            usuario.update_usuario(nome)


def menu_vendedor():
    sub = 0
    while sub != 'V':
        print("1-Inserir vendedor")
        sub = input("Operacao (V para voltar): ")

        if sub == '1':
            vendedor.create_vendedor()


def menu_produto():
    sub = 0
    while sub != 'V':
        print("1-Inserir produto")
        print("2-Procurar produto")
        sub = input("Operacao (V para voltar): ")

        if sub == '1':
            produto.create_produto()

        elif sub == '2':
            produto.read_produto()


def menu_compra():
    sub = 0
    while sub != 'V':
        print("1-Inserir compra")
        print("2-Apagar compra")
        sub = input("Operacao (V para voltar): ")

        if sub == '1':
            compra.create_compra()

        elif sub == '2':
            id = input("ID: ")
            compra.delete_compra(id)


key = 0
while key != 'S':
    print("\n1-Usuario")
    print("2-Vendedor")
    print("3-Produto")
    print("4-Compra")
    print("S-Sair")
    key = input("Acessar tabela: ")

    if key == '1':
        menu_usuario()

    elif key == '2':
        menu_vendedor()

    elif key == '3':
        menu_produto()

    elif key == '4':
        menu_compra()

cluster.shutdown()
print("Tchau Prof...")