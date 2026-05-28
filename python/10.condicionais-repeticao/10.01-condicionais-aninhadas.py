# Condicionais Aninhadas

# As condicionais aninhadas são estruturas de controle de fluxo que permitem verificar múltiplas condições de forma hierárquica. Elas são úteis quando precisamos tomar decisões baseadas em várias condições relacionadas entre si.

conta_normal = True
conta_universitaria = False

saldo = 2000.0
saque = 2500.0
credito_especial = 450.0

#condicional aninhada, onde temos um IF dentro de outro IF, ou seja, a condição do segundo IF só é verificada se a condição do primeiro IF for verdadeira.

#exemplo de condicional aninhada para verificar se o cliente tem conta normal ou universitária, e se tem saldo suficiente para realizar o saque, caso contrário, verificar se tem crédito especial disponível.
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso.")
        
    # verificar se o cliente tem crédito especial disponível, ou seja, se o saldo mais o crédito especial é maior ou igual ao valor do saque.
    elif saque <= (saldo + credito_especial):
        print("Saque realizado com sucesso utilizando crédito especial.")
    else:
        print("Saldo insuficiente para realizar o saque.")

elif conta_universitaria:
        if saldo >= saque:
            print("Saque realizado com sucesso.")
        
        else:
            print("Saldo insuficiente para realizar o saque.")