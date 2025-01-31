def solution(n, k, cmd):
    deleted = []

    # 각 행 위아래의 행의 인덱스를 저장하는 리스트
    up = [i - 1 for i in range(n+2)]
    down = [i + 1 for i in range(n+1)]

    # 첫 번째 행은 임시 공간이므로 초기 위치에 1을 더해줘야함
    k += 1

    for cmd_i in cmd:
        # 행 삭제
        if cmd_i.startswith("C"):
            deleted.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k]

        # 행 복원
        elif cmd_i.startswith("Z"):
            restore = deleted.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore

        # 행 이동
        else:
            action, num = cmd_i.split()
            if action == "U":
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):
                    k = down[k]

    answer = ["O"] * n
    for i in deleted:
        answer[i-1] = "X"
    return "".join(answer)