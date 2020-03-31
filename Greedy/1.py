# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    l = sorted(list(set(lost)-set(reserve)))
    r = list(set(reserve) - set(lost))
    answer = n - len(l)
    for e in l:
        if e-1 in r:
            r.remove(e-1)
            answer += 1
        elif e+1 in r:
            r.remove(e+1)
            answer += 1
    return answer