def solution(brown, yellow):
    answer = []
    k = 0

    while True:
        k += 1
        if yellow % k == 0:
            if (k * 2) + ((yellow // k) * 2 + 4) == brown:
                answer.append(yellow // k + 2)
                answer.append(k + 2)
                break

    return answer