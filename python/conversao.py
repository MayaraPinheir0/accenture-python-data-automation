#conversao de tipos em Python
# Em Python, é possível converter um valor de um tipo para outro usando as funções de conversão. Para converter um inteiro para um float, você pode usar a função float(). Por exemplo:

print(int(1.5))
print(int("10"))
print(float("10.90"))
print(float(10))

valor = 10
valor_str = str(valor)

print(type(valor))
print(type(valor_str))
#print(int("a")) #gera um erro, pois "a" não é um número    
print(float("a"))

#verificar se o saque é maior que o saldo
saldo = 450
saque = 200

print(saque>saldo)

saldo = 200
saque = 200

print(saque == saldo) #verificar se o saque é igual ao saldo
print(saque >= saldo) #verificar se o saque é maior ou igual ao saldo
print(saque != saldo) #verificar se o saque é diferente do saldo

#operadores de atribuicao (sinal de igual)
saldo = 500

saldo -= 100 #saldo = saldo - 100
print(saldo)

saldo += 50 #saldo = saldo + 50
print(saldo)

saldo *= 2 #saldo = saldo * 2
print(saldo)

saldo /= 2 #saldo = saldo / 2

print(saldo)

