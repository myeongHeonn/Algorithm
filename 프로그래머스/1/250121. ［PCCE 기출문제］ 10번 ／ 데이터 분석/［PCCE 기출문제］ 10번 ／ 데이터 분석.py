def solution(data, ext, val_ext, sort_by):
    answer = []
    index_ext = 0
    if ext == 'date':
        index_ext = 1
    elif ext == 'maximum':
        index_ext = 2
    elif ext == 'remain':
        index_ext = 3

    index_sort = 0
    if sort_by == 'date':
        index_sort = 1
    elif sort_by == 'maximum':
        index_sort = 2
    elif sort_by == 'remain':
        index_sort = 3

    for d in data:
        if d[index_ext] < val_ext:
            answer.append(d)

    for i in range(len(answer)-1):
        for j in range(i+1, len(answer)):
            temp = answer[i]
            if answer[j][index_sort] < answer[i][index_sort]:
                answer[i] = answer[j]
                answer[j] = temp

    return answer