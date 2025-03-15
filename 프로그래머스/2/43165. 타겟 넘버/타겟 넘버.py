from collections import deque

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    queue = deque()
    queue.append((0, numbers[0]))
    queue.append((0, - 1 * numbers[0]))

    while queue:
        idx, value = queue.popleft()
        idx += 1

        if idx < n:
            queue.append((idx, value + numbers[idx]))            
            queue.append((idx, value - numbers[idx]))
        else:
            if value == target:
                answer += 1
                
    return answer