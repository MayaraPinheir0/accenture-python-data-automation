python -c comand to run a Python script
python 01_syntax_and_variables.py
# Isso executará o script diretamente usando o interpretador Python. Certifique-se de que o arquivo "01_syntax_and_variables.py" esteja no diretório atual ou forneça o caminho correto para o arquivo.


python -m 01_syntax_and_variables
# Isso executará o script como um módulo, o que pode ser útil para determinadas instruções de importação.
# problemas de importação podem ocorrer se o script tentar importar outros módulos que não estão no mesmo diretório ou no caminho do Python.

python script.py
# Isso é a forma mais comum de executar um script Python. Certifique-se de que o script tenha permissões de execução e que o interpretador Python esteja corretamente instalado e configurado no seu sistema.

python3 script.py
# Em sistemas onde tanto Python 2 quanto Python 3 estão instalados, usar "python3" garante que você esteja executando o script com a versão correta do Python. Certifique-se de que o comando "python3" esteja disponível no seu sistema e que a versão do Python 3 esteja instalada.

python -c "import script"
# Isso executará o script como um módulo, mas não executará o código diretamente. Ele importará o módulo, o que pode ser útil para testar se o módulo pode ser importado corretamente. No entanto, se o script contiver código que deve ser executado quando importado, ele não será executado a menos que esteja dentro de um bloco "if __name__ == '__main__':". Certifique-se de que o script esteja no caminho do Python para que possa ser importado corretamente.

python  -m timeit -setup "import script"
# Isso executará o módulo "timeit" para medir o tempo de execução do código dentro