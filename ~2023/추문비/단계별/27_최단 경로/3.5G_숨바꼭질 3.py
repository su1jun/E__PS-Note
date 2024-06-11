import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
graph = [0] * 100001

que = deque([N])
graph[N] = 1
while que:
    cur = que.popleft()
    if cur == K:
        break

    next = cur*2
    if 0 <= next < 100001 and not graph[next]:
        graph[next] = graph[cur]
        que.appendleft(next)

    for next in (cur-1, cur+1):
        if 0 <= next < 100001 and not graph[next]:
            graph[next] = graph[cur] + 1
            que.append(next)

print(graph[K]-1)