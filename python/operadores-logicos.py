# Operadores lógicos são usados para combinar expressões booleanas e retornar um resultado booleano. 

# Em Python, os operadores lógicos são: and, or e not.


#o exemplo a seguir verifica se o saque é maior que o saldo atual e se o saque é menor ou igual ao limite, ou se a conta é especial e o saldo é maior ou igual ao saque.

#AND = retorna True se ambas as expressões forem verdadeiras, caso contrário, retorna False.
#OR = retorna True se pelo menos uma das expressões for verdadeira, caso contrário, retorna False.
#NOT = inverte o valor lógico de uma expressão, ou seja, retorna True se a expressão for False e retorna False se a expressão for True.

print(False and False)
print(False and True)
print(True and False)
print(True and True)
print(False or False)
print(False or True)
print(True or False)
print(True or True)

print("---------")
#operadores logicos com mais de duas expressões
#o operador AND retorna True somente se todas as expressões forem verdadeiras, caso contrário, retorna False.

print(False and False and True)
print(False and True and True)
print(True and False and True)
print(True and True and True)
print(False or False or True)
print(False or True or True)
print(True or False or True)
print(True or True or True)


saldo = 1000
saque = 200
limite = 500
conta_especial = True

#o operador AND retorna True somente se todas as expressões forem verdadeiras, caso contrário, retorna False.
expressao =(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(expressao)

#o operador NOT inverte o valor lógico de uma expressão, ou seja, retorna True se a expressão for False e retorna False se a expressão for True.
expressao2 = not (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(expressao2)

#o operador AND retorna True somente se todas as expressões forem verdadeiras, caso contrário, retorna False.
conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

#o operador OR retorna True se pelo menos uma das expressões for verdadeira, caso contrário, retorna False.
expressao3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(expressao3)