import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline

def bfs(lst):
    que = deque(lst)
    while que:
        px = que.popleft()
        for i in graph[px]:
            if not Visited[i]:
                Visited[i] = 1
                que.append((i))
    return

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
graph = defaultdict(list)

for i in range(N):
    for j in range(N):
        if matrix[i][j]:
            graph[i].append(j)
            
for i in range(N):
    Visited = [0] * N
    bfs([i])
    print(*Visited)