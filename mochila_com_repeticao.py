def max_profit(capacity, n, weight_list, price_list, dp, items):
    """
    Problema do navio: um navio com capacidade máxima (capacity) deve ser usado para transporte de ítens. Existem n
    tipos de ítens, cada um possui um peso e um lucro. Qual será o lucro máximo com este transporte, sendo que é
    possível levar mais de uma quantidade de cada ítem.

    :param capacity: capacidade da mochila
    :param n: número de items
    :param weight_list: lista de pesos
    :param price_list: lista de preços
    :param dp: matriz em que as colunas são os pesos dos items e as linhas são os pesos de 0 até o peso total
    :param items: ítens transportados
    :return: Lucro ótimo e ítens transportados
    """

    # Condição de contorno
    if n == 0 or capacity == 0:
        return 0, items

    # Se já existe esta solução, não é necessário calcular de novo
    if dp[n][capacity] is not None:
        return dp[n][capacity], items

    # Se o peso for menor que a capacidade, é possível levar o ítem
    if weight_list[n - 1] <= capacity:

        # Número de items n que cabem no navio
        x = int(capacity / weight_list[n - 1])

        # Lista com possibilidades de levar multiplos items n
        take_item = [None] * x

        # Leva o item n
        for i in range(1, x + 1):

            # Cálculo do último item
            last_item, items = max_profit(capacity - i * weight_list[n - 1], n - 1, weight_list, price_list, dp, items)

            take_item[i - 1] = price_list[n - 1] * i + last_item

        # Coletando o index do valor máximo
        max_index = take_item.index(max(take_item))

        # Não leva o item n
        dont_take_item, items = max_profit(capacity, n - 1, weight_list, price_list, dp, items)

        # Verifica o lucro máximo levando ou não levando o item n
        dp[n][capacity] = max(max(take_item), dont_take_item)

        # Atualizando informações de transporte
        if max(take_item) > dont_take_item:
            items[n - 1] = f'Levar {max_index + 1}'
        if max(take_item) < dont_take_item:
            items[n - 1] = 'Não levar'

        return dp[n][capacity], items

    else:

        # Se o item não cabe na mochila, não é possível levar este item
        dp[n][capacity], items = max_profit(capacity, n - 1, weight_list, price_list, dp, items)

        # Atualizando informações de transporte
        items[n - 1] = 'Não levar'

        return dp[n][capacity], items


if __name__ == '__main__':
    # Dados dos items e da mochila
    capacity = 4
    weight_list = [2, 3, 1]
    price_list = [31, 47, 14]
    n = len(price_list)
    dp = [[None] * (capacity + 1) for _ in range(n + 1)]

    # Matriz dos pesos
    items = [None] * n

    # Chamando função para obter o lucro máximo
    max_profit, items = max_profit(capacity, n, weight_list, price_list, dp, items)

    print('Lucro máximo: ', max_profit)
    print(items)
