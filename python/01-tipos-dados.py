#Tipos de operadores em Python
#Operadores Aritméticos: +, -, *, /, //, %, **
#Operadores de Atribuição: =, +=, -=, *=, /=, //
#Operadores de Comparação: ==, !=, >, <, >=, <=
#Operadores Lógicos: and, or, not
#Operadores de Identidade: is, is not
#Operadores de Associação: in, not in

#Operadores Aritméticos: são usados para realizar operações matemáticas entre valores numéricos. O operador + é usado para adição, - para subtração, * para multiplicação, / para divisão, // para divisão inteira, % para módulo (resto da divisão) e ** para exponenciação.

#Operadores de Atribuição: são usados para atribuir valores a variáveis. O operador = é usado para atribuição simples, enquanto os operadores +=, -=, *=, /=, // são usados para realizar a operação e atribuir o resultado à variável.

#Operadores de Comparação: são usados para comparar valores e retornar um valor booleano (True ou False). O operador == é usado para verificar se dois valores são iguais, != para verificar se são diferentes, > para verificar se um valor é maior que outro, < para verificar se é menor, >= para verificar se é maior ou igual e <= para verificar se é menor ou igual.

#Operadores Lógicos: são usados para combinar expressões booleanas. O operador and retorna True se ambas as expressões forem verdadeiras, or retorna True se pelo menos uma das expressões for verdadeira e not inverte o valor booleano de uma expressão.

#Operadores de Identidade: são usados para verificar se duas variáveis referenciam o mesmo objeto na memória. O operador is retorna True se as variáveis referenciam o mesmo objeto, enquanto is not retorna True se elas referenciam objetos diferentes.

#Operadores de Associação: são usados para verificar se um valor está presente em uma sequência (como uma lista, tupla ou string). O operador in retorna True se o valor estiver presente na sequência, enquanto not in retorna True se o valor não estiver presente.

#Exemplos de uso dos operadores:

#Operadores Aritméticos
a = 10
b = 20
soma = a + b
print(soma) # Saída: 30

#Operadores de Atribuição
x = 5
x += 3
print(x) # Saída: 8

#Operadores de Comparação
print(a == b) # Saída: False
print(a != b) # Saída: True
print(a > b) # Saída: False
print(a < b) # Saída: True
print(a >= b) # Saída: False
print(a <= b) # Saída: True

#Operadores Lógicos
print(a > 5 and b < 30) # Saída: True
print(a > 15 or b < 30) # Saída: True
print(not a > 5) # Saída: False

#Operadores de Identidade
c = a
print(a is c) # Saída: True
print(a is b) # Saída: False

#Operadores de Associação
lista = [1, 2, 3, 4, 5]
print(3 in lista) # Saída: True
print(6 in lista) # Saída: False
print(6 not in lista) # Saída: True
