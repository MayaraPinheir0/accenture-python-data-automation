# Estruturas de Repetição
# As estruturas de repetição, também conhecidas como loops, são usadas para executar um bloco de código várias vezes, com base em uma condição.

# Loop while: é usado para executar um bloco de código enquanto uma condição for verdadeira. A sintaxe do loop while é a seguinte:

# while condição:
#     bloco de código
# Exemplo de uso do loop while para contar de 1 a 5:

contador = 1
while contador <= 5:
    print(contador)
    contador += 1


#EXEMPLO SEM REPETICAO
a = int(input("Digite um número: "))

a += 1
print(a)

a += 1
print(a)

#exemplo com repetição usando while para criar um menu de opções:
opcao = -1

while opcao != 0:
    opcao = int(input("Digite uma opção: \n[1] Opção 1 \n[2] Opção 2 \n[0] Sair "))
    
    if opcao == 1:
        print("Você escolheu a opção 1.")
        
    elif opcao == 2:
        print("Você escolheu a opção 2.")
        
    elif opcao == 0:
        print("Saindo do sistema...")
    else:
        print("Opção inválida. Tente novamente.")
        
else:
    print("Obrigada por usar o sistema.")

