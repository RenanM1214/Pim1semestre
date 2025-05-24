import json
import re
import os
import uuid
import hashlib


CAMINHO_BD = "usuarios.json"

def carregar_banco_dados():
    if not os.path.exists(CAMINHO_BD):
        return {}
    try:
        with open(CAMINHO_BD, "r") as arquivo: #Apilidando arquivo
            return json.load(arquivo)
    except json.JSONDecodeError:
        return {}

def salvar_banco_dados(dados):
    with open(CAMINHO_BD, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def criar_senha():
    while True:
        print("\nA senha deve conter pelo menos:\n- 8 caracteres\n- 1 letra maiúscula\n- 1 caractere especial (!@#$%^&*)\n- 1 número")
        senha = input("Digite sua senha: ")
        if len(senha) < 8 or not re.search(r"\d", senha) or not re.search(r"[A-Z]", senha) or not re.search(r"[!@#$%^&*().]", senha):
            print("Senha inválida. Tente novamente!\n")
            continue
        return senha

def criar_conta():
    banco = carregar_banco_dados()

    nome = input("Digite seu nome completo: ").strip()
    idade = input("Digite sua idade: ").strip()
    email = input("Digite seu e-mail: ").strip()

    senha = criar_senha()
    login_id = str(uuid.uuid4())[:8]  # ID truncado

    banco[login_id] = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "senha": gerar_hash(senha)
    }

    salvar_banco_dados(banco)
    print(f"\nConta criada com sucesso! Seu ID de acesso é: {login_id}")
    print("Guarde esse ID, ele será necessário para login.\n")


def fazer_login():
    from main import principal
    banco = carregar_banco_dados()
    login_input = input("Digite seu ID de acesso: ").strip()
    senha_input = input("Digite sua senha: ")

    if login_input in banco and gerar_hash(senha_input) == banco[login_input]["senha"]:
        print("\n Login bem-sucedido!\n")
        return principal()
    else:
        print("\n Login inválido.\n")

