""" Estruturas aninhadas
Consiste em inserir ifs dentro de blocos de linhas de outros ifs """
minutos = int(input("Quantos minutos você utilizou este mês: "))
if minutos < 200:
    preco = 0.20
else: # essa condição apresenta o aninhamento visto que existe um if e um else dentro
    if minutos < 400: # esse if e o else posterior estão aninhados dentro do else acima.
        preço = 0.18
    else: # 
        preco = 0.15
print(f"Você vai pagar este mês: R${minutos * preco:6.2f}")