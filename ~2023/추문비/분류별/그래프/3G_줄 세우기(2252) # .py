import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
Deg = [0 for _ in range(N+1)]
que = deque()
ans = []

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    Deg[b] += 1

for i in range(1, N+1):
    if Deg[i] == 0:
        que.append(i)

while que:
    tmp = que.popleft()
    ans.append(tmp)
    for i in graph[tmp]:
        Deg[i] -= 1
        if Deg[i] == 0:
            que.append(i)

print(*ans)