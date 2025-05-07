def solution(alp, cop, problems):
    max_alp_req = max(p[0] for p in problems)
    max_cop_req = max(p[1] for p in problems)

    alp = min(alp, max_alp_req)
    cop = min(cop, max_cop_req)

    dp = [[float("INF")] * (max_cop_req + 2) for _ in range(max_alp_req + 2)]
    dp[alp][cop] = 0

    for i in range(alp, max_alp_req + 1):
        for j in range(cop, max_cop_req + 1):
            ni = min(i + 1, max_alp_req)
            dp[ni][j] = min(dp[ni][j], dp[i][j] + 1)

            nj = min(j + 1, max_cop_req)
            dp[i][nj] = min(dp[i][nj], dp[i][j] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    ni = min(max_alp_req, i + alp_rwd)
                    nj = min(max_cop_req, j + cop_rwd)
                    dp[ni][nj] = min(dp[ni][nj], dp[i][j] + cost)

    return dp[max_alp_req][max_cop_req]