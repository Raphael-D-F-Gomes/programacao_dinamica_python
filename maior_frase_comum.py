from builtins import range


def largest_commom_sentence(s1, s2):
    """
    Desafio da maior frase em comum: dadas duas strings, é preciso descobrir a dimensão da maior frase que se repete nas
    duas strings.
    :param s1: string 1
    :param s2: string 2
    :return:
    """
    # Dimensões das strings
    l1 = len(s1)
    l2 = len(s2)

    # Tabela de estados
    dp = [[None] * (l2 + 1) for _ in range(l1 + 1)]

    for i in range(l1 + 1):
        dp[i][0] = 0
    for j in range(l2 + 1):
        dp[0][j] = 0

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return dp[l1][l2]


if __name__ == '__main__':
    s1 = 'abbacdcba'
    s2 = 'bcdbbcaa'
    tamanho_max = largest_commom_sentence(s1, s2)
    print("Tamanho da maior frase em comum = ", tamanho_max)
