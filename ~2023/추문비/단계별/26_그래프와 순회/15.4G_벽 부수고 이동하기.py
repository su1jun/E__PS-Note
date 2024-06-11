import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

step = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def bfs(x, y, z):
    queue = deque([(x, y, z)])
    while queue and not (visited[N-1][M-1][0] or visited[N-1][M-1][1]):
        a, b, c = queue.popleft()
        for i, j in step:
            nx = a + i
            ny = b + j
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and c == 0 :
                    visited[nx][ny][1] = visited[a][b][0] + 1
                    queue.append((nx, ny, 1))
                elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[a][b][c] + 1
                    queue.append((nx, ny, c))
    return max(visited[N-1][M-1])

ans = bfs(0, 0, 0)
if ans:
    print(ans)
else:
    print(-1)