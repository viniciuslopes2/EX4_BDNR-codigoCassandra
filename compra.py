import uuid
from decimal import Decimal
from mycassandra import session


def to_uuid(valor):
    try:
        return uuid.UUID(valor)
    except ValueError:
        print("ID inválido")
        return None


def buscar_usuario_por_nome(nome):
    for usuario in session.execute("SELECT * FROM usuario"):
        if usuario.nome == nome:
            return usuario
    print("Usuario nao encontrado")
    return None


def buscar_produto_por_nome(nome):
    produto = session.execute("SELECT * FROM produto WHERE nome = %s", (nome,)).one()
    if produto is None:
        print("Produto nao encontrado")
        return None
    return produto


def ler_itens():
    itens = []
    key = "S"
    while key == "S":
        nome_produto = input("Nome do produto: ")
        produto = buscar_produto_por_nome(nome_produto)
        if produto is None:
            continue

        quantidade = int(input("Quantidade: "))

        item = {
            "produto_id": str(produto.id),
            "quantidade": str(quantidade),
            "preco_unitario": str(produto.preco)
        }
        itens.append(item)
        key = input("Adicionar outro item (S/N)? ").upper()

    return itens


def calcular_total(itens):
    total = 0
    for item in itens:
        total += int(item["quantidade"]) * Decimal(item["preco_unitario"])
    return total


def create_compra():
    nome_usuario = input("Nome do usuário: ")
    usuario = buscar_usuario_por_nome(nome_usuario)
    if usuario is None:
        return

    itens = ler_itens()
    compra_id = uuid.uuid4()

    session.execute(
        "INSERT INTO compra (id, usuario_id, itens, valor_total) VALUES (%s, %s, %s, %s)",
        (compra_id, usuario.cpf, itens, calcular_total(itens))
    )
    print("Inserido:", compra_id)


def delete_compra(compra_id):
    compra_id = to_uuid(compra_id)
    if compra_id is None:
        return

    compra = session.execute("SELECT id FROM compra WHERE id = %s", (compra_id,)).one()
    if compra is None:
        print("Nao encontrado")
        return

    session.execute("DELETE FROM compra WHERE id = %s", (compra_id,))
    print("Deletado:", compra_id)