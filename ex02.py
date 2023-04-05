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

valor = d1.values()
print(valor)

t=min(d1.values())
print(t)
for i in d1:
     if(d1[i]==t):
         # print(i)
         print(f"{i} ficou com média {t}")


# encontre o maior valor:
maiorValor = max(t)
print(f"o maior valor é: {t}")
# encontre a quantidade de elementos
quantElementos = len(t)
print(f"a quantidade de elementos é: {t}")
# encontre a média Global:
mediaGlobal = sum(t)/len(t)
print(f"a média Global é: {mediaGlobal}")
