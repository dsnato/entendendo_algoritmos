infinito = float('inf')

# Definindo o grafo
grafo = {
    'inicio': {'a': 6, 'b': 2},
    'a': {'fim': 1},
    'b': {'a': 3, 'fim': 5},
    'fim': {}
}

custos = {'a': 6, 'b': 2, 'fim': infinito}
pais = {'a': 'inicio', 'b': 'inicio', 'fim': None}
processados = []

def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float('inf')
    nodo_custo_mais_baixo = None
    for nodo in custos:
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

nodo = ache_no_custo_mais_baixo(custos)
while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos:
        novo_custo = custo + vizinhos[n]
        if n not in custos or novo_custo < custos[n]:
            custos[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo)
    nodo = ache_no_custo_mais_baixo(custos)

print("\nResultados do Algoritmo de Dijkstra:")
print("Custos finais aos nós:", custos)
print("Relação de pais:", pais)

# Reconstrução do caminho do fim até o início
if custos['fim'] != infinito:
    caminho = []
    nodo = 'fim'

    # Reconstrói o caminho de trás para frente
    while nodo is not None:
        caminho.append(nodo)
        nodo = pais.get(nodo)  # Usamos get() para evitar KeyError

    # Inverte o caminho para mostrar do início ao fim
    caminho.reverse()

    print("\nCaminho mais curto até 'fim':")
    print(' -> '.join(caminho))
    print("Custo total:", custos['fim'])
else:
    print("\nO nó 'fim' não é alcançável a partir do 'inicio'.")