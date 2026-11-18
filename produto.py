import uuid
from decimal import Decimal
from mycassandra import session


def buscar_vendedor_por_nome(nome):
    for vendedor in session.execute("SELECT * FROM vendedor"):
        if vendedor.nome == nome:
            return vendedor
    print("Vendedor nao encontrado")
    return None


def create_produto():
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    preco = Decimal(input("Preço: "))
    quantidade = int(input("Quantidade: "))

    nome_vendedor = input("Nome do vendedor: ")
    vendedor = buscar_vendedor_por_nome(nome_vendedor)
    if vendedor is None:
        return

    produto_id = uuid.uuid4()

    session.execute(
        "INSERT INTO produto (nome, id, descricao, preco, quantidade, vendedor_id) VALUES (%s, %s, %s, %s, %s, %s)",
        (nome, produto_id, descricao, preco, quantidade, vendedor.cpf_cnpj)
    )
    print("Inserido:", produto_id)


def read_produto(nome=""):
    nome = nome or input("Nome (vazio para todos): ")
    if len(nome):
        docs = session.execute("SELECT * FROM produto WHERE nome = %s", (nome,))
    else:
        docs = sorted(session.execute("SELECT * FROM produto"), key=lambda p: p.nome)
    for d in docs:
        print(d)