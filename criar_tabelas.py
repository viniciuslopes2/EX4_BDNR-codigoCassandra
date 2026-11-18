from mycassandra import session, cluster

session.execute("""
    CREATE TABLE IF NOT EXISTS usuario (
        cpf text PRIMARY KEY,
        nome text,
        sobrenome text,
        email text,
        senha text,
        enderecos list<frozen<map<text, text>>>
    )
""")

session.execute("""
    CREATE TABLE IF NOT EXISTS vendedor (
        cpf_cnpj text PRIMARY KEY,
        nome text,
        email text,
        senha text,
        enderecos list<frozen<map<text, text>>>
    )
""")

session.execute("""
    CREATE TABLE IF NOT EXISTS produto (
        nome text PRIMARY KEY,
        id uuid,
        descricao text,
        preco decimal,
        quantidade int,
        vendedor_id text
    )
""")

session.execute("""
    CREATE TABLE IF NOT EXISTS compra (
        id uuid PRIMARY KEY,
        usuario_id text,
        itens list<frozen<map<text, text>>>,
        valor_total decimal
    )
""")

print("Tabelas criadas")

cluster.shutdown()