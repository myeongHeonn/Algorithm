from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(list)
    for c in clothes:
        dic[c[1]].append(c[0])

    for d in dic:
        answer *= (len(dic[d]) + 1)
    return answer - 1