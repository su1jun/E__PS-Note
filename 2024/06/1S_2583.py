from collections import deque
import sys
input = sys.stdin.readline

M, N, K = map(int, input().split())
graph = [[0]*N for _ in range(M)]
result = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1

    area = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= M or ny >= N: continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                area += 1
                queue.append((nx, ny))

    return area

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            result.append(bfs(i, j))

print(len(result))
print(*sorted(result))