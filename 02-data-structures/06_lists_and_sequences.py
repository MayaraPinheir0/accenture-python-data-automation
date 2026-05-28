# Listas e Sequências
# Listas são mutáveis, ou seja, podem ser modificadas após a criação.
# Elas são definidas usando colchetes [] e os elementos são separados por vírgulas
# podem armazenar diferentes tipos de dados, como números, strings, outras listas, etc.

print("Listas:")
frutas = {'🍎', '🍓', '🍐', '🍎', '🍎', '🍓'}

print(type(frutas)) # Output: <class 'set'> - type() é uma função embutida em Python que retorna o tipo do objeto passado como argumento. No caso, frutas é um conjunto (set), então type(frutas) retorna <class 'set'>.
print(max(frutas)) # Output: {'🍎', '🍓', '🍐'} - max() retorna o elemento máximo do conjunto.
print(min(frutas)) # Output: {'🍎', '🍓', '🍐'} - min() retorna o elemento mínimo do conjunto.
print(sum(frutas)) # Output: TypeError - sum() é uma função embutida em Python que retorna a soma dos elementos de um iterável. No entanto, como frutas é um conjunto de strings (representando emojis de frutas), não é possível calcular a soma desses elementos, resultando em um erro do tipo TypeError.
print(sorted(frutas)) # Output: ['🍎', '🍐', '🍓'] - sorted() retorna uma nova lista com os elementos do conjunto ordenados.
print(list(frutas)) # Output: ['🍎', '🍓', '🍐'] - list() é uma função embutida em Python que converte um iterável em uma lista. No caso, frutas é um conjunto, e list(frutas) retorna uma nova lista contendo os elementos do conjunto.
print(set(frutas)) # Output: {'🍎', '🍓', '🍐'} - set() é uma função embutida em Python que converte um iterável em um conjunto. No caso, frutas já é um conjunto, então set(frutas) retorna o próprio conjunto sem alterações.
print(tuple(frutas)) # Output: ('🍎', '🍓', '🍐') - tuple() é uma função embutida em Python que converte um iterável em uma tupla. No caso, frutas é um conjunto, e tuple(frutas) retorna uma nova tupla contendo os elementos do conjunto.
print(dict.fromkeys(frutas)) # Output: {'🍎': None, '🍓': None, '🍐': None} - dict.fromkeys() é um método de classe que cria um novo dicionário a partir de um iterável, onde as chaves são os elementos do iterável e os valores são definidos como None por padrão. No caso, frutas é um conjunto, e dict.fromkeys(frutas) retorna um dicionário onde as chaves são os elementos do conjunto e os valores são None.
print(frutas.count()) # Output: AttributeError - count() é um método de sequência que conta o número de ocorrências de um elemento específico em uma sequência, como uma lista ou uma tupla. No entanto, frutas é um conjunto, e conjuntos não possuem o método count(), resultando em um erro do tipo AttributeError.
print(frutas.index()) # Output: AttributeError - index() é um método de sequência que retorna o índice da primeira ocorrência de um elemento específico em uma sequência, como uma lista ou uma tupla. No entanto, frutas é um conjunto, e conjuntos não possuem o método index(), resultando em um erro do tipo AttributeError.
print

print(len(frutas)) # Output: 3 - len() é uma função embutida em Python que retorna o número de elementos em um objeto. No caso, frutas é um conjunto com 3 elementos únicos ('🍎', '🍓', '🍐'), então len(frutas) retorna 3.

print('🍌' in frutas) # Output: True - isso porque o elemento '🍌' está presente no conjunto.
print('🍎' not in frutas) # Output: False - isso porque o elemento '🍎' está presente no conjunto.
print('🍉' in frutas) # Output: False - isso porque o elemento '🍉' não está presente no conjunto.

