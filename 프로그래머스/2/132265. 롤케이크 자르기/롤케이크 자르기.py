from collections import Counter

def solution(topping):
    answer = 0

    topping_counter = Counter(topping)
    half_topping = set()

    for t in topping:
        topping_counter[t] -= 1
        half_topping.add(t)

        if topping_counter[t] == 0:
            topping_counter.pop(t)

        if len(half_topping) == len(topping_counter):
            answer += 1

    return answer