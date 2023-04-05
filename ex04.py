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

print(chuvas)

###############     3     #############
# interação
for i in chuvas:
  print(i)
  
for chave in chuvas:
  print(chave, ' : ', end='')
  print(chuvas[chave])

###############     4     #############
#
#chuvas = {'jan': 40, 'fev': 30, 'mar': 20}
#imprimir uma lista de chaves
print(chuvas.keys()) # ['jan', 'fev', 'mar']

for chave in chuvas.keys():
  print(chuvas[chave]) # 40 30 20

###############     5     #############
#
#imprimir uma lista de valores
print(chuvas.values())

for valor in chuvas.values():
  print(valor)

###############     6     #############
#
# desempacotamento de dicionários
print(chuvas.items())

for chave, valor in chuvas.items():
  print(f"chave = {chave}, tem valor = {valor}")

# algumas funções 
print(sum(chuvas.values())) # soma
print(max(chuvas.values())) # maximo
print(min(chuvas.values())) # minimo
print(len(chuvas))          #tamanho

print(chuvas.items())
print(chuvas.keys())
print(chuvas.values())



####  abaixo revisão de DIC para a turma de POO em 


#
# precipitação de chuvas 
# set out nov
# 10  20  30
#
print("precipitação de chuvas")
print('-'*22)
print("set\t| out\t| nov")
print("10\t| 20\t| 40")
print('-'*22)
#dicionário
chuvas = {'set':10,'out':21,'nov':30}
#          set      out      nov     # dict_keys(['set', 'out', 'nov'])
print(chuvas, "-> original")

''' lista = ['a','b','c']
#         0   1   2
#        -3  -2  -1

tupla = ('a','b','c')
#         0   1   2
print(tupla[-1]) '''

# interação
''' for chave in chuvas: # *3
  print(chuvas, '->',chave)  '''

for chave in chuvas: 
  print(chave, '->',chuvas[chave])

print(chuvas.keys())
print(chuvas.values())
print(chuvas.items())

for i in chuvas.keys(): # dict_keys(['set', 'out', 'nov'])
  print(chuvas[i], ' -> ',i) 

for i in chuvas.values(): # dict_values([10, 20, 30])
  print(i, end=' ')  # 10 20 30 
print()

for i,j in chuvas.items(): # dict_items([('set', 10), ('out', 20), ('nov', 30)])
  print(f"chave = {i}, e valor = {j}")
  if not (j % 2 != 0):
    print(i, "é par")
  else:
    print(i, "é impar")



# algumas funções 
print(sum(chuvas.values())) # soma
print(max(chuvas.values())) # maximo
print(min(chuvas.values())) # minimo
print(len(chuvas))          #tamanho
