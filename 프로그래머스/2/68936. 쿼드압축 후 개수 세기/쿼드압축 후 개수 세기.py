def solution(arr):
    answer = [0, 0]

    def com(x, y, size):
        first = arr[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != first:
                    half = size // 2
                    com(x, y, half)
                    com(x, y + half, half)
                    com(x + half, y, half)
                    com(x + half, y + half, half)
                    return
        answer[first] += 1

    n = len(arr)
    com(0, 0, n)
    return answer