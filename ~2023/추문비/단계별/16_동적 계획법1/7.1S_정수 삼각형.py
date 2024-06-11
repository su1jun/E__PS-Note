import sys
input = sys.stdin.readline

n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

if n > 1:
    dp[1][0] += dp[0][0]
    dp[1][-1] += dp[0][-1]
    print(f"dp[1] : {dp[1]}")
if n > 2:
    for i in range(2, n):
        dp[i][0] += dp[i-1][0]
        for j in range(1, i):
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
        dp[i][-1] += dp[i-1][-1]
        print(f"dp[{i}] : {dp[i]}")

print(max(dp[-1]))