def solution(N, stages):
    result = {}
    total = len(stages)

    # 1단계 부터 N단계까지 검사
    for i in range(1, N+1):
        # 해당 단계에 도달했지만 실패한 플레이어 수
        cnt = 0
        for stage in stages:
            if i == stage:
                cnt += 1
        # 실패율
        if cnt == 0:
            result[i] = 0
        else:
            temp = float(cnt / total)
            total -= cnt
            result[i] = temp

    # 실패율이 높은 순으로 정렬
    answer = sorted(result, key=lambda x:result[x], reverse=True)

    return answer