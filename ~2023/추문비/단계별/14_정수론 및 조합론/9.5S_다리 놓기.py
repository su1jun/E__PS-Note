import sys

T = int(sys.stdin.readline())
for _ in range(T):
    K, N = map(int, sys.stdin.readline().split())

    dp = [[0] * (N+1) for _ in range(N+1)]
    dp[1][1] = dp[1][0] = 1

    for i in range(2, N+1):
        for j in range(K+1):
            if (j==0)or(i==j):
                dp[i][j]=1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    print(dp[N][K])
