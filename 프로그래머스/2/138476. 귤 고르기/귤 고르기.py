from collections import Counter

def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)

    stack = []
    for key in counter:
        stack.append(counter[key])

    stack.sort(reverse=True)
    for a in stack:
        if k <= 0:
            break

        k -= a
        answer += 1

    return answer