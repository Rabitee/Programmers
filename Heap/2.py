def solution(stock, dates, supplies, k):
    import heapq
    import collections
    heap = []
    l = collections.deque()
    s = stock
    d = 0
    cnt = 0
    for i in range(len(dates)):
        heapq.heappush(heap, (-supplies[i], dates[i], supplies[i]))
    while True:
        if s + d >= k:
            return cnt
        t = heapq.heappop(heap)
        if s >= t[1] - d:
            s += t[2] - (t[1] - d)
            d = t[1]
            cnt += 1
            for _ in range(len(l)):
                heapq.heappush(heap, l.pop())
        else:
            l.append(t)