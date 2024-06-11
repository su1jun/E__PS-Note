<<<<<<< HEAD
import sys
input = sys.stdin.readline

MOD = 1000000007
N, M, P = map(int, input().split())
dp = [[0] * 101 for _ in range(101)]
dp[0][0] = 1
for i in range(1, P+1):
    for j in range(0, i+1):
        if j > 0: dp[i][j] += dp[i-1][j-1] * (N-j+1) % MOD
        if j > M: dp[i][j] += dp[i-1][j] * (j-M) % MOD
        dp[i][j] %= MOD
print(dp[P][N])
=======
import sys
input = sys.stdin.readline

MOD = 1000000007
N, M, P = map(int, input().split())
dp = [[0] * 101 for _ in range(101)]
dp[0][0] = 1
for i in range(1, P+1):
    for j in range(0, i+1):
        if j > 0: dp[i][j] += dp[i-1][j-1] * (N-j+1) % MOD
        if j > M: dp[i][j] += dp[i-1][j] * (j-M) % MOD
        dp[i][j] %= MOD
print(dp[P][N])
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
