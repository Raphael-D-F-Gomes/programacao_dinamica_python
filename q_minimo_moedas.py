import sys


def min_coins(coins, price):
    """
    Desafio da quantidade mínima de moedas: dados um vetor com valores de moedas e um valor alvo, é preciso descobrir o
    número mínimo de moedas que atingirão este valor.

    :param coins: lista de moedas
    :param price: valor alvo
    :return: número mínimo de moedas
    """

    # Número de moedas
    n = len(coins)

    # Tabela de estados
    dp = [[None]*(price+1) for _ in range(n+1)]

    for j in range(price + 1):
        dp[0][j] = sys.maxsize - 1
    for i in range(n + 1):
        dp[i][0] = 0

    # Uma moeda só pode ser selecionada se seu valor é menor que o preço
    for i in range(1, n + 1):
        for j in range(1, price + 1):
            if coins[i - 1] <= j:
                dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j-coins[i-1]])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][price]


if __name__ == '__main__':
    # Informações do desafio
    coins = [1, 4, 6]
    price = 8
    ch = min_coins(coins, price)
    print(f'Número mínimo de moedas: {ch}')
