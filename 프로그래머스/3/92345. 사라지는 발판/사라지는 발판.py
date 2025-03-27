def solution(board, aloc, bloc):
    ROW, COL = len(board), len(board[0])
    DR, DC = [-1, 0, 1, 0], [0, 1, 0, -1]

    def is_valid_pos(r, c):
        return 0 <= r < ROW and 0 <= c < COL

    def dfs(alpha_pos, beta_pos, visited, step):
        # 현재 플레이어의 위치와 이동 가능한지 여부,
        # 상대 플레이어가 이긴 경우를 저장하는 변수
        r, c = alpha_pos if step % 2 == 0 else beta_pos
        can_move = False
        is_opponent_winner = True

        win_steps, lose_steps = [], []

        for i in range(4):
            nr, nc = r + DR[i], c + DC[i]
            if is_valid_pos(nr, nc) and (nr, nc) not in visited and board[nr][nc]:
                can_move =True
                # 두 플레이어의 위치가 같으면 A 플레이어가 이긴 것이므로
                # True와 step + 1을 반환
                if alpha_pos == beta_pos:
                    return True, step + 1

                # 재귀적으로 호출하여 이긴 여부와 남은 턴 수를 가져오기
                win, steps_left = (
                    dfs([nr, nc], beta_pos, visited | {(r, c)}, step + 1)
                    if step % 2 == 0
                    else dfs(
                        alpha_pos, [nr, nc], visited | {(r, c)}, step + 1
                    )
                )

                is_opponent_winner &= win
                (win_steps if win else lose_steps).append(steps_left)

        if not can_move:
            return False, step

        # 상대 플레이어가 이긴 경우
        if is_opponent_winner:
            return False, max(win_steps)
        # 현재 플레이어가 이긴 경우
        return True, min(lose_steps)

    _, steps = dfs(aloc, bloc, set(), 0)
    return steps