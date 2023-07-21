""" operadores lógicos agrupam operações que envolvem lógica booleana
3 operadores básicos: not, and, or 
not é operador unário, visto que apenas precisa de 1 operando
and e or são operadores binários, visto que dependem de 2 operandos"""

""" Operador not 
é uma inversão de verdadeiro e falso para cada operando que seja negado """
print("Negação do True: ", not True) # vira False
print("Negação do False: ", not False) # vira True
x = 2
print("Negação de x: ", not x)

""" Operador and
a relação entre os operandos de and será True apenas quando os dois forem verdadeiros"""
print("\nOperador: and")
print(True and True) # único True
print(True and False)
print(False and True)
print(False and False)

""" operador or
A relação entre os operandos de or apenas será falsa caso todos sejam falsos"""
print("\nOperador: or")
print(True or True)
print(True or False)
print(False or True)
print(False or False) # único falso


