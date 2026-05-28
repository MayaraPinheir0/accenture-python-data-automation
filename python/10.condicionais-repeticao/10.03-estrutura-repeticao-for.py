# Estruturas de Repetição
# As estruturas de repetição, também conhecidas como loops, são usadas para executar um bloco de código várias vezes, com base em uma condição. 

# Em Python, existem duas principais estruturas de repetição: 
# o loop for e 
# o loop while.

# Loop for: 
# é usado para iterar sobre uma sequência (como uma lista, tupla ou string) ou um intervalo de números. A sintaxe do loop for é a seguinte:

# for variavel in sequencia:

#     bloco de código

#FOR EM LISTA
# Exemplo de uso do loop for para iterar sobre uma lista de números e imprimir cada número:

numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)
    
#FOR EM STRING
# Outro exemplo de uso do loop for para analisar cada letra de um texto e imprime apenas as vogais:

#exemplo utilizando iteravel string
texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end = " ")
print()

#RANGE
#O loop for também pode ser usado com a função range() para iterar sobre um intervalo de números. 

# A função range() gera uma sequência de números, que pode ser usada para controlar o número de iterações do loop. A sintaxe da função range() é a seguinte:

# range(inicio, fim, passo)
# exemplo: range(0, 10, 1) gera a sequência de números de 0 a 9, com um passo de 1. 
# Se o parâmetro inicio for omitido, ele assume o valor padrão de 0. Se o parâmetro passo for omitido, ele assume o valor padrão de 1. 

# o parâmetro inicio é o número inicial da sequência (padrão é 0), 
# o parâmetro fim é o número final da sequência (não incluído) e 
# o parâmetro passo é o valor de incremento entre os números (padrão é 1).

# Exemplo de uso do loop for com a função range() para contar de 0 a 9:

for i in range(10):
    print(i)
    # O parâmetro fim é obrigatório, enquanto os parâmetros inicio e passo são opcionais. Se apenas um argumento for fornecido para a função range(), ele será interpretado como o valor de fim, e o início será assumido como 0 e o passo como 1. Por exemplo, range(5) gerará a sequência de números de 0 a 4.
    
for numero in range(0, 10):
    print(numero, end = " ")
    
    #end = " " é importante pois é usado para evitar a quebra de linha após cada número impresso, permitindo que os números sejam impressos na mesma linha, separados por um espaço. 
    # O valor padrão de end é "\n", que representa uma nova linha, mas ao definir end como " ", os números serão impressos com um espaço entre eles, em vez de cada número ser impresso em uma nova linha.
    
    #exemplo de resultado: 0 1 2 3 4 5 6 7 8 9
    
    #sem o end = " ", o resultado seria:
    #0
    #1
    #2
    #3
    #4 etc...
    
#exibindo a tabuada do 5 usando o loop for e a função range()
for i in range(0, 51, 5):
    print(i, end = " ")