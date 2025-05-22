def solution(n, lost, reserve):
    self = []
    for number in lost:
        if number in reserve:
            self.append(number)
    for number in self:
        lost.remove(number)
        reserve.remove(number)

    # 체육복을 잃어 버린 학생수
    m = len(lost)
    
    lost.sort()
    r = [False] * (n + 1)
    for number in lost:
        if number - 1 in reserve and not r[number - 1]:
            r[number - 1] = True
            continue
        if number + 1 in reserve and not r[number + 1]:
            r[number + 1] = True

    cnt = r.count(True)
    return n - m + cnt