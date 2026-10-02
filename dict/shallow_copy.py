import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0,1,2]
}

# # SHALLOW COPY 
# print('SHALLOW COPY')
# d2 = d1.copy() # copia somente os dados imutáveis. Uma lista por exemplo, apontaria para a mesma lista os dois dicionarios

# d2['c1'] = 1000 # vai alterar o valor de c2 somente no dict 2
# d2['l1'][1] = 999 # altera o valor de l1 no indice 1 nas DUAS listas
# print(d1)
# print(d2)
# print('=' * 35)

print('\nDEEP COPY')

d2 = copy.deepcopy(d1)

d2['c1'] = 1000 # vai alterar o valor de c2 somente no dict 2
d2['l1'][1] = 999 # altera o valor de l1 no indice 1 SOMENTE na lista do dict indicado
print(d1)
print(d2)