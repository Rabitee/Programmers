# https://programmers.co.kr/learn/courses/30/lessons/49189

import collections
def solution(n, edge):
    g = {}
    for e in edge:
        if e[0] in g:
            g[e[0]].append(e[1])
        else:
            g[e[0]] = [e[1]]
        if e[1] in g:
            g[e[1]].append(e[0])
        else:
            g[e[1]] = [e[0]]
    
    visited = set(g[1])
    visited.add(1)
    newVisited = visited
    while len(visited) < n:
        tmp = set()
        for e in newVisited:
            for v in g[e]:
                if v in visited or v in newVisited:
                    pass
                else:
                    tmp.add(v)
        newVisited = tmp
        visited = visited.union(tmp)
        
    return len(newVisited)

edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
n = 6
print(solution(n, edge))