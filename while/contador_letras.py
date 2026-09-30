frase = 'O python é uma linguagem de programação criado por Guido.'

i = 0
letra_mais_apareceu = ''
letra_qtd_mais_apareceu = 0

while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == ' ':
        i += 1    
        continue
    
    letra_qtd_mais_apareceu_atual = frase.count(letra_atual)

    if letra_qtd_mais_apareceu < letra_qtd_mais_apareceu_atual:
        letra_qtd_mais_apareceu = letra_qtd_mais_apareceu_atual
        letra_mais_apareceu = letra_atual
 
    i += 1

print(f'A letra que mais apareceu foi "{letra_mais_apareceu}": {letra_qtd_mais_apareceu} vezes.')