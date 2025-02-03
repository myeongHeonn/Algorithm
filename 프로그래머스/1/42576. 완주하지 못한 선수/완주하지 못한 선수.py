def solution(participant, completion):
    dic = {}

    for name in participant:
        if name in dic:
            dic[name] += 1
        else:
            dic[name] = 1

    for name in completion:
        dic[name] -= 1

    for key in dic.keys():
        if dic[key] > 0:
            return key