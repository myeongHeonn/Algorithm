def solution(schedules, timelogs, startday):
    answer = len(schedules)
    for idx, schedule in enumerate(schedules):
        now = startday
        schedule += 10
        if schedule % 100 >= 60:
            schedule = (schedule // 100 + 1) * 100 + ((schedule % 100) - 60)

        for timelog in timelogs[idx]:
            if now in [6, 7]:
                now = now % 7 + 1
                continue

            if timelog > schedule:
                answer -= 1
                break

            now = now % 7 + 1

    return answer