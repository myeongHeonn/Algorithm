from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course:
        order_list = []
        for order in orders:
            if len(order) < c:
                continue
            order_list += list(combinations(sorted(order), c))

        order_count = Counter(order_list)
        max_count = 0
        if order_count:
            max_count = max(order_count.values())

        for word, count in order_count.items():
            if 1 < max_count == count:
                answer.append(''.join(word))

    return sorted(answer)