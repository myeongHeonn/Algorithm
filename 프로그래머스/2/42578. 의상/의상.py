from collections import Counter

def solution(clothes):
    answer = 1
    # 의상의 종류별 개수
    clothes_count = Counter([kind for name, kind in clothes])
    for k in clothes_count.values():
        answer *= (k+1)
    # 의상을 아무것도 입지 않은 경우 -1
    return answer-1