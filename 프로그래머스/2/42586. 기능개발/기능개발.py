from collections import deque

def solution(progresses, speeds):
    answer = []
    q_progresses = deque(progresses)
    q_speeds = deque(speeds)

    while q_progresses:
        # 작업 진행
        for i in range(len(q_progresses)):
            q_progresses[i] += q_speeds[i]

        # 배포 가능 여부 확인
        cnt = 0
        # 맨 앞이 100 이상이면 배포
        while q_progresses and q_progresses[0] >= 100:
            q_progresses.popleft()
            q_speeds.popleft()
            cnt += 1

        if cnt > 0:
            answer.append(cnt)

    return answer