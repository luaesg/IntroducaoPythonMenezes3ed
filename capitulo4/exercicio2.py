""" Escreva um programa que requisite a velocidade de um carro. Caso ultrapasse 80km/h, insira uma mensagem
de multa com cobrança de R$5,00. """

velocidade_carro = float(input("Digite a velocidade do carro em km/h: "))
if velocidade_carro > 80:
    print("A velocidade do carro ultrapassou 80 km/h. Será inserido uma multa de R$5,00 na carteira do motorista.")
if velocidade_carro <= 80:
    print("A velocidade do carro não ultrapassou 80 km/h.")


