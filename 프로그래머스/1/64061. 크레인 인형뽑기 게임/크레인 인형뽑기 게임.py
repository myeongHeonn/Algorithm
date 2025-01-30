# board에서 인형을 뽑고 board를 업데이트 하는 함수
def func(board, index):
    n = len(board)

    for i in range(n):
        # 해당 칸에 인형이 존재한다면
        if board[i][index]:
            doll = board[i][index]
            board[i][index] = 0
            return doll
    # 인형이 존재하지 않은 경우
    return 0

def solution(board, moves):
    answer = 0

    stack = []
    for move in moves:
        value = func(board, move-1)
        # 인형을 뽑은 경우
        if value:
            if stack and stack[-1] == value:
                stack.pop()
                answer += 2
            else:
                stack.append(value)

    return answer