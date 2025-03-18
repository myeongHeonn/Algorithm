from collections import deque

def solution(priorities, location):
    answer = []
    queue = deque()
    for idx, priority in enumerate(priorities):
        queue.append((idx, priority))
    
    while queue:
        now_idx, now_priority = queue.popleft()
        flag = True
        
        for next_idx, next_priority in list(queue):
            if next_priority > now_priority:
                queue.append((now_idx, now_priority))
                flag = False
                break
        
        if flag:
            answer.append(now_idx)
            
    count = 1
    for idx in answer:
        if idx == location:
            return count
        else:
            count += 1