def sc_rate(energy, rate):
    bool_rate = energy < rate[0]
    p = len(rate[0])
    alpha = (rate[1][p - 1] - rate[1][p - 2]) / (rate[0][p - 1] - rate[0][p - 2])
    beta = rate[1][p - 1] - alpha * rate[0][p - 1]
    for j in range(1, p):
        if bool_rate[j]:
            alpha = (rate[1][j] - rate[1][j - 1]) / (rate[0][j] - rate[0][j - 1])
            beta = rate[1][j - 1] - alpha * rate[0][j - 1]
            break
    return alpha * energy + beta
