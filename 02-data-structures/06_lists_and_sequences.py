# Listas e Sequências
# Listas são mutáveis, ou seja, podem ser modificadas após a criação.
# Elas são definidas usando colchetes [] e os elementos são separados por vírgulas
# podem armazenar diferentes tipos de dados, como números, strings, outras listas, etc.

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [5, 6, "c"]
    ]
    
print(matriz[0])
print(matriz[0][0])
print(matriz[1][2])
print(matriz[1][0])
print(matriz[1][1])

print(matriz[0][1:3])


# exemplo sem compreensão de listas
numeros = [1, 2, 3, 4, 5]
quadrados = []

for numero in numeros:
    quadrados.append(numero ** 2)
print(quadrados)

#com compreensão de listas
numeros = [1, 2, 3, 4, 5]
quadrados = [numero ** 2 for numero in numeros]
print(quadrados)

