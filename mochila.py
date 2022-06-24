def max_profit(capacity, n, weight_list, price_list, dp):
    """
    Problema da mochila: um vendedor possui um mochila com capacidade w, esta mochila será usada para carregar n items,
    cada um com um lucro de venda e um peso. Qual será a melhor configuração para que o vendedor obtenha o maior lucro
    possível?

    :param capacity: capacidade da mochila
    :param n: número de items
    :param weight_list: lista de pesos
    :param price_list: lista de preços
    :param dp: matriz em que as colunas são os pesos dos items e as linhas são os pesos de 0 até o peso total
    :return: Lucro ótimo
    """

    # Condição de contorno
    if n == 0 or capacity == 0:
        return 0

    # Problema resolvido, retorna o lucro máximo.
    if dp[n][capacity] is not None:
        return dp[n][capacity]

    if weight_list[n - 1] <= capacity:

        # Leva o item n
        take_item = price_list[n - 1] + max_profit(capacity - weight_list[n - 1], n - 1, weight_list, price_list, dp)

        # Não leva o item n
        dont_take_item = max_profit(capacity, n - 1, weight_list, price_list, dp)

        # Verifica o lucro máximo levando o não levando o item n
        dp[n][capacity] = max(take_item, dont_take_item)

        return dp[n][capacity]

    else:
        # Se o item não cabe na mochila, não é possível levar este item
        dp[n][capacity] = max_profit(capacity, n - 1, weight_list, price_list, dp)

        return dp[n][capacity]


if __name__ == '__main__':
    # Dados dos items e da mochila
    capacity = 10
    weight_list = [1, 2, 5, 6, 7]
    price_list = [1, 6, 18, 22, 28]
    n = len(price_list)

    # Matriz dos pesos
    dp = [[None] * (capacity + 1) for _ in range(n + 1)]

    # Chamando função para obter o lucro máximo
    max_profit = max_profit(capacity, n, weight_list, price_list, dp)
    print('Lucro máximo: ', max_profit)
