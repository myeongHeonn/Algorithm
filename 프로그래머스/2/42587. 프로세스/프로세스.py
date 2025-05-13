from collections import deque

def solution(priorities, location):
    queue = deque()
    for idx, p in enumerate(priorities):
        queue.append((idx, p))

    cnt = 1
    while queue:
        idx, time = queue.popleft()
        if not queue:
            return cnt
        
        if time >= max([t for i, t in queue]):
            if idx == location:
                return cnt
            cnt += 1
        else:
            queue.append((idx, time))