def equal_subsets(arr, target):
    """
    Desafio da partição de conjuntos: dado vetor, é preciso verificar se é possível dividir este vetor em subconjuntos,
    cujo a soma de a,bos são iguais

    :param arr: vetor que representa o conjunto
    :param target: valor alvo
    :return: Existência da partição e subconjuntos
    """

    # Número de elementos no conjunto
    n = len(arr)

    # Tabela de estados
    dp = [[None] * (target + 1) for _ in range(n + 1)]

    for i in range(target + 1):
        dp[0][i] = False
    for j in range(n + 1):
        dp[j][0] = True

    for i in range(1, n + 1):
        for j in range(target + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    # Recuperando subconjunto 1
    subset1 = []
    i = 0
    # Obtendo subconjunto
    if dp[n][target]:
        while target > 0:
            dp_list = [dp[c][target] for c in range(n + 1)]
            x = dp_list.index(True)
            subset1.append(arr[x - 1])
            target = target - arr[x - 1]
            i += 1

    # Recuperando subconjunto 2
    subset2 = arr
    for x in subset1:
        subset2.remove(x)

    return dp[n][target], [subset1, subset2]


def is_possible(arr):
    # Se arr tem soma P e dois subconjuntos têm soma S então S+S=P. Então é preciso encontrar
    # um subconjunto com soma  P // 2 e o outro subconjuntos terá a mesma soma.
    p = sum(arr)
    s = p // 2

    return (equal_subsets(arr, s))


if __name__ == '__main__':

    # Conjunto
    arr = [3, 1, 1, 2, 2, 1]

    # Um conjunto pode ser dividido em dois subconjuntos com somatório iguais se o somatório deste conjunto for par
    if sum(arr) % 2:
        print('Não é possível formar dois subconjuntos com somatórios iguais')
    else:
        boolean, subsets = is_possible(arr)
        if boolean:
            print('Divisão em subconjuntos é possível!')
            print(subsets)
        else:
            print('Divisão em subconjuntos não é possível!')
