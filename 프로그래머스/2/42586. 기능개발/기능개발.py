def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    
    index = 0    
    while True:
        if index == n:
            break
        
        for i in range(n):
            progresses[i] += speeds[i]
            
        count = 0
        while index < n and progresses[index] >= 100:
            count += 1
            index += 1
            
        if count != 0:
            answer.append(count)

    return answer