#identação e blocos de comandos

#identação é o recuo do código para indicar que ele pertence a um bloco de comandos.

#bloco de comandos é um conjunto de instruções que são executadas juntas, como por exemplo, o corpo de uma função, o corpo de um loop ou o corpo de uma estrutura condicional.


def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Saque autorizado")
        print(f"Saldo atual: {saldo - valor}")


def depositar(valor):
    saldo = 500
    saldo += valor
    print("Depósito autorizado")
    print(f"Saldo atual: {saldo}")

sacar(200)
depositar(1000)