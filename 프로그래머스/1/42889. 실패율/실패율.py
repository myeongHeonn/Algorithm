def solution(N, stages):
    result = {}
    total = len(stages)

    for i in range(1, N+1):
        cnt = 0
        for stage in stages:
            if i == stage:
                cnt += 1
                
        if cnt == 0:
            result[i] = 0
        else:
            temp = cnt / total
            total -= cnt
            result[i] = temp

    answer = sorted(result, key=lambda x:result[x], reverse=True)
    return answer