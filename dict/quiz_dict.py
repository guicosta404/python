perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Alternativas': ['1', '2', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Alternativas': ['45', '25', '35', '15', '10'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 7+3?',
        'Alternativas': ['23', '18', '13', '11', '10'],
        'Resposta': '10',
    }
]

acertos = 0

for pergunta in perguntas:
    print('Pergunta: ', pergunta['Pergunta'])

    alternativas = pergunta['Alternativas']
    for i, alternativa in enumerate(alternativas):
        print(f'{i}) {alternativa}.')

    resp = (input('Digite sua resposta: '))

    acertou = False
    escolha_int = None
    qtd_opcoes = len(alternativas)
    if resp.isdigit():
        escolha_int = int(resp)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int <= qtd_opcoes:
            if alternativas[escolha_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        print('Acertou')
        acertos += 1
    else:
        print('Errou')
    
print(f'FIM. Você acertou {acertos} questões.')
    