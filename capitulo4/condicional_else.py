""" Condicional else
É uma cláusula utilizada quando o if anterior seja falso. Muito presente quando a condicional else 
representa um valor oposto ao if. """
idade = int(input("Digite a idade de seu carro: "))
if idade <= 3:
    print("Seu carro é novo")
else: # else é verdadeiro quando o if acima for falso, logo todo carro acima de 3 anos entra nesta condicional
    print("Seu carro é velho") # esse print é realizado visto que else representa idade > 3, que é considerado velho

