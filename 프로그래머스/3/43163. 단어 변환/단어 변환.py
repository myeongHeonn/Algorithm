from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    else:
        return bfs(begin, target, words)

def bfs(begin, target, words):
    queue = deque()
    queue.append((begin, 0))

    while queue:
        now_word, step = queue.popleft()

        if now_word == target:
            return step

        for word in words:
            if check(now_word, word):
                queue.append((word, step+1))

# 한 개의 알파벳만 차이 날때 True 반환
def check(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1

    if cnt == 1:
        return True
    else:
        return False