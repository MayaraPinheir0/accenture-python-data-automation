
#Em Python, os operadores de identidade são usados para comparar se dois objetos ocupam a mesma posição na memória. 

# Os operadores de identidade são: is e is not.

#objetivo é verificar se as duas variaveis apontam para o mesmo objeto na memoria
saldo = 1000
limite = 500

print(saldo is limite) #false, pois saldo e limite ocupam posicoes diferentes na memoria

print(saldo is not limite) #true, pois saldo e limite ocupam posicoes diferentes na memoria

print(saldo == limite) #false, pois saldo e limite tem valores diferentes