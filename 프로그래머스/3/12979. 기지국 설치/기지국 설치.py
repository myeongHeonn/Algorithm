def solution(n, stations, w):
    answer = 0
    pre_station = 0
    stations.append(n + 1)
    for station in stations:
        if station == n + 1:
            val = station - 1 - pre_station
        else:
            val = (station - 1 - w) - pre_station

        if val > 0:
            if val % (2 * w + 1) == 0:
                answer += val // (2 * w + 1)
            else:
                answer += (val // (2 * w + 1)) + 1

        pre_station = station + w
    return answer