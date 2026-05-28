#Listas
#Listas são estruturas de dados que permitem armazenar múltiplos valores em uma única variável. 
# 
# Elas são mutáveis, ou seja, podemos alterar seus elementos após a criação da lista. 
# 
# As listas são definidas usando colchetes [] e os elementos são separados por vírgulas.

#lista é indexada, ou seja, cada elemento tem um índice associado, começando do 0.
#exemplo de lista
frutas = ["maçã", "banana", "laranja", "uva"]
print(frutas)

#acessando elementos da lista
print(frutas[0]) #maçã
print(frutas[1]) #banana
print(frutas[-1]) #uva


#lista vazia
lista_vazia = []
print(lista_vazia)

#lista com elementos de tipos diferentes, como números, strings e até outras listas.
carro = ["ferrari",  2020, ["vermelho", "preto"], True]
print(carro)

#listas com range
numeros = list(range(10)) #gera uma lista de números de 0 a 9
print(numeros)

letras = list("python") #gera uma lista de caracteres da string "python"
print(letras)