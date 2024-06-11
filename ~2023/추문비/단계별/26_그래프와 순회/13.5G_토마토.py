# bfs 방문여부
import sys
from collections import deque
input = sys.stdin.readline

step = [[0, 1, 0], [1, 0, 0], [0, -1, 0], [-1, 0, 0], [0, 0, 1], [0, 0, -1]]
def bfs(lst):
    que = deque(lst)
    while que:
        px, py, pz = que.popleft()
        for i, j, k in step:
            nx = px + i
            ny = py + j
            nz = pz + k
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[pz][px][py] + 1
                que.append((nx, ny, nz))

N, M, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(M)] for _ in range(H)] # M : 가로, N : 세로, H : 높이

start = []
for i in range(H):
    for j in range(M):
        for k in range(N):
            if graph[i][j][k] == 1:
                start.append([j, k, i])
bfs(start)
ans = 0
for i in graph:
    for j in i:
        if 0 in j:
            print(-1)
            exit(0)
        ans = max(ans, *j)
print(ans-1)