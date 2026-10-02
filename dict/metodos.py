pessoa = {
    'nome': 'Luiz',
    'sobrenome': 'Costa',
}

print(len(pessoa)) # len - retorna a quantidade de CHAVES

print(pessoa.keys())
print(list(pessoa.keys())) # retorna uma lista das chaves
# tambem é possível iterar sobre as chaves com for
for chave in pessoa.keys(): 
    print(chave)

print('-' * 35)
# acessar valores das chaves
print(list(pessoa.values()))
for valor in pessoa.values():
    print(valor)

print('-' * 35)
# items

print(list(pessoa.items()))
# Possivel iterar sobre a chave e valor, similar ao .enumerate
for chave, valor in pessoa.items():
    print(chave, valor)