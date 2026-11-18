import hashlib
from mycassandra import session


def buscar_usuario_por_nome(nome):
    for usuario in session.execute("SELECT * FROM usuario"):
        if usuario.nome == nome:
            return usuario
    print("Usuario nao encontrado")
    return None


def create_usuario():
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    cpf = input("CPF: ")
    email = input("E-mail: ")
    senha = hashlib.sha256(input("Senha: ").encode()).hexdigest()

    enderecos = []
    key = "S"
    while key == "S":
        rua = input("Rua: ")
        num = input("Num: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        cep = input("CEP: ")
        endereco = {
            "rua": rua,
            "num": num,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "cep": cep
        }
        enderecos.append(endereco)
        key = input("Outro endereço (S/N)? ").upper()

    session.execute(
        "INSERT INTO usuario (cpf, nome, sobrenome, email, senha, enderecos) VALUES (%s, %s, %s, %s, %s, %s)",
        (cpf, nome, sobrenome, email, senha, enderecos)
    )
    print("Inserido:", cpf)


def update_usuario(nome):
    usuario = buscar_usuario_por_nome(nome)
    if usuario is None:
        return

    print(usuario)
    usuario = usuario._asdict()

    nome = input("Novo nome: ")
    if len(nome):
        usuario["nome"] = nome

    sobrenome = input("Novo sobrenome: ")
    if len(sobrenome):
        usuario["sobrenome"] = sobrenome

    email = input("Novo e-mail: ")
    if len(email):
        usuario["email"] = email

    session.execute(
        "UPDATE usuario SET nome = %s, sobrenome = %s, email = %s WHERE cpf = %s",
        (usuario["nome"], usuario["sobrenome"], usuario["email"], usuario["cpf"])
    )
    print("Alterado:", usuario["cpf"])