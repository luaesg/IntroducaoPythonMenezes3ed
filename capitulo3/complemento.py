""" Fatiamento: Exemplos do Professor Luis Tavares
https://www.youtube.com/watch?v=UFhYerQpSho"""
str = "Programando em Python"
c = str[15]
print(c) # P

s1 = str[15:]
print(s1) # Python

s2 = str[12:14]
print(s2) # em

s3 = str[::2] # Pormnoe yhn # O 2 indica de quantos em quantos caracteres serão acessados (de 2 em 2)
print(s3)

s4 = str[::-1] # nohtyP me odnamargorP # -1 inverte a ordem de seleção da string
print(s4)


""" Fatiamento e outros: CBFCursos (Prof. Bruno)
https://www.youtube.com/watch?v=DUZoz0HuuCU"""
curso = "Curso de Python"
print(curso[9]) # P # o espaçamento também é contado
print(curso[0:5]) # Curso
print(curso[9:15]) # Python
print(len(curso))

curso = " Curso de Python "
print(len(curso))
print(curso.strip()) # strip retira o espaço que está próximo das aspas da string
print(curso.lower()) # curso de python # lower todas as letras ficam minúsculas
print(curso.lower().strip()) # realiza as duas funções acima
print(curso.upper()) # CURSO DE PYTHON # upper todas as letras ficam maiúsculas
print(curso.replace("Python","C")) # Curso de C++  # troca caracteres(esquerda) por outros caracteres(direita)
print(curso.split(" ")) # divide a string e retorna um array.
