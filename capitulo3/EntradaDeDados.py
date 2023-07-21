""" Entrada de Dados
Quando o programa recebe dados por meio de um dispositivo, seja teclado ou algum arquivo
input é uma função que recebe parâmetros do usuário """
x = input("Digite um número: ") # apesar de escrever uma string, esta função irá receber dados para colocar em x
print(x)

nome = input("Digite seu nome: ")
print(f"Você digitou {nome}")
print(f"Olá, {nome}!UwU")

""" Conversão da entrada de dados
input sempre retorna valor do tipo string. Para isso, pode ser utilizado as funções int() e float()
para converter a variável do tipo string em inteiro ou decimal respectivamente """
anos = int(input("Anos de serviço: ")) # o input recebe o valor em string que será convertido em inteiro
valor_por_ano = (float(input("Valor por ano: "))) # float() transforma o valor dado a input em decimal
bônus = anos * valor_por_ano # prova do resultado. Caso os dois fossem string, não haveria multiplicação
print(f"Bonûs de R$ {bônus:5.2f}")