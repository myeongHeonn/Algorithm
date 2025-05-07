def numbering_str(str_list):
    str_list.sort()
    pre_s = ''
    new_str_list = []
    number = 1
    for s in str_list:
        if s == pre_s:
            number_s = s + str(number)
            new_str_list.append(number_s)
            number += 1
        else:
            new_str_list.append(s)
            number = 1

        pre_s = s

    return new_str_list


def solution(str1, str2):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    str1_list = []
    str2_list = []

    temp = ''
    for s in str1:
        if s in alphabet:
            s = s.lower()
            temp += s
            if len(temp) == 2:
                str1_list.append(temp)
                temp = temp[-1]
        else:
            temp = ''

    temp = ''
    for s in str2:
        if s in alphabet:
            s = s.lower()
            temp += s
            if len(temp) == 2:
                str2_list.append(temp)
                temp = temp[-1]
        else:
            temp = ''
            
    if not str1_list and not str2_list:
        return 65536
    elif (not str1_list and str2_list) or (str1_list and not str2_list):
        return 0

    str1_list = numbering_str(str1_list)
    str2_list = numbering_str(str2_list)

    inter_cnt = 0
    for s in str1_list:
        if s in str2_list:
            inter_cnt += 1

    union_cnt = len(str1_list) + len(str2_list) - inter_cnt
    answer = int((inter_cnt / union_cnt) * 65536)

    return answer