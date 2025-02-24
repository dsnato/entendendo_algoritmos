import numpy as np
from collections import Counter

# Criar um conjunto de dados de exemplo
# Formato: [feature1, feature2, classe]
dados_treinamento = np.array([
    [1, 2, 0],
    [2, 3, 0],
    [3, 4, 1],
    [4, 5, 1],
    [5, 6, 1],
    [6, 5, 0]
])

# Separar features e rótulos
X_treino = dados_treinamento[:, :2]  # Features
y_treino = dados_treinamento[:, 2]   # Classes

# Novo ponto a ser classificado
novo_ponto = np.array([3, 4])

# Definir o valor de K (número de vizinhos)
K = 3

# 1. Calcular distâncias entre o novo ponto e todos os pontos do treinamento
distancias = []
for i, ponto in enumerate(X_treino):
    distancia = np.sqrt(np.sum((novo_ponto - ponto)**2))  # Distância Euclidiana
    distancias.append((i, distancia))

# 2. Ordenar as distâncias e selecionar os K vizinhos mais próximos
distancias_ordenadas = sorted(distancias, key=lambda x: x[1])
vizinhos_proximos = distancias_ordenadas[:K]

# 3. Coletar as classes dos vizinhos selecionados
classes_vizinhos = []
for vizinho in vizinhos_proximos:
    indice = vizinho[0]
    classes_vizinhos.append(y_treino[indice])

# 4. Realizar votação para determinar a classe predominante
contagem = Counter(classes_vizinhos)
classe_predita = contagem.most_common(1)[0][0]

# Exibir resultados
print("Distancias calculadas:")
for i, dist in distancias:
    print(f"Ponto {i+1}: {X_treino[i]} → Distância: {dist:.2f}")

print("\nK vizinhos mais próximos:")
for vizinho in vizinhos_proximos:
    print(f"Ponto {vizinho[0]+1}: {X_treino[vizinho[0]]} → Distância: {vizinho[1]:.2f}")

print(f"\nClasses dos vizinhos: {classes_vizinhos}")
print(f"Classe predita para o novo ponto: {classe_predita}")
