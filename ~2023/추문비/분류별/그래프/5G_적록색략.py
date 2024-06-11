import sys
from collections import deque
input = sys.stdin.readline

x_step = [0, 1, 0, -1]
y_step = [1, 0, -1, 0]

def bfs(lst):
    que = deque(lst)
    px, py, color = que[0]
    Visited[px][py] = 1
    while que:
        px, py, color = que.popleft()
        for i in range(4):
            nx = px + x_step[i]
            ny = py + y_step[i]
            if 0 <= nx < N and 0 <= ny < N and color == graph[nx][ny] and not Visited[nx][ny]:
                Visited[nx][ny] = 1
                que.append([nx, ny, color])
    return

N = int(input())
graph = [input().rstrip() for _ in range(N)]
Visited = [[0] * (N+1) for _ in range(N+1)]

ans = [0] * 2
for i in range(N):
    for j in range(N):
        if not Visited[i][j]:
            ans[0] += 1
            bfs([[i, j, graph[i][j]]])

for i in range(N):
    graph[i] = graph[i].replace("G", "R")
Visited = [[0] * (N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        if not Visited[i][j]:
            ans[1] += 1
            bfs([[i, j, graph[i][j]]])
print(*ans)
