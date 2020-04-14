# https://programmers.co.kr/learn/courses/30/lessons/43237

def solution(budgets, M):
    ans = 0
    s = 0
    e = max(budgets)
    f = lambda x,y: (x + y) // 2
    if M >= sum(budgets):
        return max(budgets)
    while True:
        p = f(s, e)
        m = sum([el if el < p else p for el in budgets])
        if M < m:
            e = p
        else:
            if ans <= p:
                ans = p
            s = p
        if e - s <= 1:
            return ans