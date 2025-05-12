def solution(lottos, win_nums):
    answer = []
    low_count = 0
    high_count = 0
    
    for num in lottos:
        if num in win_nums:
            low_count += 1
            high_count += 1
        if num == 0:
            high_count += 1
            
    if high_count == 1 or high_count == 0:
        answer.append(6)
    else:
        answer.append(7 - high_count)

    if low_count == 1 or low_count == 0:
        answer.append(6)
    else:
        answer.append(7 - low_count)
    
    return answer