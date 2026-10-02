pessoa = {}
chave = 'nome'

# manipular chaves
pessoa[chave] = 'Luiz Guilherme'
pessoa['sobrenome'] = 'Caetano' # cria chave 'sobrenome' e atribui a ela o valor

print(pessoa)
print(pessoa['nome'])

del pessoa['sobrenome'] # deletar chave

# .get() - retorna None caso não exista
print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('Não existe')