from collections import defaultdict

def solution(participant, completion):
    dic = defaultdict(int)
    for name in participant:
        dic[name] += 1

    for name in completion:
        dic[name] -= 1
        if dic[name] == 0:
            del dic[name]

    return list(dic.keys())[0]