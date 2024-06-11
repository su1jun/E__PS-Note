# bfs 방문여부
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)] # M : 가로, N : 세로

step = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def bfs(x, y, k):
    que = deque([(x, y, k)])
    graph[x][y] = 0

    while graph[N-1][M-1] == "1":
        px, py, pk = que.popleft()
        for i, j in step:
            nx = px + i
            ny = py + j
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == "1":
                graph[nx][ny] = "0"
                que.append((nx, ny, pk+1))
    else:
        print(pk+2)

bfs(0, 0, 0)
