# 3 - dado um dicionário com 3 disciplinas e sua respectiva nota 
# ex: {'algoritmos': 80, 'física': 90, 'matemática': 70}, 
# depois criar uma estrutura que encontre dentro do dicionário 
# qual foi a menor nota.

d1 = {'algoritmos':80 , 'Física':90, 'matemática':70}

''' 
min (iterável, * [, padrão = obj, chave = func]) -> valor
min (arg1, arg2, * args, * [, chave = func]) -> valor

Com um único argumento iterável, retorna seu menor item. 
o argumento padrão apenas de palavra-chave especifica um objeto a ser retornado se
o iterável fornecido está vazio.
Com dois ou mais argumentos, retorna o menor argumento '''


maior = max(d1) # retorna a chave do maior valor do dicionário 
print(maior) # imprime a chave do maior valor do dicionário

# outra forma de fazer o mesmo exercício
maior = max(d1, key=d1.get) # retorna a chave do maior valor do dicionário
menor = min(d1, key=d1.get) # retorna a chave do menor valor do dicionário
print(maior) # imprime a chave do maior valor do dicionário
print(menor) # imprime a chave do menor valor do dicionário