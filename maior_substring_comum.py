def longest_commom_subsequence(string1, string2, l1, l2):
    """
    Desafio da maior subfrase em comum: dadas duas frases, é preciso descobrir qual será a maior subfrase em comum entre
    estas, qu estão na mesma ordem. A saída deverá ser subfrases iguais que podem ser obtidas excluindo elementos das
    duas frases.

    :param string1: frase 1
    :param string2: frase 2
    :param l1: tamanho da frase 1
    :param l2: tamanho da frase 2
    :return: a maior subfrase possível
    """

    # Tabela de estados
    dp = [[None] * (l2 + 1) for _ in range(l1 + 1)]

    # Subfrase
    x = ''
    subsentence = ''

    for i in range(l1 + 1):
        dp[i][0] = 0

    for j in range(l2 + 1):
        dp[0][j] = 0

    # É feita uma varredura de todas letras, se uma letra coincide em ambas frases, é somado um com o estado anterior
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]

                # Recuperando subfrase
                if dp[i - 1][j - 1] != 0 or x == '':
                    x += string1[i - 1]
                elif dp[i - 1][j - 1] == 0:
                    if len(x) > len(subsentence):
                        subsentence = x
                    x = string1[i - 1]
            else:
                dp[i][j] = 0

    # Recuperando subfrase
    if len(x) > len(subsentence):
        subsentence = x

    # Recuperando número de letras da subfrase
    maximum = -9999
    for i in dp:
        maximum = max(maximum, max(i))

    return maximum, subsentence


if __name__ == '__main__':
    # Frases
    string1 = 'aabcdaf'
    string2 = 'gbcdf'
    maxlen, subsentence = longest_commom_subsequence(string1, string2, len(string1), len(string2))

    print('Quantidade de letras da subfrase  =', maxlen, f'\nsubfrase: {subsentence}')
