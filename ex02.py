# autores:
# Michel

# data: 05/04/2023  

# Exercício 2: 
# obtenha a chave do valor 
# mínimo do seguinte dicionário
d1 = {
  'física': 82,
  'Matemática': 65,
  'historia': 75}

valor = d1.values() # retorna os valores do dicionário 
print(valor) # imprime os valores do dicionário 

t = min(d1.values()) # encontra o menor valor do dicionário 
print(t) # imprime o menor valor do dicionário
for i in d1: # percorre o dicionário 
     if(d1[i]==t):  # compara o valor do dicionário com o menor valor 
         # print(i)
         print(f"{i} ficou com média {t}") # imprime a chave do menor valor do dicionário 


# encontre o maior valor:
maiorValor = max(t)
print(f"o maior valor é: {t}")
# encontre a quantidade de elementos
quantElementos = len(t)
print(f"a quantidade de elementos é: {t}")
# encontre a média Global:
mediaGlobal = sum(t)/len(t)
print(f"a média Global é: {mediaGlobal}")
