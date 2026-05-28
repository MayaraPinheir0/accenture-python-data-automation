#entrada de dados do usuario, a função input() retorna uma string, por isso é necessário converter para o tipo desejado, nesse caso, inteiro.

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você está apto a se canditadar ao exame de habilitação")
else: 
    print("Você não está apto a se canditadar ao exame de habilitação")
    
#IF condicional simples, onde a condição é verificada e se for verdadeira, o bloco de comandos é executado, caso contrário, o programa continua a execução normalmente.
saldo = 2000.0
saque = float(input("Digite o valor do saque: "))

if saldo >= saque:
    print("Saque autorizado")

if saldo < saque:
    print("Saldo insuficiente")
    
# ELSE, onde o bloco de comandos do ELSE é executado quando a condição do IF é falsa, ou seja, quando o saldo é menor que o valor do saque.

saldo = 2000.0
saque = float(input("Digite o valor do saque: "))

if saldo >= saque:
    print("Saque autorizado")
    
else:
    print("Saldo insuficiente")
    

#ELIF, onde é possível verificar múltiplas condições, ou seja, quando a condição do IF é falsa, o programa verifica a condição do ELIF, e assim por diante, até chegar no ELSE, que é executado quando todas as condições anteriores são falsas.


#------------
#exemplo do uso de ELIF para saque e extrato em conta bancária

opcao = int(input(" Digite a opção desejada: [1] saque \n[2] extrato "))

if opcao == 1:
    valor = float(input("Informe o valor do saque: "))
    print(f"Saque de R$ {valor:,.2f} autorizado.")

elif opcao == 2:
    print("Exibindo extrato...")

else:
    sys.exit("Saindo do sistema...")