""" Operações com strings
fatiamento: utilizar apenas uma parte da string original
concatenação: juntar strings separadas em uma única maior
composição: utilizar strings como modelos para inserção de outras strings em si """

""" concatenação
somar ou multiplicar ENTRE strings """
s = "ABC"
print(s + "c") #ABCc
print(s + "d" * 4) #ABCdddd

print("X" + "-" * 10 + "X") # X----------X
print(s + "x4 = " + s * 4) # ABCx4 = ABCABCABCABC

#print(s + 10) # Erro. Um dos valores não é string

""" composição 
Insere o valor de uma variável dentro de um modelo de string por meio do marcador de posição"""
print("João tem %d anos" % 10) # o marcador de posição é %d e este recebe a indicação de % fora da string

""" composição: marcadores
%d refere-se a tipos números inteiros
%s refere-se a Strings
%f refere-se a números decimais """
print("Olá, eu sou %s, mago nível %d, com resistência à terra %f acima da média" % ("Lenius", 14, 2.7))

""" composição: mudando posição de marcadores
Basta inserir o valor da mudança de posição entre % e a letra do marcador"""
idade = 22
print("[%d]" % idade) # [22] o colchete vai auxiliar a identificar as futuras mudanças de posição
print("[%03d]" % idade) # [022] inseriu um 0 na terceira posição criada, visto que a 2 e a 1 já estão ocupadas
print("[%3d]" % idade) # [ 22] apenas inseriu um espaço visto que a 3 posição não foi identificada
print("[%-3d]" % idade) #[22 ] a subtração informa que a posição criada deve ser feita no sentido inverso

""" composição: formatação de números decimais
quando se utiliza %f, é possivel identificar o número total de caracteres, seguido por um ponto e
depois identificar quantos desses caracteres serão as casas decimais """
print("%5f" % 5) #5.000000 só 5 entre % e f apresenta a quantidade de caracteres após o ponto
print("%5.2f" % 5) # 5.00 note que há um espaçamento a esquerda da impressão, identificando 2 valores extras
print("%10.5f" % 5) # 5.00000 o espaço a esquerda aumenta ainda mais

""" composição: vários marcadores na string em uma mesma string
substituir vários marcadores de posição por valores requer que as variáveis sejam postas entre () """
nome = "João"
idade = 22
grana = 51.34
print("%s tem %d anos e R$%f no bolso." % (nome, idade, grana))
print("%12s tem %3d anos e R$%5.2f no bolso." % (nome, idade, grana))
print("%12s tem %03d anos e R$%5.2f no bolso." % (nome, idade, grana))
print("%-12s tem %-3d anos e R$%-5.2f no bolso." % (nome, idade, grana))

""" Composição: .format
método mais moderno de utilizar composição"""
print("\ncomposição: .format")
print("{} tem {} anos e R${} no bolso." .format(nome, idade, grana))
print("{:12} tem {:3} anos e R${:5.2f} no bolso." .format(nome, idade, grana))
print("{:12} tem {:03} anos e R${:5.2f} no bolso." .format(nome, idade, grana))
print("{:<12s} tem {:<3} anos e R${:5.2f} no bolso." . format(nome, idade, grana))

""" Composição: f-string 
forma mais compacta que o .format """
print("\nComposição: f-string")
print(f"{nome} tem {idade} anos e R${grana} no bolso.")
print(f"{nome:12} tem {idade:3} anos e R${grana:5.2f} no bolso.")
print(f"{nome:12} tem {idade:03} anos e R${grana:5.2f} no bolso")
print(f"{nome:<12s} tem {idade:<3} anos e R${grana:5.2f} no bolso.")

""" Fatiamento de Strings
é inserido : dentro do buscador do índice da string. O lado esquerdo irá identificar o valor inicial
da fatia. O lado direito irá identificar o fim da fatia, mas o valor inserido nesta parte não aparecerá
no resultado """
s = "ABCDEFGHI"
print(s[0:2]) # AB Note que 0 é A, B é 1. C não aparece pois identifica o fim da fatia, que é 2.
print(s[1:2]) # B
print(s[2:4]) # CD
print(s[0:5]) # ABCDE
print(s[1:8]) # BCDEFGH

""" Fatiamento: omissão de valores
é possível omitir o valor do índice a esquerda ou a direita de : para que seja colocado até fim os
caracteres não descartados anteriormente"""
print(s[:2]) # AB
print(s[1:]) # BCDEFGHI
print(s[:]) # ABCDEFGHI

""" Fatiamento: valores negativos
a leitura do índice começa pela direita quando o número for negativo """
print(s[0:-2]) # ABCDDEFG -2 indica que a leitura do indice deve parar em H, visto que -1 é I
print(s[-1:]) # I 
print(s[-5:7]) # EFG
print(s[-2:-1]) # H

