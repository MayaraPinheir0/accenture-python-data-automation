profissao = "programador"
linguagem = "python"

dados = {"name": "joao", "idade": 25, "profissao": "programador", "linguagem": "python"}

print("Eu sou {}, e programo em {}".format(profissao, linguagem))

print("Eu sou {0}, e programo em {1}". format(profissao, linguagem))

print(f"Eu sou {profissao}, e programo em {linguagem}")

print("Eu sou %s, e programo em %s" %(profissao, linguagem))

print("Eu sou {profissao}, e programo em {linguagem}".format(**dados))