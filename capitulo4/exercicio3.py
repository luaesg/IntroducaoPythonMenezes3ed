""" Escreva um programa que leia 3 números e imprima o maior e o menor valor """
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

if a > b and a > c:
    print(f"{a} é o maior valor")
if a < b and a < c:
    print(f"{a} é o menor valor")
if b > a and b > c:
    print(f"{b} é o maior valor")
if b < a and b < c:
    print(f"{b} é o menor valor")
if c > a and c > b:
    print(f"{c} é o maior valor")
if c < a and c < b:
    print(f"{c} é o menor valor")

""" Escreva um programa que dê entrada no salário de um funcionário e calcule o valor do aumento. Salários
acima de R$ 1.250,00, calcule aumento de 10% e iguais ou inferiores calcule 15% de aumento. """
salario = float(input("Digite o salário do funcionário: "))
if salario > 1250.00:
    aumento = salario * 0.10
    print(f"Salário é R$ {salario:6.2f}. Aumento de R$ {aumento:6.2f}")
if salario <= 1250.00:
    aumento = salario * 0.15
    print(f"Salário é R$ {salario:6.2f}. Aumento de R$ {aumento:6.2f}")


