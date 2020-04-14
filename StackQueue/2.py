# https://programmers.co.kr/learn/courses/30/lessons/42583

import collections
def solution(bridge_length, weight, truck_weights):
    t = 0
    waiting = collections.deque(truck_weights)
    passing = collections.deque()
    while waiting or passing:
        if passing:
            if passing[0][1] == bridge_length:
                passing.popleft()
        if waiting:
            if weight >= sum([e[0] for e in passing]) + waiting[0]:
                truck = waiting.popleft()
                passing.append([truck, 0])
        for passing_track in passing:
            passing_track[1] += 1
        t += 1
        print(waiting)
        print(passing)
    return t