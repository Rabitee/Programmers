# https://programmers.co.kr/learn/courses/30/lessons/42626

def solution(scoville, K):
    answer = 0
    import heapq
    heapq.heapify(scoville)
    while(True):
        if len(scoville) == 1:
            if scoville[0] < K:
                answer = -1
            break
        m1 = heapq.heappop(scoville)
        if m1 < K:
            m2 = heapq.heappop(scoville)
            heapq.heappush(scoville, m1 + (m2 * 2))
            answer += 1
        else:
            break
    return answer