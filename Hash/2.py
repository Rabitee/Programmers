# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True
    l = sorted(phone_book, key=lambda x:len(x))
    d = {}
    for e in l:
        for i in range(1, len(l) + 1):
            if e[:i] in d:
                answer = False
                break
        d[e] = True
    return answer