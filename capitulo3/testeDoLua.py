""" Identifique os tipos lógicos das operações a seguir """
letras = {}
letras["a"] = 4
letras["b"] = 10
letras["c"] = 5.0
letras["d"] = 1
letras["f"] = 5

primeiraLetra = input("Escolha a primera Letra: ")
operador = input("Escolha um operador lógico: ")
segundaLetra = input("Escola a segunda letra: ")
resultado = eval(f"{letras[primeiraLetra]} {operador} {letras[segundaLetra]}")

print(f"{primeiraLetra} {operador} {segundaLetra} é", resultado)

"""
Nota: tive dificuldade na hora de montar o dicionário e a variável resultado.
"""