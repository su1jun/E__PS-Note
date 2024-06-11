import sys

n = int(sys.stdin.readline())
board = [0] * n
for i in range(n):
    board[i] = list(map(int, sys.stdin.readline().split()))
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        l = board[i][j]
        if l != 0:
            if i+l < n:
                dp[i+l][j] += dp[i][j]
            if j+l < n:
                dp[i][j+l] += dp[i][j]
print(dp[-1][-1])

