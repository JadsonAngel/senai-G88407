usuarios = {
    
}


def cadastrar_user():
    usuario = str(input("Crie um Usuário para login: "))
    if usuario in usuarios:
        print("usuario ja cadastrado!")
    else:
        print("Agora crie uma Senha, use somente numeros!")
        usuarios[usuario] = int(input("Crie uma senha para seu login: "))
        print("Usuario e senha cadastrada ", usuarios)

def login_user():
    print("Faça seu login. ")
    usuario = str(input("Insira seu usuário: "))
    senha = int(input("Insira sua Senha: "))
    if usuario in usuarios and senha == usuarios[usuario]:
        print("Login bem sucedido.")
    else:
        print("Login Invalido ou inexistente \n Verifique o login ou casdastre um novo.")
        deseja_criar = str(input("Deseja criar um novo login ? Sim ou Nao: "))
        if deseja_criar == "Sim":
          cadastrar_user()
        if deseja_criar == "Nao":
          print("Fechando Programa")
    

opcao = 0

while opcao != 3:
    print("[1] Cadastrar Usuário \n[2] Fazer Login \n[3] Encerrar programa")
    opcao = int(input("Insira a opção desejada: "))
    if opcao == 1:
        cadastrar_user()


    elif opcao == 2:
        login_user()

    else:
        print("Encerrando Programa...")