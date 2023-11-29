import turtle 

Distancia = int(input("Digite a distancia em km que o usuário percorreu:"))
Veiculo = str(input("Dentre os veículos mencionados, digite qual foi utilizado:(Carro, Moto, Bicicleta)"))

if Veiculo == "carro":
    Custo_Por_Km = 0.50
elif Veiculo == "moto":
    Custo_Por_Km = 0.20
elif Veiculo == "bicicleta":
    Custo_Por_Km = 0.10
else: 
    print ("Veículo não identificado.")
    exit ()


Calculo_Por_Km = Distancia*Custo_Por_Km
print ("O valor total é R$:", Calculo_Por_Km)




