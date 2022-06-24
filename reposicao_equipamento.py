def max_income(income, operational_cost, sale_value, machine_cost, n, n_max, t, t_max, dp, decisions):
    """
    Desafio da reposição de equipamento: uma empresa deve determinar uma política ótima de reposição de uma máquina com
    t anos de uso nos próximos n_max anos. Ao final do período, a máquina será vendida. Como dados de entrada,
    referentes a uma máquina com t anos de uso, são considerados: receita anual, custo operacional anual e valor de
    venda. Também é especificado o valor de compra de uma máquina nova (machine_cost). A empresa exige que uma máquina
    não pode passar de t_max anos de uso. Qual será a receita máxima da empresa?

    :param income: Receita de uma máquina com idade t
    :param operational_cost: Custo operacional de uma máquina com idade t
    :param sale_value: Valor de venda de uma máquina com idade t
    :param machine_cost: Custo de compra de uma máquina nova
    :param n: período atual
    :param n_max: período do projeto
    :param t: idade atual da máquina
    :param t_max: idade limite, se atingida, a máquina deve ser vendida
    :param dp: tabela com resultados
    :param decisions: decisões tomadas em cada ano
    :return: Receita máxima e decisões tomadas
    """

    # Condições de contorno
    if n == n_max:
        return sale_value[t], decisions

    # Não calcula estados repetidos
    if dp[n][t] is not None:
        return dp[n][t], decisions

    # Se máquina atingir sua idade máxima, deve ser substituída
    if t == t_max:

        # Receita máxima do próximo ano
        next_year_income1, decisions = max_income(income, operational_cost, sale_value, machine_cost, n + 1,
                                                  n_max, 0, t_max, dp, decisions)

        # Substituir máquina
        replace_machine = income[0] - operational_cost[0] + sale_value[t] - machine_cost + next_year_income1

        # Atualizando tabela
        dp[n][t] = replace_machine

        # Atualizando decisões
        decisions[n] = 'Substituir'

        return dp[n][t], decisions

    else:
        # Receita máxima do próximo ano
        next_year_income1, decisions = max_income(income, operational_cost, sale_value, machine_cost, n + 1,
                                                  n_max, 0, t_max, dp, decisions)

        # Substituir máquina
        replace_machine = income[0] - operational_cost[0] + sale_value[t] - machine_cost + next_year_income1

        # Receita do próximo ano
        next_year_income2, decisions = max_income(income, operational_cost, sale_value, machine_cost, n + 1, n_max,
                                                  t + 1, t_max, dp, decisions)

        # Manter máquina
        keep_machine = income[t + 1] - operational_cost[t + 1] + next_year_income2

        # Atualizando tabela
        if replace_machine == keep_machine:
            dp[n][t] = replace_machine
            decisions[n] = 'Substituir'
        else:
            dp[n][t] = max(replace_machine, keep_machine)
            # Atualizando decisões
            if replace_machine > keep_machine:
                decisions[n] = 'Substituir'
            if keep_machine > replace_machine:
                decisions[n] = 'Manter'

        return dp[n][t], decisions


if __name__ == "__main__":

    # Dados do projeto
    income = [20, 19, 18.5, 17.2, 15.5, 14, 12.2]
    operational_cost = [0.2, 0.6, 1.2, 1.5, 1.7, 1.8, 2.2]
    sale_value = [80, 60, 50, 30, 10, 5]
    machine_cost = 100
    t = 2
    t_max = 5
    n = 0
    n_max = 4
    decisions = [None] * (n_max)

    # Matriz dos pesos
    dp = [[None] * (t_max + 1) for _ in range(n_max + 1)]

    # Máxima receita líquida
    max_income, decisions = max_income(income, operational_cost, sale_value, machine_cost, n, n_max, t, t_max, dp,
                                       decisions)
    print("Máxima receita:", max_income * 1000, 'reais')
    print(decisions)
