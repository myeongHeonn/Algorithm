def solution(d, budget):
    answer = 0
    d.sort()

    for request in d:
        if request <= budget:
            answer += 1
            budget -= request

    return answer