from collections import deque
import sys
input = sys.stdin.readline

def bfs(mid):
    visited[ftr1] = 1
    q = deque()
    q.append(ftr1)
    while q:
        start = q.popleft()
        if start == ftr2: return True
        for nx, nc in graph[start]:
            if not visited[nx] and mid <= nc:
                q.append(nx)
                visited[nx] = 1
    return False

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

ftr1, ftr2 = map(int, input().split())
low, high = 1, int(1e9)
while low <= high:
    visited = [0 for _ in range(N + 1)]
    mid = (low + high) // 2
    if bfs(mid): low = mid + 1
    else: high = mid - 1
print(high)