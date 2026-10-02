pessoa = {
    'nome': 'Luiz',
    'sobrenome': 'Costa',
}

# setdefault - adiciona valor se a chave não existe

pessoa.setdefault('idade', 26)
print(pessoa['idade'])