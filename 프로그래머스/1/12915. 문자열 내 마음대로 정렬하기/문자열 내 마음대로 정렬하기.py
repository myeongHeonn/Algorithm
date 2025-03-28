from collections import defaultdict

def solution(strings, n):
    answer = []
    dic = defaultdict(list)

    for string in strings:
        dic[string[n]].append(string)

    for i in range(26):
        if chr(i + 97) in dic:
            dic[chr(i + 97)].sort()
            answer += dic[chr(i + 97)]
    return answer