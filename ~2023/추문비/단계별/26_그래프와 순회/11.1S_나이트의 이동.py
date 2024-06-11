# bfs
import sys
from collections import deque
input = sys.stdin.readline

step = [[-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1]]
def bfs(x, y):
    que = deque([(x, y)])
    visited[x][y] = 1
    while que:
        px, py = que.popleft()
        if px == x_t and py == y_t:
            return visited[px][py]
        for i, j in step:
            nx = px + i
            ny = py + j
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny] :
                visited[nx][ny] = visited[px][py] + 1
                que.append((nx, ny))

T = int(input())
for _ in range(T):
    l = int(input())
    x_a, y_b = map(int, input().split())
    x_t, y_t = map(int, input().split())
    visited = [[0] * l for _ in range(l)]
    print(bfs(x_a, y_b)-1)