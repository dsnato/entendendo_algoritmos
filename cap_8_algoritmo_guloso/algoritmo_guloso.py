# Conjunto de estados que precisam ser cobertos
estados_abranger = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}

# Dicionário de estações e os estados que cada uma cobre
estacoes = {
    'kum': {'id', 'nv', 'ut'},
    'kdois': {'wa', 'id', 'mt'},
    'ktres': {'or', 'nv', 'ca'},
    'kquatro': {'nv', 'ut'},
    'kcinco': {'ca', 'az'}
}

# Conjunto para armazenar as estações selecionadas
estacoes_finais = set()

while estados_abranger:
    melhor_estacao = None
    estados_cobertos = set()

    # Encontrar a estação que cobre o maior número de estados restantes
    for estacao, estados in estacoes.items():
        cobertos = estados_abranger & estados
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos

    # Se não encontrar mais estações válidas, interromper
    if melhor_estacao is None:
        break

    # Atualizar o conjunto de estados restantes e adicionar a melhor estação
    estados_abranger -= estados_cobertos
    estacoes_finais.add(melhor_estacao)

print("Estações selecionadas:", estacoes_finais)
