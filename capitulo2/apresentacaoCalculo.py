""" Python pode ser utilizado como calculadora """
x = 2+3
b = 10 - 4 + 2
print("soma", "subtração")
print(x,b)

""" * indica multiplicação
/ indica divisão """
print("multiplicação")
x = 2 * 10
print(x)
print("divisão")
x = 20 / 4
print(x)

""" Meandros da divisão
/ pode ser uilizado para obter o resulto de inteiros e decimais
// obtem resultados com valor inteiro(arredondado para baixo em caso do resultado ser decimal)"""
print("divisão decimal")
x = 10 / 4
print(x)
print("divisão com valor inteiro")
x = 10 // 4
print(x)

""" ** indica potenciação """
print("Potenciação")
x = 2 ** 3
print(x)

""" calculando a raiz com expoente fracionário """
print("raiz por meio de expoente fracionário")
x = 2 ** (1/3)
print(x)

""" Obter resto da divisão """
print("resto da divisão de 10 / 3")
x = 10 % 3
print(x)

""" Ordem de procedência: 
1 - **
2 - *, /, //, % 
3 - +, - 
Lembrando que em caso de mesma prioridade, começa pela esquerda até a direita """
x = 1500 + (1500 * 5 /100)
print(x)

