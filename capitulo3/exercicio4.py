""" Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto.
Considere que pagam imposto pessoas cujo salário é maior que R$1200 """
salario = 1000
imposto = 1200
pagamentoImposto = salario > 1200

print(f"O salário de Fulano é de R${salario}. Ele deve pagar imposto?", pagamentoImposto)

""" Calcule os valores de A > B and C or D """
A = 1
B = 2
C = True
D = False
operacao = A > B and C or D

print(operacao) # False
""" Processo:
(1 > 2) and True or False
False and True or False
False or False
False """

A = 10
B = 3
C = False
D = False
operacao = A > B and C or D

print(operacao) # False
""" Processo:
(10 > 3) and False or False
True and False or False
False or False
False """




A = 5
B = 1
C = True
D = True
operacao = A > B and C or D

print(operacao) # True
"""Processo:
(5 > 1) and True or True
True and True or True
True or True
True """

""" Escreva uma expressão para decidir se um aluno foi ou não aprovado. 
Para ser aprovado, todas as médias precisam ser maiores que 7.
O aluno cursa 3 matérias e cada nota está armazenada nas seguintes variáveis:
matéria1, matéria2, matéria3 """
materia1 = 6
materia2 = 7
materia3 = 8
aprovacao = materia1 > 7 and materia2 > 7 and materia3 > 7

print("O aluno foi aprovado?", aprovacao) # False
""" processo:
6 > 7 and 7 > 7 and 8 > 7
False and False and True
False and True
False """
