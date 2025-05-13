def solution(arr):
    answer = [arr[0]]
    
    for num in arr:
        if num == answer[-1]:
            continue
        else:
            answer.append(num)
    
    return answer