# bfs 방문여부
import sys
from collections import deque
input = sys.stdin.readline

step = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def bfs(lst):
    que = deque(lst)
    while que:
        px, py = que.popleft()
        for i, j in step:
            nx = px + i
            ny = py + j
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0:
                graph[nx][ny] = graph[px][py] + 1
                que.append((nx, ny))

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)] # M : 가로, N : 세로

start = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            start.append([i, j])
bfs(start)
ans = 0
for i in graph:
    if 0 in i:
        print(-1)
        break
    ans = max(ans, *i)
else:
    print(ans-1)