#BREAK
# A instrução break é usada para sair de um loop antes que a condição do loop seja satisfeita. 
# Ela é útil quando queremos interromper a execução de um loop com base em uma condição específica, sem precisar esperar que o loop termine naturalmente.

#EXEMPLO ANTERIOR DO WHILE COM BREAK
opcao = -1

while opcao != 0:
    opcao = int(input("Digite uma opção: \n[1] Opção 1 \n[2] Opção 2 \n[0] Sair "))
    
    if opcao == 10:
        break
    print(f"Você escolheu a opção {opcao}.")
    

#
while True:
    numero = int(input("Digite um número: "))
    
    if numero == 10:
        print("Saindo do loop...")
        break
    
    
# A sintaxe da instrução break é a seguinte:   
# break
# Quando a instrução break é executada dentro de um loop, o controle do programa é transferido para a primeira linha de código após o bloco do loop.
# Exemplo de uso da instrução break para sair de um loop while quando um número específico é encontrado:
while True:
    numero = int(input("Digite um número (0 para sair): "))
    
    if numero == 0:
        print("Saindo do loop...")
        break
    else:
        print(f"Você digitou o número {numero}.")
        
        
#CONTINUE
# A instrução continue é usada para pular a iteração atual de um loop e passar para a próxima iteração. Ela é útil quando queremos ignorar certas condições dentro de um loop, mas ainda queremos continuar a execução do loop para as próximas iterações.
# A sintaxe da instrução continue é a seguinte:

# continue

# Quando a instrução continue é executada dentro de um loop, o controle do programa é transferido para a próxima iteração do loop, ignorando o restante do código dentro do bloco do loop para a iteração atual.

# Exemplo de uso da instrução continue para pular a iteração atual de um loop for quando um número específico é encontrado:

for i in range(1, 11):
    if i == 5:
        continue
    print(i)
    
# Neste exemplo, quando o número 5 é encontrado, a instrução continue é executada, o que faz com que o loop pule a iteração atual e continue com a próxima iteração. Portanto, o número 5 não será impresso na saída, mas os outros números de 1 a 10 serão impressos normalmente.

#