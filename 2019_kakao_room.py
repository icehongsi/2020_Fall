import sys
sys.setrecursionlimit(1<<16)

def get_vacant_room(n):
    print(room)
    if n not in room:
        room[n] = n + 1
        return n
    empty = get_vacant_room(room[n])
    room[n] = empty + 1
    return empty

def solution(k, room_number):
    global room
    room = {}
    answer = []
    for i in room_number:
        print("-"*50)
        print(i)
        answer.append(get_vacant_room(i))
    return answer

print(solution(20, [1,3,4,1,3,1]))