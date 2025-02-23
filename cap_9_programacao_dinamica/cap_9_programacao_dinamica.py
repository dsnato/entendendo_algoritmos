def mochila_01(pesos, valores, capacidade):
    n = len(pesos)
    # Cria uma tabela DP (n+1) x (capacidade+1)
    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]

    # Preenche a tabela
    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if pesos[i - 1] > w:
                # Item não cabe: mantém o valor anterior
                dp[i][w] = dp[i - 1][w]
            else:
                # Escolhe a melhor opção: incluir ou não o item
                dp[i][w] = max(
                    dp[i - 1][w],  # Não inclui o item
                    dp[i - 1][w - pesos[i - 1]] + valores[i - 1]  # Inclui o item
                )

    return dp[n][capacidade]


# Exemplo de uso:
pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
capacidade = 5

print("Valor máximo possível:", mochila_01(pesos, valores, capacidade))  # Saída: 7