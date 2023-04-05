# autores:
# michel

# data: 05/04/2023  

#
#Exercício 1: duas listas para convertê-lo no dicionário

L1 = ['dez', 'vinte', 'trinta'] # lista de chaves 
valores = [10, 20, 30] # lista de valores
 
copact1 = zip(L1, valores) # zip retorna um objeto zip
compactDic = dict(copact1) # converte o objeto zip em dicionário
print(compactDic) # imprime o dicionário


# outra forma de fazer o mesmo exercício 
zipDic = dict(zip(L1, valores)) # converte o objeto zip em dicionário
print(zipDic) # imprime o dicionário