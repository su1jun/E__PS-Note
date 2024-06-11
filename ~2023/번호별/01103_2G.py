<<<<<<< HEAD
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(input().rstrip()))
visited = [[0] * M for _ in range(N)]
dp = [[0] * M for _ in range(N)]
ans = 0

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i, j in zip(dx, dy):
        nx = x + int(arr[x][y])*i
        ny = y + int(arr[x][y])*j
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != "H" and cnt+1 > dp[nx][ny]:
            if visited[nx][ny]:
                print(-1)
                exit()
            else:
                dp[nx][ny] = cnt+1
                visited[nx][ny] = 1
                dfs(nx, ny, cnt+1)
                visited[nx][ny] = 0

dfs(0, 0, 0)
=======
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(input().rstrip()))
visited = [[0] * M for _ in range(N)]
dp = [[0] * M for _ in range(N)]
ans = 0

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i, j in zip(dx, dy):
        nx = x + int(arr[x][y])*i
        ny = y + int(arr[x][y])*j
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != "H" and cnt+1 > dp[nx][ny]:
            if visited[nx][ny]:
                print(-1)
                exit()
            else:
                dp[nx][ny] = cnt+1
                visited[nx][ny] = 1
                dfs(nx, ny, cnt+1)
                visited[nx][ny] = 0

dfs(0, 0, 0)
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
print(ans+1)