from collections import deque
def solution(n, t, m, timetable):
    #init: 540
    timetable = deque(sorted(list(map(lambda x: int(x[:2]) * 60 + int(x[3:]), timetable))))

    last = (540 + n*t)
    if last < timetable[0]: answer = last
    else:
        time = 540
        member = 0
        while time < last and timetable:
            while timetable and timetable[0] <= time:
                timetable.popleft()
                member += 1
            time += t
            member = 0
    print(timetable)
    print(time)
    answer = ''
    return answer


solution(1,1,5, ['08:00', '08:01', '08:02', '08:03'])