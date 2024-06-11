import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
 
def f(x, y):
    # 도착
    if x == M-1 and y == N-1:
        return 1
 
    # 방문처리
    if dp[x][y] != -1:
        return dp[x][y]
    
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and data[x][y] > data[nx][ny]:
            cnt += f(nx, ny)
    
    dp[x][y] = cnt
    return dp[x][y]
 
# 초기 입력 
M, N = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
dx, dy = [1,-1,0,0], [0,0,1,-1]
 
print(f(0,0))