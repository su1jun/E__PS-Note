import sys
input = sys.stdin.readline

def floyd():
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if i != j and i != k and j != k:
                    dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k])
    for i in range(N):
        for j in range(N):
            if dp[i][j] == INF:
                dp[i][j] = 0

N = int(input())
M = int(input())
INF = sys.maxsize
dp = [[INF for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    dp[a-1][b-1] = min(dp[a-1][b-1], c)

floyd()

for i in range(N):
    print(*dp[i])
