def subset_sum(arr, target):
    """
    Desafio da soma de subconjuntos: dados um vetor e um valor alvo, é preciso descobrir se existe algum subconjunto
    deste vetor, cujo a soma é igual ao valor alvo.

    :param arr: vetor dado
    :param target: target
    :return: Existência de tal subconjunto
    """

    # Número de elementos no conjunto
    n = len(arr)

    # Tabela de estados: colunas: [0, target], linhas: elementos do conjunto
    dp = [[None] * (target + 1) for _ in range(n + 1)]
    for i in range(target + 1):
        dp[0][i] = False
    for j in range(n + 1):
        dp[j][0] = True

    # Um elemento é escolhido apenas se a soma for menor que o arr[i], ao contrário não será incluído
    for i in range(1, n + 1):
        for j in range(target + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    # Recuperando subset
    subset = set()
    i = 0
    # Obtendo subconjunto
    if dp[n][target]:
        while target > 0:
            dp_list = [dp[c][target] for c in range(n + 1)]
            x = dp_list.index(True)
            subset.add(arr[x - 1])
            target = target - arr[x - 1]
            i += 1

    return dp[n][target], subset


if __name__ == '__main__':

    # Dados do desafio
    arr = [0, 3, 2, 7, 1]
    target = 6
    exists, subset = subset_sum(arr, target)

    # Resposta
    print(f'O subconjunto com a soma que leva ao target existe: {exists}')
    print(subset)
