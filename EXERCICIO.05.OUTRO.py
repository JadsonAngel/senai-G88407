def login(user):
    while True:

        Username = input("Informe o seu usuário: ")
        Senha = input("Informe sua senha: ")

        for u in user:
            if Username == u[0] and Senha == u[1]:
                return Username
        
        print ("Usuário ou senha estão incorretos. Tente novamente.")


user = [["jadson123", "jad123"], ["jadson1234", "jad1234"], ["jadson12345", "jad12345"]]

Username = login(user)
print (Username,", Seja bem vindo!")
