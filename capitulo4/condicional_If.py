""" Condiconal If
Condicional é a estrutura que seleciona e ativa uma parte do programa, ou ignora a mesma.
If <condição> for verdadeira, será executado um código. """
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
if a > b: # caso seja verdadeira, executará o código interno. Caso contrário, esta condicional será ignorada
    print("O primeiro valor é o maior!") # está contido no if superior
if b > a: # será executada caso a primeira condicional seja ignorada(falsa). 
    print("O segundo valor é o maior!") 
# Lembrando: será lido as duas condicionais, mas uma NÃO será executada!

""" Outro exemplo: """
idade = int(input("Digite a idade do seu carro: "))
if idade <= 3:
    print(" Seu carro é novo")
if idade > 3:
    print("Seu carro é velho")

""" Exemplo em que é feito mais de 1 linha de código dentro do bloco de um if: """
salario = float(input("Digite o salário para cálculo do imposto: "))
base = salario # base será uma copia de salario visto que sofrerá modificação
imposto = 0
if base > 3000: # caso verdadeiro, recairá sobre o salário um imposto de 35%
    imposto = imposto + ((base - 3000) * 0.35) 
    base = 3000 # a base se torna 3000 visto que o imposto acima de 3000 já foi deferido
if base > 1000: # Quem teve que pagar um imposto acima de 3000 também precisará pagar este imposto dentro do valor de 3000.
    imposto = imposto + ((base - 1000) * 0.20) 
print(f"Salário: R${salario:6.2F} Imposto a pagar: R${imposto:6.2f}")



