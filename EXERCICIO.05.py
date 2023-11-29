usuarios = {
    'usuario1': 'usuario1',
    'usuario2': 'usuario2',
    'usuario3': 'usuario3',
}

usuario = input("Informe seu usuário: ")
senha = input("Informe sua senha: ")

if usuario in usuarios and usuarios[usuario] == senha:
    print(usuario)
else:
    print ("Usuário não existe!")