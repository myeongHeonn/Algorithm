def solution(keyinput, board):
    n, m = board[1], board[0]
    y, x = n // 2, m // 2

    for key in keyinput:
        if key == 'down':
            if 0 <= y - 1:
                y -= 1
        elif key == 'up':
            if y + 1 < n:
                y += + 1
        elif key == 'left':
            if 0 <= x - 1:
                x -= 1
        elif key == 'right':
            if x + 1 < m:
                x += 1

    return [x - (m // 2), y - (n // 2)]