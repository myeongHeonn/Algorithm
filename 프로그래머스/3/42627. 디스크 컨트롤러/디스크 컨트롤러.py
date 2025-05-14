from collections import deque
import heapq

def solution(jobs):
    n = len(jobs)
    answer = []
    wait_queue = []
    execution = []
    jobs.sort(key=lambda x: x[0])
    request_queue = deque(jobs)
    time = 0

    while request_queue or wait_queue or execution:
        # 실행 중인 작업을 완료한 경우
        if execution:
            if execution[0][0] == 0:
                answer.append(time - execution[0][1])
                execution.pop()

        # 요청 큐에서 대기 큐에 삽입할 작업들이 있는지 확인
        while request_queue:
            request_time = request_queue[0][0]
            # 요청 시각이 현재 시각과 같다면 대기 큐에 삽입
            if request_time == time:
                r_time, e_time = request_queue.popleft()
                heapq.heappush(wait_queue, (e_time, r_time))
            else:
                break

        # 대기 큐에 작업이 존재하고, 실행 중인 작업이 없다면 작업 실행
        if wait_queue and not execution:
            e_time, r_time = heapq.heappop(wait_queue)
            execution.append([e_time, r_time])

        # 실행 중인 작업이 있다면 실행 시간 (남은 시간) 1초 빼기
        if execution:
            execution[0][0] -= 1

        time += 1

    return int(sum(answer) / n)