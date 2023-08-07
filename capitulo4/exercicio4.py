""" Execute o seguinte programa: """
idade = int(input("Digite a idade de seu carro: "))
if idade <= 3:
    print("Seu carro é novo")
else:
    print("Seu carro é velho")

""" O resultado é o mesmo que: """
idade = int(input("Digite a idade do seu carro: "))
if idade <= 3:
    print(" Seu carro é novo")
if idade > 3:
    print("Seu carro é velho")

# Resposta: Sim. Testando com idade = 14, os resultados apontam que o carro é velho.

""" Escreva um programa que peça a distância a ser percorrida pelo passageiro. O preço de viagens até
200km/h é de R$ 0,50 por km/h enquanto valores maiores são por R$ 0,45. """
distancia_viagem = float(input("Qual a distância em km/h a ser percorrida pelo passageiro? "))
preco_viagem = 0
if distancia_viagem <= 200:
    preco_viagem = distancia_viagem * 0.50
    print(f"A distancia da viagem foi de {distancia_viagem}km/h, com valor de R$ {preco_viagem}.")
else:
    preco_viagem = distancia_viagem * 0.45
    print(f"A viagem foi de {distancia_viagem}km/h, com valor de R$ {preco_viagem}.")

