""" Crie um programa que receba 2 números inteiros e emprima os dois números na tela """
numero1 = int(input("Primeiro número: "))
numero2 = int(input("Segundo número: "))
print(f"Número 1: {numero1} e número 2: {numero2}")

""" Escreva um código que leia o valor em metros e exiba em milímetros """
metros = float(input("Digite o valor em metros: "))
milimetros = metros * 1000
print(f"{metros:.2f} metros valem {milimetros:.2f} milimetros")

""" Programe um leitor de dias, horas, minutos e segundos do usuário e mostre os resultados em segundos """
dia = int(input("Insira a quantidade de dia(s): "))
hora = int(input("Insira a quantidade de hora(s): "))
minuto = int(input("Insira a quantidade de minuto(s): "))
segundo = int(input("Insira a quantidade de segundo(s): "))
calculo = (dia * 86400) + (hora * 3600) + (minuto * 60) + (segundo)
print(f"O total em segundo(s) é de: {calculo}")

""" Crie um programa que receba o valor do salário e a porcentagem do aumento. Mostre o valor do aumento
e o salário atual """
salario = float(input("Insira o valor do salário atual: R$"))
bonus = float(input("Insira o valor do bonus(%): "))
salario = salario + (salario * bonus/100)
print(f"Com o bônus de {bonus}%, o salário atual é de R${salario:.2f}")

""" Faça um programa que requisite o preço da mercadoria e o desconto da mesma. Mostre o valor de
de desconto e o preço do produto com desconto """
preçoMercadoria = float(input("Digite o preço da mercadoria: R$"))
desconto = float(input("Digite o percentual de desconto: "))
mercadoriaComDesconto = preçoMercadoria - (preçoMercadoria * desconto/100)
print(f"O desconto de {desconto}% reduziu o preço de R${preçoMercadoria} para R${mercadoriaComDesconto}")

""" Crie um programa que calcule o tempo de viagem de um carro. Deve ser perguntado a distância a percorrer
e a velocidade média esperada para realizar a viagem """
distancia = float(input("Quanto é a distância da viagem em km?"))
velocidadeMedia = float(input("Qual a velocidade média esperada para realizar a viagem?"))
tempoViagem = distancia/ velocidadeMedia
print(f"O tempo para realizar a viagem é de {tempoViagem:.2f} horas")

""" Faça um programa que converta C em F. """
celsius = float(input("Insira o valor da temperatura em Celsius: "))
fahrenheit = 9 * celsius/5 + 32
print(f"O valor de {celsius}Cº em Fahrenheit é {fahrenheit}")

""" O programa deve requisitar a quantidade de km percorridos por um carro alugado e a quantidade
de dias que foi alugado. O software deve apresentar o preço a pagar, sendo que o carro custa R$60
por dia e R$0.15/km rodado """
km_percorrido = float(input("Insira o valor de km percorrido pelo carro: "))
dias_alugado = float(input("Insira a quantidade de dias que o carro foi alugado: "))
valor_aluguel_carro = km_percorrido * 0.15 + dias_alugado * 60
print(f"O custo do carro alugado é de: R${valor_aluguel_carro:.2f}")

""" Calcule a redução do tempo de vida de um fumante: a máquina deve perguntar quantidade de cigarros
fumados por dia e por quantos anos já fumado. Considere que o fumante perde 10 minutos de vida para 
cada cigarro e apresente o valor perdido em dias. """
dias_do_ano = 365
cigarros_por_dia = int(input("Quantos cigarros o fumante consumiu por dia? "))
anos_de_fumo = int(input("Por quantos anos o fumante consumiu os cigarros? "))
reducao_vida_minuto_para_dia = cigarros_por_dia * 10 / 1440
reducao_vida_anos_para_dias = anos_de_fumo * dias_do_ano 

reducao_vida_dia = (reducao_vida_minuto_para_dia + reducao_vida_anos_para_dias)
print(f"A redução de vida vale: {reducao_vida_dia} dias")



