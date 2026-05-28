#fatiamento de string

#exemplo de fatiamento de string
texto = "Hello, World!"
print(texto[0]) #H
print(texto[7]) #W
print(texto[-1]) #! -> último caractere da string
print(texto[0:5]) #Hello -> do índice 0 até o índice 4 (5 é exclusivo)
print(texto[7:12]) #World -> do índice 7 até o índice 11 (12 é exclusivo)
print(texto[:5]) #Hello -> do início da string até o índice 4 (5 é exclusivo)
print(texto[7:]) #World! -> do índice 7 até o final da string
print(texto[::2]) #Hlo ol! -> do início ao fim, pulando de 2 em 2 caracteres
print(texto[::-1]) #!dlroW ,olleH -> string invertida

# O fatiamento de string é uma técnica que permite extrair partes de uma string usando índices.

# A sintaxe para fatiamento é: string[inicio:fim:passo],

# onde inicio é o índice inicial (inclusivo), fim é o índice final (exclusivo) e passo é o intervalo entre os índices.

arg = "Mayara Costa"

print(arg[0])
print(arg[1])
print(arg[9])
print(arg[-1])
print(arg[0:5])
print(arg[4:])
print(arg[:5])
print(arg[::2])
print(arg[::-1])