def solution(s):
    result = []
    list_s = []
    temp = ""
    idx = -1
    flag = True

    for c in s[1:-1]:
        if c == '{':
            flag = True
            list_s.append([])
            idx += 1
            continue
        if c == '}':
            flag = False
            list_s[idx].append(int(temp))
            temp = ""

        if flag:
            if c != ',':
                temp += c
            else:
                list_s[idx].append(int(temp))
                temp = ""

    list_s = sorted(list_s, key=lambda x: len(x))

    result.append(list_s[0][0])
    for i in range(1, len(list_s)):
        value = [x for x in list_s[i] if x not in list_s[i-1]]
        result.append(value[0])

    return result