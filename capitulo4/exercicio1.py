""" Analise o programa a seguir:
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
if a > b: 
    print("O primeiro valor é o maior!") # está contido no if superior
if b > a:  
    print("O segundo valor é o maior!") 
Agora responda: O que acontece se o primeiro e o segundo valores forem iguais?
"""

""" Resposta: O programa não apresentará erro de escrita caso os números inseridos sejam inteiros. As
duas condicionais serão lidas e ignoradas visto que ambas são falsas. Logo, o programa será encerrado
quando tentar ler as proximas linhas e não encontrar nada. """