frutas.add('🍌'); print(frutas) # Output: - Adiciona '🍌' ao conjunto
frutas.pop(); print(frutas) # Output: - Remove um elemento aleatório do conjunto e o retorna. Se o conjunto estiver vazio, ele gera um erro.
frutas.remove('🍎'); print(frutas) # Output: - Remove o elemento '🍎' do conjunto. Se o elemento não estiver presente no conjunto, ele gera um erro.
frutas.update(['🍉', '🍇', '🍊']); print(frutas) # Output: - Adiciona os elementos '🍉', '🍇' e '🍊' ao conjunto. Se algum desses elementos já estiver presente no conjunto, ele não será adicionado novamente, pois conjuntos não permitem elementos duplicados.   
frutas.discard('🍐'); print(frutas) # Output: - Remove o elemento '🍐' do conjunto. Se o elemento não estiver presente no conjunto, ele não gera um erro, ao contrário do método remove(   ).
#frutas.clear(); print(frutas) # Output: - Remove todos os elementos do conjunto, deixando-o vazio. O conjunto resultante será um conjunto vazio, ou seja, set(). 



print("---")
print("Matriz:")
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
# slicing em listas 
# O slicing é uma técnica que permite extrair uma parte de uma lista usando a sintaxe [início:fim:passo].
print(matriz[0][1:3])
print(matriz[1][0:2])
print(matriz[2][::2])


# exemplo sem compreensão de listas
print("Quadrados sem compreensão de listas:")
numeros = [1, 2, 3, 4, 5]
quadrados = []

for numero in numeros:
    quadrados.append(numero ** 2)
print(quadrados)

#com compreensão de listas
numeros = [1, 2, 3, 4, 5]
quadrados = [numero ** 2 for numero in numeros]
print(quadrados)


# funcoes de lista
print("Funções de lista:")

lista = [1, 2, 3, 4, 5]

#APPEND, INSERT, EXTEND

# Inserindo no FINAL
# O elemento a ser adicionado é passado como argumento para o método append().
# argumento é o valor a ser adicionado à lista.

lista.append(6)
print(lista)
# Output: [1, 2, 3, 4, 5, 6]

# Inserindo no INICIO
# 1o elemento é o índice, 2o elemento é o value.
# é util para adicionar um elemento em uma posição específica da lista, deslocando os elementos existentes para a direita para acomodar o novo elemento.
lista.insert(0, 0)
print(lista)
# Output: [0, 1, 2, 3, 4, 5, 6]

# Inserindo em uma POSIÇAO ESPECÍFICA
lista.insert(3, 2.5)
print(lista)
# Output: [0, 1, 2, 2.5, 3, 4, 5, 6]


# inserindo os elementos de uma lista em outra lista
# é util para combinar os elementos de duas listas em uma única lista, permitindo que você crie uma nova lista que contenha todos os elementos de ambas as listas.
# atencao: o método extend() modifica a lista original, enquanto o operador + cria uma nova lista sem modificar as listas originais.

print("Inserindo os elementos de uma lista em outra lista:")
lista_base = [1, 2, 3]
lista_extra = [4, 5, 6]

# usando extend()

# usando operador + 
# forma A - modificando a lista original
resultado_a = lista_base + lista_extra
print(resultado_a)
# Output: [1, 2, 3, 4, 5, 6]

# usando extend()
# forma B - criando uma nova lista sem modificar as listas originais
lista_base.extend(lista_extra)
print(lista_base)
# Output: [1, 2, 3, 4, 5, 6]




casa = ["branca", "classica", "branca", "10x20"]
x = casa.count("branca")
print(x) # Output: 2 - O método count() é usado para contar o número de ocorrências de um elemento específico em uma lista. No caso, casa é uma lista que contém os elementos "branca", "classica" e "10x20". O método count("branca") conta quantas vezes o elemento "branca" aparece na lista casa, e como ele aparece duas vezes, o resultado é 2.

#metodo set
casa = ["branca", "classica", "branca", "10x20"]
y = set(casa)
print(y) # Output: {'classica', '10x20', 'branca'} - O método set() é usado para criar um conjunto a partir de um iterável, como uma lista. No caso, casa é uma lista que contém os elementos "branca", "classica" e "10x20". O método set(casa) cria um conjunto contendo os elementos únicos da lista casa, ou seja, {'classica', '10x20', 'branca'}. Note que a ordem dos elementos em um conjunto não é garantida, então a saída pode variar.