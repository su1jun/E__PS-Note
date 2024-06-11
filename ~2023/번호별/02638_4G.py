<<<<<<< HEAD
# 치즈
from collections import deque
input = __import__('sys').stdin.readline

def bfs():
    q = deque()
    visited = [[0] * M for _ in range(N)]

    q.append((0, 0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or N <= nx or ny < 0 or M <= ny:
                continue

            if cheese[nx][ny] == 0 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1
            elif cheese[nx][ny] == 1:
                visited[nx][ny] += 1
    melt = []
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2:
                melt.append((i, j))
    return melt

N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

ans = 0
while True:
    melt = bfs()
    if not melt:
        break
    ans += 1
    for x, y in melt:
        cheese[x][y] = 0

=======
# 치즈
from collections import deque
input = __import__('sys').stdin.readline

def bfs():
    q = deque()
    visited = [[0] * M for _ in range(N)]

    q.append((0, 0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or N <= nx or ny < 0 or M <= ny:
                continue

            if cheese[nx][ny] == 0 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1
            elif cheese[nx][ny] == 1:
                visited[nx][ny] += 1
    melt = []
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2:
                melt.append((i, j))
    return melt

N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

ans = 0
while True:
    melt = bfs()
    if not melt:
        break
    ans += 1
    for x, y in melt:
        cheese[x][y] = 0

>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
print(ans)