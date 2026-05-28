# Interpolação de Strings em Python
# A interpolação de strings é uma técnica que permite inserir valores de variáveis dentro de uma string de forma mais legível e conveniente. 
# Em Python, existem várias maneiras de realizar a interpolação de strings, incluindo o uso do operador de formatação %, o método format() e as f-strings.

########### FORMATACOES STRINGS

#old style de formatação de string usando o operador %

#%s string 
#%d inteiro
#%f float
#%x hexadecimal

# cuidado pois ele precisa está em ordem, ou seja, se tiver mais de um tipo de dado, ele precisa estar na mesma ordem do formato.

#exemplo de formatação de string usando o operador %:

nome = "joao" #%s
idade = 25 #%d
profissao = "programador" #%s
linguagem = "python" #%s

print("Meu nome é %s, tenho %d anos, sou %s e programo em %s." %(nome, idade, profissao, linguagem))
#--------------

#segundo exemplo
preco = 19.99 #%f
print("O preço do produto é %.2f." %preco)

#terceiro exemplo
nome = "maria" #%s
sobrenome = "silva" #%s
print("O nome completo é %s %s." %(nome, sobrenome))

#### METODO DE FORMATAÇÃO DE STRING COM O MÉTODO FORMAT()

#{} 
# é um marcador de posição que indica onde o valor deve ser inserido na string. O método format() é chamado na string e os valores a serem inseridos são passados como argumentos para o método. Os valores são inseridos na string na ordem em que aparecem nos argumentos do método format().

#exemplo

nome = "joao"
idade = 25
profissao = "programador"
linguagem = "python"

print("Meu nome é {}, tenho {} anos, sou {} e programo em {}.".format(nome, idade, profissao, linguagem))
# O método format() permite que você use chaves vazias {} como marcadores de posição, e os valores serão inseridos na ordem em que aparecem nos argumentos do método format(). 

print("-------")

print("Meu nome é {0}, tenho {1} anos, sou {2} e programo em {3}.".format(nome, idade, profissao, linguagem))

# O método format() também permite que você especifique a ordem dos argumentos usando índices numéricos dentro das chaves. 
# No exemplo acima, {0} se refere ao primeiro argumento (nome), {1} se refere ao segundo argumento (idade), {2} se refere ao terceiro argumento (profissao) e {3} se refere ao quarto argumento (linguagem).

#é util para evitar erros de ordem dos argumentos, especialmente quando a string contém muitos marcadores de posição ou quando os argumentos são passados em uma ordem diferente da que aparecem na string.

#outro modo metodo format
#passar argumentos de forma variada 
print("Meu nome é {nome}, tenho {idade} anos, sou {profissao} e programo em {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

#exemplo

# No exemplo abaixo, os valores são passados como um dicionário usando o operador **, e os marcadores de posição na string correspondem às chaves do dicionário.

pessoa = {
    "nome": "joao",
    "idade": 25,
    "profissao": "programador",
    "linguagem": "python"
}

print("Olá, meu nome é {nome}. Eu tenho {idade} anos e sou um {profissao} que programa em {linguagem}.".format(**pessoa))

#outro exemplo 

# Funciona, mas é má prática pois perde a semântica dos dados, ou seja, não sabemos qual valor corresponde a qual chave do dicionário, e isso pode levar a erros de formatação se a ordem dos valores no dicionário for diferente da ordem dos marcadores de posição na string.
print("Olá, meu nome é {}. Eu tenho {} anos e sou um {} que programa em {}.".format(*pessoa.values()))

#F STRING

nome = "joao"
idade = 25
print(f"Meu nome é {nome} e tenho {idade} anos.")




#comparacao

profissao = "programador"
linguagem = "python"

dados = {"name": "joao", "idade": 25, "profissao": "programador", "linguagem": "python"}

print("Eu sou {}, e programo em {}".format(profissao, linguagem))

print("Eu sou {0}, e programo em {1}". format(profissao, linguagem))

print(f"Eu sou {profissao}, e programo em {linguagem}")

print("Eu sou %s, e programo em %s" %(profissao, linguagem))

print("Eu sou {profissao}, e programo em {linguagem}".format(**dados))

#-------
idade = 25
nome = "joao"

print("Meu nome é {} e tenho {} anos.".format(nome, idade))

print("Meu nome é {0} e tenho {1} anos.".format(nome, idade))