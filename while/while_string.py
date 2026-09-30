nome = 'Luiz Guilherme'
novo_nome = ''
indice = 0

while indice < len(nome):
    novo_nome += f'*{nome[indice]}'

    indice += 1
novo_nome += '*'
print(novo_nome)