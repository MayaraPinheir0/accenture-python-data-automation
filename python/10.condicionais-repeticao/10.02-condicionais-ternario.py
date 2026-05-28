#condicionais ternário

# O operador ternário é uma forma concisa de escrever uma expressão condicional. Ele é usado para atribuir um valor a uma variável com base em uma condição, tudo em uma única linha. A sintaxe do operador ternário é a seguinte: 

# variavel = valor_se_verdadeiro if condição else valor_se_falso

# Exemplo de uso do operador ternário para verificar se um número é par ou ímpar:

numero = int(input("Digite um número: "))

resultado = "par" if numero % 2 == 0 else "ímpar"

print(f"O número {numero} é {resultado}.")

#outro exemplo de uso do operador ternário para verificar se um aluno foi aprovado ou reprovado com base em sua nota:

nota = float(input("Digite a nota do aluno: "))

resultado_aluno = "aprovado" if nota >= 6 else "reprovado"

print(f"O aluno está {resultado_aluno}.")

#outro exemplo de uso do operador ternário para verificar se um cliente tem saldo suficiente para realizar um saque:

saldo = int(input("Digite o saldo da conta: "))
saque = int(input("Digite o valor do saque: "))

status = "sucesso" if saldo >= saque else "falha"
print(f"{status} ao realizar o saque)")

#outro exemplo de uso do operador ternário para verificar se um número é positivo, negativo ou zero:

numero = int(input("Digite um número: "))

id_numero = "positivo" if numero > 0 else "negativo" if numero < 0 else "zero"

print(f"O número {numero} é {id_numero}.")

#outro exemplo de uso do operador ternário para verificar se um ano é bissexto ou não:

ano = int(input("Digite um ano: "))

bissexto = "bissexto" if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) else "não bissexto"
print(f"O ano {ano} é {bissexto}.")