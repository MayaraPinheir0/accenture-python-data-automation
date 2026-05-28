#verifica se um objeto esta presente em uma sequencia, como uma string, lista ou tupla

#variaveis de exemplo
curso = "Curso de Python"
frutas = ["banana", "maça", "uva"]
saques = (100, 200, 300)

#vamos verificar se a string "Python" esta presente na string "Curso de Python". 

#para isso usamos o operador "in", que retorna True se a string "Python" estiver presente na string "Curso de Python" e False caso contrário.

print("Python" in curso) 
#true, pois a string "Python" esta presente na string "Curso de Python"

#vamos verificar se a string "Java" esta presente na string "Curso de Python".
print("Java" in curso)
#false, pois a string "Java" nao esta presente na string "Curso de Python"

print("--- lista de frutas ---")

print("laranja"in frutas)
#false, pois a string "laranja" nao esta presente na lista "frutas"

print("maça"in frutas)
#true, pois a string "maça" esta presente na lista "frutas"

print("limao" in frutas)
#false, pois a string "limao" nao esta presente na lista "frutas"