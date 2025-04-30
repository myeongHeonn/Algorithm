def solution(players, m, k):
    answer = 0
    server = []

    for player_num in players:
        need_server = player_num // m
        now_server = len(server)

        if now_server < need_server:
            for _ in range(need_server - now_server):
                server.append(k)
                answer += 1

        if server:
            for i in range(len(server)):
                server[i] = server[i] - 1

        while 0 in server:
            server.remove(0)

    return answer