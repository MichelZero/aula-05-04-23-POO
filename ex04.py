# autores:
# Michel

# data: 05/04/2023  

# 4 - dado uma tabela de dados de chuva, crie um dicionário com os dados da tabela.
#
# precipitação de chuva
# jan fev mar
# 40  30  20

###############     1     #############
#print("jan\t fev\t mar")
#print("40 \t 30 \t 20")

###############     2     #############
print("precipitação de chuva")
print("----------------")
print("jan\t| fev\t| mar")
print("40 \t| 30 \t| 20")
print("----------------")

# dic = {chave: valor}

chuvas = {'jan': 40, 'fev': 30, 'mar': 20}

print(chuvas) # imprime: {'jan': 40, 'fev': 30, 'mar': 20}

###############     3     #############
# interação
for i in chuvas: # percorre o dicionário 
  print(i) # imprime as chaves do dicionário 
  
for chave in chuvas: # percorre o dicionário
  print(chave, ' : ', end='') # imprime as chaves do dicionário
  print(chuvas[chave]) # imprime os valores do dicionário

###############     4     #############
#
#chuvas = {'jan': 40, 'fev': 30, 'mar': 20}
#imprimir uma lista de chaves
print(chuvas.keys()) # imprime ['jan', 'fev', 'mar']

for chave in chuvas.keys(): # percorre o dicionário pegando as chaves
  print(chuvas[chave]) # imprime os valores do dicionário

###############     5     #############
#
#imprimir uma lista de valores
print(chuvas.values()) # imprime [40, 30, 20]

for valor in chuvas.values(): # percorre o dicionário pegando os valores
  print(valor) # imprime os valores do dicionário

###############     6     #############
#
# desempacotamento de dicionários
print(chuvas.items()) # imprime [('jan', 40), ('fev', 30), ('mar', 20)] 

for chave, valor in chuvas.items(): # percorre o dicionário pegando as chaves e os valores
  print(f"chave = {chave}, tem valor = {valor}") # imprime as chaves e os valores do dicionário

# algumas funções 
print(sum(chuvas.values())) # soma dos valores 
print(max(chuvas.values())) # máximo 
print(min(chuvas.values())) # mínimo 
print(len(chuvas))          #tamanho

print(chuvas.items()) # imprime [('jan', 40), ('fev', 30), ('mar', 20)]
print(chuvas.keys()) # imprime ['jan', 'fev', 'mar']
print(chuvas.values()) # imprime [40, 30, 20]

