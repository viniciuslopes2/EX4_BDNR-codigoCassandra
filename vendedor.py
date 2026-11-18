from mycassandra import session


def create_vendedor():
    nome = input("Nome: ")
    cpf_cnpj = input("CPF/CNPJ: ")
    email = input("E-mail: ")
    senha = input("Senha: ")

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
        "INSERT INTO vendedor (cpf_cnpj, nome, email, senha, enderecos) VALUES (%s, %s, %s, %s, %s)",
        (cpf_cnpj, nome, email, senha, enderecos)
    )
    print("Inserido:", cpf_cnpj)