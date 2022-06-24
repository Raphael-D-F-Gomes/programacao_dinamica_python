def largest_palindromic(s):
    """
    Desafio do palíndromo: dada uma string, é necessário encontrar o maior palíndromo formado por sequência de letras
    desta string
    :param s: string
    :return: dimensão do máximo palíndromo
    """

    # string invertida
    s_rev = s[::-1]

    # Dimensões das strings
    l1 = len(s)
    l2 = len(s_rev)

    # Tabela de estados
    dp = [[None] * (l2 + 1) for _ in range(l1 + 1)]

    for i in range(l1+1):
        dp[i][0] = 0
    for j in range(l2+1):
        dp[0][j] = 0

    # Comparando a string e sua string invertida, se letras se coincidirem o estado será a o estado anterior mais 1
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if s[i - 1] == s_rev[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    # dp[l1][l2] contém a dimensão do maior palíndromo possível
    return dp[l1][l2]


if __name__ == '__main__':
    # String
    s = 'agbdba'
    length = largest_palindromic(s)

    print(f'Length of the largest Palindromic Subsequence is {length}')
