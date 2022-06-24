def longest_repeating_subsequence(s):
    """
    Desafio da maior subfrase repetida: dada uma string, é precisco encontrar a maior subfrase que se repete em ordem em
    uma string. Exemplo: a maior subfrase que se repete na string "aabebcdd" é "abd".
    :param s: string
    :return: Dimensão da maior frase repetida
    """
    # Dimensão da string
    n = len(s)

    # Cópia da string
    s1 = s

    # Tabela de estados
    dp = [[0]*(n+1) for _ in range(n+1)]

    # Varredura para encontrar letras que se repetem
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Se letras coincidem, o estado i, j será o estado anterior mais 1
            if s[i - 1] == s1[j - 1] and i != j:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][n]


if __name__ == '__main__':
    s = 'aabebcdd'
    length = longest_repeating_subsequence(s)
    print(f'Quantidade de letras da maior subfrase repetida : {str(length)}')
