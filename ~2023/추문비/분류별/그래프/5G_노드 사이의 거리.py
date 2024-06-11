import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline

def bfs(lst):
    que = deque(lst)
    px, l = que[0]
    Visited[px] = 1
    while que:
        px, l = que.popleft()
        if px == end:
            break
        for i, j in graph[px]:
            if not Visited[i]:
                Visited[i] = 1
                que.append((i, l+j))
    return l

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

for _ in range(M):
    Visited = [0 for _ in range(N+1)]
    start, end = map(int, input().split())
    print(bfs(graph[start]))