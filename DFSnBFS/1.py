# https://programmers.co.kr/learn/courses/30/lessons/43165

import collections
def solution(numbers, target):
    answer = 0
    l = collections.deque(numbers)
    e = l.pop()
    if len(numbers) == 1:
        if e == target or e == -1 * target:
            return 1
        else:
            return 0
    else:
        answer += solution(numbers[:-1], target - e) + solution(numbers[:-1], target + e)
    return answer