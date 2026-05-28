#STRING

# As strings em Python são sequências de caracteres usadas para armazenar e manipular texto. Elas são delimitadas por aspas simples (' ') ou aspas duplas (" ").

# As strings são imutáveis, o que significa que uma vez criada, seu conteúdo não pode ser alterado. No entanto, é possível criar novas strings a partir de operações em strings existentes.

# As strings em Python suportam uma variedade de operações, como concatenação, fatiamento, formatação e métodos de string para manipulação de texto.

curso = "PYthon"

#LETRAS MAIUSCULAS E MINUSCULAS
print(curso.upper()) #PYTHON
# O método upper() é usado para converter todos os caracteres de uma string para maiúsculas. Ele retorna uma nova string com os caracteres convertidos, sem modificar a string original.

print(curso.lower()) #python
# O método lower() é usado para converter todos os caracteres de uma string para minúsculas. Ele retorna uma nova string com os caracteres convertidos, sem modificar a string original.

print(curso.title()) #Python
# O método title() é usado para converter o primeiro caractere de cada palavra em uma string para maiúscula. Ele retorna uma nova string com os caracteres convertidos, sem modificar a string original.

print(curso.capitalize()) #Python
# O método capitalize() é usado para converter o primeiro caractere de uma string para maiúscula e os demais para minúscula. Ele retorna uma nova string com os caracteres convertidos, sem modificar a string original.

print(curso.swapcase()) #pyTHON
# O método swapcase() é usado para inverter o caso de todos os caracteres de uma string. Ele retorna uma nova string com os caracteres convertidos, sem modificar a string original.


#REMOVE ESPAÇOS EM BRANCO
print(curso.lstrip()) #PYthon
# O método lstrip() é usado para remover os caracteres em branco (espaços, tabulações, quebras de linha) do início de uma string. Ele retorna uma nova string com os caracteres removidos, sem modificar a string original.

print(curso.rstrip()) #python
# O método rstrip() é usado para remover os caracteres em branco (espaços, tabulações, quebras de linha) do final de uma string. Ele retorna uma nova string com os caracteres removidos, sem modificar a string original.

print(curso.strip()) #python
# O método strip() é usado para remover os caracteres em branco (espaços, tabulações, quebras de linha) do início e do final de uma string. Ele retorna uma nova string com os caracteres removidos, sem modificar a string original.

#JUNCOES E CENTRALIZACOES
curso = "python"

print(curso.center(10, "-")) #--python--

# O método center() é usado para centralizar uma string em um campo de largura especificada

print(".".join(curso)) 
#p.y.t.h.o.n

# O método join() é usado para concatenar os elementos de uma sequência (como uma lista ou tupla) em uma única string, usando um separador especificado. 
# No exemplo acima, o separador é um ponto (".") e a sequência é a string "python". O resultado é a string "p.y.t.h.o.n", onde cada caractere da string original é separado por um ponto.



#outro exemplo
nome = "MaRIa"

print(nome.upper()) #MARIA
print(nome.lower()) #maria
print(nome.title()) #Maria

#RESUMO
nome = "gUIlherME"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá mundo!    "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu))
