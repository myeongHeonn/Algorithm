def cal_score(ryan, apeach):
    ryan_score, apeach_score = 0, 0
    for i in range(11):
        if ryan[i] == 0 and apeach[i] == 0:
            continue
        if ryan[i] > apeach[i]:
            ryan_score += (10 - i)
        else:
            apeach_score += (10 - i)
    return ryan_score, apeach_score

def dfs(idx, arrows_left, ryan, info, max_diff, best_shot):
    if idx == 11:
        if arrows_left > 0:
            ryan[10] += arrows_left

        ryan_score, apeach_score = cal_score(ryan, info)
        value = ryan_score - apeach_score

        if value > max_diff[0]:
            max_diff[0] = value
            best_shot[0] = ryan[:]
        elif value == max_diff[0] and value > 0:
            for i in range(10, -1, -1):
                if ryan[i] != best_shot[0][i]:
                    if ryan[i] > best_shot[0][i]:
                        best_shot[0] = ryan[:]
                    break

        if arrows_left > 0:
            ryan[10] -= arrows_left
        return

    if arrows_left > info[idx]:
        ryan[idx] = info[idx] + 1
        dfs(idx + 1, arrows_left - ryan[idx], ryan, info, max_diff, best_shot)
        ryan[idx] = 0

    dfs(idx + 1, arrows_left, ryan, info, max_diff, best_shot)


def solution(n, info):
    max_diff = [0]
    best_shot = [[-1]]
    ryan = [0] * 11

    dfs(0, n, ryan, info, max_diff, best_shot)

    return best_shot[0]