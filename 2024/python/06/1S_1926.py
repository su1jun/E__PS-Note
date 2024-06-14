from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
number = 0
max_area = 0

def bfs(x, y):
    cnt = 1
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue

            if graph[nx][ny] == 1:
                cnt += 1
                graph[nx][ny] = 0
                queue.append((nx, ny))
    
    return cnt

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            number += 1
            max_area = max(max_area, bfs(i, j))

print(number)
print(max_area)