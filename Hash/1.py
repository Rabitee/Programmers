def solution(participant, completion):
    answer = ''
    p = {}
    for e in participant:
        if e in p:
            p[e] += 1
        else:
            p[e] = 1
    for e in completion:
        p[e] -= 1
    for key in p.keys():
        if p[key] == 1:
            answer = key
            break
    return answer