import itertools
def solution(n, q, ans):
    answer = 0
    arr = [(i + 1) for i in range(n)]
    combi = list(itertools.combinations(arr, 5))

    m = len(ans)
    for com in combi:
        flag = True

        for idx in range(m):
            compare_q = q[idx]
            compare_ans = ans[idx]

            cnt = 0
            for i in range(5):
                if com[i] in compare_q:
                    cnt += 1

            if cnt != compare_ans:
                flag = False
                break

        if flag:
            answer += 1

    return answer