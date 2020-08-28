from collections import deque

def solution(n, edge):
    answer = 0
    check = [0] * (n + 1)
    check[1] = 1
    edges = [[] for _ in range(n + 1)]
    counts = [0] * (n + 1)
    q = deque()
    q.append((1, 0))

    for v in edge:
        v1, v2 = v
        edges[v1].append(v2)
        edges[v2].append(v1)
    while q:
        node, cnt = q.popleft()
        for possible_node in edges[node]:
            if check[possible_node] == 0:
                q.append((possible_node, cnt + 1))
                counts[possible_node] = cnt + 1
                check[possible_node] = 1

    maxval = max(counts)
    for c in counts:
        if maxval == c:
            answer += 1

    return answer
