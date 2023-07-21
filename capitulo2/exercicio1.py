""" Exercício 2.1: converta as equações em escrita python 
10 + 20 x 30
4^2 / 30
(9^4 + 2) x 6 - 1 """
print(10 + 20 * 6 - 1)
print(4 ** 2 / 30)
print((9 ** 4 + 2) * (6-1) )

""" Exercício 2.2: digíte e identifique a ordem de prioridade da equação:
10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2 """

a = (((10 % 3) * (10 ** 2)) + 1) - ((10 * 4) / 2)
print(a == 10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2)
