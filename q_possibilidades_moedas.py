def max_ways(coins, price):
    """
    Desafio do número de possibilidades de moedas: dados um vetor com valores de moedas e um valor alvo, é preciso
    descobrir o número de possibilidades possíveis spara atingir este valor com as moedas

    :param coins: vetor com valores das moedas
    :param price: preço alvo
    :return: número de possibilidades
    """

    # Quantidade de moedas
    n = len(coins)

    # Tabela de estados
    dp = [[None] * (price + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1
    for j in range(price + 1):
        dp[0][j] = 0

    # Uma moeda só pode ser selecionada se seu valor é menor que o preço
    for i in range(1, n + 1):
        for j in range(1, price + 1):
            if coins[i - 1] <= j:
                dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][price]


if __name__ == '__main__':
    # Informações do desafio
    coins = [1, 2, 3]
    price = 5
    ch = max_ways(coins, price)

    print('Número de possibilidades: ', ch)
