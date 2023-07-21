""" Variáveis String
Armazenam uma cadeia de caracteres. Podem ser letras, númeroes, sinais de pontuação, espaço em branco
etc. São identificados pela abertura e fechamento de aspas. Útil em escrever mensagens ou criação de
arquivos.Python pode acessar o tamanho da string por meio da função len. Esta retorna o número de 
caracteres da string. Note que uma string vazia não pode haver espaço em branco. """
print(len("")) # 0
print(len("A")) # 1
print(len("AB"), len("A E C")) # 2 5
print(len("O rato roeu a roupa")) # 19

""" é possível acessar um caractere da string por meio da indicação de sua posição. Isso ocorre devido
a existência do índice. O índice inicia em 0 quando uma string é criada, logo uma string com 10
caracteres apresentará índices de 0 à 9. O índice é acessado por meio de []"""
a = "ABCDEF"
print(a[0]) # A
print(a[1]) # B
print(a[5]) # F
#print(a[6]) # Erro


