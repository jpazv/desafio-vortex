t = int(input('Digite quanto tempo resta no relógio: '))
q = int(input('Digite a quantidade de jogadores no treino: '))
x = int(input('Digite quanto tempo os jogadores correrão: '))

quantidade_de_passes = q - 1
passes_totais = 0
segundo = 1

if 2 <= x <= 5 and 0 < t <= 24 and 0 < x <= q - 1:
    for i in range(t):
        passes_totais += quantidade_de_passes
        print(f'No {segundo}º segundo, a quantidade de passes possíveis é: {quantidade_de_passes}')
        if quantidade_de_passes != (q - x):
            quantidade_de_passes -= 1
        segundo += 1

    print(f'Ao final do treino, a quantidade de passes totais foi de {passes_totais}')
else:
    print('Esse treino infelizmente não atende às condições necessárias...')
