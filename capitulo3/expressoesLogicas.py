""" os operadores lógicos básicos e relacionais podem se juntar em expressões mais complexas
ordem de operação:
primeiro é not 
segundo é and
por ultimo é or """

print(True or False and not True) # resultado é True
""" processo: 
True or False and True
True or False
True """

""" operadores lógicos com e relacionais"""
salario = 100
idade = 20
operacao = salario > 1000 and idade > 18

print(f"{salario} > 1000 and {idade} > 18:", operacao) # False
""" processo: 
(100 > 1000) and (20 > 18)
False and True
False """

salario = 2000
idade = 30
operacao = salario > 1000 and idade > 18

print(f"{salario} > 1000 and {idade} > 18:", operacao) # True
""" processo:
(2000 > 1000 and (20 > 18)
True and True
True """
