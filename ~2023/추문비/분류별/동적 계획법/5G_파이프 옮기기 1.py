import sys
input = sys.stdin.readline

N = int(input())

dp = [[[0] * N for _ in range(N)] for _ in range(3)]
graph = [list(map(int, input().split())) for _ in range(N)]

dp[0][0][1] = 1  # 첫 시작 위치

# dp를 위해서는 윗 행을 사용해야하므로 첫 행을 먼저 초기화
for i in range(2, N):
    if graph[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

for r in range(1, N):
    for c in range(1, N):
        if graph[r][c] == 0:
            # 대각선
            if graph[r][c-1] == 0 and graph[r-1][c] == 0:
                dp[2][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]
            # 가로
            dp[0][r][c] = dp[0][r][c-1] + dp[2][r][c-1]
            # 세로
            dp[1][r][c] = dp[1][r-1][c] + dp[2][r-1][c]

print(sum(dp[i][N-1][N-1] for i in range(3)))